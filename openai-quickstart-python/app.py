'''This script create picture variation
'''
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
path = os.path.join("pics",image_name)
def main():
    print('Hello, world!\nPress Alt+P for a variantion\nIt takes approximately 10-20 seconds')
    while True:
        if keyboard.is_pressed('Alt+P'):
            print('working')
            response = openai.Image.create_variation(
                image=open(path, "rb"),
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            print(image_url)
            print('daa')
            time.sleep(5)

if __name__ == '__main__':
    main()