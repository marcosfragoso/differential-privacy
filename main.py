import secrets
import numpy

# Função para gerar nomes privados com a mesma quantidade de letras
def gera_nome_anonimo(nome):
    vogais = "AEIOU"
    consoantes = "BCDFGHJKLMNPQRSTVWXYZ"
    nome_privado = ''
    for i in range(len(nome)):
        if nome[i].isspace():
            nome_privado += ' '
        elif nome[i].isalpha():
            if i % 2 == 0:
                nome_privado += secrets.choice(vogais)
            else:
                nome_privado += secrets.choice(consoantes)
    return nome_privado

# Função para gerar idades privadas
def gera_idade_anonima(idade):
    epsilon = 1.0 # Controlador de nível de privacidade (1 geralmente é considerado como um nível moderado de privacidade)
    sensibilidade = 2.0 # Sensibilidade igual a 1 para valores não duplicados, sensibilidade padrão
    ruido = numpy.random.laplace(scale=sensibilidade/epsilon) # Distribuição de laplace é usada comumente em DP
    idade_ruidosa = idade + ruido
    
    if idade_ruidosa < 18:
        idade_ruidosa = gera_idade_anonima(idade)
        
    return idade_ruidosa

# Função para gerar salários privados
def gera_salario_anonimo(valor):
    epsilon = 1.0 # Controlador de nível de privacidade (1 geralmente é considerado como um nível moderado de privacidade)
    sensibilidade = 1550 # Metade da diferença máxima entre os salários
    escala = sensibilidade / epsilon
    ruido = numpy.random.laplace(0, escala) # Distribuição de laplace é usada comumente em DP (0 = a distribuição tá centrada em um valor zero, escala = quanto maior a escala maior o ruído)
    valor_ruidoso = valor + ruido
    return valor_ruidoso


# Dados originais
dados_pessoais = [
    {'nome': 'João Silva','salario': 3500,'idade': 23}, 
    {'nome': 'Maria Santos','salario': 3300,'idade': 19}, 
    {'nome': 'Pedro Oliveira','salario': 2600,'idade': 39},
    {'nome': 'Ana Costa','salario': 2700,'idade': 29}, 
    {'nome': 'Luiz Pereira','salario': 3300,'idade': 31}, 
    {'nome': 'Laura Rodrigues','salario': 3500,'idade': 25}, 
    {'nome': 'Carlos Almeida','salario': 4200,'idade': 27}, 
    {'nome': 'André Ferreira','salario': 5600,'idade': 33}, 
    {'nome': 'Juliana Souza','salario': 6200,'idade': 35}, 
    {'nome': 'Rafael Martins','salario': 3000,'idade': 37}, 
    {'nome': 'Camila Ramos','salario': 6400,'idade': 21}, 
]

# Dados anônimos
dados_anonimos = []

for i in range(0, len(dados_pessoais)):
    dados_privados = dict()
    dados_privados['nome'] = gera_nome_anonimo(dados_pessoais[i]['nome']) # Gerando nome privado da pessoa
    dados_privados['salario'] = gera_salario_anonimo(dados_pessoais[i]['salario']) # Gerando salário privado da pessoa
    dados_privados['idade'] = gera_idade_anonima(dados_pessoais[i]['idade']) # Gerando idade privado da pessoa
    dados_anonimos.append(dados_privados) # Adicionando todos os dados privados da pessoa

# Exibir os dados originais e privados
for i in range(0, len(dados_pessoais)):
    print('-=' * 40)
    print(f"| Nome original =   {dados_pessoais[i]['nome']:>10} | Nome privado = {dados_anonimos[i]['nome']:>10}")
    print(f"| Idade original =  {dados_pessoais[i]['idade']:>10} | Idade privada = {dados_anonimos[i]['idade']:>10.0f}")
    print(f"| Salário original ={dados_pessoais[i]['salario']:>10} | Salário privado = {dados_anonimos[i]['salario']:>10.2f}")
