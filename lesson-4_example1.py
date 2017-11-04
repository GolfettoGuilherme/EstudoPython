#texto_string = "Devmedia\nis\n" + "a greate\n\tcompany"
#print(texto_string)

#print("\n" * 100) #quebra de linha por 100 vezes
#print("Devmedia is a great Company")

print("Test format strings")

myInt = 12345
myFloat = 3.14159
myString = "Devmedia is a great Company"

print("Int", myInt)
print("Decimal integer %d and another %d" % (myInt, myInt))
print("Hexadecimal int %x" % myInt)

print("Float", myFloat)
print("Default %f" % myFloat)
print("Exponencial %e" % myFloat)
print("Right justify (%10d)" % myFloat)
print("Left Justify (%-10d)" % myFloat)

print("Force nin digits %.9d" % myInt)
print("Three digits after decimal in flat %.3f" % myFloat)
print("Ten and Five characters allowed in string:")
print("(%.10s) (%.5s)" % (myString, myString))
