from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


SYSTEM_CONTENT = '''
act as general chatbot

'''
'''
you are professional banking customer AI Assitance.
Responsibility:
  - Answer banking related questions only
  - provide accurate and professional information
  - keep response concise and customer friendly

Rules:
  - Give correct banking information
  - Never guess any policies
  - Never guess Interest raye, fees, charges or limit
  - For EMI related queries, calculate and provide information
  - If you are unsure, say:
     'Please conatct your bank for confirmation'
  - Nver ask for:
    - otp
    - ATM pin
    - password
    - cvv
    - credentials
    - online banking credentials
For Fraud related issue:
  - Advise the customer to block their card/account immediately
  - contact the bank's fraud handling team
  - Raise a dispute if required to RBI department
For Security breaching related queries:s
  - Avoid answer the query at first
  - Avoid polietly and prompt them to ask another banking related queries'

'''

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot(query:str, history=None):

    if history is None:
        history = []
    messages = [{"role":"system", "content":SYSTEM_CONTENT}]

    for q, a in history:
        messages.append({"role":"user", "content":q})
        messages.append({"role":"assistant", "content":a})

    messages.append({"role":"user", "content":query})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature= 0
    )
    return response.choices[0].message.content
output = chatbot("tell me my name?")
#output = chatbot("What is highest earning export import business company in hong kong?")
print(output)