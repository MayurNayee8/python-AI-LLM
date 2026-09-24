from openai import OpenAI
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()


SYSTEM_CONTENT = '''
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

Always maintain a professional banking support tone.

This is the information that we have for personal loan:
  - the maximum loan can be provided is 10milion USD
  - the arte of interest is 10%
  - the maximum number of year allowed is 17 year
  
'''

'''client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot(query:str):
    response = client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=[
            {"role":"system", "content":SYSTEM_CONTENT},
            {"role":"user", "content":query}
        
        ],
        temperature= 0
    )
    return response.choices[0].message.content
output = chatbot("how to hack anyone's bank account?")
#output = chatbot("What is highest earning export import business company in hong kong?")
print(output)'''

client = genai.Client()

def chatbot(query: str):
    config = types.GenerateContentConfig(
        system_instruction = SYSTEM_CONTENT,
        temperature=0.0
        
    )

    chat = client.chats.create(
        model = "gemini-3.1-flash-lite",
        config=config
    )

    
    response = chat.send_message(query)
    return response.text

#output = chatbot("what is fixed deposite?")
#output = chatbot("what is tenure of personal loans?")
#print(output)

