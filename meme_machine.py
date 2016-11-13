"""This is a program to send my friends text messages periodically to remind
them that I'm thinking about them, so I can satisfy their need for constant
validation and endless memes.
"""


import smtplib
import sys
import random

library_of_memes = ['MEME\nmeme',
                    'What the fuck did you just fucking say about me, you '
                    'little bitch? I’ll have you know I graduated top of my '
                    'class in the Navy Seals, and I’ve been involved in '
                    'numerous secret raids on Al-Quaeda, and I have over 300 '
                    'confirmed kills. I am trained in gorilla warfare and I’m '
                    'the top sniper in the entire US armed forces. You are '
                    'nothing to me but just another target. I will wipe you '
                    'the fuck out with precision the likes of which has never '
                    'been seen before on this Earth, mark my fucking words. '
                    'You think you can get away with saying that shit to me '
                    'over the Internet? Think again, fucker. As we speak I am '
                    'contacting my secret network of spies across the USA and '
                    'your IP is being traced right now so you better prepare '
                    'for the storm, maggot. The storm that wipes out the '
                    'pathetic little thing you call your life. You’re fucking '
                    'dead, kid. I can be anywhere, anytime, and I can kill '
                    'you in over seven hundred ways, and that’s just with '
                    'my bare hands. Not only am I extensively trained in '
                    'unarmed combat, but I have access to the entire arsenal '
                    'of the United States Marine Corps and I will use it to '
                    'its full extent to wipe your miserable ass off the face '
                    'of the continent, you little shit. If only you could '
                    'have known what unholy retribution your little “clever” '
                    'comment was about to bring down upon you, maybe you '
                    'would have held your fucking tongue. But you couldn’t, '
                    'you didn’t, and now you’re paying the price, you goddamn '
                    'idiot. I will shit fury all over you and you will drown '
                    'in it. You’re fucking dead, kiddo.',
                        
                    "I just want to reblog this and stress this\nLevi "\
                    "his entire squad. He didn't lose 20% of his squad. "\
                    "He didn't even lose 50%. He lost his whole squad. "\
                    "Look at what it's done to him. You can see the death "\
                    "in his eyes, but he keeps on going. This is why Levi "\
                    "is one of my favorite characters.",
                        
                    "Just so you guys know:\nThis is the first thing that "\
                    "I've used my coding for other than school or work"
                    ]

def meme_selector():
    return library_of_memes[random.randint(0, len(library_of_memes) - 1)]


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
    meme_machine.login('247mememachine@gmail.com', psswd)

    meme_machine.sendmail('247mememachine@gmail.com',
                          '247mememachine@gmail.com', # TODO Replace
                          'Subject: ' + meme_selector())
    print('Message sent. Exiting')
    meme_machine.quit()


if __name__ == '__main__':
    main()
