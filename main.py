from diffprivlib.mechanisms import Laplace
import numpy as np

def adicionar_ruido_diferencial(valor, sensibilidade, epsilon):
    ruido = Laplace(epsilon=epsilon, sensitivity=sensibilidade).randomise(0)  # Adiciona ruído de Laplace
    valor_privado = valor + ruido
    return max(0, valor_privado)  # Garante que o valor não seja negativo

dados_pessoais = [
    {'salario': 3500,'idade': 23}, 
    {'salario': 3300,'idade': 19}, 
    {'salario': 2600,'idade': 39},
    {'salario': 2700,'idade': 29}, 
    {'salario': 3300,'idade': 31}, 
    {'salario': 3500,'idade': 25}, 
    {'salario': 4200,'idade': 27}, 
    {'salario': 5600,'idade': 33}, 
    {'salario': 6200,'idade': 35}, 
    {'salario': 3000,'idade': 37}, 
    {'salario': 6400,'idade': 21}, 
]

sensibilidade_salario = 1000
epsilon_salario = 1.0

sensibilidade_idade = 10
epsilon_idade = 1.0

dados_anonimos = []

for dado in dados_pessoais:
    salario_privado = adicionar_ruido_diferencial(dado['salario'], sensibilidade_salario, epsilon_salario)
    idade_privada = adicionar_ruido_diferencial(dado['idade'], sensibilidade_idade, epsilon_idade)

    dados_anonimos.append({'salario': salario_privado, 'idade': idade_privada})

for i in range(len(dados_pessoais)):
    print('-=' * 40)
    print(f"| Idade original =  {dados_pessoais[i]['idade']:>10} | Idade privada = {dados_anonimos[i]['idade']:>10.0f}")
    print(f"| Salário original ={dados_pessoais[i]['salario']:>10} | Salário privado = {dados_anonimos[i]['salario']:>10.2f}")

