import eel
import google.generativeai as genai

API_KEY = "AIzaSyC3xBgYpCphaDGjDXiNC9Z1DKSNVwr5wPk"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def gemini(query):
    user_input = query
    response = chat.send_message(user_input)
    return response.text

eel.init('www')

@eel.expose
def chat_with_bot(user_query):
    response = gemini(user_query)
    return response

eel.start('index.html', size=(1000, 1000))
