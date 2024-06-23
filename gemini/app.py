import google.generativeai as genai

API_KEY="AIzaSyC3xBgYpCphaDGjDXiNC9Z1DKSNVwr5wPk"

genai.configure(
    api_key=API_KEY

)

model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def gemini(query):
    user_input = query
    print("running")
    response=chat.send_message(user_input)
    print(f"chatbot:{response.text}")
    return response.text


n=input("enter the text")
gemini(n)