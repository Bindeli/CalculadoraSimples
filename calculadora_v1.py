# Calculadora em Python

#Uma calculadora simples que irei melhorando e deixando-a avançada.

print("\n******************* Python Calculator *******************")

def soma(x,y):
    return x + y

def subtrair(x,y):
    return x - y

def multiplicar(x,y):
    return x * y

def dividir(x,y):
    return x % y


print("\nSelecione umas dessas operações:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

Valor_Selecionado = int(input("\nDigite a opção que deseja (1,2,3,4): "))

Valor1 = int(input("\nDigite o primeiro número: "))

Valor2 = int(input("\nDigite o segundo número: "))

if Valor_Selecionado == 1:
    
	print("\n",Valor1, "+", Valor2, "=", soma(Valor1,Valor2))
    
elif Valor_Selecionado == 2:
    
	print("\n",Valor1,"-",Valor2, "=", subtrair(Valor1,Valor2))
    
elif Valor_Selecionado == 3:
    
	print("\n",Valor1,"*", Valor2, "=", multiplicar(Valor1,Valor2))
    
elif Valor_Selecionado == 4:
	print("\n",Valor1, "%", Valor2, "=", dividir(Valor1,Valor2))
    
else:
	print("Opção incorreta!")

