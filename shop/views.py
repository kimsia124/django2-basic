# shop/views.py

from django.http import HttpResponse
from django.shortcuts import render

import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용입니다.'.format(year))

def response_pillow_image(request, str):
    ttf_path = 'C:/Windows/fonts/malgun.ttf'
    
    image_url = 'https://www.flowermeaning.com/flower-pics/Gladiolus-Meaning.jpg'
    res = requests.get(image_url)
    io = BytesIO(res.content)
    io.seek(0)

    canvas = Image.open(io).convert('RGBA')
    font = ImageFont.truetype(ttf_path, 40)
    draw = ImageDraw.Draw(canvas)

    text = str
    left, top = 10, 10
    margin = 10
    width, heigth = font.getsize(text)
    right = left + width + margin
    bottom = top + heigth + margin

    draw.rectangle((left, top, right, bottom), (255, 255, 255))
    draw.text((15, 15), text, font=font, fill=(0, 0, 0))
    
    response = HttpResponse(content_type='image/png')
    canvas.save(response, format='PNG')
    return response
