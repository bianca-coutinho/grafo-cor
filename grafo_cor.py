import time

def parse_matriz_incidente(matriz):
    n = len(matriz)
    m = len(matriz[0])
    adj = [[] for _ in range(n)]
    for j in range(m):
        vertices = [i for i in range(n) if matriz[i][j] == 1]
        if len(vertices) == 2:
            u, v = vertices
            adj[u].append(v)
            adj[v].append(u)
    return adj

def color_refinement(adj):
    n = len(adj)
    cor = [len(viz) for viz in adj]
    while True:
        nova_cor = []
        mapa = {}
        for i in range(n):
            chave = (cor[i], tuple(sorted(cor[v] for v in adj[i])))
            if chave not in mapa:
                mapa[chave] = len(mapa)
            nova_cor.append(mapa[chave])
        if nova_cor == cor:
            break
        cor = nova_cor
    return sorted(cor)

def main():
    with open("C:/Users/Bianca Coutinho/Downloads/instancias_isomorfismo.txt") as f:
        linhas = [linha.strip() for linha in f if linha.strip()]

    i = 0
    for indice in range(1, 41):
        try:
            n = int(linhas[i])
            i += 1
            m1 = [list(map(int, list(linhas[i + j]))) for j in range(n)]
            i += n
            m2 = [list(map(int, list(linhas[i + j]))) for j in range(n)]
            i += n

            adj1 = parse_matriz_incidente(m1)
            adj2 = parse_matriz_incidente(m2)

            start = time.process_time()
            iso = color_refinement(adj1) == color_refinement(adj2)
            tempo = round(time.process_time() - start, 3)
            print(f"{indice}) n = {n} {'+++' if iso else '---'} {tempo:.3f}")
        except Exception as e:
            print(f"\nErro ao processar par {indice} (linha {i}): {e}")
            break

if __name__ == "__main__":
    main()