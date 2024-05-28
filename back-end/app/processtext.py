# imports
import os
os.environ['OPENAI_API_KEY'] = 'API-key'
import openai
openai.api_key = 'API-key'
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
            Your task is to convert the text into an email message. 
            The tone should be semi-formal (NOT OVERLY FORMAL), professional and polite.
            Focus on conciseness. Use as few words as possible. 
            Keep the email short and to the point. Send a full email message, and make sure it is under a 100 words.
            """
        },
        {
            "role": "user",
            "content": content
        }
        ],
        temperature=0.7, 
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

