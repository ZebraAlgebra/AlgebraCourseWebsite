import os
import re
import itertools
def generate_md():
    '''
    Helps the user generate md from tex file
    '''
    # describe usage in terminal
    print("=" * os.get_terminal_size()[0])
    print("Usage: generate md from tex.")
    print("=" * os.get_terminal_size()[0])
    # prompt the user to input homework id
    hw_id = input("What is the homework id? (e.g. 01, 13)\n")
    SOURCE_DIR = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'tex', hw_id + ".tex"))
    TARGET_DIR_TEX = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'md', hw_id + ".md"))
    with open(TARGET_DIR_TEX, 'w') as target, open(SOURCE_DIR, 'r') as source:
        old = source.read()
        old = create_headers_in_md(old, hw_id)
        # print(old)
        old = replace_dollars_underlines(old)
        # print(old)
        old = replace_enum_items(old)
        print(old)
        target.write(old)
    return None

def create_headers_in_md(old, hw_id):
    '''
    Add a title
    Replaces percent signs by ##
    '''
    old = old.replace("%", "##")
    return "\n\n".join(["# Questions - Week hw_id".replace('hw_id', hw_id), old])

def replace_dollars_underlines(old):
    '''
    Replaces dollar signs and underlines by mdbook renderable syntax
    '''
    # replace underlines
    old = old.replace("_", "\\_")
    # replace displaystyle $$'s
    d = {(True, "$"): "\\\\(", (False, "$"): "\\\\)",
         (True, "$$"): "\\\\[", (False, "$$"): "\\\\]",}
    for c in  ["$$", "$"]:
        old_displaystyle_split = old.split(c)
        parity = True
        for i in range(0, len(old_displaystyle_split) - 1):
            old_displaystyle_split[i] += d[(parity, c)]
            parity = not parity
        old = "".join(old_displaystyle_split)
    return old

def replace_enum_items(old):
    '''
    Replaces enumerates and items to a boiler plate of things.
    Will always convert to unordered lists.
    If need more specialization, need to manually update.
    '''
    lines = old.split("\n")
    unsupported_strs = ["\\prefix{env}".replace("prefix", p).replace("env", q)
                   for p ,q in itertools.product(["begin", "end"], ["enumerate", "itemize"])]
    new = []
    for line in lines:
        for unsupported_str in unsupported_strs:
            print(unsupported_str)
            if unsupported_str in line:
                line = ""
                continue
        new.append(line.replace("    \\item", "*"))
    return "\n".join(new)


def main():
    generate_md()

if __name__ == '__main__':
    main()