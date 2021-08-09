#From waveshare, included in folder
#https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python
#You can look at their examples for how stuff works. (I did!)
import epd2in7

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

from bs4 import BeautifulSoup
import urllib

def main():
    epd = epd2in7.EPD()
    epd.init()
    #get a haiku!
    page = urllib.request.urlopen('https://randomhaiku.com/').read()
    soup = BeautifulSoup(page, 'html.parser')
    soup.prettify()
    #the random haiku website has 3 line elements in it. makes it easy to scrape.
    lines = soup.find_all('line')
    #we define a blank canvas the size of the e-paper module (but with the width and height switched because we need to rotate it at the end)
    image = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)    # rotato!
    #we're making a blank image to write on
    draw = ImageDraw.Draw(image)
    #specify some fonts
    font = ImageFont.truetype('/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf', 16)
    fontbig = ImageFont.truetype('/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',72)
    #telling it how far I want the haiku indented
    x_pos = 5
    draw.text((x_pos, 0), 'Haiku!', font = fontbig, fill = 0)
    #we're going down 4 pixels below the big Haiku!
    y_pos = 80
    #and now for the 3 little lines to get a visit from the big bad wolf.
    for line in lines:
        draw.text((x_pos, y_pos), line.text, font = font, fill = 0)
        #move down the size of the font + 4 pixels again for each line
        y_pos += 20
    #display our text image on the e-paper module
    epd.display(epd.getbuffer(image.rotate(90, expand=True)))


if __name__ == '__main__':
    main()
