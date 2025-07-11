# Algoritmo Color Refinement para Isomorfismo de Grafos

## Enunciado
  
Existem vários algoritmos para tentar resolver o problema de determinar se dois grafos simples são ou não isomórficos. Um destes algoritmos é chamado “Color refinement”, que é descrito no artigo intitulado “The Graph Isomorphism Problem: Exploring the theoretical and practical aspects of the graph isomorphism problem”, by Martin Grohe and Pascal Schweitzer, Communications of the ACM, Posted Nov 1 2020.  
https://cacm.acm.org/research/the-graph-isomorphism-problem/

Nesta lista de exercícios, você precisará implementar o algoritmo “Color refinement” e testá-lo sobre o conjunto de grafos que estão no arquivo “Instâncias isomorfismo.txt”.

As instâncias são dadas pelas matrizes de incidências dos grafos. Por exemplo, suponha os grafos G1 = (V1, E1) e G2 = (V2, E2), com |V1| = |V2| = 4, E1 = {(1, 2),(1, 4),(2, 3),(3, 4)} e E2 = {(1, 2),(1, 3),(2, 4),(3, 4)}. As matrizes de incidências de G1 e G2 são as seguintes, respectivamente:

```
0101
1010
0101
1010

0110
1001
1001
0110
```

O seu código em C, C++ ou Python deve ler as matrizes de incidências e imprimir a seguinte mensagem para cada um dos 40 pares de grafos. Por exemplo:

```
40) n = 4 +++ 0.001
```

No par de instâncias número 40: n=4, +++ (isomórfico) e 0.001 (cpu time).  
Se os grafos no par não forem isomórficos, então deve-se imprimir --- na terceira coluna acima.

Para que você entenda um pouco mais sobre o problema de decidir se dois grafos simples são isomórficos ou não, sugiro a leitura do texto no seguinte link:  
https://en.wikipedia.org/wiki/Graph_isomorphism_problem

---

## Sobre o Projeto

Este projeto implementa o algoritmo de Color Refinement para testar isomorfismo entre pares de grafos simples, utilizando suas matrizes de incidência como entrada.

- O código principal está em [`grafo_cor.py`](c:/Users/Bianca%20Coutinho/Downloads/grafo_cor.py).
- As instâncias de teste devem estar no arquivo `Instâncias isomorfismo.txt` (ajuste o caminho no código conforme necessário).

## Como Executar

1. Certifique-se de ter Python 3 instalado.
2. Coloque o arquivo de instâncias no caminho especificado no código.
3. Execute o script:

```sh
python grafo_cor.py
```

O resultado será impresso no terminal, indicando para cada par de grafos se são isomórficos (`+++`) ou não (`---`), junto com o tempo de CPU utilizado.

## Referências

- [The Graph Isomorphism Problem: Exploring the theoretical and practical aspects of the graph isomorphism problem](https://cacm.acm.org/research/the-graph-isomorphism-problem/)
- [Graph isomorphism problem (Wikipedia)](https://en.wikipedia.org/wiki/Graph_isomorphism_problem)
