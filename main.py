#!/usr/bin/python3
import Bot

if __name__ == '__main__':

    msg = "You have an article due by tonight. Also, daily reminder "\
        "to everyone to 1) like social media posts 2) engage our "\
        "articles on third party forums and 3) comment on our "\
        "articles on the site. Thanks and FUCK A&M!"

    Bot.run('Big12.csv', 'big12_names.txt', '0d8ac1c1ac45a12a3a290181a5', msg)

    #msg = "ROLL MFN ARMCHAIR BOYS!!!"
    #Bot.run('MLB.csv', 'mlb_names.txt', '9fa3d39e97f404bb361d61782a', msg)
