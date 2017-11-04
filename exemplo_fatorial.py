factorial = int(input("Digite um número:"))

if (factorial > 0):
    passo = factorial
    total = factorial
    while (passo > 1):
        passo = passo - 1
        total = total * passo
    print("%d" % total)
elif(factorial == 0):
    print("1")
else:
    print("Erro")
