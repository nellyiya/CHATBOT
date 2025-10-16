import streamlit as st
from transformers import T5Tokenizer, TFT5ForConditionalGeneration

MODEL_PATH = "./agri_chatbot_t5"

@st.cache_resource
def load_model():
    tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
    model = TFT5ForConditionalGeneration.from_pretrained(MODEL_PATH, from_pt=True)
    return tokenizer, model

tokenizer, model = load_model()

def generate_answer(question, max_length=64):
    input_text = "question: " + question
    input_ids = tokenizer.encode(input_text, return_tensors="tf", truncation=True, padding="max_length", max_length=64)
    outputs = model.generate(input_ids, max_length=max_length, num_beams=5, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

st.title("🌱 Agriculture Chatbot - T5")
st.write("Ask any question about agriculture and get accurate responses!")

user_input = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_input.strip():
        answer = generate_answer(user_input)
        st.success(f"Answer: {answer}")
    else:
        st.warning("Please enter a valid question.")
