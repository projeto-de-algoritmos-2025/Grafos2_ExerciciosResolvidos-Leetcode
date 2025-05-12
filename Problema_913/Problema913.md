# 913. Cat and Mouse  
**Hard**  
**Topics:** Graph, Game Theory  

---

## Descrição

A game on an undirected graph is played by two players, **Mouse** and **Cat**, who alternate turns.

The graph is given as follows: `graph[a]` is a list of all nodes `b` such that **ab** is an edge of the graph.

- The **Mouse** starts at node **1** and goes first.  
- The **Cat** starts at node **2** and goes second.  
- There is a **Hole** at node **0**.

During each player's turn, they must travel along **one edge** of the graph that meets where they are.  
For example, if the Mouse is at node `1`, it must travel to any node in `graph[1]`.

**Note:** The **Cat is not allowed to travel to the Hole** (node `0`).

---

## Terminações possíveis do jogo:

- ✅ If the **Cat** and the **Mouse** occupy the same node → **Cat wins**.
- ✅ If the **Mouse** reaches the **Hole (node 0)** → **Mouse wins**.
- 🔁 If **a position repeats** (same node positions and same turn) → **Draw**.

---

## Objetivo

Given a graph, and assuming both players play **optimally**, return:

- `1` if the **Mouse wins the game**.
- `2` if the **Cat wins the game**.
- `0` if the game is a **draw**.

---

## Examples

### Example 1:

```text
Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0
```

**Explanation:** The game ends in a draw if both play optimally.

---

### Example 2:

```text
Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1
```

**Explanation:** The mouse can reach the hole before the cat catches it.

---

## Constraints

- `3 <= graph.length <= 50`
- `1 <= graph[i].length < graph.length`
- `0 <= graph[i][j] < graph.length`
- `graph[i][j] != i` (no self-loops)
- `graph[i]` is unique (no duplicate edges)
- Both Mouse and Cat **can always move**

