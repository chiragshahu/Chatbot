import streamlit as st
import PyPDF2
import requests
import google.generativeai as genai

# Replace with your Gemini API key
API_KEY = "AIzaSyABCiFFITN_j2ROqOqUzVnQBPSzBAAp2QQ"

def extract_text(pdf_file):
  reader = PyPDF2.PdfReader(pdf_file)
  text = ""
  for page in reader.pages:
    text += page.extract_text()
  return text

def query_gemini(prompt, question):
  text = prompt + "Question is : " + question + "."
  response = model.generate_content(text)
#   url = "https://language.googleapis.com/v1/documents:analyzeSentiment"
  
#   url = "https://api.sandbox.gemini.com"
#   headers = {"Authorization": f"Bearer {API_KEY}"}
#   data = {
#       "encodingType": "UTF8",
#       "documents": [
#           {
#               "content": prompt + "\n\n" + text
#           }
#       ]
#   }
#   response = requests.post(url, headers=headers, json=data)
#   response.raise_for_status()  # Raise error for non-200 status codes
  return response.text

def answer_question(text, question):
  prompt = f"Analyse this text and give answers of user: {text}"
  response = query_gemini(prompt,question)
  # Extract answer from sentiment analysis response (modify as needed)
  answer = response["documents"][0]["sentences"][0]["text"]["content"]
  return answer.strip()

model = genai.GenerativeModel("gemini-1.0-pro") 
st.title("PDF Chatbot using Gemini AI")
uploaded_file = st.file_uploader("Upload a PDF")
if uploaded_file is not None:
  text = extract_text(uploaded_file)
  user_question = st.text_input("What you want to discuss?")
  if user_question:
    answer = answer_question(text, user_question)
    st.write(answer)

