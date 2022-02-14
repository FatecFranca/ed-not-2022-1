""" Função para calcular o Índice de Massa Corpórea (IMC) """
def imc(peso, altura): # DECLARAÇÃO DA FUNÇÃO
    return peso / (altura ** 2)
    
    
#print(f"Peso: 89, altura: 1.75, IMC: {imc(89, 1.75)}")

#p = float(input("Qual o peso?"))
#a = float(input("Qual a altura?"))
#i = imc(p, a) # CHAMADA DA FUNÇÂO
#print(f"peso: {p}, altura: {a}, IMC: {imc(p, a):.3f}")

#IMPORTA O NUMERO PI
from math import pi

""" Função que calcula a área de uma forma geometrica especifica """
def calcular_area (base, altura, forma):
    if forma == "R": #RETÂNGULO
        return base * altura
    elif forma == "T": #TRIÂNGULO
        return base * altura / 2
    elif forma == "E": #ELIPSE
        return (base / 2) * (altura / 2) * pi #NUMERO PI
    else: #FORMA DESCONHECIDA
        return None
        
        
#EXEMPLOS DE CHAMADA DA FUNÇÃO calcular_area
print(f"Retângulo 15x25: {calcular_area (15, 25, 'R')}")
print(f"Triângulo 12x16: {calcular_area (12, 16, 'T')}")
print(f"Elipse 10x20: {calcular_area (10, 20, 'E')}")
