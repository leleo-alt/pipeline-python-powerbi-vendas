import os
import csv


pasta_script = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta_script, "vendas.csv")


vendas = [
    {"ID": 101, "Cliente": "Carlos Silva", "Produto": "Curso de Python", "Valor": 1500.00, "Cidade": "Fortaleza"},
    {"ID": 102, "Cliente": "Ana Oliveira", "Produto": "Curso de JavaScript", "Valor": 2000.00, "Cidade": "Caucaia"},
    {"ID": 103, "Cliente": "Maria Santos", "Produto": "Curso de HTML/CSS", "Valor": 1800.00, "Cidade": "Fortaleza"},
    {"ID": 104, "Cliente": "Pedro Costa", "Produto": "Curso de React", "Valor": 2500.00, "Cidade": "Maracanaú"},
    {"ID": 105, "Cliente": "Juliana Pereira", "Produto": "Curso de Node.js", "Valor": 2200.00, "Cidade": "Fortaleza"}
]

colunas = ["ID", "Cliente", "Produto", "Valor", "Cidade"]


with open(caminho_arquivo, mode="w", newline="", encoding="utf-8-sig") as arquivo_csv:
    escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=";")
    escritor.writeheader()
    escritor.writerows(vendas)  

print("=" * 60)
print(f"✅ ARQUIVO CRIADO COM SUCESSO EM:\n{caminho_arquivo}")
print("=" * 60)
 
