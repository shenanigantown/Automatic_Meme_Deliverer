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


def main():

    recipients = [  # Recipients' email addresses removed for privacy.
                    # Kacie
                    # Jonny
                  ]

    
    meme_machine = smtplib.SMTP('smtp.gmail.com', 587)

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


    psswd = raw_input("Enter my password, please? ")
    meme_machine.login("247mememachine@gmail.com", psswd)

    meme_machine.sendmail("247mememachine@gmail.com",
                          "", # TODO Insert recipients
                          "Subject: \n" + meme_selector())
    print("Message sent. Exiting")
    meme_machine.quit()


if __name__ == '__main__':
    main()
