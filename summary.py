from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.chains import LLMChain
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
llm = ChatGroq(api_key=GROQ_API_KEY,model = "llama-3.3-70b-versatile")

def review_summary(reviews):
    summary_prompt = PromptTemplate(
        input_variables=["reviews"],
        template="""
    You are a helpful assistant that summarizes movie reviews.
    Here are the collected reviews:
    {reviews}
    Provide a single concise summary capturing the main themes and viewer sentiment. Also return some top reviews 
    which according to you may match the summary.
    """
    )

# 3️⃣ Build the Chain
    summary_chain = LLMChain(
        llm=llm,
        prompt=summary_prompt,
        output_parser=StrOutputParser()
    )
    result = summary_chain.invoke({"reviews": reviews})
    return result