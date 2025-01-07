from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

from core.database import get_database
from core.prompts import get_system_message


def create_agent(selected_model: str):
    model = ChatOpenAI(model=selected_model)
    db = get_database()
    toolkit = SQLDatabaseToolkit(db=db, llm=model)

    system_message = get_system_message()

    agent = create_react_agent(
        llm=model,
        tools=toolkit.get_tools(),
        prompt=system_message,
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=toolkit.get_tools(),
        verbose=True,
    )

    return agent_executor
