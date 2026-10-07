# A proof of Graffiti conjecture 262

[日本語](README.ja.md)

Shin Kimura (木村心), 2026-10-07

The proof was found with the help of AI (Claude Opus 5.5 by Anthropic and GPT-6.1 Sol by OpenAI).

## The conjecture

S. Fajtlowicz, *Written on the Wall* (July 2004 version), conjecture 262 (p. 78, "Conjectures for arbitrary graphs (246 : 274)"):

> 262. -smallest eigenvalue ≤ maximum of Even.

The eigenvalues are those of the adjacency matrix $`A`$, and $`\mathrm{Even}(v)`$ is the number of vertices at even
distance from $`v`$, including $`v`$ itself (T. L. Brewster, M. J. Dinneen, V. Faber, Discrete Math. 147 (1995) 35–55, p. 52).

## Theorem

Let $`G`$ be a finite simple graph with adjacency matrix $`A`$, and let $`s_v`$ be the number of vertices at distance
exactly $`2`$ from $`v`$. Then $`A + \mathrm{diag}(1 + s_v)`$ is positive semidefinite. Consequently

$$
-\lambda_{\min}(A) \le 1 + \max_v s_v \le \max_v \mathrm{Even}(v),
$$

so conjecture 262 holds for every graph. Equality holds for complete graphs and for the complete bipartite graphs $`K_{a,a}`$.
The graph need not be connected (unreachable vertices are at no finite distance).

## Proof

For a real vector $`x`$ let

$$
F(x) = \sum_v x_v^2 + 2 \sum_{uv \in E} x_u x_v + 2 \sum_{\mathrm{dist}(u,v) = 2} |x_u x_v| ,
$$

where each unordered pair is counted once.

**Claim.** $`F(x) \ge 0`$ for every real vector $`x`$.

Suppose not, and take $`x`$ with $`F(x) < 0`$ and as few nonzero coordinates as possible.
Suppose two nonzero coordinates $`u, v`$ are adjacent with $`x_u x_v > 0`$, or are at distance $`2`$.
Move weight between $`u`$ and $`v`$, keeping their signs and $`|x_u| + |x_v|`$ fixed. The terms involving only $`u`$ and $`v`$
add up to $`x_u^2 + x_v^2 + 2|x_u x_v| = (|x_u| + |x_v|)^2`$, which does not change, and the remaining terms are affine in the
amount moved. So at one of the two ends $`F`$ is still negative and there are fewer nonzero coordinates, a contradiction.

Hence among the nonzero coordinates the only interacting pairs are adjacent pairs with opposite signs, and these pairs
are disjoint: if $`u`$ had two such partners $`v`$ and $`w`$, then $`v`$ and $`w`$ would have the same sign and be adjacent
or at distance $`2`$ (through $`u`$). So $`F(x)`$ is the sum of $`(x_u + x_v)^2`$ over these pairs and of $`x_v^2`$ over the
other nonzero coordinates, which is nonnegative, a contradiction.

**Conclusion.** Since $`x^{\mathsf{T}} A x = 2 \sum_{uv \in E} x_u x_v`$ and $`2|x_u x_v| \le x_u^2 + x_v^2`$ for each pair at distance $`2`$,

$$
0 \le F(x) \le x^{\mathsf{T}} A x + \sum_v (1 + s_v) x_v^2 .
$$

So $`A + \mathrm{diag}(1 + s_v)`$ is positive semidefinite. Taking $`x`$ to be an eigenvector for $`\lambda_{\min}(A)`$ gives
$`0 \le (\lambda_{\min}(A) + 1 + \max_v s_v) \lVert x \rVert^2`$. Finally $`\mathrm{Even}(v)`$ counts $`v`$ itself and the
$`s_v`$ vertices at distance $`2`$, so $`1 + s_v \le \mathrm{Even}(v)`$. $`\square`$

## Numerical check

`check_strong_form.py` checks that $`A + \mathrm{diag}(1 + s_v)`$ is positive semidefinite and that the chain of
inequalities holds on all graphs with 1 to 7 vertices, 3000 random graphs with 8 to 80 vertices, and complete bipartite
graphs. It is not part of the proof. Requires Python 3, networkx and numpy.

## References

- S. Fajtlowicz, *Written on the Wall* (July 2004 version).
- T. L. Brewster, M. J. Dinneen, V. Faber, A computational attack on the conjectures of Graffiti: New counterexamples and proofs,
  Discrete Math. 147 (1995) 35–55.

## License

Code: MIT (see `LICENSE`). Text: CC BY 4.0.
