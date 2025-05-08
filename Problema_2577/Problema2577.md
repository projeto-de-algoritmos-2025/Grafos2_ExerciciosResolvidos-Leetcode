# [2577. Minimum Time to Visit a Cell In a Grid](https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/?envType=daily-question&envId=2024-11-29) 

Você recebe uma matriz `grid` de tamanho `m x n` composta por números inteiros **não-negativos**, onde `grid[linha][coluna]` representa o tempo **mínimo** necessário para poder visitar a célula `(linha, coluna)`. Isso significa que você só pode visitar a célula `(linha, coluna)` quando o tempo em que você a visita for maior ou igual a `grid[linha][coluna]`.

Você começa na célula **superior esquerda** no tempo `0` segundos, e pode se mover para **qualquer** célula adjacente nas quatro direções: cima, baixo, esquerda ou direita. Cada movimento leva 1 segundo.

Retorne o tempo **mínimo** necessário para alcançar a célula inferior direita. Se for impossível alcançá-la, retorne `-1`.

#### Exemplo 1:
![Grafo exemplo 1](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_2577/img/ex1.png)<br>
*Grafo exemplo 1* <br>
**Entrada:** `grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]`
**Saída:** `7`
**Explicação:** Um dos caminhos possíveis é o seguinte:
- No instante **t = 0**, estamos na célula **(0,0)**.
- No instante **t = 1**, movemos para a célula **(0,1)**. Isso é possível porque `grid[0][1] ≤ 1`.
- No instante **t = 2**, movemos para a célula **(1,1)**. Isso é possível porque `grid[1][1] ≤ 2`.
- No instante **t = 3**, movemos para a célula **(1,2)**. Isso é possível porque `grid[1][2] ≤ 3`.
- No instante **t = 4**, movemos para a célula **(1,1)**. Isso é possível porque `grid[1][1] ≤ 4`.
- No instante **t = 5**, movemos para a célula **(1,2)**. Isso é possível porque `grid[1][2] ≤ 5`.
- No instante **t = 6**, movemos para a célula **(1,3)**. Isso é possível porque `grid[1][3] ≤ 6`.
- No instante **t = 7**, movemos para a célula **(2,3)**. Isso é possível porque `grid[2][3] ≤ 7`.
- O **tempo final** é **7**. Pode-se demonstrar que este é o **tempo mínimo possível**.


#### Exemplo 2:
![Grafo exemplo 2](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_2577/img/ex2.png)<br>
*Grafo exemplo 2* <br>
**Entrada:** `grid = [[0,2,4],[3,2,1],[1,0,4]]`
**Saída:** `-1`
**Explicação:** Não há um caminho válido do canto superior esquerdo ao canto inferior direito da matriz.

#### Restrições:
- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 10^5`
- `0 <= grid[i][j] <= 10^5`
- `grid[0][0] == 0`

# Solução
![Problema 2577](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_2577/img/prob2577.png) <br>
*Problema 2577 aceitação*

[Solução](https://github.com/projeto-de-algoritmos-2025/Grafos2_ExerciciosResolvidos-Leetcode/blob/ae1809ca00db9c44b883091b07df18a0c685e8c9/Problema_2577/problema2577.py)