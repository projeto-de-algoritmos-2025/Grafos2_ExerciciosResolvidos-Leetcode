# [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)

Existem `n` cidades conectadas por um certo número de voos. Você recebe um array `flights`, onde `flights[i] = [from_i, to_i, price_i]` indica que há um voo da cidade `from_i` para a cidade `to_i` com custo `price_i`.

Você também recebe três inteiros: `src`, `dst` e `k`, retorne **o preço mais barato** de `src` para `dst` com no máximo `k` paradas. Se não existir tal rota, retorne `-1`.

#### Exemplo 1:
![Grafo exemplo 1](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_787/img/ex1.png)<br>
*Grafo exemplo 1* <br>
**Entrada:** `n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1`
**Saída:** `700`
**Explicação:**
- O grafo é mostrado acima.  
- O caminho ideal com `no máximo 1 parada` da cidade `0` para a cidade `3` está marcado em vermelho e tem um custo de `100 + 600 = 700`.  
- Note que o caminho que passa pelas cidades `[0, 1, 2, 3]` é mais barato mas é inválido porque utiliza 2 paradas.

#### Exemplo 2:
![Grafo exemplo 2](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_787/img/ex2.png)<br>
*Grafo exemplo 2* <br>
**Entrada:** `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1`
**Saída:** `200`
**Explicação:**
- O grafo é mostrado acima.  
- O caminho ideal com `no máximo 1 parada` da cidade `0` para a cidade `2` está marcado em vermelho e tem um custo de `100 + 100 = 200`.  

#### Exemplo 3:
![Grafo exemplo 3](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_787/img/ex3.png)<br>
*Grafo exemplo 3* <br>
**Entrada:** `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0`
**Saída:** `500`
**Explicação:**
- O grafo é mostrado acima.  
- O caminho ideal `sem paradas` da cidade `0` para a cidade `2` está marcado em vermelho e tem um custo de `500`.  

#### Restrições:
- `1 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= fromi, toi < n`
- `fromi != toi`
- `1 <= pricei <= 104`
- `Não haverá múltiplos voos entre duas mesmas cidades.`
- `0 <= src, dst, k < n`
- `src != dst`

# Solução
![Problema 787](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_787/img/prob787.png) <br>
*Problema 787 aceitação*

[Solução](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_787/problema787.py)