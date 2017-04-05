import csv
import datetime as dt
import requests


def write_text(writer_names, name_list, text, locs, name_ids, curr_loc):
    for each in writer_names:
        # each is regular name
        # name is nickname in group
        for name in name_list:
            if name.startswith(each):
                tag, num = name.split(',')
                text += "@"+tag+"\n"
                name_ids += [num[1:]]
                locs += [[curr_loc, len(tag)+1]]
                curr_loc += len(tag) + 2
                break
    return text


def run(sched, names, bot_id, editor_msg):
    with open(sched, newline='') as sched_csv:
        dept = csv.reader(sched_csv, quotechar='|')
        dept = [row for row in dept]

        # for this to work all days of week must be defined in csv
        # monday is 0 index.

        day = dt.datetime.today().weekday()
        writers_today = dept[day]
        if day + 1 <= 6:
            writers_tomrr = dept[day+1]
        else:
            writers_tomrr = dept[0]

        name_list = []
        with open(names, 'r') as names:
            for line in names:
                line = line.strip()
                name_list += [line]

        text = "Due Today:\n"
        locs = []
        name_ids = []
        curr_loc = len(text)

        text = write_text(writers_today, name_list, text,
                          locs, name_ids, curr_loc)

        mess2 = {
            "bot_id": bot_id,
            "text": text,
            "attachments": [
                {
                    "type": "mentions",
                    "user_ids": name_ids,
                    "loci": locs
                }
            ]
        }
        print(text)
        r = requests.post('https://api.groupme.com/v3/bots/post', json=mess2)
        print(r)

        text = "Due Tomorrow:\n"
        curr_loc = len("Due Tomorrow:\n")

        text = write_text(writers_tomrr, name_list, text,
                          locs, name_ids, curr_loc)

        text += editor_msg

        message = {
            "bot_id": bot_id,
            "text": text,
            "attachments": [
                {
                    "type": "mentions",
                    "user_ids": name_ids,
                    "loci": locs
                }
            ]
        }
        print(text)
        r = requests.post('https://api.groupme.com/v3/bots/post', json=message)
        print(r)
