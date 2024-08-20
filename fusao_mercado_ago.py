import json
import csv

from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract

dados_empresaA = Dados(path_json, 'json')
print(dados_empresaA.nome_colunas)
print(dados_empresaA.qtd_linhas)

dados_empresaB = Dados(path_csv, 'csv')
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)

# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto':'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

# Load

path_dados_combinados = 'data_processed/dados.combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)











                                                                             #primeiros passos





# def leitura_json(path_jason):
#     dados_json = []
#     with open(path_json, 'r') as file:
#          dados_json = json.load(file)
#     return dados_json

# def leitura_csv(path_csv):

#     dados_csv = []
#     with open(path_csv, 'r') as file:
#         spamreader = csv.DictReader(file,delimiter=',')
#         for row in spamreader:
#             dados_csv.append(row)
#     return dados_csv

# def leitura_dados(path, tipo_arquivo):
    # dados = []


    # if tipo_arquivo == 'csv':
    #    dados = leitura_csv(path)
    # elif tipo_arquivo == 'json':
    #     dados = leitura_json(path)
    # return dados
    
# def get_columns (dados):
#     return list(dados[-1].keys())

# def rename_columns(dados, key_mapping):
#     new_dados_csv = []

#     for old_dict in dados:
#         disct_temp = {}
#         for old_key, value in old_dict.items():
#             disct_temp[key_mapping[old_key]] = value
#         new_dados_csv.append(disct_temp)
#     return new_dados_csv

# def size_data(dados):
#     return len(dados)

# def join(dadosA, dadosB):
#     combined_list = []
#     combined_list.extend(dadosA)
#     combined_list.extend(dadosB)
#     return combined_list

# def transformando_dados_tabela(dados, nome_colunas):

#     dados_combinado_tabela = [nome_colunas]
    
#     for row in dados:
#         linha = []
#         for coluna in nome_colunas:
#             linha.append(row.get(coluna, 'Indisponivel'))
#         dados_combinado_tabela.append(linha)

#     return dados_combinado_tabela

# def salvando_dados(dados, path):
#     with open(path, 'w') as file:
#         writer = csv.writer(file)
#         writer.writerows(dados)

# # Transformação dos dados

# dados_csv = rename_columns (dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# print(nome_colunas_csv)

# dados_fusao = join(dados_json, dados_csv)
# nome_colunas_fusao = get_columns(dados_fusao)
# tamanho_dados_fusao = size_data(dados_fusao)
# print(nome_colunas_fusao)
# print(tamanho_dados_fusao)


# # Salvamento de dados

# dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

# path_dados_combinados = 'data_processed/dados.combinados.csv'

# salvando_dados(dados_fusao_tabela, path_dados_combinados)

# print(path_dados_combinados)