import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Classificador de Ocorrências", page_icon="🚓", layout="centered")

@st.cache_resource
def load_artifacts():
    model = load_model("mlp_roubo_furto.keras")
    preprocessor = joblib.load("preprocessor.pkl")
    top_bairros = joblib.load("top_bairros.pkl")
    return model, preprocessor, top_bairros

try:
    model, preprocessor, top_bairros = load_artifacts()
except Exception as e:
    st.error(f"Erro ao carregar o modelo. Verifique os arquivos: {e}")
    st.stop()

st.title("🚓 Classificador de Ocorrências: Roubo vs Furto")
st.markdown("""
Esta aplicação utiliza uma Rede Neural (MLP) treinada com dados da SSP-SP para classificar o tipo de ocorrência com base no perfil do registro.
*Nota: O modelo analisa o perfil de uma ocorrência já registrada, não prevê a chance de um crime acontecer.*
""")

st.divider()

with st.form("form_ocorrencia"):
    st.subheader("Preencha as características da ocorrência:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        bairro = st.selectbox("Bairro", top_bairros + ['OUTROS_BAIRROS'])
        
        # NOVIDADE: Selectbox de faixas de horário amigáveis
        faixa_horario = st.selectbox(
            "Faixa de Horário", 
            [
                "Madrugada (00h às 05h)",
                "Manhã (06h às 11h)",
                "Tarde (12h às 17h)",
                "Noite (18h às 23h)"
            ]
        )
        
    with col2:
        tipo_local = st.selectbox("Tipo de Local", 
            ["Via Pública", "Outros", "Terminal/Estação", "Residência", 
             "Comércio e Serviços", "Lazer e Recreação", "Restaurante e Afins", "Rodovia/Estrada"])
        
        autoria = st.selectbox("Autoria (se conhecida)", ["Desconhecida", "Conhecida"])

    submitted = st.form_submit_button("Classificar Ocorrência", type="primary")

if submitted:
    # 1. Traduzir a faixa amigável de volta para a Hora Matemática (0 a 23) e o Período
    if faixa_horario == "Madrugada (00h às 05h)":
        hora_num = 3 # Ponto médio
        periodo_str = "MADRUGADA"
    elif faixa_horario == "Manhã (06h às 11h)":
        hora_num = 8
        periodo_str = "MANHA"
    elif faixa_horario == "Tarde (12h às 17h)":
        hora_num = 14
        periodo_str = "TARDE"
    else:
        hora_num = 20
        periodo_str = "NOITE"

    # 2. Aplicar a transformação cíclica na hora
    hora_sin = np.sin(2 * np.pi * hora_num / 24)
    hora_cos = np.cos(2 * np.pi * hora_num / 24)

    # 3. Montar o DataFrame com TODAS as features esperadas pelo modelo
    input_data = pd.DataFrame({
        'HORA_SIN': [hora_sin],
        'HORA_COS': [hora_cos],
        'BAIRRO': [bairro],
        'DESCR_PERIODO': [periodo_str],
        'DESCR_TIPOLOCAL': [tipo_local],
        'AUTORIA_BO': [autoria]
    })
    
    # 4. Pré-processar e Prever
    input_scaled = preprocessor.transform(input_data).astype('float32')
    prob_roubo = float(model.predict(input_scaled, verbose=0)[0][0])
    prob_furto = 1 - prob_roubo
    
    # 5. Exibir Resultados
    st.divider()
    st.subheader("Resultado da Classificação")
    
    if prob_roubo > 0.5:
        st.error(f"🚨 **Classe Estimada: ROUBO**")
    else:
        st.success(f"🕵️ **Classe Estimada: FURTO**")
        
    # Gráfico de barras com as probabilidades
    st.write("Probabilidades atribuídas pelo modelo:")
    df_prob = pd.DataFrame({
        "Probabilidade (%)": [prob_furto * 100, prob_roubo * 100]
    }, index=["Furto", "Roubo"])
    
    st.bar_chart(df_prob, color="#4c72b0")
    
    st.caption(f"Furto: {prob_furto*100:.1f}% | Roubo: {prob_roubo*100:.1f}%")