from PIL import Image, ImageDraw, ImageFont
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-50, 5), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('F:/Picture/touxiang.jpg')
    add_num(image)
    image.show()
