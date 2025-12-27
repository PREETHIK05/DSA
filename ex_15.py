list = [12, 45, 3, 98, 7, 34, 21]
'''a . print each number 
for i in  list:
    print(i)'''
'''b. print numbers greater than 30
for i in  list:
    if(i>30):
        print(i)'''
count=0
for i in  list:
    if(i>30):
        count+=1
print('total no of numbers greater than 30 is:',count)