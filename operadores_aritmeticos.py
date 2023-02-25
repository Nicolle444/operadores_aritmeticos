 # Programa para implementar operadores aritmeticos

print("----------------------------------------")
print("---------OPERACIONES ARITMETICAS--------")
print("----------------------------------------")

 # input
x= int (input("Digite el valor de x"))
y= int (input("Digite el valor de y"))

# procesing
s = x + y
r = x - y
m = x * y
d = x / y
mod = x % y
de = x // y
p = x ** y

 # output
print("----------------------------------------")
print("--------------RESULTADOS----------------")
print("----------------------------------------")
print("Suma: "+ str(s))
print("Resta: "+ str(r))
print("Multiplicación: "+ str(m))
print("División: "+ str(d))
print("Módulo: "+ str(mod))
print("División entera: "+ str(de))
print("Potencia: "+ str(p))
