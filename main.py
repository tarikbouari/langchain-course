import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))
    #definir une variable information
    information ="""Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, X, and xAI. Musk has been the wealthiest person in the world since 2025; as of May 2026, Forbes estimates his net worth to be US$788 billion.

        Born into the wealthy Musk family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002."""

    #write a prompt template

    summary_template = """
    given information {information} about the person I want you to create
    1. A short summary
    2. two interresting facts about them
    """

    #Initialiser un objet prompt template

    summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
    )



    llm = ChatOpenAI(temperature=0, model="gpt-5")
    #llm = ChatOllama(temperature=0, model="gemma3:270m")
    #creation de notre premiere chain

    chain = summary_prompt_template | llm
    #la chaine devient un object runable que peut appeler avec la methode invoke

    response = chain.invoke(input={"information":information})
    print(response.content)

if __name__ == "__main__":
    main()
