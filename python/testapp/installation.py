
'''

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

def chatbot(query:str):
    client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[],
        temperature=0 #[0-1]
    )

'''

from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Note: Standard OpenAI setups usually look for "OPENAI_API_KEY", 
# but I am keeping "OPEN_API_KEY" to match your provided snippet.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chatbot(query: str):
    # The system message sets the behavior, role, and boundaries of the assistant
    system_instruction = """You are a highly experienced expert in the logistics, supply chain, and international export business. 
    You answer questions regarding freight forwarding, customs clearance, shipping documents (like Bills of Lading), Incoterms, 
    supply chain optimization, and international trade regulations. 
    Provide clear, professional, and accurate answers."""

    try:
        # Call the OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": query}
            ],
            temperature=0.2 # Kept low for factual, consistent answers
        )
        
        # Extract the text content from the API response
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred while connecting to the API: {e}"

# --- Interactive Terminal Loop ---
if __name__ == "__main__":
    print("Logistics & Export Expert Chatbot initialized. (Type 'exit' or 'quit' to close)")
    print("-" * 75)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Closing the chatbot. Goodbye!")
            break
            
        # Get the answer from the function and print it
        answer = chatbot(user_input)
        print(f"\nExpert: {answer}\n") 


