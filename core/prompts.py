from langchain import hub


def get_system_message():
    return hub.pull('hwchase17/react')


def get_prompt_template():
    prompt = '''
    Use as ferramentas necessárias para responder perguntas relacionadas ao
    estoque de produtos. Você fornecerá insights sobre produtos, preços, 
    reposição de estoque e relatórios conforme solicitado pelo usuário.
    A resposta final deve ter uma formatação amigável de visualização para o usuário.
    Sempre responda em português brasileiro.
    Pergunta: {q}
    '''
    from langchain.prompts import PromptTemplate
    return PromptTemplate.from_template(prompt)
