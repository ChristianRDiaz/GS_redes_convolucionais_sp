# 🚓 Classificador de Ocorrências: Roubo vs Furto (SSP-SP)

Este projeto foi desenvolvido como requisito para a **Global Solution** da disciplina de **Aprendizado Profundo com Redes Neurais Convolucionais**. O objetivo é utilizar uma Rede Neural Multilayer Perceptron (MLP) para classificar ocorrências de subtração de celulares na cidade de São Paulo como **Roubo** ou **Furto**, com base em dados públicos da Secretaria da Segurança Pública (SSP-SP).

## 👥 Integrantes
*   **CHRISTIAN RAYMUNDO DIAZ** - RM568324

## 🌐 Aplicação Web (Streamlit)
A aplicação web está hospedada e pronta para uso no Streamlit Community Cloud. Você pode testar o modelo pelo navegador através do link abaixo:
👉 **[Acessar a Aplicação Web](https://gs-redes-neuronais-convolucionais.streamlit.app/)**

---

## 📊 Base de Dados e Procedimento de Obtenção
*   **Fonte Pública:** Secretaria da Segurança Pública do Estado de São Paulo (SSP-SP).
*   **Link do Portal:** [Portal de Estatísticas SSP-SP](https://www.ssp.sp.gov.br/estatistica/consultas)
*   **Recorte Utilizado:** Dados do ano de 2025, referentes exclusivamente ao município de São Paulo (Capital).

**Como obter os dados para reproduzir o projeto:**
1. Acesse o Portal de Estatísticas da SSP-SP no link acima.
2. Na seção "Bases de Dados", selecione a opção **"Celulares Subtraídos"**.
3. Baixe a base referente ao ano de 2025 (formato Excel).
4. Devido ao limite de tamanho do GitHub (100MB), o arquivo `.xlsx` **não está neste repositório**.
5. Renomeie o arquivo baixado para `CelularesSubtraidos_2025.xlsx` e coloque-o na raiz desta pasta para executar o Jupyter Notebook.

---

## 🧠 Arquitetura e Metodologia
*   **Alvo (Target):** Coluna `RUBRICA` convertida em 0 (Furto) e 1 (Roubo).
*   **Atributos (Features):** Bairro, Período do dia, Tipo de Local e Autoria.
*   **Engenharia de Features:** Aplicação de Hora Cíclica (Seno e Cosseno) para a variável de horário e limpeza de strings (remoção de acentos e padronização de abreviações de bairros).
*   **Modelagem:** Foram testadas 3 arquiteturas de MLP. A arquitetura escolhida foi a `A_Simples` (16 neurônios, ReLU), por apresentar o melhor equilíbrio (F1-Score na validação) e evitar o overfitting das redes mais profundas.

---

## 📁 Estrutura do Repositório
*   `app.py`: Código da aplicação web em Streamlit.
*   `GS_SEGURANCA_PUBLICA_SP.ipynb`: Jupyter Notebook com toda a análise exploratória, tratamento de dados, treinamento e avaliação.
*   `mlp_roubo_furto.keras`: O modelo da Rede Neural treinado e exportado.
*   `preprocessor.pkl`: O ColumnTransformer (One-Hot Encoder + StandardScaler) ajustado no treino.
*   `top_bairros.pkl`: Lista dos 30 bairros mais frequentes (usado no app).
*   `columns.pkl`: Lista com a ordem exata das colunas (evita erros de Shape Mismatch).
*   `requirements.txt`: Dependências do projeto.

---

## 🚀 Como executar o projeto localmente

### 1. Pré-requisitos
Certifique-se de ter o Python (versão 3.9 a 3.11) instalado em sua máquina.

### 2. Instalar as dependências
Abra o terminal na pasta do projeto e rode:
```bash
pip install -r requirements.txt
```
(Recomendamos usar um ambiente virtual, como o venv ou conda, para evitar conflitos com outras bibliotecas do seu computador).

### 🚀 Como executar o projeto

### Opção A: Rodar no Google Colab (Recomendado para quem não quer instalar nada)
1. Faça o download do arquivo `GS_SEGURANCA_PUBLICA_SP.ipynb` deste repositório.
2. Acesse o [Google Colab](https://colab.research.google.com/) e faça o upload do notebook.
3. Baixe a base de dados no site da SSP-SP (instruções acima).
4. No Colab, clique no ícone de pasta (📁) na barra lateral esquerda, clique no ícone de upload (setinha) e envie o arquivo `CelularesSubtraidos_2025.xlsx`.
5. Rode a primeira célula do notebook. Ela verificará se o arquivo está lá e instalará as dependências necessárias.

### Opção B: Rodar Localmente (VS Code ou Jupyter)
1. Instale as dependências:
```bash
pip install -r requirements.txt
```
O projeto foi construído usando um Jupyter Notebook (.ipynb).
Para rodá-lo:

Se estiver no VS Code: 
1. Abra o arquivo .ipynb, clique no canto superior direito (onde geralmente aparece "Select Kernel") e selecione o interpretador Python onde você instalou as dependências (ex: Python 3.10.x ou o seu ambiente virtual).

2. Se estiver no Jupyter Lab/Notebook: Ao abrir o arquivo, vá no menu superior em Kernel -> Change Kernel e selecione o ambiente correto que possui o TensorFlow e o Scikit-Learn instalados.

3. Após configurar o Kernel, você pode executar todas as células em ordem:

```bash
jupyter notebook GS_SEGURANCA_PUBLICA_SP.ipynb
```

### 4. Rodar a Aplicação Web
Para executar o Streamlit localmente:

```bash
streamlit run app.py
```

### 🤖 Uso de IA Generativa
A **Inteligência Artificial (Claude)** foi utilizada como copiloto no desenvolvimento deste projeto. 
- Ela apoiou na depuração de erros (como Shape Mismatch no TensorFlow e problemas de índice no Pandas),
- na estruturação do pipeline de pré-processamento (ColumnTransformer) para evitar Data Leakage e na criação do layout do Streamlit.
### Todo o código foi executado, validado e compreendido pela equipe, garantindo a integridade acadêmica da solução. 🟢
