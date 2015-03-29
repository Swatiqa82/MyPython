#Write a program to print reverse string
#eg: input=swati output=itaws

myString= raw_input("Enter your string:")
print myString
 
#for C in myString:
#       print C
xyz=""

for i in range (len(myString)):
    #print i
    #print len(myString)-i-1
    #print myString [len(myString)-i-1]
    xyz=xyz+ myString[len(myString)-i-1]
    #xyz += myString[len(myString)-i-1]

print xyz