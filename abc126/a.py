N, K = map(int, input().split())
S=input()
char_list = [char for char in S]
char_list[K-1] = char_list[K-1].lower()
S=""
for char in char_list:
    S+=char
print(S)