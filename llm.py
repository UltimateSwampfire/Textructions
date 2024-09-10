from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv


load_dotenv()

def join_context(context_list : list[str]) -> str:
    context = ''
    for item in context_list:
        context += " " + item
    return context


def get_instructions_from_context(context : str, add_details= "None") -> str:

    llm = OpenAI(temperature=0.7)

    prompt_template = """
    You are provided with context strings from screenshots of the Google Play Store page of an app.
    Your task is to generate a set of clear and concise instructions on how to use the app based on the information in the context.
    The context includes descriptions of the app's features, functionality, and other relevant details.
    Focus only on giving actionable steps to the user for interacting with the app.
    Limit to only 10-12 instructions.
    
    Pay attention to the additional details given by the user, follow them accordingly.

    Context: 
    {context}
    Additional Details:
    {add_details}
    Based on the above context, provide numbered instructions on how to use the app, ranging from most to least important.
    """
    prompt = PromptTemplate(
        input_variables = ['context'],
        template = prompt_template
    )
    chain = LLMChain(
        llm = llm,
        prompt = prompt
    )

    response = chain.run(question = prompt, context = context,add_details = add_details)
    # response = response.replace('\n','')

    return response


