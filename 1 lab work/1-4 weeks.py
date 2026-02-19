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
    for key in d1:
        res[key] = d1[key]
    for key in d2:
        key_exists = False
        for result_key in res:
            if key == result_key:
                key_exists = True
                break
        if key_exists:
            res[key] = res[key] + d2[key]
        else:
            res[key] = d2[key]
    return res

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts_sum(dict1, dict2))

#4
def filter_sets(sets_list):
    res = []
    for set in sets_list:
       if len(set) > 3:
           negative = False
           even_number = False
           for num in set:
               if num < 0:
                   negative = True
               if num % 2 == 0:
                   even_number = True
           if even_number and not negative:
                res.append(set)
    return res

sets = [
    {1, 2, 3, 4},
    {-1, 2, 3, 4, 5},
    {1, 3, 5, 7},
    {1, 2, 3},
    {2, 4, 6, 8, 10},
    {0, 1, 2, 3, -5},
    {10, 20, 30, 40},
]
print(filter_sets(sets))

#6
def deep_sum(d):
    total = 0
    for value in d.values():
        if type(value) == int or type(value) == float:
            total += value
        elif type(value) == list:
            for x in value:
                if type(x) == int or type(x) == float:
                    total += x
        elif type(value) == dict:
            total += deep_sum(value)
    return total

print(deep_sum({
    'a': 1, 'b': 2, 'c': [3, 4], 'd': {"e": 1, "f": 4}
}))

#7
