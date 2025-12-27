grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
A=0
B=0
C=0
# got below 70
F=0
for i in grades:
    if(i>=90):
        A+=1
    elif (i>=89 and i<=80):
        B+=1
    elif (i>=79 and i<=70):
        C+=1
    else:
        F+=1
print('the no of students got A is:',A)
print('the no of students got B is:',B)
print('the no of students got C is:',C)
print('the no of students got F is:',F)


