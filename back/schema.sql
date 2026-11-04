-- Issue #4: tabelas de categorias (ofícios) e prestadores

CREATE TABLE IF NOT EXISTS categorias (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nome   TEXT    NOT NULL UNIQUE,
    icone  TEXT,
    ativa  INTEGER NOT NULL DEFAULT 1 CHECK (ativa IN (0, 1))
);

CREATE TABLE IF NOT EXISTS prestadores (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    nome          TEXT    NOT NULL CHECK (length(trim(nome)) > 0),
    telefone      TEXT    NOT NULL
                  CHECK (length(telefone) = 11 AND telefone NOT GLOB '*[^0-9]*'),
    categoria_id  INTEGER NOT NULL REFERENCES categorias(id),
    status        TEXT    NOT NULL DEFAULT 'ocupado'
                  CHECK (status IN ('disponivel', 'ocupado')),
    atualizado_em TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))
);

CREATE INDEX IF NOT EXISTS idx_prestadores_categoria ON prestadores(categoria_id);
CREATE INDEX IF NOT EXISTS idx_prestadores_status    ON prestadores(status);
