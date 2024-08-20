import json
import csv

class Dados: 

    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()


    def leitura_json(self,):
        dados_json = []
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def leitura_csv(self):

        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file,delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def leitura_dados(self):
        dados = []


        if self.tipo_dados == 'csv':
             dados = self.leitura_csv()

        elif self.tipo_dados == 'json':
             dados = self.leitura_json()

        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'

        return dados

    def get_columns (self):
        return list(self.dados[-1].keys())


    def rename_columns(self, key_mapping):
        new_dados = []

        for old_dict in self.dados:
            disct_temp = {}
            for old_key, value in old_dict.items():
                disct_temp[key_mapping[old_key]] = value
            new_dados.append(disct_temp)

        self.dados = new_dados
        self.nome_colunas = self.get_columns()


    def size_data(self):
        return len(self.dados)
    

    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)

        return Dados(combined_list, 'list')
    

    def transformando_dados_tabela(self):

        dados_combinado_tabela = [self.nome_colunas]
        
        for row in self.dados:
            linha = []
            for coluna in self.nome_colunas:
                linha.append(row.get(coluna, 'Indisponivel'))
            dados_combinado_tabela.append(linha)

        return dados_combinado_tabela
    
    def salvando_dados(self, path):

        dados_combinado_tabela = self.transformando_dados_tabela()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinado_tabela)
