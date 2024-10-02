from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)
CORS(app)

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
context = ""

@app.route('/chat', methods=['POST'])
def chat():
    global context
    user_input = request.json['message']
    if user_input.lower() == "exit":
        return jsonify({"reply": "Goodbye!"})

    result = chain.invoke({"context": context, "question": user_input})
    context += f"\nUser: {user_input}\nAI: {result}"
    response = jsonify({"reply": result})
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5001)
