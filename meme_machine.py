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

def meme_ehlo(meme_machine):
    hello = meme_machine.ehlo()
    if hello[0] != 250:
        print("Ehlo failed. Exiting.")
        meme_machine.quit()
        sys.exit()

def meme_tls(meme_machine):
    tls = meme_machine.starttls()
    if tls[0] != 220:
        print("TLS failed. Exiting.")
        meme_machine.quit()
        sys.exit()


def main(): # TODO Proper documentation for functions
    # TODO Make path more general
    cur_directory = "/home/caitlyn/Projects/Automatic_Meme_Deliverer/";
    recipients = read_recipients(cur_directory + sys.argv[2])

    meme_machine = smtplib.SMTP('smtp.gmail.com', 587)

    meme_ehlo(meme_machine);
    meme_tls(meme_machine);

    with open(cur_directory + sys.argv[1], "r") as pss:
        psswd = pss.read().strip()
    meme_machine.login("247mememachine@gmail.com", psswd)

    with open(cur_directory + sys.argv[3], "r") as sndr:
        sender = sndr.read().strip();

    for address in recipients:
        meme_machine.sendmail(sender, address, "Subject: \n" + meme_selector())
    
    meme_machine.quit()


if __name__ == '__main__':
    main()
