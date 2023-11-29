x  = int(input("Enter first number :- "))
y  = int(input("Enter second number :- "))
my_operator = ['+' , '-' , '*' , '/' , 'to pwr']

for i, item in enumerate(my_operator, start=1):
    print('[', i, ']', item)

select_operator = int(input("select the operator :- "))

def addition():
    result = x + y
    print ("your result is " , result , sep= " ")

def subtraction():
    result = x - y
    print ("your result is " , result , sep= " ")

def multiply():
    result = x * y
    print ("your result is " , result , sep= " ")

def devision():
    result = float(x / y)
    print ("your result is " , result , sep= " ")

def expo():
    result = x ** y
    print ("your result is " , result , sep= " ")

if select_operator == 1:
    addition()

elif select_operator == 2:
    subtraction()

elif select_operator == 3:
    multiply()

elif select_operator == 4:
    devision()
 

elif select_operator == 5:
    expo()

else:
    print ('please select the correct operator')
 