from flask import Flask, g, jsonify, request

import db


def create_app(database="bicoz.db"):
    app = Flask(__name__)
    app.config["DATABASE"] = database

    with db.conectar(database) as conn:
        db.init_db(conn)

    def get_conn():
        if "conn" not in g:
            g.conn = db.conectar(app.config["DATABASE"])
        return g.conn

    @app.teardown_appcontext
    def fechar(_exc):
        conn = g.pop("conn", None)
        if conn is not None:
            conn.close()

    @app.errorhandler(db.ErroValidacao)
    def erro_validacao(e):
        return jsonify(erro=str(e)), 400

    # Issue #4 — lista predefinida de ofícios (alimenta o formulário H02 e os filtros H04)
    @app.get("/api/categorias")
    def categorias():
        return jsonify(db.listar_categorias(get_conn()))

    # Issue #4 — cadastro (reaproveitado pelo formulário da issue #3)
    @app.post("/api/prestadores")
    def criar_prestador():
        d = request.get_json(silent=True) or {}
        p = db.criar_prestador(
            get_conn(), d.get("nome"), d.get("telefone"), d.get("categoria_id")
        )
        return jsonify(p), 201

    @app.get("/api/prestadores/<int:pid>")
    def obter_prestador(pid):
        p = db.buscar_prestador(get_conn(), pid)
        if p is None:
            return jsonify(erro="Prestador não encontrado."), 404
        return jsonify(p)

    # Issue #1 — alterna/define status (H01).
    # Body opcional: {"status": "disponivel" | "ocupado"}. Sem body = toggle.
    @app.patch("/api/prestadores/<int:pid>/status")
    def alterar_status(pid):
        d = request.get_json(silent=True) or {}
        p = db.atualizar_status(get_conn(), pid, d.get("status"))
        if p is None:
            return jsonify(erro="Prestador não encontrado."), 404
        return jsonify(p)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
