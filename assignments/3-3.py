x = input("Enter Score: ")
x=float(x)

if(x<0. or x>1.0):
    print('Not in range')
elif(x>=0.9):
    print('A')
elif(x>=0.8):
    print('B')
elif(x>=0.7):
    print('C')
elif(x>=0.6):
    print('D')
elif(x<0.6):
    print('F')
