# 📂 Filtro e Organização de Fotos com Base em Planilha Excel

## 📌 Descrição

Este projeto foi desenvolvido para automatizar a filtragem e organização de imagens com base em uma planilha do Excel. 
Ele permite que fotos sejam movidas automaticamente para uma pasta de destino, garantindo que apenas os arquivos relevantes sejam selecionados.

O sistema foi criado para otimizar processos internos de uma empresa, reduzindo erros manuais e aumentando a eficiência na gestão de arquivos.

## 🚀 Funcionalidades

- ✅ Filtragem Automática: Lê uma planilha do Excel e busca as imagens correspondentes na pasta de origem.
- ✅ Organização Inteligente: Move as fotos encontradas para uma pasta específica.
- ✅ Relatório de Fotos Faltantes: Gera um arquivo fotos_nao_encontradas.txt, listando os nomes das imagens que não foram encontradas na pasta de origem.
- ✅ Otimiza o Processo: Evita buscas manuais e melhora o controle dos arquivos da empresa.

## 🛠 Tecnologias Utilizadas

- Python 3
- Pandas (Para manipulação de planilhas Excel)
- Shutil e OS (Para manipulação de arquivos e pastas)

## 📜 Como Usar

### 1️⃣ Configurar Caminhos
    caminho_planilha = r"C:\PROJETO\ExtrairFotos\DEMANDAALTERADA.XLSX"
    caminho_pasta_fotos = r"C:\PROJETO\ExtrairFotos\FOTOSDEDEMANDA"
    caminho_pasta_destino = r"C:\PROJETO\ExtrairFotos\FOTOS_FILTRADAS"
Antes de rodar o script, ajuste os caminhos no arquivo filtrar_fotos.py para refletir a estrutura do seu diretório:
### 2️⃣ Instalar Dependências
    pip install pandas
Se ainda não tem o pandas, instale com:
### 3️⃣ Executar o Script
    python filtrar_fotos.py
Basta rodar o script principal:
### 4️⃣ Resultados
As fotos encontradas serão movidas para a pasta FOTOS_FILTRADAS.
Um arquivo fotos_nao_encontradas.txt será gerado com a lista das imagens que estavam na planilha, mas não foram encontradas na pasta de origem.

## 📄 Estrutura do Projeto
- 📂 ExtrairFotos/
    - ├── 📂 FOTOSDEDEMANDA/  # Pasta com todas as fotos originais
    - ├── 📂 FOTOS_FILTRADAS/ # Pasta onde serão movidas as fotos encontradas
    - ├── 📄 DEMANDAALTERADA.XLSX  # Planilha com os nomes das fotos
    - ├── 📜 filtrar_fotos.py  # Script principal
    - ├── 📄 fotos_nao_encontradas.txt  # Lista de fotos que não foram encontradas

## 🏢 Sobre o Desenvolvimento
Este projeto foi desenvolvido por Henrique Ferreira para melhorar a gestão de arquivos de imagens dentro de uma empresa. 
Com essa solução, foi possível otimizar processos, eliminar tarefas manuais e garantir um fluxo de trabalho mais eficiente.
💡 Contribuições e melhorias são bem-vindas!

## 📩 Contato

Se tiver dúvidas ou quiser sugerir melhorias, entre em contato:

[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:henriqueanalista.ads@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/henriqueferreira-ofc)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/henriqueferreira-ofc/)



## 📩 Contato
Se tiver dúvidas ou quiser sugerir melhorias, entre em contato via: 📧 Email: [henriqueanalista.ads@gmail.com] 🐙 GitHub: [https://github.com/henriqueferreira-ofc] 🔗 LinkedIn: [https://www.linkedin.com/in/henriqueferreira-ofc/]

⭐ **Se este projeto foi útil para você, deixe uma estrela no repositório!**  
📌 Basta clicar no botão **"Star"** no topo da página!  

**💬 Deixe seu feedback na seção de [Issues](https://github.com/henriqueferreira-ofc/ExtrairFotos/issues)!**











