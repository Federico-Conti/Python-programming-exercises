#Question: Write a program which will find all such 
# numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers obtained should 
# be printed in a comma-separated sequence on a single line.

#Hints: Consider use range(#begin, #end) method
print("\nQuestion 1\n")
list =[]
for num in range(2000,3201):
   if (num%7==0 and num%5 != 0):
     list.append(num) #l.append(str(i))

print(*list, sep=",") #print(','.join(l))


# Question: Write a program which can compute the factorial of a given numbers. 
# The results should be printed in a comma-separated sequence on a single line. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
print("\nQuestion 2\n")
def fact(x):
  if(x == 0):
    return 1
  return x*fact(x-1)

#x=int(input())
print(fact(5))

#Question: With a given integral number n, write a program to generate a 
# dictionary that contains (i, i*i) such that is an integral number 
# between 1 and n (both included). and then the program should print 
# the dictionary. Suppose the following input is supplied to the 
# program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

#Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input. Consider use dict()
print("\nQuestion 3\n")

n=8
d=dict()
for i in range(1,n+1):
    d[i]=i*i

print(d)

# Question: Write a program which accepts a sequence of comma-separated numbers 
# from console and generate a list and a tuple which contains every number. 
# Suppose the following input is supplied to the program: 34,67,55,33,12,98 
# Then,the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

#Hints: In case of input data being supplied to the question, 
# it should be assumed to be a console input. tuple() method can convert list to tuple

print("\nQuestion 4\n")

values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)
