# Questão 2 — Decomposição numérica de 142.981

## Técnicas utilizadas

- **Few-Shot:** um exemplo resolvido com um número menor mostra exatamente o formato e a profundidade esperados.
- **Chain-of-Thought:** cálculos aritméticos são propensos a erro; exigir cada etapa explícita permite conferir o resultado.
- **Especificação de escopo:** "decomposição numérica" pode significar coisas diferentes, então o prompt pede todas as formas relevantes, garantindo uma resposta completa.

## Prompt

```
Você é um professor de matemática. Quero uma resposta completa sobre a decomposição numérica de um número.

Apresente as seguintes formas de decomposição, nesta ordem:
1. Valor posicional de cada algarismo (classes e ordens).
2. Decomposição aditiva.
3. Decomposição multiplicativa (algarismo × potência de 10).
4. Decomposição em potências de 10 (forma polinomial).
5. Decomposição em fatores primos, mostrando passo a passo os testes de divisibilidade.

Exemplo para o número 3.528:
1. 3 → unidade de milhar (3.000); 5 → centena (500); 2 → dezena (20); 8 → unidade (8)
2. 3.000 + 500 + 20 + 8
3. 3 × 1.000 + 5 × 100 + 2 × 10 + 8 × 1
4. 3 × 10³ + 5 × 10² + 2 × 10¹ + 8 × 10⁰
5. 3.528 ÷ 2 = 1.764 ÷ 2 = 882 ÷ 2 = 441 ÷ 3 = 147 ÷ 3 = 49 ÷ 7 = 7 ÷ 7 = 1
   Resultado: 2³ × 3² × 7²

Agora faça o mesmo para o número 142.981. Pense passo a passo, mostre cada cálculo e confira o resultado final antes de responder.
```

## Resposta obtida

### 1. Valor posicional

| Classe | Ordem | Algarismo | Valor |
|--------|-------|-----------|-------|
| Milhares | Centena de milhar | 1 | 100.000 |
| Milhares | Dezena de milhar | 4 | 40.000 |
| Milhares | Unidade de milhar | 2 | 2.000 |
| Unidades simples | Centena | 9 | 900 |
| Unidades simples | Dezena | 8 | 80 |
| Unidades simples | Unidade | 1 | 1 |

### 2. Decomposição aditiva

```
142.981 = 100.000 + 40.000 + 2.000 + 900 + 80 + 1
```

### 3. Decomposição multiplicativa

```
142.981 = 1 × 100.000 + 4 × 10.000 + 2 × 1.000 + 9 × 100 + 8 × 10 + 1 × 1
```

### 4. Forma polinomial

```
142.981 = 1 × 10⁵ + 4 × 10⁴ + 2 × 10³ + 9 × 10² + 8 × 10¹ + 1 × 10⁰
```

### 5. Decomposição em fatores primos

Basta testar os primos até a raiz quadrada do número: √142.981 ≈ 378,1, ou seja, primos de 2 a 373.

Testes iniciais pelas regras de divisibilidade:

| Primo | Teste | Divisível? |
|-------|-------|------------|
| 2 | Termina em 1 (ímpar) | Não |
| 3 | 1+4+2+9+8+1 = 25, não é múltiplo de 3 | Não |
| 5 | Não termina em 0 ou 5 | Não |
| 7 | 7 × 20.425 = 142.975, resto 6 | Não |
| 11 | Soma alternada 1−8+9−2+4−1 = 3 | Não |
| 13 | 13 × 10.998 = 142.974, resto 7 | Não |
| 17 | 17 × 8.410 = 142.970, resto 11 | Não |
| 19 | 19 × 7.525 = 142.975, resto 6 | Não |

O mesmo procedimento aplicado aos demais primos até 373 (23, 29, 31, …, 367, 373) sempre deixa resto diferente de zero.

**Conclusão:** 142.981 não possui nenhum divisor primo menor ou igual à sua raiz quadrada, portanto **é um número primo**. Sua decomposição em fatores primos é ele mesmo:

```
142.981 = 142.981¹
```

### Resumo

| Forma | Resultado |
|-------|-----------|
| Aditiva | 100.000 + 40.000 + 2.000 + 900 + 80 + 1 |
| Multiplicativa | 1×100.000 + 4×10.000 + 2×1.000 + 9×100 + 8×10 + 1×1 |
| Polinomial | 1×10⁵ + 4×10⁴ + 2×10³ + 9×10² + 8×10¹ + 1×10⁰ |
| Fatores primos | 142.981 (número primo) |
