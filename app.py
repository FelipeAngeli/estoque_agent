import streamlit as st
from ui.interface import render_interface

st.set_page_config(page_title='Estoque GPT', page_icon=":shark:")

if __name__ == "__main__":
    render_interface()

# import os
# import streamlit as st

# from decouple import config

# from langchain import hub
# from langchain.agents import create_react_agent, AgentExecutor
# from langchain.prompts import PromptTemplate
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
# from langchain_openai import ChatOpenAI

# os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

# st.set_page_config(
#     page_title='Estoque GPT',
#     page_icon=":shark:",
# ),

# st.header('Assistente de estoque')

# model_options = [
#     'gpt-3.5-turbo',
#     'gpt-4',
#     'gpt-4-turbo',
#     'gpt-4o-mini',
#     'gpt-4o'
# ]

# selected_model = st.sidebar.selectbox(
#     label='Selecione o modelo de LLM',
#     options=model_options,
# )

# st.sidebar.markdown('## SOBRE')
# st.sidebar.markdown('Este é um assistente de estoque baseado em modelos de linguagem de grande porte (LLM).')

# st.write('Faça uma pergunta sobre o estoque de produtos, preços e reposições')

# user_question = st.text_input('O que deseja saber sobre o estoque?')

# model = ChatOpenAI(model=selected_model)

# db = SQLDatabase.from_uri('sqlite:///estoque.db')

# toolkit = SQLDatabaseToolkit(
#     db=db,
#     llm=model,
# )
# system_message = hub.pull('hwchase17/react')

# agent = create_react_agent(
#     llm=model,
#     tools=toolkit.get_tools(),
#     prompt=system_message,
# )

# agent_executor = AgentExecutor(
#     agent=agent,
#     tools=toolkit.get_tools(),
#     verbose=True, 
#     )

# prompt = '''
# Use as ferramentas necessárias para responder perguntas relacionadas ao
# estoque de produtos. Você fornecerá insights sobre produtos, preços, 
# reposição de estoque e relatórios conforme solicitado pelo usuário.
# A resposta final deve ter uma formatação amigável de visualização para o usuário.
# Sempre responda em português brasileiro.
# Pergunta: {q}
# '''
# prompt_template = PromptTemplate.from_template(prompt)

# if st.button('Consultar'):
#     if user_question:
#         with st.spinner('Consultando o banco de dados...'):
#             formatted_prompt = prompt_template.format(q=user_question)
#             output = agent_executor.invoke({'input': formatted_prompt})
#             st.markdown(output.get('output'))
#     else:
#         st.warning('Por favor, insira uma pergunta.')

