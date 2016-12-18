# lesson 2 - number operations and strings


print("Part 1: Number operations")
#integers
a = 123
b = 3


#floats
c = 12.3
d = -0.3

print(a + b)
print(a - b)
print(a * b)
print(a / b) # float value

# Except for divisions, Integer operations between two integers will result in an integer

print(a ** b) # a ^ b = 123 ^ 3 = 123 * 123 * 123

print(a / 4)    # 30.75
print(a // 4)   # integer division: truncates (a / 4) = 30
                #(i.e. remove decimal part of a / 4)

print(a % 4)    # 3(i.e. remainder of a // 4 )
print(a % b)    # 0(no remainder: 123/ 3 = 41 Remainder0)
                # % is called the modulus operator


print(2e100)    # 2 x 10^100

# Last Class
# float + float
# 1. Any operations with two floats will result in float. (e.g. 12.4 + 0.6 = 13.0)
# 2. Any operation with a float and an integer will result in a float. (e.g. 9.0 * 9 = 81.0)

# ---- End of Number Operations ---




print('Part 2: String operations')

c = "Hello"     #replace float values of c and d with strings
d = "World"     # Hello

print(type(c))  #str

# Two ways to make strings
print("This is Colin's dog named Frank.")
print('Mom said, "Take out the garbage."')

print(c + d)    #HelloWorld 
print(d + c)    #WorldHello

# How do you print "Hello World!" with c and d?

print(c + " " + d + "!")

# print(c - d) does not work
# print(c * d) does not work
# print(c / d) does not work
# print(c + 3) does not work

print(c * 3)    # Can't print when decimal or number less than 1 (e.g. c * 3.5, c -1, c * 0)

print("6" + "6")    #12? No, it prints 66

#Summmary for String Operations:
# 1. You can only add two strings, which joins the strings together. Order matters.
# 2. Other operations with two strings do not work
# 3. You can multiply a string by an integer, which repeats the string when int > 0.
# 4. You cannot do any operation to a string with a number, exception

# Homework: Explore the modulo operation (%).
# 1. What happens when one number is negative?
#   a) a % b when a < 0 and b > 0. Also check a // b.
print(-17 % 4)   # F-val is positive
print(-24 // 3) #F-val is negative

#   b) a % b when a > 0 and b < 0. Also check a // b.
print(16 % -3) #F-val is negative
print(4 // -3)  #F-val is negative

# 2. What happens when both negative?
print(-3 % -4) #F- val is negative

# 3. What happens when one number is float? re: -ve
print(2.0 % 1.) #Final become a float
print(-8. % -2.0)   #Final value becomes a negative float

# 4. What happens when both float? Consider -ve floats
print(4.0 %2.0)     # Final Value is positive float 
print(-12.0 % -6.0)     # Final value is negative float



