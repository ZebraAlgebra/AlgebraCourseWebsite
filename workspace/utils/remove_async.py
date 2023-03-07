import os

def remove_async():
    '''
    Removes all the asyncs from the htmls files in book
    since it makes mathjax texts look awful
    '''
    print("=" * os.get_terminal_size()[0])
    print("Usage: removes async from some html files.")
    print("=" * os.get_terminal_size()[0])
    TARGET_DIR = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'website', 'book'))
    for subdir, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file[-4:] == "html":
                with open(os.path.join(subdir, file), 'r') as s:
                    temp = s.read().replace("async ", " ")
                with open(os.path.join(subdir, file), 'w') as s:
                    s.write(temp)
    print("Done.")
    return None

def main():
    remove_async()

if __name__ == '__main__':
    main()