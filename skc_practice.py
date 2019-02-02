# coding: utf-8
#スキルチェック練習問題「本の整理」より
#テスト７でタイムオーバー

num = int(input().rstrip())
books = list(map(int,input().rstrip().split(" ")))
count = 0

for i in range(num):
    for j in range(i,num):
        if books[j] == i+1:
            break;
    if i!=j:
        books[j] = books[i]
        count += 1
    books[i] = i+1
print(str(count))
