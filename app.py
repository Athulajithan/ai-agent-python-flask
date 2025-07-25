from flask import Flask, render_template, request, jsonify, redirect, url_for
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

# Load FAQs
with open("faqs.json", encoding="utf-8") as f:
    faqs = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/customer-support")
def customer_support():
    return render_template("faq.html", faqs=faqs)

@app.route("/genetic-agent")
def genetic_agent():
    return render_template("wellness.html")

@app.route("/ask-genetic", methods=["POST"])
def ask_genetic():
    question = request.form.get("question", "")
    try:
        response = model.generate_content(question)
        return jsonify({"answer": response.text})
    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
