import os
import keyboard
import time


import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

###
image_name = "output_tileset.png"
### 
def main():
    print('Hello, world!')
    while True:
        if keyboard.is_pressed('alt+p'):
            response = openai.Image.create_variation(
                image=open(image_name, "rb"),
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            print(image_url)
            print('daa')
            time.sleep(5)

if __name__ == '__main__':
    main()