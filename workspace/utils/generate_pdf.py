import os
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
    os.system(" ".join(["pdflatex", TARGET_DIR_TEX, TARGET_DIR_PDF]))
    for suffix in ['aux', 'log', 'out', 'pdf']:
        os.system(f"rm {hw_id}.{suffix}")
    return None

def main():
    generate_pdf()
    return None

if __name__ == '__main__':
    main()