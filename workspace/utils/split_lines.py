import os

def split_lines():
    '''
    Creates a tex file.
    Opens the required png and tex.
    '''
    print("=" * os.get_terminal_size()[0])
    print("Usage: copy txt file to tex.")
    print("=" * os.get_terminal_size()[0])
    hw_id = input("What is the homework id? (e.g. 01, 13)\n")
    SOURCE_TEX = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'tex', hw_id + ".tex"))
    with open(SOURCE_TEX, 'r') as s:
        S = s.read().replace(". ", ".\n")
    with open(SOURCE_TEX, 'w') as s:
        s.write(S)
    return None

def main():
    split_lines()

if __name__ == '__main__':
    main()