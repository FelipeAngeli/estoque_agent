import streamlit as st


st.set_page_config(
    page_title='Estoque GPT',
    page_icon=":shark:",
),

st.header('Assistente de estoque')

model_options = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4-turbo',
    'gpt-4o-mini',
    'gpt-4o'
]

selected_model = st.sidebar.selectbox(
    label='Selecione o modelo de LLM',
    options=model_options,
)

st.sidebar.markdown('## SOBRE')
st.sidebar.markdown('Este é um assistente de estoque baseado em modelos de linguagem de grande porte (LLM).')