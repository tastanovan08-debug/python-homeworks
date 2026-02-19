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
