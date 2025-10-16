from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import T5Tokenizer, TFT5ForConditionalGeneration

app = Flask(__name__)
CORS(app)  # <---- Add this line to enable CORS

MODEL_PATH = "./agri_chatbot_t5"

tokenizer = T5Tokenizer.from_pretrained(MODEL_PATH)
model = TFT5ForConditionalGeneration.from_pretrained(MODEL_PATH)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_question = data.get("message", "")
    if not user_question:
        return jsonify({"error": "Empty message"}), 400

    input_text = "question: " + user_question
    input_ids = tokenizer.encode(input_text, return_tensors="tf", truncation=True, max_length=64)
    outputs = model.generate(input_ids, max_length=64, num_beams=4, early_stopping=True)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
