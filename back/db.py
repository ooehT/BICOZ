import re
import sqlite3
from pathlib import Path

SCHEMA = Path(__file__).with_name("schema.sql")

# Lista predefinida de ofícios (H02). O Admin poderá editar na Sprint 3 (H06).
CATEGORIAS_PADRAO = [
    ("Encanador", "🚰"),
    ("Eletricista", "💡"),
    ("Chaveiro", "🔑"),
    ("Frete", "🚚"),
    ("Gás", "🔥"),
]

STATUS_VALIDOS = ("disponivel", "ocupado")
TELEFONE_RE = re.compile(r"^\d{11}$")


class ErroValidacao(ValueError):
    pass


def conectar(caminho):
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(conn):
    conn.executescript(SCHEMA.read_text(encoding="utf-8"))
    conn.executemany(
        "INSERT OR IGNORE INTO categorias (nome, icone) VALUES (?, ?)",
        CATEGORIAS_PADRAO,
    )
    conn.commit()


def listar_categorias(conn, apenas_ativas=True):
    sql = "SELECT id, nome, icone, ativa FROM categorias"
    if apenas_ativas:
        sql += " WHERE ativa = 1"
    return [dict(r) for r in conn.execute(sql + " ORDER BY nome")]


def criar_prestador(conn, nome, telefone, categoria_id):
    """Cria prestador (começa 'ocupado'). Valida telefone e categoria (RNF03)."""
    nome = (nome or "").strip()
    if not nome:
        raise ErroValidacao("Nome é obrigatório.")
    if not isinstance(telefone, str) or not TELEFONE_RE.match(telefone):
        raise ErroValidacao("Telefone deve ter exatamente 11 dígitos numéricos (DDD + número).")
    cat = conn.execute(
        "SELECT id FROM categorias WHERE id = ? AND ativa = 1", (categoria_id,)
    ).fetchone()
    if cat is None:
        raise ErroValidacao("Ofício inválido: selecione uma categoria da lista.")
    cur = conn.execute(
        "INSERT INTO prestadores (nome, telefone, categoria_id) VALUES (?, ?, ?)",
        (nome, telefone, categoria_id),
    )
    conn.commit()
    return buscar_prestador(conn, cur.lastrowid)


def buscar_prestador(conn, prestador_id):
    row = conn.execute(
        """SELECT p.id, p.nome, p.telefone, p.status, p.atualizado_em,
                  c.id AS categoria_id, c.nome AS categoria
           FROM prestadores p JOIN categorias c ON c.id = p.categoria_id
           WHERE p.id = ?""",
        (prestador_id,),
    ).fetchone()
    return dict(row) if row else None


def atualizar_status(conn, prestador_id, novo_status=None):
    """Define o status; se novo_status for None, alterna (toggle).
    Retorna o prestador atualizado ou None se não existir."""
    if novo_status is not None and novo_status not in STATUS_VALIDOS:
        raise ErroValidacao("Status deve ser 'disponivel' ou 'ocupado'.")
    atual = conn.execute(
        "SELECT status FROM prestadores WHERE id = ?", (prestador_id,)
    ).fetchone()
    if atual is None:
        return None
    if novo_status is None:
        novo_status = "ocupado" if atual["status"] == "disponivel" else "disponivel"
    conn.execute(
        """UPDATE prestadores
           SET status = ?, atualizado_em = strftime('%Y-%m-%dT%H:%M:%fZ', 'now')
           WHERE id = ?""",
        (novo_status, prestador_id),
    )
    conn.commit()
    return buscar_prestador(conn, prestador_id)
