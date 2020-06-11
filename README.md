# Pushwords
you can push words to your group by schedule runing this code

# Usage

## Set a schedule task on your mac

1. Open terminal input: crontab -e

2. Input command description： * * * * *  python  telegram-bot.py
                              
                               分 时 日 月 年 python终端 执行文件

eg: 0 8 * * * [the path of your python] [the path of your file]

    每天8点运行程序

link:how to get group id and token:
https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

3. In order to get the group chat id, do as follows:

(1) Add the Telegram BOT to the group.

(2) Get the list of updates for your BOT:

https://api.telegram.org/bot<YourBOTToken>/getUpdates
Ex:

https://api.telegram.org/bot123456789:jbd78sadvbdy63d37gda37bd8/getUpdates

(3) Look for the "chat" object:

{"update_id":8393,"message":{"message_id":3,"from":{"id":7474,"first_name":"AAA"},"chat":{"id":,"title":""},"date":25497,"new_chat_participant":{"id":71,"first_name":"NAME","username":"YOUR_BOT_NAME"}}}

This is a sample of the response when you add your BOT into a group.

Use the "id" of the "chat" object to send your messages.



