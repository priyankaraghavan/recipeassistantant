from openai import OpenAI
import os

def create_recipe_prompt_Clean():
    prompt = f"""
Act as an old lady from south India specifically Karnataka who is an expert in cooking. This lady is Mrs Kamala and has 60 years of experience cooking.
When the user asks for a recipe, Mrs Kamala will provide the recipe in a friendly and helpful manner.
The user can ask for recipes for any Indian dish and Mrs Kamala will provide the recipe.
If the user asks for dishes from any other cuisine, Mrs Kamala will politely decline and ask the user to ask for Indian dishes only.
"""
    return prompt

def create_prompt():
    prompt = f"""
Act as a system assistant.
"""
    return prompt

prompt= create_prompt()
openai_api_key = os.getenv("OPEN_AI_API_KEY")
def get_recipesforinput(input_text):
    systemprompt= prompt
    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": systemprompt
                },
                {
                    "role": "user",
                    "content": input_text
                }
            ],
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )        
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return None