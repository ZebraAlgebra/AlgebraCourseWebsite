import os
from PIL import Image, ImageFont, ImageDraw
# import PIL
import inflect
def generate_png():
    '''
    Helps the user to generate a combined screenshot of homeworks.
    Reads all png from a specified directory, combine them,
    and annotate them if needed.
    '''
    # describe usage in terminal
    print("=" * os.get_terminal_size()[0])
    print("Usage: generate combined png.")
    print("=" * os.get_terminal_size()[0])
    # prompt the user to input homework id
    hw_id = input("What is the homework id? (e.g. 01, 13)\n")
    # read photos and fonts
    SOURCE_DIR = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 2), 'png', hw_id))
    TARGET_DIR = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'png'))
    FONTS_FILE = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 2), 'fonts', 'Tilt_Warp', 'static', 'TiltWarp-Regular.ttf'))
    CAPTION_SIZE = 35
    FONT = ImageFont.truetype(FONTS_FILE, CAPTION_SIZE)
    TARGET_WIDTH = 910
    raw_screenshots_files = [f for f in os.listdir(SOURCE_DIR)]
    raw_screenshots_files.sort()
    raw_screenshots_imgs = [Image.open(os.path.join(SOURCE_DIR, f))
                            for f in raw_screenshots_files]
    num_pics = len(raw_screenshots_imgs)
    print(f"There are {num_pics} pictures in here.")
    # resize them all to the same width
    for i in range(num_pics):
        raw_screenshots_imgs[i] = resize_by_width(raw_screenshots_imgs[i],
                                                  TARGET_WIDTH)
    # see if need to input caption, if need to then do it
    need_input = input("Are captions needed? (y/n)\n") == "y"
    p = inflect.engine()
    if not need_input:
        combined = combine(raw_screenshots_imgs, CAPTION_SIZE, FONT, TARGET_WIDTH)
    else:
        while need_input:
            input_info = {}
            item_count = 1
            is_inputting = True
            while is_inputting:
                print(f"-- Start of {p.ordinal(item_count)} caption:")
                pos = int(input("---- Specify position (start=0, end=num_pics):\n---- "))
                if not 0 <= pos <= len(raw_screenshots_imgs):
                    input(f"---- invalid input! try again!")
                    continue
                text = input("---- Specify text:\n---- ")
                input_info[pos] = text
                item_count += 1
                is_inputting = input("---- Input more (y/n)?\n---- ") == "y"
            input_info = list(input_info.items())
            input_info.sort()
            captions_summarize(input_info)
            combined = combine(raw_screenshots_imgs, CAPTION_SIZE, FONT, TARGET_WIDTH, input_info)
            need_input = input("Does this look wrong? (y/n)\n---- ").lower() == 'y'
    # save file
    combined.save(os.path.join(TARGET_DIR, hw_id + ".png"), "PNG")
    return None

def resize_by_width(img, TARGET_WIDTH):
    width, height = img.size
    new_height = int(TARGET_WIDTH * height / width)
    new_img = img.resize((TARGET_WIDTH, new_height))
    return new_img

def captions_summarize(input_info):
    print("Here is a summary of the homeworks you inputted:")
    for pos, text in input_info:
        print(f"-> position {pos}: {text}")
    return None

def combine(raw_screenshots_imgs, CAPTION_SIZE, FONT, TARGET_WIDTH, input_info=[]):
    num_pics = len(raw_screenshots_imgs)
    # if caption is required:
    if input_info:
        # convert input_info to an array of pictures
        all_caption_pos = [pos for pos, _ in input_info]
        all_caption_texts = [text for _, text in input_info]
        all_caption_pics = list(map(lambda x: text_to_im(x, CAPTION_SIZE, FONT),
                                    all_caption_texts))
        # insert in appropriate position
        pic_array = []
        alternate_pos = 0
        for i in range(num_pics + 1):
            if i in all_caption_pos:
                pic_array.append(all_caption_pics[alternate_pos])
                alternate_pos += 1
            if i != num_pics:
                pic_array.append(raw_screenshots_imgs[i])
        return combine(pic_array, CAPTION_SIZE, FONT, TARGET_WIDTH)
    # else we just combine them
    heights = [img.size[1] for img in raw_screenshots_imgs]
    for i in range(1, num_pics):
        heights[i] += heights[i - 1]
    total_height = heights[-1]
    heights.insert(0, 0)
    BACKGROUND_COLOUR = (200, 200, 200)
    img = Image.new("RGB", (TARGET_WIDTH, total_height), BACKGROUND_COLOUR)
    for i in range(num_pics):
        img.paste(raw_screenshots_imgs[i].copy(), (0, heights[i]))
    img.show()
    return img


def text_to_im(text, CAPTION_SIZE, FONT):
    START_COORDINATE = (CAPTION_SIZE // 2, CAPTION_SIZE // 2)
    width, height = CAPTION_SIZE * len(text), int(CAPTION_SIZE * 2.5)
    BACKGROUND_COLOUR = (200, 200, 200)
    TEXT_COLOUR = (0, 0, 139)
    img = Image.new("RGB", (width, height), BACKGROUND_COLOUR)
    draw = ImageDraw.Draw(img)
    draw.text(START_COORDINATE, text, TEXT_COLOUR, font=FONT)
    return img


def main():
    generate_png()

if __name__ == '__main__':
    main()