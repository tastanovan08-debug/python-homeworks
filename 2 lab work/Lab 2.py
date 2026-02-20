#1
file = open("shop_logs.txt", "r")
users = set()
total_buys = 0
total_sum = 0
users_spending = {}
for line in file:
    parts = line.strip().split(";")
    user_id = parts[1]
    action = parts[2]
    users.add(user_id)
    if action == "BUY":
        total_buys += 1
        amount = int(parts[3])
        total_sum += amount
        if user_id not in users_spending:
            users_spending[user_id] = amount
        else:
            users_spending[user_id] += amount
file.close()
max_user = ""
max_spent = 0
for user in users_spending:
    if users_spending[user] > max_spent:
        max_spent = users_spending[user]
        max_user = user
if total_buys > 0:
    average = total_sum / total_buys
else:
    average = 0


result = open("result.txt", "w", encoding="utf-8")
result.write("Уникальных пользователей:" + str(len(users)) + "\n" )
result.write("Всего покупок:" + str(total_buys) + "\n")
result.write("Общая сумма:" + str(total_sum) + "\n")
result.write("Самый активный покупатель:" + max_user + "\n")
result.write("Средний чек:" + str(average) + "\n")

result.close()


#2
import csv
file = open("employees.csv", "r")
reader = csv.reader(file)
next(reader)
total_salary = 0
count = 0
departs = {}
names = []
max_zhumyshy = None
max_salary = None
for row in reader:
    zhumyshy = row[0]
    salary = int(row[2])
    department = row[1]
    names.append({
        "name": zhumyshy,
        "department": department,
        "salary": salary
    })
    total_salary += salary
    count += 1
    if department not in departs:
        departs[department] = []
        departs[department].append(salary)
    if max_salary is None or salary > max_salary:
        max_salary = salary
        max_zhumyshy = zhumyshy
average = total_salary / len(names)
print("Средняя зарплата: ", average)
print(departs)
departs_avg = {}
for dep in departs:
    dep_total = 0
    dep_count = 0
    for sal in departs[dep]:
        dep_total += sal
        dep_count += 1
    departs_avg[dep] = dep_total / dep_count
    print(f"{dep}: {departs_avg[dep]}")

best_department = None
best_avg = None

for dep in departs_avg:
    if best_avg is None or departs_avg[dep] > best_avg:
        best_avg = departs_avg[dep]
        best_department = dep

print("Отдел с самой высокой средней зарплатой:", best_department)

high_salary = []

for emp in names:
    if emp["salary"] > average:
        high_salary.append(emp)
        print(emp["name"], emp["salary"])
print(max_zhumyshy)
