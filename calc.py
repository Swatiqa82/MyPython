
print ("Enter 1st Number:")
param1 = input()

print ("Enter 2nd Number:")
param2= input()


def myCalc(message):
    print message
    print ("Enter operations(eg:+,-,/,*)")           
    Oprand = raw_input()

    if Oprand == "+":
            print param1 + param2
    elif Oprand== "-":
            print param1- param2   
    elif Oprand== "*":
            print param1 * param2   
    elif Oprand== "/":
            print param1 / param2             
  
    else:
        print "Invalid Operation"
        return
    myCalc("Hi")

myCalc("Bye")

0