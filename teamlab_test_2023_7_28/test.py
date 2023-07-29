
# print(7**777)

number_int = int(7**777)

number_str = str(number_int)

l = [int(x) for x in list(number_str) ]

print(len(l))

# for i in range()
#     print(l[657//2-4])

mid = 657//2 - 4

while True:
    print(l[mid])
    mid+=1
    if mid > 657//2 + 4:
        break

 