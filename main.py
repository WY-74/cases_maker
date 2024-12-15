from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.schema import StrOutputParser


def __init_main_prompt():
    with open("main_prompt.txt", "r", encoding="utf-8") as f:
        main_prompt = PromptTemplate.from_template(f.read())
    return main_prompt


def __init_chian(main_prompt: PromptTemplate, llm: ChatOpenAI):
    return {"docs": RunnablePassthrough()} | main_prompt | llm | StrOutputParser()


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    llm = ChatOpenAI(model="gpt-4o-mini")
    main_prompt = __init_main_prompt()
    chain = __init_chian(main_prompt, llm)

    docs = input("请提供您的需求文档：\n")
    for s in chain.stream(docs):
        print(s, end="", flush=True)
