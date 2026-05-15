def isalpha1(s):
    if len(s) != 1:
        return False
    all_letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz" + "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" + "абвгдежзийклмнопрстуфцчшщъыьэюя")
    for letter in all_letters:
        if letter == s:
            return True
    return False

def isdigit1(s):
    if len(s) != 1:
        return False
    all_letters = ("1234567890")
    for letter in all_letters:
        if letter == s:
            return True
    return False

#1
def analyze_text(text):
    dauysty = "aeuioy"
    seen = []
    cleaned = ""
    for letter in text:
        if isalpha1(letter):
            cleaned += letter.lower()
        else:
            cleaned += " "
    words = cleaned.split()
    for letter in cleaned:
        i = 0
        while i < len(dauysty):
            if letter == dauysty[i]:
                if letter not in seen:
                    seen.append(letter)
            i += 1
    res = []
    for word in words:
        if len(word) >= 5 and word[0] == word[-1]:
            if word not in res:
                res.append(word)
    return (len(seen), " ".join(res))
print("task 1: ", analyze_text("This is yummy"))

#2
task_2 = lambda s: " ".join(
    map(lambda w: w[::-1],
        filter(lambda w: len(w) % 2 == 0,
               filter(lambda w: not any(isdigit1(l) for l in w),
                      s.split())))
)
print("task 2: ", task_2("My name is Naz , I am 17"))

#3
def top_k_words(text, k):
    clean = ""
    for ch in text.lower():
        if isalpha1(ch) or ch == " ":
            clean += ch
        else:
            clean += " "
    words = clean.split()
    uniq = []
    counts = []
    for w in words:
        i = 0
        found = False
        while i < len(uniq):
            if uniq[i] == w:
                counts[i] += 1
                found = True
            i += 1
        if not found:
            uniq.append(w)
            counts.append(1)
    i = 0
    while i < len(uniq):
        j = 0
        while j < len(uniq)-1:
            if counts[j] < counts[j+1] or (counts[j] == counts[j+1] and uniq[j] > uniq[j+1]):
                counts[j], counts[j+1] = counts[j+1], counts[j]
                uniq[j], uniq[j+1] = uniq[j+1], uniq[j]
            j += 1
        i += 1
    return uniq[:k]
print("task 3: ", top_k_words("Today is sunny day , I like sunny day", 2))

#4
task_4 = lambda s: " ".join(
    map(lambda w: w.lower(),
        filter(lambda w: sum(1 for c in w if 'A' <= c <= 'Z') == 1
               and not ('A' <= w[0] <= 'Z')
               and not ('A' <= w[-1] <= 'Z'),
               s.split()))
)
print("task 4: ", task_4("Hello I like chOcolate"))

#5
def compress_text(text):
    if text == "":
        return ""
    res = ""
    count = 1
    for i in range(1, len(text)):
        if text[i].lower() == text[i - 1].lower():
            count += 1
        else:
            res += text[i - 1]
            if count > 1:
                res += str(count)
            count = 1
    res += text[-1]
    if count > 1:
        res += str(count)
    return res
print("task 5: ", compress_text("aaBBcDDD"))

#6
task_6 = lambda s: list(
    filter(lambda w: len(w) >= 4 and
                     not any(isdigit1(c) for c in w) and
                     len(set(w)) == len(w),
           s.split())
)
print("task 6: ", task_6("I am 17 years old"))

#8
task8 = lambda s: " ".join(
    map(lambda w: w if any(isdigit1(c) for c in w)
        else ("VOWEL" if w[0].lower() in "aeiouy" else "CONSONANT"),
        s.split())
)
print("task 8: ", task8("I am 17 years old"))

#9
def alternate_case_blocks(text, n):
    res = ""
    block = 0
    i = 0
    while i < len(text):
        part = text[i:i+n]
        if block % 2 == 0:
            res += part.upper()
        else:
            res += part.lower()
        block += 1
        i += n
    return res.replace(" ", "")
print("task 9: ", alternate_case_blocks("I am 17 years old", 2))

#10
task10 = lambda s: sum(
    1 for w in s.split()
    if any(isdigit1(c) for c in w)
    and not isdigit1(w[0])
    and len(w) >= 5
)
print("task 10: ", task10("My name is Na7erke"))

#11
def common_unique_chars(s1, s2):
    res = ""
    for c in s1:
        if c != " " and not isdigit1(c):
            if c in s2 and c not in res:
                res += c
    return res
print("task 11: ", common_unique_chars("nazerke", "zere"))

#12
task12 = lambda s: list(
    filter(lambda w: len(w) > 3 and w[0] == w[-1] and w != w[::-1],
           s.split())
)
print("task 12: ", task12("This is yummy"))

#13
def replace_every_nth(text, n, char):
    res = ""
    count = 0
    for i in range(len(text)):
        c = text[i]

        if c != " ":
            count += 1

        if count % n == 0 and c != " " and not isdigit1(c):
            res += char
        else:
            res += c
    return res
print("task 13: ", replace_every_nth("My name is Nazerke", 3, "o"))

#14
task14 = lambda s: ",".join(
    filter(lambda w: len(set(w)) > 3 and
                     all(w.count(v) <= 1 for v in "aeiouy"),
           s.split())
)
print("task 14: ", task14("I live in Almaty"))

#16
def transform_list(nums):
    result= []
    for i in nums:
        if i<0:
            continue
        if i%2 == 0:
            result.append(i**2)
        elif i>10:
            summa= 0
            x= i
            while x>0:
                summa += x%10
                x //= 10
            result.append(summa)
        else:
            result.append(i)
    return result

nums= [1, 2, 3, 6, 9, 7]
print("task 16: ", transform_list(nums))

#17
result= lambda nums: list(
    map(
        lambda x: x**2,
        filter(
            lambda x: (x%3 == 0 or x%5 == 0)
                      and x%15 != 0
                      and len(str(abs(x)))%2 == 1,
            nums
        )
    )
)

nums= [1, 2, 3, 103, 405]
print("task 17: ", result(nums))

#18
def flatten_and_filter(lst):
    result= []

    def flatten(sublist):
        for item in sublist:
            if isinstance(item, list):
                flatten(item)
            elif isinstance(item, int):
                if (
                    item > 0 and
                    item%4 != 0 and
                    len(str(item)) > 1
                ):
                    result.append(item)

    flatten(lst)
    result.sort()
    return result

data= [1, [12, -5, [33, 8], 44], [[101, 3], 16], 25]
print("task 18: ", flatten_and_filter(data))

#19
result= lambda lst1, lst2: list(
    filter(
        lambda x: x%2 == 0,
        map(
            lambda pair: pair[0],
            filter(
                lambda pair: pair[0] == pair[1],
                zip(lst1, lst2)
            )
        )
    )
)

print("task 19: ", result([2, 3, 5, 6, 8], [2, 5, 4, 6, 9]))

#20
def max_subarray_sum(nums, k):
    if k > len(nums) or k <= 0:
        return None
    max_sum= None
    for i in range(len(nums) - k+1):
        window= nums[i:i+k]
        valid= True
        current_sum= 0

        for num in window:
            if num <= 0:
                valid= False
                break
            current_sum += num

        if valid:
            if max_sum is None or current_sum > max_sum:
                max_sum= current_sum
    return max_sum

print("task 20: ", max_subarray_sum([1, 2, 3, -2, 5], 2))

#21
result21= lambda strings: list(
    map(
        lambda s: s.upper(),
        filter(
            lambda s: (
                s.isalpha() and
                len(s) > 4 and
                len(set(s)) == len(s)
            ),
            strings
        )
    )
)


print("task 21: ", result21(["Hello", "world", "Python", "Nazerke", "Code"]))

#22
def group_by_parity_and_sort(nums):
    evens= []
    odds= []

    for num in nums:
        if num%2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    evens.sort()
    odds.sort()

    return evens+odds

print("task 22: ", group_by_parity_and_sort([1, 2, 5, 8, 9, 4, 3]))

#24
def longest_increasing_sublist(nums):
    if not nums:
        return []
    max_sublist= []
    current_sublist= [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_sublist.append(nums[i])
        else:
            if len(current_sublist) > len(max_sublist):
                max_sublist= current_sublist
            current_sublist= [nums[i]]
    if len(current_sublist) > len(max_sublist):
        max_sublist= current_sublist
    return max_sublist
print("task 24: ", longest_increasing_sublist([1, 2, 3, 2, 3, 4, 1, 2]))

#25
from functools import reduce
result25= lambda lst: list(
    map(
        lambda sub: reduce(lambda a, b: a+b, sub)/len(sub),
        filter(
            lambda sub: len(sub) >= 3 and reduce(lambda a, b: a+b, sub)%2 == 0,
            lst
        )
    )
)

print("task 25: ", result25([[1, 2, 3], [2, 4, 6], [1, 1], [5, 5, 2]]))

#26
def remove_duplicates_keep_last(nums):
    seen = []
    result_reversed = []
    for num in reversed(nums):
        if num not in seen:
            seen.append(num)
            result_reversed.append(num)
    result = []
    for num in reversed(result_reversed):
        result.append(num)
    return result
print("task 26: ", remove_duplicates_keep_last([1, 2, 3, 2, 4, 1, 5]))

#27
result27= lambda strings: sorted(
    strings,
    key=lambda s: (-len(s), s)
)[:5]
print("task 27: ", result27(["apple", "banana", "kiwi", "cherry", "date", "grapefruit"]))

#28
def moving_average(nums, k):
    if k <= 0 or k > len(nums):
        return []
    averages= []
    for i in range(len(nums) - k+1):
        window= nums[i:i+k]
        if any(n < 0 for n in window):
            continue
        total= 0
        for n in window:
            total += n
        avg= total/k
        averages.append(avg)
    return averages
print("task 28: ", moving_average([1, 2, 3, -1, 4, 5, 6], 3))

#29
result29= lambda lst1, lst2: list(
    filter(
        lambda x: x > (sum(lst1)/len(lst1)) and x not in lst2,
        lst1
    )
)
print("task 29: ", result29([1, 4, 6, 8, 10], [4, 10]))

#30
def analyze_strings_list(words):
    seen= set()
    result= []
    for word in words:
        if any(char.isdigit() for char in word):
            continue
        if len(word)%2 == 0:
            processed= word[::-1]
        else:
            processed= word.upper()
        if processed not in seen:
            seen.add(processed)
            result.append(processed)
    return result
words= ["hello", "w0rld", "python", "code", "hello", "data", "B1"]
print("task 30: ", analyze_strings_list(words))



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
print("task 1: ", invert_unique(d1))

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
print("task 2: ", filter_numbers(s1))

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
print("task 3: ", merge_dicts_sum(dict1, dict2))

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
print("task 4: ", filter_sets(sets))

#5
dict_sorted = lambda d:(

)

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

print("task 6: ", deep_sum({
    'a': 1, 'b': 2, 'c': [3, 4], 'd': {"e": 1, "f": 4}
}))

#7
task_7 = lambda s1, s2: {x for x in (s1 ^ s2) if x % 2 == 0}
A = {1, 2, 3, 4, 5}
B = {1, 3, 6, 9, 12}
print("task 7: ", task_7(A, B))

#8
def sort_dict_by_value_length(d):
    items = list(d.items())
    for i in range(len(items)):
        for j in range(len(items) - 1):
            if (len(items[j][1]) > len(items[j + 1][1])) or \
                    (len(items[j][1]) == len(items[j + 1][1]) and items[j][0] > items[j + 1][0]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items
res5 = {
    "a" : "hello",
    "b" : "world!",
    "c" : "Naz",
    "d" : "Diana",
    "e" : "Maral",
    "f" : "Zere"
}
print("task 8: ", sort_dict_by_value_length(res5))

#9
def common_elements_all(sets_list):
    if len(sets_list) == 0:
        return set()
    res = set()
    first_set = sets_list[0]

    for element in first_set:
        in_all = True

        for s in sets_list:
            if element not in s:
                in_all = False
                break

        if in_all:
            res.add(element)
    return res
res6 = [
    (1, 2, 3),
    (3, 4, 5, 2),
    (3, 2, 6)
]
print("task 9: ", common_elements_all(res6))

#10
def filter_lists(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
filter_dict10 = lambda d: {
    k: filter_lists([x for x in v if x%2 != 0])
    for k,v in d.items()
    if len([x for x in v if x % 2 != 0]) > 0
}
task_10 = {
    "a" : [1, 2, 3, 4],
    "b" : [1, 2, 3, 5],
    "c" : [3, 6, 9, 12]
}
print("task 10: ", filter_dict10(task_10))

#11
def group_by_length(words):
    res = {}
    for word in words:
        length = len(word)
        if length not in res:
            res[length] = []
        res[length].append(word)
    return res

task_11 = ["apple", "Almaty", "Nazerke"]
print("task 11: ", group_by_length(task_11))

#12
filter_strings = lambda s: {
    x for x in s
    if len(x) > 4
    and len({c for c in x}) == len(x)
    and all(('a' <= c <= 'z') or ('A' <= c <= 'Z') for c in x)
}

task_12 = {"apple", "Nazerke", "Ersultan", "house"}
print("task 12: ", filter_strings(task_12))

#13
def invert_dict_strict(d):
    counts = {}
    for v in d.values():
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    res = {}
    for k, v in d.items():
        if counts[v] == 1:
            res[v] = k
    return res
task_13 = {
    "1" : "Naz",
    "2" : "Botagoz",
    "3" : "Botagoz",
    "4" : "Diana",
    "5" : "Zere",
    "6" : "Maral"
}
print("task 13: ", invert_dict_strict(task_13))

#14
def top_k_frequent(nums, k):
    res = set()
    count = 0
    x = {}
    for num in nums:
        if num in x:
            x[num] += 1
        else:
            x[num] = 1
    while count < k and len(x) > 0:
        best_num = None
        best = -1
        for num in x:
            if x[num] > best:
                best = x[num]
                best_num = num
            elif x[num] == best and num < best_num:
                best_num = num
        res.add(best_num)
        del x[best_num]
        count += 1
    return res

task_14 = [1, 1, 1, 3, 2, 4, 3]
print("task 14: ", top_k_frequent(task_14, 2))

#15
def filter_dict(d):
    total = 0
    count = 0
    for key in d:
        total += d[key]
        count += 1
    avg = total / count
    f = lambda d: {k: d[k] for k in d if d[k] >= avg and d[k] % 2 != 0}
    return f(d)

task_15 = {
    "Naz": 17,
    "Maral" : 13,
    "Diana" : 18,
    "Zere" : 12,
    "Botagoz" : 20

}
print("task 15: ", filter_dict(task_15))

#17
task=lambda set1,set2,set3:(set1&set2)-set3
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {5, 6, 9, 10}
result17=task(A,B,C)
print("task 17: ", result17)

#19
def filter_by_digit_sum(nums):
    result =set()
    for num in nums:
        if num%2!=0:
            n=num
            total_sum=0
            if n<0:
                n=-n
            while n>0:
                total=n%10
                total_sum+=total
                n=n//10
            if total_sum%2==0:
                result.add(num)
    return result
nums={15,12,21,44,34,37}
print("task 19: ", filter_by_digit_sum(nums))

#20
task20 = lambda d: [k for k, v in sorted(d.items(), key=lambda item: (item[1], len(item[0])))][:3]
d1 = {
    "apple": 5,
    "banana": 2,
    "kiwi": 5,
    "pear": 3,
    "plum": 2
}
result20 = task20(d1)
sorted_items = sorted(d1.items(), key=lambda item: (item[1], len(item[0])))
print("task 20: ", result20)

#21
def count_leaf_values(d):
    count=0
    for key in d:
        value=d[key]
        if type(value)==dict:
            count+=count_leaf_values(value)
        else:
            count+=1
    return count
d1={
    "apple": 5,
    "banana": [1,2,3],
    "kiwi": {
        "d":10,
        "e":{
            "f":20,
        }
    }
}
result_21 = count_leaf_values(d1)
print("task 21: ", result_21)


#22
a=lambda x1,x2:{
    x for x in x1
    if x not in x2 and x>(lambda t:(
        (lambda total=0: (
            (lambda s=0: (
                s
            ))()
        ))()
    ))(x2)
}
b={3,5,7,10}
d={2,4,6}
print("task 22: ", a(b,d))


#23
def group_by_last_letter(words):
    result={}
    for word in words:
        last=word[-1]
        if last not in result:
            result[last]=[]
        if word not in result[last]:
            result[last].append(word)
    return result
words=["diana","maral","bota","asyl","zere","nazerke"]
print("task 23: ", group_by_last_letter(words))


#24
def union_of_filtered_sets(sets_list):
    result=set()
    for s in sets_list:
        for num in s:
            if num >10 and num%2!=0:
                result.add(num)
    return result
sets_list=[
    {5,11,20},
    {13,8,25},
    {7,30,15}
]
print("task 24: ", union_of_filtered_sets(sets_list))


#25
task25=lambda d:{
    k: __import__("functools").reduce(lambda a,b:a*b,[x for x in v if x>0])
    for k,v in d.items()
    if len([x for x in v if x>0])>0
}
data={
    "a": [1,2,-3],
    "b": [-6,-9],
    "c": [2,4],
}
print("task 25: ", task25(data))

#27
is_prime=lambda n: n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
filter_d=lambda d:{k:v for k,v in d.items() if len(k)%2==1 and is_prime(v)}
data27={
    "a": 2,
    "diana":5,
    "sum":4,
    "asd":5
}
print("task 27: ", filter_d(data27))


#28
def sorted_unique_chars(d):
    chars=set()
    for a in d:
        for b in a:
            if b<'0' or b>'9':
                if b !='':
                    chars.add(b)
    return sorted(chars)
d28=["diana","nazerke","zere2","a l a"]
print("task 28: ", sorted_unique_chars(d28))


#29
sort_keys_by_last_digit=lambda a: sorted(a.keys() ,key=lambda k:(a[k]%10,k))
data29={
    "apple": 23,
    "diana":15,
    "zere":32,
    "almaty":25,
}
print("task 29: ", sort_keys_by_last_digit(data29))

#1 Big Data
def analyze_students(data):
    students = []
    count = {}
    all_vowels = []
    vowels = "aeyuio"
    k = 0
    while k < len(data):
        name = data[k]["name"]
        has_digit = False
        for letter in name:
            if isdigit1(letter):
                has_digit = True

        if has_digit:
            k += 1
            continue
        name = name.title()
        grades = data[k]["grades"]
        proc = []
        j = 0
        while j<len(grades):
            g=grades[j]
            if g<=0:
                j+=1
                continue
            if g%2==1 and g<10:
                s=0
                n=g
                while n>0:
                    s+=n%10
                    n//=10
                proc.append(s)
            elif g%2==0 and g>=10:
                proc.append(g*g)
            else:
                proc.append(g)
            j+=1
        text=" ".join(data[k]["comments"]).lower()
        word=text.split()
        unique=[]
        for w in word:
            if len(w)>=4 and w!=w[::-1]:
                exis=False
                for v in unique:
                    if v==w:
                        exis=True
                if not exis:
                    unique.append(w)
        for w in unique:
            if w in count:
                count[w]+=1
            else:
                count[w]=1
            for i in w:
                for t in vowels:
                    if i.lower()==t:
                        found=False
                        for v in all_vowels:
                            if v==t:
                                found=True
                        if not found:
                            all_vowels.append(t)
        students.append({
            "name":name,
            "processed":proc
        })
        k+=1
    return {
        "students":students,
        "count":count,
        "all_vowels":all_vowels
    }
data=[
    {
        "name":"Zere2008",
        "grades":[12,9,15,8],
        "comments":["Good work","excellent effort","Needs Improvement"]
    },
    {
        "name":"Diana",
        "grades":[10,5,-2,7],
        "comments":["Good job","very nice work","you have high level"]
    },
    {
        "name":"Maral",
        "grades":[14,3,11],
        "comments":["Excellent progress","Good work", "Needs Improvement"]
    }
]
print("1: ", analyze_students(data))

#2 Big Data
def analyze_orders(a):
    pro_order=[]
    count={}
    all_vowels=[]
    unique=[]
    vowels="oiuyea"
    k=0
    while k<len(a):
        order=a[k]
        customer=order["customer"]
        digit=False
        for i in customer:
            if "0"<=i<="9":
                digit=False
                break
        if digit:
            k+=1
            continue
        customer=customer.title()
        pro=[]
        summa=0
        j=0
        while j<len(order["items"]):
            item=order["items"][j]
            name=item["name"]
            price=item["price"]
            quantity=item["quantity"]
            if price <=0:
                j+=1
                continue
            if quantity%2==1:
                n=int(price)
                summa=0
                while n>0:
                    summa+=n%10
                    n//=10
                price=price+summa
            pro.append({
                "name":name,
                "price":price
            })
            summa+=price
            exis=False
            c=0
            while c<len(unique):
                if unique[c]==name:
                    exis=True
                c+=1
            if not exis:
                unique.append(name)
            j+=1
        text=" ".join(order["notes"])
        words=text.split()
        un_word=[]
        j=0
        while j<len(words):
            w=words[j]
            if len(w)>=4 and w!=w[::-1]:
                exis=False
                c=0
                while c<len(un_word):
                    if un_word[c]==w:
                        exis=True
                    c+=1
                if not exis:
                    un_word.append(w)
            j+=1
        j=0
        while j<len(un_word):
            w=un_word[j]
            if w in count:
                count[w]+=1
            else:
                count[w]=1
            m=0
            while m<len(w):
                i=w[m].lower()
                index=0
                while index<len(vowels):
                    if i==vowels[index]:
                        found=False
                        t=0
                        while t<len(all_vowels):
                            if all_vowels[t]==vowels[index]:
                                found=True
                            t+=1
                        if not found:
                            all_vowels.append(vowels[index])
                    index+=1
                m+=1
            j+=1
        pro_order.append({
            "order_id":order["order_id"],
            "customer":customer,
            "pro":pro,
            "total":summa
        })
        k+=1
    filtered={}
    for w in count:
        if count[w]>=2:
            filtered[w]=count[w]
    k=0
    while k<len(pro_order):
        best=k
        j=k+1
        while j<len(pro_order):
            if pro_order[j]["total"]>pro_order[best]["total"]:
                best=j
            elif pro_order[j]["total"]==pro_order[best]["total"]:
                if pro_order[j]["order_id"]<pro_order[best]["order_id"]:
                    best=j
            j+=1
        temp=pro_order[k]
        pro_order[k]=pro_order[best]
        pro_order[best]=temp
        k+=1
    or_total=[]
    k=0
    while k<len(pro_order):
        or_total.append(pro_order[k]["order_id"])
        k+=1
    or_item={}
    k=0
    while k<len(pro_order):
        amount=len(pro_order[k]["pro"])
        if amount in or_item:
            or_item[amount].append(pro_order[k]["order_id"])
        else:
            or_item[amount]=[pro_order[k]["order_id"]]
        k+=1
    return {
        "orders":pro_order,
        "word_counts":filtered,
        "all_vowels":all_vowels,
        "unique_products":unique,
        "orders_by_total":or_total,
        "orders_by_item_count":or_item
    }
data=[
    {
        "order_id":"A123",
        "customer":"maral_08",
        "items":[
            {"name":"Phone","price":999.99,"quantity":1},
            {"name":"Mouse2","price":25,"quantity":2}
        ],
        "notes":["fragile package","handle with care"]
    },
    {
        "order_id":"B456",
        "customer":"diana_smith",
        "items":[
            {"name":"Monitor","price":200,"quantity":2},
            {"name":"Keyboard","price":50,"quantity":1}
        ],
        "notes":["Tumar with care","fast delivery"]
    },
    {
        "order_id":"C789",
        "customer":"Zere008",
        "items":[
            {"name":"Laptop","price":900,"quantity":2}
        ],
        "notes":["fragile package","deliver tomorrow"]
    }
]
print("2: ", analyze_orders(data))