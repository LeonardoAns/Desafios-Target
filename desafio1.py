def fib(n):
    Fib = [0,1]
    while len(Fib) < n:
        nextFib = Fib[-1] + Fib[-2]
        Fib.append(nextFib)
    return Fib

def verificador(num):
    fib_sequence = fib(n)
    if num in fib_sequence:
        return "O número {} pertence a sequencia".format(num)
    else:
         return "O número {} não  a sequencia".format(num)
    
n = int(input("Digite um número"))

print(verificador(n))