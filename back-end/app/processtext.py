# imports
import os
os.environ['OPENAI_API_KEY'] = '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'
import openai
openai.api_key = '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'
from datetime import datetime
SEED = 3

# function that calls openAI API to extract relevant data from text
def process_text(content):
    response = openai.ChatCompletion.create(
        seed=SEED, # setting seed for more deterministic outputs
        model="gpt-3.5-turbo",
        messages=[
        {
            "role": "system",
            "content": f"""Here is the problem: the user is struggling to write an effective email.
            You will be provided with text that the user intends to send as an email. 
            Your task is to convert the text into a semi-formal email message, with a professional and polite tone.
            Keep the email short and to the point. Send a full email message, and make sure it is under a 100 words.
            """
        },
        {
            "role": "user",
            "content": content
        }
        ],
        temperature=0.2, # setting temperature as 0.5 for more deterministic outputs
        max_tokens=512,
        top_p=1
    )
    details = response.choices[0].message.content

    return details

# function to create a unique ID for each user
def get_id():
    fmt = '%Y%m%d%H%M%S'
    current = datetime.now()
    cur_dt = current.strftime(fmt) 
    id = hash("USER" + str(cur_dt))
    return id

