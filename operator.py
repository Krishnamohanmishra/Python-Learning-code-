#Arithmetic Operators 
#( + , - , * , / , % , ** , // )  
a=2
b=2
print("a + b = " ,a+b) #additional
print("a - b = " ,a-b) #subtraction 
print("a * b = " ,a*b) #multiplication
print("a / b = " ,a/b) #division
print("a % b = " ,a%b) #modulus
print("a ** b = " ,a**b) #exponentiation 
print("a // b = " ,a//b) #floor division (interger value)

#comprison / Relational Operators 
#(== , != , > , < , >= , <= )

a=33
b=3
print("a == b = " ,a==b) #equal to 
print("a != b = " ,a!=b) #not equal to
print("a > b = " ,a>b)   #greater than 
print("a < b = " ,a<b)   #less than 
print("a >= b = " ,a>=b) #greater than or equal to
print("a <= b = " ,a<=b) #less than or equal to 

#assignment operators 
#(= , +# , -= , *= , /= , %= , //= , **= )

a=10
print("a = " ,a) 
a+=5
print("a += 5 = " ,a)
a-=5
print("a -= 5 = " ,a)
a*=5
print("a *= 5 = " ,a)
a/=5
print("a /= 5 = " ,a)
a%=5
print("a %= 5 = " ,a)
a//=5
print("a //= 5 = " ,a)
a**=2
print("a **= 2 = " , a)

#Logical Operators
#(and , or , not ) 


a=0
b=3
print("a and b = " ,a and b) #returns last true value but if any value is false it returns false
print("a or b = " ,a or b)   #returns first true value but if first / all vaues are false it returns false
print("not a = " ,not a)     #returns false 