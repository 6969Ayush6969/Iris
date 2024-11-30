import google.generativeai as genai

genai.configure(api_key="AIzaSyCMWZyhUb4EM_n8_rvaf79Zc63FWpwngfs")

def generate_reply(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    return response.text
      
