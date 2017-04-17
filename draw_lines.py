#!/usr/bin/python3

from PIL import Image, ImageDraw

im = Image.new('RGB', (600, 600), (255, 255, 255))
draw = ImageDraw.Draw(im)

data = open('data.csv', 'r')
for line in data.readlines():
    x1, y1, x2, y2 = [float(i) * 300 + 600 for i in line.split(',')]
    color = None
    if x1 == x2:   # vertical
        color = 'blue'
    elif y1 == y2: # horizontal
        color = 'green'
    draw.line([(x1, y1), (x2, y2)], fill=color)

data.close()
del draw
im.save('lines.png', 'PNG')
