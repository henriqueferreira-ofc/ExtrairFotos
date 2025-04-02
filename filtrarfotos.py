import os
import shutil
import pandas as pd

# 🟢 Caminhos dos arquivos e pastas
caminho_planilha = r"C:\PROJETO\ExtrairFotos\DEMANDAALTERADA.XLSX"
caminho_pasta_fotos = r"C:\PROJETO\ExtrairFotos\FOTOSDEDEMANDA"  # Certifique-se de que a pasta tem esse nome
caminho_pasta_destino = r"C:\PROJETO\ExtrairFotos\FOTOS_FILTRADAS"

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

# 🟢 Nome da coluna que contém os nomes das fotos (ajuste conforme a planilha)
coluna_nomes = "Nome"  # Altere para o nome exato da coluna

# Criar lista de nomes da planilha, removendo espaços extras e convertendo para minúsculas
nomes_planilha = [str(nome).strip().lower() for nome in df[coluna_nomes].astype(str).tolist()]

# 🟢 Listar todas as fotos na pasta de origem
fotos_na_pasta = os.listdir(caminho_pasta_fotos)

# 🟢 Filtrar e mover apenas as fotos que fazem parte da planilha
fotos_movidas = 0
for foto in fotos_na_pasta:
    nome_base, extensao = os.path.splitext(foto)  # Separar nome e extensão
    if nome_base.strip().lower() in nomes_planilha:  # Comparação robusta
        origem = os.path.join(caminho_pasta_fotos, foto)
        destino = os.path.join(caminho_pasta_destino, foto)
        shutil.move(origem, destino)  # Mover a foto para a pasta destino
        fotos_movidas += 1

print(f"✅ Processo concluído! {fotos_movidas} fotos foram movidas para a pasta FOTOS_FILTRADAS.")