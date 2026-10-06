# Desafio Prompt Engineering

Aplicação de técnicas de Prompt Engineering para extrair respostas precisas, relevantes e detalhadas de uma ferramenta de IA generativa (ChatGPT).

Para cada questão foi identificada a técnica mais adequada, considerando clareza, contexto, detalhamento e relevância do resultado esperado.

## Questões

| # | Tema | Técnicas | Arquivo |
|---|------|----------|---------|
| 1 | Cor de um pixel no Ray Tracing | Persona + Chain-of-Thought + Formato de saída | [questao-1-ray-tracing.md](questao-1-ray-tracing.md) |
| 2 | Decomposição numérica de 142.981 | Few-Shot + Chain-of-Thought | [questao-2-decomposicao-numerica.md](questao-2-decomposicao-numerica.md) |
| 3 | Maquiavel em As Crônicas de Gelo e Fogo | Persona + Contextualização + Saída estruturada | [questao-3-maquiavel-cronicas-gelo-fogo.md](questao-3-maquiavel-cronicas-gelo-fogo.md) |
| 4 | Endpoint FastAPI com validação de `Item` | Especificação estruturada + Restrições + Formato de saída | [questao-4-fastapi](questao-4-fastapi) |

## Executando a questão 4

```bash
cd questao-4-fastapi
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Documentação interativa em `http://127.0.0.1:8000/docs`.

Testes:

```bash
pytest
```
