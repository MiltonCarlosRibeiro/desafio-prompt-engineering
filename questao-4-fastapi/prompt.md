# Questão 4 — Endpoint FastAPI com validação de `Item`

## Técnicas utilizadas

- **Persona:** um desenvolvedor Python sênior tende a seguir boas práticas e versões atuais das bibliotecas.
- **Especificação estruturada:** os campos, tipos e regras são passados em lista, sem ambiguidade.
- **Restrições explícitas:** versão do Pydantic, código sem comentários e uso de recursos nativos de validação.
- **Formato de saída definido:** arquivos separados, testes e instruções de execução.

## Prompt

```
Você é um desenvolvedor Python sênior especialista em FastAPI e Pydantic v2.

Tarefa: crie um endpoint POST /items com FastAPI que valide e processe um objeto do tipo Item.

Estrutura do Item:
- nome: string com no máximo 25 caracteres
- valor: float
- data: date, que não pode ser superior à data atual

Requisitos:
1. O endpoint deve validar os valores recebidos e retornar 422 com mensagem clara quando forem inválidos.
2. Após a validação, retorne o corpo da requisição com um campo adicional "uuid", contendo um identificador único gerado dinamicamente a cada requisição.
3. Responda com status 201.

Restrições:
- Use Pydantic v2 (Field e field_validator).
- Use um modelo de resposta separado que herde de Item.
- Código limpo, tipado e sem comentários.

Formato da resposta:
1. main.py
2. test_main.py com pytest e TestClient cobrindo: item válido, uuid único, nome com 25 e 26 caracteres, data futura, valor inválido, data inválida e corpo vazio.
3. requirements.txt
4. Comandos para executar a API e os testes.
```

## Resposta obtida

Os arquivos gerados estão nesta pasta:

- [main.py](main.py)
- [test_main.py](test_main.py)
- [requirements.txt](requirements.txt)

### Executando

```bash
pip install -r requirements.txt
uvicorn main:app --reload
pytest
```

### Exemplo de requisição

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"nome": "Notebook", "valor": 3500.9, "data": "2025-01-15"}'
```

Resposta `201 Created`:

```json
{
  "nome": "Notebook",
  "valor": 3500.9,
  "data": "2025-01-15",
  "uuid": "3f1c9a2e-8b7d-4e6a-9c51-2d4f7a8b6e10"
}
```

Data futura, `422 Unprocessable Entity`:

```json
{
  "detail": [
    {
      "type": "value_error",
      "loc": ["body", "data"],
      "msg": "Value error, a data não pode ser superior à data atual",
      "input": "2099-01-01",
      "ctx": {"error": {}}
    }
  ]
}
```
