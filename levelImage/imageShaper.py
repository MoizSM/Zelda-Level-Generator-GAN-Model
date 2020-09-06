from PIL import Image

fName = 'fireBlock_cyan'
image = Image.open(fName + '.png')
image.load()

background = Image.new("RGB", image.size, (255, 255, 255))
background.paste(image, mask=image.split()[3]) # 3 is the alpha channel

background.save(fName + '_new.png', 'PNG', quality=80)