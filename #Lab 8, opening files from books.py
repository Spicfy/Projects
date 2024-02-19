#Lab 8, opening files from books
 
def create_books_2Dlist(file_name):
    bookinfo = open(file_name).read().splitlines()
    bookinfo = [line.replace('\t', '')]
    for line in bookinfo:
    print(line)
create_books_2Dlist('NYT_short.txt')
