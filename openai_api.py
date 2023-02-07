import openai

# Set up the OpenAI API client
openai.api_key = str_apikey

# Set up the model and prompt
model_engine_complex_answer = "text-davinci-003"
prompt = "How to create a SQL query to bring the max amount per client"

def respond_to_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text
    


print(respond_to_text(prompt))
