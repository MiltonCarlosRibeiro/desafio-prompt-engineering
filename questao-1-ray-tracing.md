# Questão 1 — Como o Ray Tracing calcula a cor de um pixel

## Técnicas utilizadas

- **Persona (Role Prompting):** define o nível técnico e o vocabulário da resposta.
- **Chain-of-Thought:** o cálculo da cor é um processo em etapas encadeadas; pedir o raciocínio passo a passo evita uma resposta superficial.
- **Formato de saída definido:** exige fórmulas, pseudocódigo e um resumo, tornando a resposta verificável e didática.

## Prompt

```
Você é um engenheiro de computação gráfica especialista em renderização física e professor universitário de Computação Gráfica.

Contexto: sou desenvolvedor de software, entendo vetores e álgebra linear básica, mas nunca implementei um renderizador.

Tarefa: explique, passo a passo, como o algoritmo de Ray Tracing calcula a cor final de um único pixel de uma imagem renderizada.

Siga esta ordem de raciocínio:
1. Geração do raio primário a partir da câmera passando pelo pixel.
2. Teste de interseção do raio com os objetos da cena (dê o exemplo da esfera).
3. Dados obtidos no ponto de interseção (ponto, normal, material).
4. Cálculo da iluminação local (componentes ambiente, difusa e especular).
5. Raios de sombra.
6. Raios secundários de reflexão e refração e a recursão.
7. Combinação das contribuições e conversão para o valor final do pixel (gamma, clamp, anti-aliasing).

Formato da resposta:
- Uma seção por etapa, com a fórmula matemática envolvida.
- Ao final, um pseudocódigo da função trace(raio, profundidade).
- Feche com um resumo de no máximo 5 linhas.
Responda em português.
```

## Resposta obtida

### 1. Geração do raio primário

Para cada pixel `(i, j)` da imagem, cria-se um raio que parte da posição da câmera `O` e atravessa o centro do pixel no plano de projeção:

```
u = (i + 0.5) / largura
v = (j + 0.5) / altura
P_pixel = canto_inferior_esquerdo + u · horizontal + v · vertical
D = normalizar(P_pixel − O)
R(t) = O + t · D,   t > 0
```

### 2. Interseção com os objetos

O raio é testado contra todos os objetos da cena e fica-se com a interseção de menor `t` positivo (o objeto mais próximo). Para uma esfera de centro `C` e raio `r`:

```
|O + tD − C|² = r²
a = D·D,  b = 2 D·(O − C),  c = (O − C)·(O − C) − r²
Δ = b² − 4ac
```

Se `Δ < 0` não há interseção e o pixel recebe a cor de fundo. Caso contrário, `t = (−b − √Δ) / 2a`. Em cenas grandes, estruturas de aceleração como BVH ou kd-tree reduzem o número de testes.

### 3. Dados do ponto de interseção

```
P = O + t · D
N = normalizar(P − C)
V = −D
```

Também se obtém o material do objeto: cor base, coeficientes `ka`, `kd`, `ks`, expoente de brilho `n`, refletividade `kr`, transparência `kt` e índice de refração `η`.

### 4. Iluminação local (modelo de Phong)

Para cada fonte de luz `l` com intensidade `I_l` e direção `L = normalizar(pos_luz − P)`:

```
Ambiente:  I_a · ka · cor
Difusa:    I_l · kd · cor · max(0, N·L)
Especular: I_l · ks · max(0, R·V)^n,   R = 2(N·L)N − L

I_local = I_a·ka·cor + Σ_l visível(l) · [I_l·kd·cor·max(0, N·L) + I_l·ks·max(0, R·V)^n]
```

### 5. Raios de sombra

Para decidir `visível(l)`, lança-se um raio de `P + εN` em direção à luz. Se ele atingir algum objeto antes da luz, o ponto está em sombra para aquela fonte e as parcelas difusa e especular dela são descartadas. O deslocamento `ε` evita a autointerseção (*shadow acne*).

### 6. Reflexão, refração e recursão

Se o material for reflexivo, gera-se um raio refletido:

```
D_r = D − 2(D·N)N
cor_reflexão = trace(P + εN, D_r, profundidade + 1)
```

Se for transparente, gera-se um raio refratado pela Lei de Snell (`η = η1/η2`):

```
cosθi = −N·D
k = 1 − η²(1 − cos²θi)
D_t = η·D + (η·cosθi − √k)·N      (se k < 0 ocorre reflexão interna total)
cor_refração = trace(P − εN, D_t, profundidade + 1)
```

A proporção entre reflexão e refração pode ser calculada pela aproximação de Schlick para os termos de Fresnel. A recursão termina ao atingir uma profundidade máxima ou quando a contribuição fica desprezível.

### 7. Cor final do pixel

```
cor = I_local + kr · cor_reflexão + kt · cor_refração
```

Em seguida:

- **Anti-aliasing:** vários raios por pixel com pequenas variações de posição e média dos resultados.
- **Clamp:** cada canal limitado a `[0, 1]` (ou aplicação de *tone mapping*).
- **Correção gama:** `cor_final = cor^(1/2.2)`.
- **Quantização:** conversão para `[0, 255]` em RGB.

### Pseudocódigo

```
função trace(origem, direção, profundidade):
    se profundidade > MAX_PROFUNDIDADE:
        retorne PRETO

    hit = intersecao_mais_proxima(origem, direção)
    se hit é nulo:
        retorne COR_FUNDO

    P, N, material = hit.ponto, hit.normal, hit.material
    V = −direção
    cor = luz_ambiente * material.ka * material.cor

    para cada luz em luzes:
        L = normalizar(luz.posicao − P)
        se não em_sombra(P + ε·N, L, luz):
            difusa = luz.intensidade * material.kd * material.cor * max(0, N·L)
            R = refletir(−L, N)
            especular = luz.intensidade * material.ks * max(0, R·V) ^ material.n
            cor += difusa + especular

    se material.kr > 0:
        cor += material.kr * trace(P + ε·N, refletir(direção, N), profundidade + 1)

    se material.kt > 0:
        D_t = refratar(direção, N, material.eta)
        se D_t existe:
            cor += material.kt * trace(P − ε·N, D_t, profundidade + 1)

    retorne cor

para cada pixel (i, j):
    acumulado = PRETO
    para s em 1..AMOSTRAS:
        raio = gerar_raio_camera(i + aleatorio(), j + aleatorio())
        acumulado += trace(raio.origem, raio.direcao, 0)
    imagem[i][j] = gama(clamp(acumulado / AMOSTRAS))
```

### Resumo

Para cada pixel, um raio sai da câmera e encontra o objeto mais próximo. No ponto atingido calcula-se a iluminação local (ambiente, difusa e especular), verificando com raios de sombra quais luzes são visíveis. Se o material reflete ou refrata, novos raios são lançados recursivamente e suas cores são somadas com pesos. O resultado é suavizado por múltiplas amostras, limitado, corrigido por gama e gravado como cor RGB do pixel.
