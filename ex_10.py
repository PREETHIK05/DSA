c=float(input('enter temperature in Celsius:'))
Fahrenheit=(c*9/5)+32
if(Fahrenheit<0):
    print("Very cold! Wear thick jacket")
elif(Fahrenheit>=0 and Fahrenheit <= 15):
    print("Cold. Wear jacket")
elif(Fahrenheit>=16 and Fahrenheit <= 25):
    print("Nice weather")
elif(Fahrenheit>25):
    print("Hot! Stay hydrated")