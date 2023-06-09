from diffprivlib.mechanisms import Laplace


def adicionar_ruido(valor, sensibilidade, epsilon):
    valor_privado = Laplace(epsilon=epsilon, sensitivity=sensibilidade).randomise(valor)  
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

sensibilidade_salario = 3000
epsilon_salario = 1.0

sensibilidade_idade = 3
epsilon_idade = 1.0

dados_anonimos = []

soma_salarios_privados = 0
soma_salarios_originais = 0
soma_idades_privadas = 0
soma_idades_originais = 0

for dado in dados_pessoais:
    salario_privado = adicionar_ruido(dado['salario'], sensibilidade_salario, epsilon_salario)
    idade_privada = adicionar_ruido(dado['idade'], sensibilidade_idade, epsilon_idade)

    soma_salarios_originais += dado['salario']
    soma_salarios_privados += salario_privado
    soma_idades_originais += dado['idade']
    soma_idades_privadas += idade_privada

    dados_anonimos.append({'salario': salario_privado, 'idade': idade_privada})

for i in range(len(dados_pessoais)):
    print('-=' * 40)
    print(f"| Idade original =  {dados_pessoais[i]['idade']:>10} | Idade privada = {dados_anonimos[i]['idade']:>10.0f}")
    print(f"| Salário original ={dados_pessoais[i]['salario']:>10} | Salário privado = {dados_anonimos[i]['salario']:>10.2f}")

print('-=' * 40)
print(f'| Média idades originais =   {soma_idades_originais/len(dados_pessoais):>10.2f} | Média idades privadas = {soma_idades_privadas/len(dados_pessoais):>10.2f}')
print(f'| Média salários originais = {soma_salarios_originais/len(dados_pessoais):>10.2f} | Média salários privados = {soma_salarios_privados/len(dados_pessoais):>10.2f}')