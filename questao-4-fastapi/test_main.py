from datetime import date, timedelta
from uuid import UUID

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def payload(**overrides):
    dados = {"nome": "Notebook", "valor": 3500.9, "data": date.today().isoformat()}
    dados.update(overrides)
    return dados


def test_cria_item_valido_com_uuid():
    resposta = client.post("/items", json=payload())

    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["nome"] == "Notebook"
    assert corpo["valor"] == 3500.9
    assert corpo["data"] == date.today().isoformat()
    assert UUID(corpo["uuid"])


def test_uuid_diferente_a_cada_requisicao():
    primeiro = client.post("/items", json=payload()).json()["uuid"]
    segundo = client.post("/items", json=payload()).json()["uuid"]

    assert primeiro != segundo


def test_aceita_nome_com_25_caracteres():
    resposta = client.post("/items", json=payload(nome="a" * 25))

    assert resposta.status_code == 201


def test_rejeita_nome_maior_que_25_caracteres():
    resposta = client.post("/items", json=payload(nome="a" * 26))

    assert resposta.status_code == 422


def test_rejeita_data_futura():
    amanha = (date.today() + timedelta(days=1)).isoformat()
    resposta = client.post("/items", json=payload(data=amanha))

    assert resposta.status_code == 422
    assert "data atual" in resposta.text


def test_rejeita_valor_invalido():
    resposta = client.post("/items", json=payload(valor="abc"))

    assert resposta.status_code == 422


def test_rejeita_data_invalida():
    resposta = client.post("/items", json=payload(data="2024-13-40"))

    assert resposta.status_code == 422


def test_rejeita_campos_ausentes():
    resposta = client.post("/items", json={})

    assert resposta.status_code == 422
