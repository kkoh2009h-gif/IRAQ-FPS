#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
img=Image.new("RGB",(512,512),(5,12,26))
d=ImageDraw.Draw(img)
d.rectangle((0,0,512,18),fill=(220,25,48))
d.rectangle((0,494,512,512),fill=(15,190,75))
try:
 f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",76)
 f2=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",42)
except: f=f2=None
d.text((40,170),"IRAQ",font=f,fill=(245,248,255))
d.text((40,255),"FPS",font=f,fill=(255,40,60))
d.text((42,365),"MCHAWE",font=f2,fill=(190,210,235))
img.save("sce_sys/icon0.png")
