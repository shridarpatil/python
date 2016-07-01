from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 



new_im = Image.open("sample_in.jpg")
draw = ImageDraw.Draw(new_im)

fontsize=75;
font = ImageFont.truetype("Dosis-Regular/dosis/Dosis-Regular.ttf", fontsize)
draw.text((1500, 100),"Text", font=font)
draw.text((4200, 100),"Text", font=font)

new_im.save('sample-out.jpg',dpi=(300, 300),quality=96)
