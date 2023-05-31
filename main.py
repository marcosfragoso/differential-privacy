from diffprivlib.mechanisms import Laplace
import numpy as np

def adicionar_ruido_idade(valor, sensibilidade, epsilon):
    while True: #Faz com que a idade esteja dentro da sensibilidade
    	ruido = Laplace(epsilon=epsilon, sensitivity=sensibilidade).randomise(0)  # Adiciona ruído de Laplace
    	valor_privado = valor + ruido
    	if valor_privado < valor + sensibilidade_idade and valor_privado > sensibilidade_idade - valor:
    	    return valor_privado
    

def adicionar_ruido_salario(valor, sensibilidade, epsilon):
    while True: #Faz com que o salário esteja dentro da sensibilidade
    	ruido = Laplace(epsilon=epsilon, sensitivity=sensibilidade).randomise(0)  # Adiciona ruído de Laplace
    	valor_privado = valor + ruido
    	if valor_privado < valor + sensibilidade_salario and valor_privado > sensibilidade_salario - valor:
    	    return valor_privado

dados_pessoais = [
    {'salario': 3500.34,'idade': 23}, 
    {'salario': 3300.55,'idade': 19}, 
    {'salario': 2600.89,'idade': 39},
    {'salario': 2700.98,'idade': 29}, 
    {'salario': 3300.43,'idade': 31}, 
    {'salario': 3500.33,'idade': 25}, 
    {'salario': 4200.12,'idade': 27}, 
    {'salario': 5600.83,'idade': 33}, 
    {'salario': 6200.34,'idade': 35}, 
    {'salario': 3000.01,'idade': 37}, 
    {'salario': 6400.00,'idade': 21}, 
]

sensibilidade_salario = 500 #O salário sempre estará dentro desse valor, maior ou menor
epsilon_salario = 1.0

sensibilidade_idade = 5 #A idade sempre estará dentro desse valor, maior ou menor
epsilon_idade = 1.0

dados_anonimos = []

for dado in dados_pessoais:
    salario_privado = adicionar_ruido_salario(dado['salario'], sensibilidade_salario, epsilon_salario)
    idade_privada = adicionar_ruido_idade(dado['idade'], sensibilidade_idade, epsilon_idade)

    dados_anonimos.append({'salario': salario_privado, 'idade': idade_privada})

for i in range(len(dados_pessoais)):
    print('-=' * 40)
    print(f"| Idade original =  {dados_pessoais[i]['idade']:>10} | Idade privada = {dados_anonimos[i]['idade']:>10.0f}")
    print(f"| Salário original ={dados_pessoais[i]['salario']:>10} | Salário privado = {dados_anonimos[i]['salario']:>10.2f}")

