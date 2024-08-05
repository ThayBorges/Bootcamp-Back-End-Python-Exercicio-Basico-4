'''Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.

Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta.
'''

def celsius_para_fahrenheit(celsius):
    """
    Converte a temperatura de Celsius para Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """
    Converte a temperatura de Fahrenheit para Celsius.
    """
    return (fahrenheit - 32) * 5/9

def menu():
    """
    Exibe o menu e chama a função de conversão apropriada com base na escolha do usuário.
    """
    print("Escolha a conversão desejada:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    
    escolha = input("Digite o número da opção desejada (1 ou 2): ")
    
    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

# Chama a função do menu para iniciar o programa
menu()