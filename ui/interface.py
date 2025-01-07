import streamlit as st
from core.agent import create_agent
from core.prompts import get_prompt_template

def render_interface():
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

    st.write('Faça uma pergunta sobre o estoque de produtos, preços e reposições')

    user_question = st.text_input('O que deseja saber sobre o estoque?')

    if st.button('Consultar'):
        if user_question:
            with st.spinner('Consultando o banco de dados...'):
                agent_executor = create_agent(selected_model)
                prompt_template = get_prompt_template()
                formatted_prompt = prompt_template.format(q=user_question)
                output = agent_executor.invoke({'input': formatted_prompt})
                st.markdown(output.get('output'))
        else:
            st.warning('Por favor, insira uma pergunta.')
