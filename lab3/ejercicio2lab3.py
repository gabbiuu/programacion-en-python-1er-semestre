a = [10,9,12,15,18]
b= [21,8,15,3,12]
print()
ambaslistas= (a+b)
print(ambaslistas)
print()
ambaslistas.insert(1,30)
print(ambaslistas)
print()
ambaslistas.sort()
print(ambaslistas)
print()
ambaslistas.insert(11,4)
ambaslistas.insert(12,5)
ambaslistas.insert(13,6)
print(ambaslistas)
print()
print("La sumas de los numeros de la listas es: ",sum(ambaslistas))
media = sum(ambaslistas)/len(ambaslistas)
print("La media es : ",int(media))
print()

ambaslistas.sort()
print("La mediana es: ", ambaslistas[6]) 