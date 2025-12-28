# my-insta-bot
import os
from flask import Flask
from threading import Thread
from instagrapi import Client
import time
import random

app = Flask('')

@app.route('/')
def home():
    return "Бот фаъол аст!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# МАЪЛУМОТИ ШУМО
USER = 'Jiyonkhon_style'
PASS = 'jiyon_2007'

def start_bot():
    cl = Client()
    try:
        print("Воридшавӣ ба Instagram...")
        cl.login(USER, PASS)
        print("Муваффақият!")
        while True:
            threads = cl.direct_threads()
            for thread in threads:
                if thread.unread_count > 0:
                    cl.direct_answer(thread.id, "Салом! Ман боти худкор ҳастам. Паёми шумо қабул шуд.")
            time.sleep(random.randint(120, 300)) # Танаффуси 2-5 дақиқа
    except Exception as e:
        print(f"Хатогӣ: {e}")
        time.sleep(60)

if __name__ == "__main__":
    keep_alive()
    start_bot()
