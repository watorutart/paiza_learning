# coding: utf-8
#スキルチェック練習問題「単語のカウント」より

list = input().rstrip().split(" ")

check_list = []

for i in range(len(list)):
    if list[i] not in check_list:
        check_list.append(list[i])

for i in range(len(check_list)):
    count = 0
    for j in range(len(list)):
        if check_list[i] == list[j]:
            count += 1
    print(check_list[i] + " " + str(count))
