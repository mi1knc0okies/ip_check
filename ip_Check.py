from requests import get
import os
from time import sleep
from msg import create_message_and_send


def main():
    ip = get('https://api.ipify.org').text
    ip_list = check_ip(ip)
    if ip not in ip_list:
        to = "jesse56@gmail.com"
        sender = "j5bot24@gmail.com"
        subject = "IP Test"
        message_text_html = ip
        message_text_plain = ip
        attached_file = r'C:\Users\Me\Desktop\audio.m4a'
        create_message_and_send(sender, to, subject, message_text_plain, message_text_html, attached_file)
    else:
        sleep(6000)


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
        print("Your IP has changed to", new_ip)
    else:
        print("Your IP has not changed.")

    with open("iplog.txt", "w") as f:
        for new_ip in past_ip:
            f.write(new_ip + "\n")
        f.close()

    return past_ip



main()