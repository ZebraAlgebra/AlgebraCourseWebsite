import os
import re
def generate_pdf():
    '''
    Helps the user generate pdf from tex file
    '''
    # describe usage in terminal
    print("=" * os.get_terminal_size()[0])
    print("Usage: generate pdf from tex.")
    print("=" * os.get_terminal_size()[0])
    # prompt the user to input homework id
    hw_id = input("What is the homework id? (e.g. 01, 13)\n")
    SOURCE_TEMPLATE = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 2), 'templates', "sample_qtn.tex"))
    SOURCE_DIR = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'tex', hw_id + ".tex"))
    TARGET_DIR_TEX = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'pdf', hw_id + ".tex"))
    TARGET_DIR_PDF = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'pdf', hw_id + ".pdf"))
    with open(TARGET_DIR_TEX, 'w') as targ, open(SOURCE_TEMPLATE, 'r') as temp, open(SOURCE_DIR, 'r') as cont:
        template = temp.read()
        content = cont.read()
        targ.write(template.replace("$ $", content))
    prettify_problems(TARGET_DIR_TEX)
    if os.path.isfile(TARGET_DIR_PDF):
        os.system(f"rm {TARGET_DIR_PDF}")
    os.system(" ".join(["pdflatex", TARGET_DIR_TEX, TARGET_DIR_PDF]))
    for suffix in ['aux', 'log', 'out']:
        os.system(f"rm {hw_id}.{suffix}")
    os.system(f"mv {hw_id}.pdf {TARGET_DIR_PDF}")
    return None

def prettify_problems(TARGET_DIR_TEX):
    header = "\section*{$}\paragraph{}"
    with open(TARGET_DIR_TEX, 'r') as t, open("temp.txt", 'w') as temp:
        for line in t:
            if line[0] == "%":
                temp.write(header.replace("$", line[2:-1]))
            else:
                temp.write(line)
    with open(TARGET_DIR_TEX, 'w') as t, open("temp.txt", 'r') as temp:
        for line in temp:
            t.write(line)
    os.system("rm temp.txt")
    return None

def main():
    generate_pdf()
    return None

if __name__ == '__main__':
    main()