"""This is a program to send my friends text messages periodically to remind
them that I'm thinking about them, so I can satisfy their need for constant
validation and endless memes.
"""


import smtplib
import sys
import random

import library_of_memes as memelib

def meme_selector():
    meme = memelib.library_of_memes[random.randint(0,
                                    len(memelib.library_of_memes) - 1)]
    return meme

def read_recipients(filename):
    recipients = []
    with open(filename, "r") as f:
        for line in f:
            recipients.append(line.strip())

    return recipients

def main():
    recipients = read_recipients( # TODO Make this path more general
            "/home/caitlyn/Projects/Automatic_Meme_Deliverer/recipients.txt")

    meme_machine = smtplib.SMTP('smtp.gmail.com', 587)

    # TODO Separate into other functions
    hello = meme_machine.ehlo()
    if hello[0] != 250:
        print("Ehlo failed. Exiting.")
        meme_machine.quit()
        sys.exit()
    tls = meme_machine.starttls()
    if tls[0] != 220:
        print("TLS failed. Exiting.")
        meme_machine.quit()
        sys.exit()


    psswd = raw_input() # TODO Should standardize input. Read or redirected
    meme_machine.login("247mememachine@gmail.com", psswd)

    # TODO Generalize sending address, while you're at it

    for address in recipients:
        meme_machine.sendmail("247mememachine@gmail.com",
                            address, "Subject: \n" + meme_selector())
    
    meme_machine.quit()


if __name__ == '__main__':
    main()
