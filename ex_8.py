signal=input('enter the colour of traffic signal :')
if(signal.lower()=='red'):
    print("STOP!")
elif(signal.lower()=='yellow'):
    print("Prepare to stop")
elif(signal.lower()=='green'):
    print("You can go")
else:
    print("Wrong input!")
