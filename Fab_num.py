fib =[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
a, b = 1, 1
list_fib = []
while a <= 55:
    list_fib.append(a)
    a, b = b, a + b 
print(list_fib)