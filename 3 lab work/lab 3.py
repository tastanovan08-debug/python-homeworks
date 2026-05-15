#1
check = lambda x : "положительное" if x > 0 else "отрицательное" if x < 0 else "ноль"
print(f"task 1: 5 = {check(5)}, -3 = {check(-3)}, 0 = {check(0)}")

#2
words = ["арбуз", "кот", "машина", "дом", "ананас"]
sorted_words = sorted(words, key=lambda word: (len(word), word))
print("task 2: ", sorted_words)

#3
numbers3 = [5, 12, 7, 20, 33, 8]
filtered_numbers = list(filter(lambda x: (x % 2 == 0 and x > 10), numbers3))
print("task 3: ", filtered_numbers)

#4
numbers_4 = [1, 2, 3, 4, 5, 6]
task_4 = list(map(lambda x : x**2 if x % 2 == 0 else 3*x, numbers_4))
print("task 4: ", task_4)

#5
compare = lambda a, b: "a больше" if a>b else "b больше" if b>a else "равны"
print(f"task 5: {compare(10, 7)}, {compare(3, 5)}, {compare(4, 4)}")

#6
numbers6 = [0, -3, 5, -7, 8]
new_list = list(map(lambda x: "положительное" if x > 0 else "отрицательное" if x < 0 else "ноль", numbers6))
print("task 6: ", new_list)

#1 Генераторы
def even_numbers(n):
    for i in range(2, n+1, 2):
        if i % 4 == 0:
            yield "кратно 4"
        else:
            yield i
print("task 7 : ")
for x in even_numbers(10):
    print(x)

#2
def filter_words(words):
    for word in words:
        if len(word) > 4:
            if "а" in word:
                yield "c a"
            else:
                yield word
print("task 8: ")
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)

#3
def infinite_numbers():
    i = 1
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i
        i += 1
print("task 9: ")
counter = 0
for value in infinite_numbers():
    print(value)
    counter += 1
    if counter >= 15:
        break

#4
def squares(n):
    for i in range(1, n+1):
        if (i**2) % 2 == 0:
            yield "чётный квадрат"
        else:
            yield i**2
print("task 10: ")
for x in squares(5):
    print(x)


#1 Итераторы и comprehension
numbers1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
squares = [n ** 2 for n in numbers1]
print("task 11: ", squares)

#2
matrix = [[1,2,3], [4,5,6], [7,8,9]]

#3
words = ["кот", "машина", "ананас", "дом", "цветы"]
new_words = [word for word in words if len(word) > 4 and "а" not in word]
print("task 13: ", new_words)

#4
numbers4 = [1,2,3,4,5]
even_or_odd = {n: "чётное" if n%2 == 0 else "нечётное" for n in numbers4}
print("task 14: ", even_or_odd)

#5
matrix = [[1,2], [3,4], [5,6]]
all_numbers = [num for numbers in matrix for num in numbers]
print("task 15: ", all_numbers)

#6
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = ["FizzBuzz" if n%3 == 0 and n%5 == 0 else "Fizz" if n%3 == 0 else "Buzz" if n%5 ==0 else n for n in nums]
print("task 16: ", result)


#1 Генератор и фильтр по сложному условию
def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def special_numbers(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        elif is_prime(i) == True:
            yield "простое"
        else:
            yield i
        i += 1
print("task 17:")
for x in special_numbers(15):
    print(x)

#2
words = ["кот", "машина", "арбуз", "дом", "ананас"]
res = [(lambda word: word.upper() + ("*" if "а" in word else " ") if len(word) > 4 else "short") (word) for word in words]
print("task 18: ", res)

#3
def process_numbers(numbers):
    a = filter(lambda x: x >= 0, numbers)
    for num in a:
        yield (lambda x: x/2 if x % 2 == 0 else (3*x) + 1)(num)
print("task 19: ")
numbers = [5, -2, 8, 0, -7, 3]
for x in process_numbers(numbers):
    print(x)

#4
students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
students_dict = lambda x: "Отлично" if x >= 90 else ("Хорошо" if x >= 70 else "Удовлетворительно")
result_stud = {name: students_dict(score) for name, score in students}
print("task 20: ", result_stud)

#5
def matrix_transform(matrix):
    for row in matrix:
        for num in row:
            if num % 2 == 0 and num % 3 == 0:
                yield "кратно 6"
            elif num % 2 == 0:
                yield "чётное"
            elif num % 3 == 0:
                yield "кратно 3"
            else:
                yield num
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("task 21:")
for x in matrix_transform(matrix):
    print(x)

#1 Задачи для понимания map and filter
numbers_map = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers_map))
print("task 22: ", doubled)

#2
words = ["кот", "машина", "арбуз", "дом"]
result_upper = list(map(lambda w: w.upper() + "!" if len(w) > 3 else w.upper(), words))
print("task 23: ", result_upper)

#3
numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers_3))
print("task 24: ", evens)

#4
numbers_4 = [0, 5, 12, 7, 20, -3, 8]
result_num = list(
    map(lambda x: x / 2 if x % 2 == 0 else x * 3,
        filter(lambda x: x > 5, numbers_4))
)
print("task 25: ", result_num)

