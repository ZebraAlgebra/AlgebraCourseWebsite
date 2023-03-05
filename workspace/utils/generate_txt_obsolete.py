'''
It turns out that https://snip.mathpix.com/ does a far much better job.
This function will never be called.
'''

import os
import pygame
from PIL import Image
from pytesseract import image_to_string

def generate_txt():
    '''
    Helps the user generate screenshots of images and later use for conversion.
    '''
    # describe usage in terminal
    print("=" * os.get_terminal_size()[0])
    print("Usage: dissect combined png to pngs, label them, and convert.")
    print("=" * os.get_terminal_size()[0])
    # prompt the user to input homework id and retrieve combined png
    hw_id = input("What is the homework id? (e.g. 01, 13)\n")
    SOURCE_PNG = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'png', hw_id + ".png"))
    TARGET_TXT = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'txt', hw_id + ".txt"))
    big_png = Image.open(SOURCE_PNG)
    # segment into horizontal lines and segment vertically into chunks
    big_png = big_png.resize((int(dim * 2) for dim in big_png.size))
    lines = horizontal_strip(big_png)
    segmented_png = []
    for line in lines:
        segmented_png.append(vertical_strip(line))
    print(len(segmented_png))
    # transform to text
    custom_oem_psm_config = r'-l grc+eng --oem 3 --psm 7'
    model = lambda x: image_to_string(x, config = custom_oem_psm_config)
    with open(TARGET_TXT, 'w') as t:
        line_count = 0
        for line in segmented_png:
            line_count += 1
            d = {"regular": "", "inline": "$", "display": "$$"}
            for (pic, label) in line:
                t.write(d[label] + model(pic)[:-2] + d[label] + " ")
            if line_count == len(segmented_png) - 1:
                continue
            t.write("\n")
    os.system(f"code {TARGET_TXT}")
    return None

def horizontal_strip(big_png):
    '''
    Cut image into horizontal strips.
    Choose a top left corner (alternative: press key to choose top left corner)
    and choose bottom right corner to crop.
    '''
    pygame.init()
    screen = pygame.display.set_mode(big_png.size)
    capturing = True
    refresher = pygame.time.Clock()
    corners = [0, 0, 0, 0]
    parity = False
    strips = []
    while capturing:
        refresher.tick(60)
        surface = pygame.image.fromstring(big_png.tobytes(),
                                      big_png.size, big_png.mode).convert()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                capturing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if parity:
                    corners[2], corners[3] = pygame.mouse.get_pos()
                else:
                    corners[0], corners[1] = pygame.mouse.get_pos()
                parity = not parity
            elif event.type == pygame.KEYDOWN:
                parity = not parity
        pygame.display.flip()
        screen.fill(0)
        screen.blit(surface, surface.get_rect(topleft = (0, 0)))
        if corners[3] != 0:
            if corners[3] > big_png.size[0]:
                continue
            strips.append(big_png.crop(tuple(corners)))
            big_png = big_png.crop((0, corners[3], *(big_png.size)))
            corners = [0, 0, 0, 0]
    return strips

def vertical_strip(strip):
    '''
    Given horizontal strip, convert to vertical strips.
    Returns a list of 2-tuples, containing image,
    along with the info that whether it is LaTeX or not.
    If any key is pressed, label is LaTeX inline;
    if pressed again, label is LaTeX Display;
    otherwise nothing.
    '''
    pygame.init()
    screen = pygame.display.set_mode(strip.size)
    capturing = True
    refresher = pygame.time.Clock()
    right_side = 0
    label = "regular"
    label_switch = {"regular": "inline",
                    "inline": "display",
                    "display": "display",}
    strips = []
    while capturing:
        refresher.tick(60)
        surface = pygame.image.fromstring(strip.tobytes(),
                                      strip.size, strip.mode).convert()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                capturing = False
            elif event.type == pygame.KEYDOWN:
                label = label_switch[label]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                right_side, _ = pygame.mouse.get_pos()
        pygame.display.flip()
        screen.fill(0)
        screen.blit(surface, surface.get_rect(topleft = (0, 0)))
        if right_side != 0:
            strips.append((strip.crop((0, 0, right_side, strip.size[1])),
                           label))
            strip = strip.crop((right_side, 0,
                                strip.size[0], strip.size[1]))
            right_side = 0
            label = "regular"
    return strips

def main():
    generate_txt()

if __name__ == '__main__':
    main()