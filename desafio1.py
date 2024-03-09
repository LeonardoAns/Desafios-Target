def fib(n):
    fib_list = [0,1]
    while len(fib_list) < n:
        nextFib = fib_list[-1] + fib_list[-2]
        fib_list.append(nextFib)
    return fib_list 

def verificador(num):
    fib_sequence = fib(n)
    if num in fib_sequence:
        return "O número {} pertence a sequencia".format(num)
    else:
         return "O número {} não pertence a sequencia".format(num)
    
n = int(input("Digite um número"))
print(verificador(n))