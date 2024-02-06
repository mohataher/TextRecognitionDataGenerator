import os

import arabic_reshaper
import arabic_reshaper.reshaper_config

config = arabic_reshaper.reshaper_config.default_config
#print(config['language'])
#config['language']='ArabicV2'
config['delete_harakat']=False
config['use_unshaped_instead_of_isolated']=True
config['ARABIC LIGATURE ALLAH'] = False
areshaper= arabic_reshaper.ArabicReshaper(config)
#areshaper=arabic_reshaper

count=0
dir_ = 'fonts/'
for font in os.listdir(dir_):
  print(count)
  count+=1
  font_dir = dir_+font
  text_to_be_reshaped = 'النَّفْسُ - ١٢٣ إنّ الله غفُور - بالله - 0123'

  reshaped_text = areshaper.reshape(text_to_be_reshaped)
  # At this stage the text is reshaped, all letters are in their correct form
  # based on their surroundings, but if you are going to print the text in a
  # left-to-right context, which usually happens in libraries/apps that do not
  # support Arabic and/or right-to-left text rendering, then you need to use
  # get_display from python-bidi.
  # Note that this is optional and depends on your usage of the reshaped text.

  from bidi.algorithm import get_display
  bidi_text = get_display(reshaped_text)
  # At this stage the text in bidi_text can be easily rendered in any library
  # that doesn't support Arabic and/or right-to-left, so use it as you'd use
  # any other string. For example if you're using PIL.ImageDraw.text to draw
  # text over an image you'd just use it like this...

  from PIL import Image, ImageDraw, ImageFont

  # We load Arial since it's a well known font that supports Arabic Unicode
  font = ImageFont.truetype(font_dir, 40)

  image = Image.new('RGBA', (900, 100), (255,255,255,0))
  image_draw = ImageDraw.Draw(image)
  image_draw.text((10,10), reshaped_text, fill=(0,0,0,255), font=font)

  # Now the text is rendered properly on the image, you can save it to a file or just call `show` to see it working
  print(font_dir)
  image.show()
  # For more details on PIL.Image and PIL.ImageDraw check the documentation
  # See http://pillow.readthedocs.io/en/5.1.x/reference/ImageDraw.html?#PIL.ImageDraw.PIL.ImageDraw.Draw.text

