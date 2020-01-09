from requests import get
import os
from time import sleep
from msg import create_message_and_send


def main():
    while 0 !=True:
        ip = get('https://api.ipify.org').text
        ipstatus = check_ip(ip)
        if ipstatus is False:
            print("ip has not changed...zzzz")
            sleep(28000)
        else:
            to = "jesse56@gmail.com"
            sender = "j5bot24@gmail.com"
            subject = "Home IP has changed"
            message_text_html = ip
            message_text_plain = ip
            create_message_and_send(sender, to, subject, message_text_plain, message_text_html,)
            print("email has been sent")
            sleep(28000)


def check_ip(ip):
    new_ip = ip
    if not os.path.isfile("iplog.txt"):
        past_ip = []
    else:
        with open("iplog.txt", "r") as f:
            past_ip = f.read().split("\n")
            past_ip = list(filter(None, past_ip))

    if new_ip not in past_ip:
        past_ip.append(new_ip)
        with open("iplog.txt", "w") as f:
            for new_ip in past_ip:
                f.write(new_ip + "\n")
            f.close()
        return True
    else:
        f.close()
        return False





main()