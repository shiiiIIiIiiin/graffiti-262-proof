"""Check the strong form behind the proof of Graffiti 262.

  A + diag(1 + s_v) is positive semidefinite,  s_v = #{u : dist(u, v) = 2},
  hence -lambda_min(A) <= 1 + max_v s_v <= max_v Even(v).
"""
import random

import networkx as nx
import numpy as np


def check(G):
    n = G.number_of_nodes()
    A = nx.to_numpy_array(G, nodelist=range(n))
    s = np.zeros(n)
    even = np.zeros(n)
    for v, row in nx.all_pairs_shortest_path_length(G):
        s[v] = sum(1 for d in row.values() if d == 2)
        even[v] = sum(1 for d in row.values() if d % 2 == 0)
    m = np.linalg.eigvalsh(A + np.diag(1 + s))[0]
    lam = np.linalg.eigvalsh(A)[0]
    return m, -lam, 1 + s.max(), even.max()


def graphs():
    for G in nx.graph_atlas_g()[1:]:
        yield G
    rng = random.Random(21)
    for _ in range(3000):
        n = rng.randint(8, 80)
        yield nx.gnp_random_graph(n, rng.uniform(0.02, 0.98), seed=rng.randrange(10 ** 9))
    for a in range(2, 12):
        for b in range(a, 14):
            yield nx.complete_bipartite_graph(a, b)


def main():
    worst_psd = 1e9
    tight = viol = 0
    total = 0
    for G in graphs():
        G = nx.convert_node_labels_to_integers(G)
        m, lhs, mid, rhs = check(G)
        total += 1
        worst_psd = min(worst_psd, m)
        if not (lhs <= mid + 1e-9 and mid <= rhs + 1e-9):
            viol += 1
        if abs(lhs - mid) < 1e-9:
            tight += 1
    print(f"graphs: {total}; min eigenvalue of A + diag(1+s): {worst_psd:.3e}; chain violations: {viol}; "
          f"equality -lambda_min = 1 + max s in {tight} graphs")


if __name__ == "__main__":
    main()
