import os

def generate_tex():
    '''
    Creates a tex file.
    Opens the required png and tex.
    '''
    print("=" * os.get_terminal_size()[0])
    print("Usage: copy txt file to tex.")
    print("=" * os.get_terminal_size()[0])
    hw_id = input("What is the homework id? (e.g. 01, 13)\n")
    SOURCE_PNG = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'png', hw_id + ".png"))
    SOURCE_TEX = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'tex', hw_id + ".tex"))
    os.system(f"code {SOURCE_PNG}")
    os.system(f"code {SOURCE_TEX}")
    return None

def main():
    generate_tex()
    return None

if __name__ == '__main__':
    main()