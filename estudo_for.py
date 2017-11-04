print("Exemplo FOR com passo definido")

total = 0

number = int(input("Digite o numero"))

if(number % 2 == 0 ):
    number = number -1

for i in range(number, 0, -2):
    total = total + i
    print("numero", i)

print("soma:", total)
