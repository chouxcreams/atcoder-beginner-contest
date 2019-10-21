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

## Warshall-Floyd Algorithm
abc143_e

時間計算量O(N^3)
```python
# Warshall-Floyd Algorithm
def warshall_floyd(distance):
    N = len(distance)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    return distance
```

参考
https://ja.wikipedia.org/wiki/%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E2%80%93%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95
