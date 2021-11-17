import csv

print('0:追加、1:やめる')
select = input("0か1を入力して下さい。(数字は半角で)> ")


# todo = []

if (select == '0') :
    while select == '0' :
        item_list = []
        print('意識する項目を追加します。')
        item = input('追加する項目を入力> ')
        item_list.append(item)
        with open('todo_list.csv', 'a', newline='', encoding='utf-8') as f :
            writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(item_list)
        select = input('0か1を入力してください。> ')
        if (select == '0') :
            continue
        elif (select == '1') :
            print('リストへの追加を終了します。')
            print('このファイルを閉じて、"apex.py"を開いてください。')
            break
elif (select == '1') :
    print('このファイルを閉じて、"apex.py"を開いてください。')


# with open('todo_list.csv', newline='', encoding='utf-8') as csvreaderfile :
#     reader = csv.reader(csvreaderfile, delimiter=',')
#     for row in reader :
#         todo.append(','.join(row))
#     print(todo)
#     print(len(todo))

# print(item_list)

# with open('todo_list.csv', 'a', newline='', encoding='utf-8') as append :
#     writer = csv.writer(append, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINMAL)
#     writer.writerow([])