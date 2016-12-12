"""This is a program to send my friends text messages periodically to remind
them that I'm thinking about them, so I can satisfy their need for constant
validation and endless memes.
"""


import smtplib
import sys
import random

library_of_memes = ['MEMEmeme',

                    "Greetings Earthings! I have come to tell you that you, ,, "
                    "are very cool,, ,,, and do cool things.... I have come "
                    "all the way from space to tell you this,,....",

                    "BODE",

                    "If you would like to submit a meme of your own, please "
                    "email 247mememachine@gmail.com and it will be placed "
                    "under review. ",

                    "This is meme number 4.",

                    "I want y'all to know that this is the first project I've"
                    " done outside of class",

                    "I hope you are enjoying this exercise in meme production, "
                    "and that I have been able to contribute to the growth of "
                    "the memeconomy like a good citizen",

                    "Your Daily Dose of Validation! You are a rad person with"
                    " lots of creative talent and great potential!",

                    "Your Daily Dose of Validation! I care about you and hope"
                    " that you always have abundant memes and good pets!",

                    "Tis I, the frenchiest fry",

                    "Cars are tasty"
                    ]
def meme_selector():
    meme = library_of_memes[random.randint(0, len(library_of_memes) - 1)]
    print meme
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
