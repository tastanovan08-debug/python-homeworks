def isalpha1(s):
    if len(s) != 1:
        return False
    all_letters = ("ABCDEFGHIJKLMNOPQRST" + "abcdefghijklmnopqrst" + "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" + "абвгдежзийклмнопрстуфцчшщъыьэюя")
    for letter in all_letters:
        if letter == s:
            return True


#1
def analyze_text(text):
    text1 = text.lower()
    text2 = ""
    for alpha in text1:
        if isalpha1(alpha) or alpha == "":
            text2 += alpha
    dauysty = "aeiouy"
    new = ""
    for alpha in text2:
        if alpha in dauysty:
            new += alpha
    text3 = text2.split()


#1(dict and set)
def invert_unique(d):
    res = {}
    for key, value in d.items():
        if value not in res:
            res[value] = []
        if key not in res[value]:
            res[value].append(key)
    return res
d1 = {"a" : 1, "b" : 2, "c" : 1, "d" : 3}
print(invert_unique(d1))

#2
def calculate_average(nums):
    if not nums:
        return 0
    total = 0
    count = 0
    for num in nums:
        total += num
        count += 1
    return total / count

filter_numbers = lambda nums: {
    num for num in nums
    if num > calculate_average(nums)
    and num % 2 != 0
    and num % 5 != 0
}

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(filter_numbers(s1))

#3
def merge_dicts_sum(d1, d2):
    res = {}
