from dotenv import load_dotenv
load_dotenv()
import openai
import os
class ml_backend:
        
    openai.api_key = os.getenv("OPEN_API_KEY")

    def ui(self, userPrompt ="Generate a super comprehensive user interface with html, css and javascript from the user prompt, then make it responsive and better looking with css styling. Make sure that the generated User interface is readeable and stylish. Make sure to use a nice and visibly pleasing font other than the default one, and try to make the elements centered in the middle of the screen when possible.", ):
        """Returns a html page using GPT3"""

        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=userPrompt,
        temperature=0.71,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0.36,
        presence_penalty=0.75
        )
        return response.get("choices")[0]['text']
        

