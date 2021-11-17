# APEXのやることリストを作る
# その日意識することを3つランダムで取り出してくれるようにする
#
# 追加、追加するのをやめるというのができる
# 追加したのをリストに入れる、やめるを選んだらループ抜ける
# リストの中からランダムに3つ選んで表示

# def item_select() :
#     select = input("0か1を入力して下さい(数字は半角で)> ")

#     return select

import random
import csv

todo = []
with open('todo_list.csv', newline='', encoding='utf-8') as csvreaderfile :
    reader = csv.reader(csvreaderfile, delimiter=',')
    for row in reader :
        todo.append(','.join(row))
#    print(todo)

list_num = len(todo)

# print(list_num)

count = 0

number = int(input('今日意識する項目の数を入力してください。(0 ~ 5)> '))

print('')
while count < number :
    num = random.randrange(0, list_num)
    print(todo[num])
    count += 1