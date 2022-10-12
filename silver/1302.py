#1302
numberOfBooksSold = int(input())
nameOfBooks = []
countOfBooks = []

for _ in range(numberOfBooksSold):
    nameOfBooks.append(input())

bookSeted = list(set(nameOfBooks))
bookSeted = sorted(bookSeted)

for name in bookSeted:
    countOfBooks.append(nameOfBooks.count(name))

print(bookSeted[countOfBooks.index(max(countOfBooks))])