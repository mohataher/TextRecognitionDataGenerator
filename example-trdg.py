import os

from trdg.generators import GeneratorFromStrings

# The generators use the same arguments as the CLI, only as parameters
for font in ['./fonts/'+f for f in os.listdir('fonts')]:
    generator = GeneratorFromStrings(
        ['النَّفْسُ - ١٢٣ إنّ الله غفُــور - بالله - 0123'], #[ ' إن الله غفور بالله', ],
        size=70,
        count=1, #45,
        blur=0,
        fonts=[font],#['./fonts/Rakkas-Regular.ttf'], #['./fonts/'+f for f in os.listdir('fonts')],
        rtl=True,
        word_split=False
    )

    count=0
    for img, lbl in generator:
        print(count)
        print(lbl)
        print(font)
        img.show()
        count+=1
        #break
