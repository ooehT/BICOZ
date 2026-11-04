import os, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app import create_app


class ApiTest(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".db")
        os.close(fd)
        self.client = create_app(self.path).test_client()

    def tearDown(self):
        os.remove(self.path)

    def novo(self, **kw):
        d = {"nome": "João", "telefone": "31999998888", "categoria_id": 1}
        d.update(kw)
        return self.client.post("/api/prestadores", json=d)

    def test_categorias_predefinidas(self):
        nomes = [c["nome"] for c in self.client.get("/api/categorias").get_json()]
        for n in ("Encanador", "Eletricista", "Chaveiro", "Frete"):
            self.assertIn(n, nomes)

    def test_cadastro_valido_inicia_ocupado(self):
        r = self.novo()
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.get_json()["status"], "ocupado")

    def test_telefone_invalido(self):
        for tel in ("3199999888", "319999988889", "31 99999888", "abcdefghijk", None, 31999998888):
            self.assertEqual(self.novo(telefone=tel).status_code, 400, tel)

    def test_oficio_invalido(self):
        self.assertEqual(self.novo(categoria_id=999).status_code, 400)
        self.assertEqual(self.novo(categoria_id=None).status_code, 400)

    def test_toggle_status(self):
        pid = self.novo().get_json()["id"]
        r = self.client.patch(f"/api/prestadores/{pid}/status")
        self.assertEqual(r.get_json()["status"], "disponivel")
        r = self.client.patch(f"/api/prestadores/{pid}/status")
        self.assertEqual(r.get_json()["status"], "ocupado")

    def test_status_explicito_e_persistencia(self):
        pid = self.novo().get_json()["id"]
        self.client.patch(f"/api/prestadores/{pid}/status", json={"status": "disponivel"})
        self.assertEqual(self.client.get(f"/api/prestadores/{pid}").get_json()["status"], "disponivel")

    def test_status_invalido(self):
        pid = self.novo().get_json()["id"]
        r = self.client.patch(f"/api/prestadores/{pid}/status", json={"status": "verde"})
        self.assertEqual(r.status_code, 400)

    def test_prestador_inexistente(self):
        self.assertEqual(self.client.patch("/api/prestadores/999/status").status_code, 404)


if __name__ == "__main__":
    unittest.main()
