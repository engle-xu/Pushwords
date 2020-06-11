# Pushwords
you can push words to your group by schedule runing this code

# Usage

## Set a schedule task on your mac

1. Open terminal input: crontab -e

2. Input command description： * * * * *  python  telegram-bot.py
                              
                               分 时 日 月 年 python终端 执行文件

eg: 0 8 * * * [the path of your python] [the path of your file]

    每天8点运行程序
   
3. Click 'esc' button to exit, then 'shift' + ':' ,input 'wq' to save command and exit vim edit.

## Result presentation

Today is 2020-06-11, Tofel Words are:

1  alter : v.改变，更改 

2  alternate : a.轮流的，交替的；v.轮流，交替n.候选人，替代性选择 

3  altruism : n.利他主义；无私 

4  altruistic : a.无私的，为他人着想的 

5  aluminium : n.铝 

6  amalgam : n.混合物 

7  amalgamate : v.合并；混合 

8  amass : v.积聚 

9  amateur : n.业余爱好者 

10  amateurish : a.业余爱好的，不熟练的



## Reference:how to get group id and token:
https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

In order to get the group chat id, do as follows:

(1) Add the Telegram BOT to the group.

(2) Get the list of updates for your BOT:

https://api.telegram.org/bot<YourBOTToken>/getUpdates
Ex:

https://api.telegram.org/bot123456789:jbd78sadvbdy63d37gda37bd8/getUpdates

(3) Look for the "chat" object:

{"update_id":8393,"message":{"message_id":3,"from":{"id":7474,"first_name":"AAA"},"chat":{"id":,"title":""},"date":25497,"new_chat_participant":{"id":71,"first_name":"NAME","username":"YOUR_BOT_NAME"}}}

This is a sample of the response when you add your BOT into a group.

Use the "id" of the "chat" object to send your messages.



