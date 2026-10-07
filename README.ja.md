# Graffiti 予想 262 の証明

[English](README.md)

木村心（Shin Kimura）、2026-10-07

証明は AI（Anthropic の Claude Opus 5.5 と OpenAI の GPT-6.1 Sol）の助けを借りて見つけた。

## 予想

S. Fajtlowicz『Written on the Wall』（2004 年 7 月版）の予想 262（p. 78、「任意のグラフについての予想（246 : 274）」）：

> 262. -smallest eigenvalue ≤ maximum of Even.
>
> （最小固有値の符号を変えたもの ≤ Even の最大値）

固有値は隣接行列 $`A`$ の固有値で、$`\mathrm{Even}(v)`$ は $`v`$ から偶数の距離にある頂点の数（$`v`$ 自身を含む）
（T. L. Brewster, M. J. Dinneen, V. Faber, Discrete Math. 147 (1995) 35–55, p. 52）。

## 定理

$`G`$ を有限単純グラフ、$`A`$ をその隣接行列とし、$`v`$ からちょうど距離 $`2`$ にある頂点の数を $`s_v`$ とする。
このとき $`A + \mathrm{diag}(1 + s_v)`$ は半正定値である。したがって

$$
-\lambda_{\min}(A) \le 1 + \max_v s_v \le \max_v \mathrm{Even}(v)
$$

であり、予想 262 はすべてのグラフで成り立つ。完全グラフと完全二部グラフ $`K_{a,a}`$ で等号が成り立つ。
グラフは連結でなくてよい（到達できない頂点は、どの有限の距離にもない）。

## 証明

実ベクトル $`x`$ に対して

$$
F(x) = \sum_v x_v^2 + 2 \sum_{uv \in E} x_u x_v + 2 \sum_{\mathrm{dist}(u,v) = 2} |x_u x_v|
$$

とおく。各和では、順序を区別しない頂点の組を 1 回ずつ数える。

**主張.** すべての実ベクトル $`x`$ について $`F(x) \ge 0`$。

そうでないとして、$`F(x) < 0`$ を満たす $`x`$ のうち、0 でない成分が最も少ないものをとる。
0 でない成分 $`u, v`$ が「隣接していて $`x_u x_v > 0`$」または「距離 $`2`$」だとする。
符号と $`|x_u| + |x_v|`$ を保ったまま $`u`$ と $`v`$ の間で重みを移す。$`u`$ と $`v`$ だけを含む項の和は
$`x_u^2 + x_v^2 + 2|x_u x_v| = (|x_u| + |x_v|)^2`$ で変わらず、残りの項は移す量の 1 次式である。
よって両端のどちらかで $`F`$ は負のままで、0 でない成分が減る。これは $`x`$ の選び方に矛盾する。

したがって、0 でない成分の間に残る組は「異符号で隣接する組」だけであり、しかもそれらは頂点を共有しない。
$`u`$ にそのような相手 $`v, w`$ が 2 つあれば、$`v`$ と $`w`$ は同符号で、隣接しているか（$`u`$ を経由して）距離 $`2`$ にあるからである。
よって $`F(x)`$ は、これらの組についての $`(x_u + x_v)^2`$ と、残りの 0 でない成分についての $`x_v^2`$ の和になり、0 以上である。矛盾。

**結論.** $`x^{\mathsf{T}} A x = 2 \sum_{uv \in E} x_u x_v`$ と、距離 $`2`$ の各組についての $`2|x_u x_v| \le x_u^2 + x_v^2`$ より

$$
0 \le F(x) \le x^{\mathsf{T}} A x + \sum_v (1 + s_v) x_v^2 .
$$

よって $`A + \mathrm{diag}(1 + s_v)`$ は半正定値である。$`x`$ を $`\lambda_{\min}(A)`$ の固有ベクトルとすれば
$`0 \le (\lambda_{\min}(A) + 1 + \max_v s_v) \lVert x \rVert^2`$。最後に、$`\mathrm{Even}(v)`$ は $`v`$ 自身と距離 $`2`$ の
$`s_v`$ 個の頂点を数えるので、$`1 + s_v \le \mathrm{Even}(v)`$。$`\square`$

## 数値による確認

`check_strong_form.py` は、1〜7 頂点のすべてのグラフ、8〜80 頂点のランダムグラフ 3000 個、完全二部グラフについて、
$`A + \mathrm{diag}(1 + s_v)`$ が半正定値であることと、不等式の連鎖が成り立つことを確かめる。証明の一部ではない。
Python 3、networkx、numpy が必要。

## 参考文献

- S. Fajtlowicz, *Written on the Wall* (July 2004 version).
- T. L. Brewster, M. J. Dinneen, V. Faber, A computational attack on the conjectures of Graffiti: New counterexamples and proofs,
  Discrete Math. 147 (1995) 35–55.

## ライセンス

コード：MIT（`LICENSE` を参照）。文章：CC BY 4.0。
