import os
import datetime
import inflect
import json
def generate_notification():
    '''
    Prompts the user to input info about homework.
    Reads the sample notification file, and generate another one.
    Also generates a file containing title, datetime to be specified
    in the notification.
    '''
    # describe usage in terminal
    print("=" * os.get_terminal_size()[0])
    print("Usage: generate notification to put on COOL.")
    print("=" * os.get_terminal_size()[0])
    # prompt the user to input homework info
    due_date = datetime.datetime.strptime(
        input("What is the due date? (format: %Y %m%d %H%M, e.g. 2023 0303 2359)\n"),
        "%Y %m%d %H%M")
    hw_id = input("What is the homework id? (e.g. 01, 13)\n")
    # specify output location
    TARGET_DIR = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 3), 'files', 'notification'))
    SOURCE_DIR = os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 2), 'templates'))
    generate_notification_info(hw_id, due_date, TARGET_DIR, SOURCE_DIR)
    generate_notification_content(hw_id, due_date, TARGET_DIR, SOURCE_DIR)
    return None

def generate_notification_info(hw_id, due_date, TARGET_DIR, SOURCE_DIR):
    FILE_POSTFIX = "_info"
    FILE_TYPE = ".txt"
    due_date_str_coarse = due_date.strftime("%m/%d %a.")
    due_date_str_fine = due_date.strftime("%Y%m%d%H%M")
    source = os.path.join(SOURCE_DIR, "sample_notification" + FILE_POSTFIX + FILE_TYPE)
    target = os.path.join(TARGET_DIR, hw_id + FILE_POSTFIX + FILE_TYPE)
    with open(target, 'w') as t, open(source, 'r') as s:
        title = s.read()
        t.write(title.replace("<", hw_id).replace(">", due_date_str_coarse) +
                "\n" + due_date_str_fine)
    flag = input("Notification info has been generated! do you want to open it? (y/n)\n").lower() == 'y'
    if flag:
        os.system("open " + target)
    return None

def generate_notification_content(hw_id, due_date, TARGET_DIR, SOURCE_DIR):
    FILE_POSTFIX = "_content"
    FILE_TYPE = ".txt"
    source = os.path.join(SOURCE_DIR, "sample_notification" + FILE_POSTFIX + FILE_TYPE)
    target = os.path.join(TARGET_DIR, hw_id + FILE_POSTFIX + FILE_TYPE)
    data = json.load(open(os.path.normpath(os.path.join(
        os.path.abspath(__file__), *([os.pardir] * 2), 'data', 'generate_notification.json'))))
    hw_labels = list(data["urls"].keys())
    print("Now let's get your homework info:")
    done_input = False
    while not done_input:
        no_new_items = False
        item_count = 1
        p = inflect.engine()
        home_work_list = []
        while not no_new_items:
            print(f"-- Start of {p.ordinal(item_count)} homework item.")
            # prompt user to input the details
            label = input(f"-- Input your label: (expected labels: {hw_labels})\n   ")
            if label not in hw_labels:
                input(f"-- invalid input! try again!")
                continue
            description = input(f"-- Input your description:\n   ")
            read = input(f"-- Is this a reading assignment? (y/n)\n   ").lower() == 'y'
            optional = input(f"-- Is this assignment optional? (y/n)\n   ").lower() == 'y'
            home_work_list.append(hw_obj(label, description, data, read, optional))
            no_new_items = input("-- Finished inputting items? (y/n)\n   ").lower() == 'y'
            item_count += 1
        hw_summary(home_work_list)
        done_input = input("Does this looks good? (y/n)\n   ").lower() == 'y'
    with open(target, 'w') as t, open(source, 'r') as s:
        result = s.read()
        chunk = "\n".join(map(str, home_work_list))
        due_date_str_fine = due_date.strftime("%m/%d %H:%M (%a.)")
        file_urls = {"{pdf-link}": "https://zebraalgebra.github.io/AlgebraCourseWebsite/files/pdf/{label}.pdf",
                          "{tex-link}": "https://zebraalgebra.github.io/AlgebraCourseWebsite/files/tex/{label}.tex",
                          "{png-link}": "https://zebraalgebra.github.io/AlgebraCourseWebsite/files/png/{label}.png",
                          "{web-link}": "https://zebraalgebra.github.io/AlgebraCourseWebsite/my-first-book/book/hw/week_{label}/qtns.html",}
        for key in file_urls.keys():
            file_urls[key] = file_urls[key].replace("{label}", hw_id)
            result = result.replace(key, file_urls[key])
        t.write(result.replace("{hw_item}", chunk).replace("{due_date}", due_date_str_fine))
    flag = input("Notification content has been generated! do you want to open it? (y/n)\n").lower() == 'y'
    if flag:
        os.system("open " + target)
    return None

def hw_summary(home_work_list):
    print("Here is a summary of the homeworks you inputted:")
    for hw in home_work_list:
        print(f"-> {hw.label}: {hw.description}")
    return None

class hw_obj:
    def __init__(self, label, description, data, read, optional) -> None:
        self.label = label
        self.description = description
        self.data = data
        self.url = data["urls"][label]
        self.read = read
        self.optional = optional
    def __str__(self) -> str:
        if self.read:
            head = "Read"
        else:
            head = "Complete"
        if self.optional:
            head = " ".join(["(Optional)", head])
        mid = self.description
        tail = self.hrefify()
        if self.optional or self.read:
            tail = " ".join([tail, self.data["no_need"]])
        formatter = self.data["hw_item_format"]
        return formatter.replace("{head}", head).replace("{mid}", mid).replace("{tail}", tail)
    def hrefify(self) -> str:
        result = self.label
        if not self.url:
            return result
        formatter = self.data["href_settings"]
        return formatter.replace("{url}", self.url).replace("{label}", self.label)

def main():
    generate_notification()

if __name__ == '__main__':
    main()