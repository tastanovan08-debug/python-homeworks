import csv
data = [
    ["Name", "Age"],
    ["Maral", "27"],
    ["Diana", "18"]
]
with open("data.csv", mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)


with open("first.txt", "w") as f:
    f.write("Hello World")

with open("second.txt", "w") as f2:
    for i in range(1, 11):
        f2.write(str(i) + "\n")

students = ["Diana", "Nazerke", "Maral", "Zere"]
with open("names.txt", "w") as f3:
    for student in students:
        f3.write(student.lower() + "\n")
with open("names.txt", "r", encoding="utf-8") as f3:
    for line in f3:
        print(line.strip().capitalize())