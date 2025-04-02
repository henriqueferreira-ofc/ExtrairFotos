import os
import shutil
import pandas as pd

# 🟢 Caminhos dos arquivos e pastas
caminho_planilha = r"C:\PROJETO\ExtrairFotos\DEMANDAALTERADA.XLSX"
caminho_pasta_fotos = r"C:\PROJETO\ExtrairFotos\FOTOSDEDEMANDA"
caminho_pasta_destino = r"C:\PROJETO\ExtrairFotos\FOTOS_FILTRADAS"
caminho_fotos_nao_encontradas = r"C:\PROJETO\ExtrairFotos\fotos_nao_encontradas.txt"

# Verificar se as pastas e a planilha existem
if not os.path.exists(caminho_pasta_fotos):
    print(f"❌ ERRO: A pasta de fotos '{caminho_pasta_fotos}' não foi encontrada.")
    exit()

if not os.path.exists(caminho_planilha):
    print(f"❌ ERRO: O arquivo da planilha '{caminho_planilha}' não foi encontrado.")
    exit()

# Criar a pasta de destino, se não existir
os.makedirs(caminho_pasta_destino, exist_ok=True)

# 🟢 Carregar a planilha
try:
    df = pd.read_excel(caminho_planilha)
    print("✅ Planilha carregada com sucesso!")
    print("📌 Colunas disponíveis:", df.columns)
except Exception as e:
    print(f"❌ Erro ao carregar a planilha: {e}")
    exit()

# Nome da coluna que contém os nomes das fotos
coluna_nomes = "Nome"  

# Criar lista de nomes da planilha, removendo espaços extras e convertendo para minúsculas
nomes_planilha = [str(nome).strip().lower() for nome in df[coluna_nomes].astype(str).tolist()]

# Listar todas as fotos na pasta de origem
fotos_na_pasta = os.listdir(caminho_pasta_fotos)

# Criar lista de nomes das fotos na pasta, sem extensão
fotos_na_pasta_nomes = [os.path.splitext(f)[0].strip().lower() for f in fotos_na_pasta]

# 🟢 Filtrar e mover apenas as fotos que fazem parte da planilha
fotos_movidas = 0
for foto in fotos_na_pasta:
    nome_base, extensao = os.path.splitext(foto)
    if nome_base.strip().lower() in nomes_planilha:
        origem = os.path.join(caminho_pasta_fotos, foto)
        destino = os.path.join(caminho_pasta_destino, foto)
        shutil.move(origem, destino)
        fotos_movidas += 1

# 🟢 Verificar fotos que NÃO foram encontradas
fotos_nao_encontradas = sorted([nome for nome in nomes_planilha if nome not in fotos_na_pasta_nomes])

# 🟢 Salvar a lista de fotos não encontradas em um arquivo .txt
with open(caminho_fotos_nao_encontradas, "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Total de fotos não encontradas: {len(fotos_nao_encontradas)}\n\n")
    for nome in fotos_nao_encontradas:
        arquivo.write(nome + "\n")

# Exibir relatório
print(f"\n📌 Total de nomes na planilha: {len(nomes_planilha)}")
print(f"📌 Total de fotos na pasta: {len(fotos_na_pasta)}")
print(f"✅ Total de fotos movidas: {fotos_movidas}")

if fotos_nao_encontradas:
    print(f"❌ {len(fotos_nao_encontradas)} fotos NÃO foram encontradas na pasta.")
    print(f"📄 Lista salva em: {caminho_fotos_nao_encontradas}")
# python filtrar_fotos.py / comando