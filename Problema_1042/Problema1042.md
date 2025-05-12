# 1042. Flower Planting With No Adjacent  
**Medium**  
**Topics:** Graph, Greedy  

---

## Descrição

Você tem `n` jardins, rotulados de `1` a `n`, e um array `paths`, onde `paths[i] = [xi, yi]` descreve um caminho bidirecional entre o jardim `xi` e o jardim `yi`.

Cada jardim deve receber **um dos 4 tipos de flores**.

**Regra:** Jardins que estão conectados por um caminho **não podem ter o mesmo tipo de flor**.

Todos os jardins têm **no máximo 3 caminhos conectando** a outros.

---

## Objetivo

Sua tarefa é escolher um tipo de flor para cada jardim de forma que:

- Jardins conectados diretamente tenham **tipos diferentes** de flores.

Retorne **uma possível escolha** como um array `answer`, onde `answer[i]` é o tipo de flor plantado no jardim `(i+1)`.

As flores são representadas pelos números: `1`, `2`, `3` e `4`.

⚠️ **É garantido que uma solução sempre existe.**

---

## Exemplos

### Exemplo 1:

```text
Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
```

**Explicação:**  
- Jardim 1 e 2 são diferentes  
- Jardim 2 e 3 são diferentes  
- Jardim 3 e 1 são diferentes  
Outras respostas válidas: `[1,2,4]`, `[1,4,2]`, `[3,2,1]`, etc.

---

### Exemplo 2:

```text
Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
```

---

### Exemplo 3:

```text
Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
```

---

## Constraints

- `1 <= n <= 10⁴`
- `0 <= paths.length <= 2 * 10⁴`
- `paths[i].length == 2`
- `1 <= xi, yi <= n`
- `xi != yi`
- Cada jardim tem **no máximo 3 caminhos conectando a ele**
