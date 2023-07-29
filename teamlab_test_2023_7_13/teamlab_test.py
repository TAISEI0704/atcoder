#Q1
x = 387420489

for i in range(42):
    x = int(x*0.8)

print(x)

#Q2
result = 0.0

for i in range(1, 12346):
    if i % 3 == 1 or i % 3 ==2:
        continue
    result += (i-2) * (i-1) / (i)

result = int(result)

print(result)

#Q3
x = 0
for i in range(1,33334):
    if i % 3 == 0:
        x = x + i
    elif 100 <= i <= 999:
        x = x + i
    elif '3' in str(i):
        x = x + i
    else:
        continue
print(x)

#Q4
a = []

for i in range(1,1000001):
    total = 0
    for digit in str(i):
        total += int(digit)
    if i % total == 0:
        a.append(i)

print(len(a))





        

