import csv
import matplotlib.pyplot as plt

def average(ls):
    total = 0
    for num in ls:
        total = total + num
    return total / len(ls)

def prop_above(ls):
    avg = average(ls)
    count = 0

    for num in ls:
        if num > avg:
            count = count + 1

    return count / len(ls)

def median(ls):
    sorted_ls = sorted(ls)
    n = len(sorted_ls)

    if n % 2 == 1:
        return sorted_ls[n // 2]
    else:
        middle1 = sorted_ls[n // 2 - 1]
        middle2 = sorted_ls[n // 2]
        return (middle1 + middle2) / 2



hours = []

with open("StudentExercise.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        hr = row[0]
        if hr != '':
            hours.append(float(hr))

print(hours)

plt.hist(hours)
plt.xlabel("Hours of Exercise per Week")
plt.ylabel("Number of Students")
plt.title("Student Exercise Hours")
plt.show()


print("Average exercise hours:", average(hours))
print("Proportion above average:", prop_above(hours))

print("Median exercise hours:", median(hours))

