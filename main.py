#sequencia de fibonacci

#funcao que calcula a seq de fib
valor = int(input("Digite um valor: "))
def fib(valor):
    anterior_index = 0
    atual_index = 1
    seq_fib = [0,1]
    state = True
    while(state):
        prox = seq_fib[anterior_index] + seq_fib[atual_index]
        seq_fib.append(prox)
        print(seq_fib)
        if valor in seq_fib:
            state = False
            return True
        elif seq_fib[-1] > valor:
            state = False
            return False
        anterior_index += 1
        atual_index += 1


print(fib(valor))

#verificar a string
def ver_string(string_qualquer):
    string_qualquer= string_qualquer.lower()
    for i in string_qualquer:
        if i == "a":
            return True
    return False

palavra = input("Digite uma string qualquer:")

print(ver_string(palavra))

#ex3
def ex3():
    index = 12
    sum =0
    k = 1
    while k<index:
        k +=1
        sum +=k
        print(sum)
ex3()
