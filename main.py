from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI


def __init_main_prompt():
    with open("main_prompt.txt", "r", encoding="utf-8") as f:
        return f.read()


def __save_cases(ret: str):
    with open("cases.md", "a", encoding="utf-8") as f:
        f.write(ret)


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    llm = ChatOpenAI(model="gpt-4o-mini")
    main_prompt = __init_main_prompt()

    ret = llm.invoke(main_prompt)
    __save_cases(ret.content)
