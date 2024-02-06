import os

from PIL import ImageFont

from trdg.generators import GeneratorFromStrings
from trdg.utils import get_text_height

# The generators use the same arguments as the CLI, only as parameters
text = 'النَّفْسُ - ١٢٣ إنّ الله غفُــور - بالله - 0123'

image_font = ImageFont.truetype(font='./fonts/Rakkas-Regular.ttf', size=50)

for c in text:
    print('char:', c, ': ', get_text_height(image_font, c))

print('height of all text:', get_text_height(image_font, text))
print('height of ghain+ with tashkeel', get_text_height(image_font, 'ـفـغُّـ'))
print('height of ghain with tashkeel', get_text_height(image_font, 'غ'))

print('height of غفور with tashkeel', get_text_height(image_font, 'غفور'))
print('height of مرمر with tashkeel', get_text_height(image_font, 'سمير'))