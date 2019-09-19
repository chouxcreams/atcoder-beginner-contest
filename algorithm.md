# algorithm.md
出くわしたアルゴリズムの
- 名前
- 出現箇所
- サンプルコード
- 参考

をメモする

## Z-algorithm
abc141_e

時間計算量O(N)
### コード
```python
# Z-algorithm
A = [-1]*N
c = 0
for i, s in enumerate(S):
    if i == 0:
        continue
    if c+A[c] > i+A[i-c]:
        A[i] = A[i-c]
        continue
    j = max(0, A[c]-i+c)
    while i+j < N and S[j] == S[i+j]:
        j += 1
    A[i] = j
    c = i
```
### 参考
https://snuke.hatenablog.com/entry/2014/12/03/214243