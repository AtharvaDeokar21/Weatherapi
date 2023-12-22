import requests  
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date
  
api_key = "2305d4e86f2c2a7f2474c8fbddde756d"
position = [705, 1020, 1340, 1655, 1975]

uk_list = ["London", "Manchester", "Edinburgh", "Bristol", "Birmingham"]
india_list = ["Jaipur", "Delhi", "Mumbai", "Kolkata", "Chennai"]
us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]
country_list = [uk_list, india_list, us_list]

for country in country_list:
    image = Image.open("my.png") 
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("inter.ttf",size=100)
    content = "Latest Weather Forecast"
    color = 'rgb(255,255,255)'
    (x,y) = (75,55)
    draw.text((x,y), content, color, font=font)

    font = ImageFont.truetype("inter.ttf",size=85)
    content = date.today().strftime("%A - %B %d, %Y")
    color = 'rgb(255,255,255)'
    (x,y) = (75,315)
    draw.text((x,y), content, color, font=font)


    index = 0
    for city in country:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        font = ImageFont.truetype("font.ttf",size=85)
        color = 'rgb(0,0,0)'
        (x,y) = (85,position[index])
        draw.text((x,y), city, color, font=font)
        
        font = ImageFont.truetype("inter.ttf",size=60)
        temperature = data['main']['temp']
        content = f"{temperature}\u00b0"
        color = 'rgb(255,255,255)'
        (x,y) = (910,position[index])
        draw.text((x,y), content, color, font=font)
        
        font = ImageFont.truetype("inter.ttf",size=60)
        humidity = data['main']['humidity']
        content =  f"{humidity}%"
        color = 'rgb(255,255,255)'
        (x,y) = (1250,position[index])
        draw.text((x,y), content, color, font=font)
        
        index += 1
        
    #image.show()
    image.save(str(date.today()) + country[0] + ".png")
    image_pdf = image.convert('RGB')
    image_pdf.save(str(date.today()) + country[0] + ".pdf")
#This code just saves the created image in .png & .pdf format inside the folder.
#IF we use image.show() it will also show the three images one by one after default interval of time.