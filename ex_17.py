import random
number=[]
for i in range(8):
    num = random.randint(1,100)
    number.append(num)
print(number)
biggest_number=number[0]
lowest_number=number[0]
for i in number:
    if (i > biggest_number):
        biggest_number=i
    elif(i< lowest_number):
        lowest_number=i
print("the biggest number is :",biggest_number)
print("the lowest_number is :",lowest_number)


