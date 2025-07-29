from flask import Flask, render_template, request
from openai import OpenAI
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv



app = Flask(__name__)
load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/ciphers")
def ciphers():
    return render_template("ciphers.html")

@app.route("/ciphers/atbash")
def atbash_cipher():
    return render_template("atbash_cipher.html")
@app.route("/ciphers/caesar")
def caesar_cipher():
    return render_template("caesar_cipher.html")
@app.route("/ciphers/vigenere")
def vigenere_cipher():
    return render_template("vigenere_cipher.html")

@app.route("/ciphers/rail_fence")
def rail_fence():
    return render_template("rail_fence_cipher.html")
@app.route("/ciphers/scytale")
def scytale_cipher():
    return render_template("scytale_cipher.html")

@app.route("/ciphers/aes")
def aes_cipher():
    return render_template("aes_cipher.html")
@app.route("/ciphers/des")
def des_cipher():
    return render_template("des_cipher.html")

@app.route("/ciphers/chacha20")
def chacha20_cipher():
    return render_template("chacha20_cipher.html")
@app.route("/ciphers/rc4")
def rc4_cipher():
    return render_template("rc4_cipher.html")


@app.route("/articles")
def articles_page():
    return render_template("articles.html")
@app.route("/articles/what_is_cryptography")
def article_1():
    return render_template("article_1.html")


@app.route("/readme")
def readme():
    return render_template("readme.html")


@app.route("/tools/encryptor", methods=("GET", "POST"))
def encryptor():
    if request.method == "POST":
        if not request.form.get("plain_text"):
            return render_template("err_encrypt.html")

        plain_text = request.form.get("plain_text")
        key = Fernet.generate_key()
        fer = Fernet(key)
        cipher_text = fer.encrypt(plain_text.encode("utf-8"))

        return render_template("encrypted.html",
                               plain_text = plain_text,
                               cipher_text = cipher_text.decode("utf-8"),
                               key = key.decode("utf-8"))

    return render_template("encrypting.html")

@app.route("/tools/decryptor", methods=("GET", "POST"))
def decryptor():
    if request.method == "POST":
        if not request.form.get("key") or not request.form.get("cipher_text"):
            return render_template("err_decrypt.html")

        key = request.form.get("key").encode("utf-8")
        cipher_text = request.form.get("cipher_text").encode("utf-8")

        fer = Fernet(key)

        decryption = fer.decrypt(cipher_text)

        return render_template("decrypted.html",
                               key=key.decode("utf-8"),
                               cipher_text=cipher_text.decode("utf-8"),
                               decryption=decryption.decode("utf-8"))

    return render_template("decrypting.html")

@app.route("/tools/chatbot", methods=("GET", "POST"))
def chatbot():
    if request.method == "POST":
        user_text = request.form.get("user_text")

        prompt = f"user: {user_text}\nChatbot: "
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.5,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0
        )

        gpt_response = response.choices[0].text.strip()

        return render_template("chatbot_response.html",
                               user_text=user_text,
                               gpt_response=gpt_response)

    return render_template("chatbot.html")



if __name__ == "__main__":
    app.run(debug=True)
