#!/usr/bin/env python3
from rivescript import RiveScript

bot = RiveScript(utf8=True)
bot.load_directory("./brain")
bot.sort_replies()

unpol = str.maketrans("ąćęłńóśźż", "acelnoszz")


def banner():
    print("""
    __  __ __   ____  ______  ____    ___   ______
   /  ]|  |  | /    ||      ||    \  /   \ |      |
  /  / |  |  ||  o  ||      ||  o  )|     ||      |
 /  /  |  _  ||     ||_|  |_||     ||  O  ||_|  |_|
/   \_ |  |  ||  _  |  |  |  |  O  ||     |  |  |
\     ||  |  ||  |  |  |  |  |     ||     |  |  |
 \____||__|__||__|__|  |__|  |_____| \___/   |__|
                                                   """)


def prompt():
    print("> ", end="")
    feed = input().translate(unpol)
    if feed == "/quit":
        quit()
    else:
        return feed


def response(msg):
    reply = bot.reply("localuser", msg)
    print("Bot >", reply)


def main():
    banner()
    while True:
        response(prompt())


if __name__ == '__main__':
    main()
