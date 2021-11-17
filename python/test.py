#

import csv

# with open('data/src/sample.csv') as f :
#     reader = csv.reader(f)
#     for row in reader :
#         print

todo = []
# 読み取り
# with open('todo_list.csv', newline='', encoding='utf-8') as f :
#     reader = csv.reader(f, delimiter=',')
#     for row in reader :
#         todo.append(','.join(row))
#         print(todo)
#         print(len(row))
# delimiter = '区切り文字' tsvファイル(タブ区切り)の場合は、\t


#  書き取り
# with open('todo_list.csv', 'w', newline='', encoding='utf-8') as f :
#     writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow

a = '自分の画面は常にきれいに','キャラコンのミスを減らす、スライディング大事'
# 追記
with open('todo_list.csv', 'a', newline='', encoding='utf-8') as f :
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(a)



with open('todo_list.csv', newline='', encoding='utf-8') as f :
    reader = csv.reader(f, delimiter=',')
    for row in reader :
        todo.append(','.join(row))
        print(todo)
        print(len(row))
        print(len(todo))
