#!/usr/bin/python3
import csv
import datetime as dt
import requests


def main():
    with open('MLB.csv', newline='') as mlb_csv:
        mlb = csv.reader(mlb_csv, quotechar='|')
        mlb = [row for row in mlb]

        # for this to work all days of week must be defined in csv
        # monday is 0 index.

        day = dt.datetime.today().weekday()
        writers = mlb[day+1]

        name_list = []
        with open('mlb_names.txt', 'r') as names:
            for line in names:
                line = line.strip()
                name_list += [line]

        text = "Due Today: "
        locs = []
        name_ids = []
        curr_loc = len(text)

        for each in writers:
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

        message = {
            "bot_id": "9fa3d39e97f404bb361d61782a",
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
if __name__ == '__main__':
    main()
