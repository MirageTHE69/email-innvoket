import openai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=API_KEY)

def generate_email(company, person, about, service):
    prompt = f"""
Generate a highly personalized email for {person} from {company} regarding potential collaboration. 
Details about the person: {about}. 
Our service: {service}. 
Make the email conversational, polite, and professional, without following any fixed format. Add a human touch and make the email engaging.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )
    return response.choices[0].message.content
