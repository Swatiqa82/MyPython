
def cube(number):
    #return number*number*number
    return number**4
def by_three(number):
    if number%3==0:
       return cube(number)
    else:
        return False
        
print by_three(5)
print by_three(3)
    