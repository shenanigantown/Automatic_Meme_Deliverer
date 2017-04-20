"""Caitlyn Cook
247mememachine@gmail.com

The messages that meme_selector chooses from to send and a function to
select a random meme from the list.
"""

def meme_selector():
    meme = library_of_memes[random.randint(0,
                                    len(library_of_memes) - 1)]
    return meme

library_of_memes = ['MEMEmemeMEMEmemeMEMEmemeMEMEmemeMEMEmemeMEMEmemeMEMEmeme', 

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

                    "Cars are tasty",

                    "Your Daily Dose of Validation! Life is hard but it is"
                    " doable, you have people around you to help you!",

                    "Your Daily Dose of Validation! I care about you and hope"
                    " that you have a good day! Pet a dog, see a rainbow,"
                    " something like that.",

                    "Your Daily Dose of Validation! Your hair looks"
                    " fantastic. Honestly. Like wow.",

                    "Your Daily Dose of Validation! You may be a little bit "
                    "of a furry but it's okay, we love you anyway.",

                    "Please. Please submit memes. Or you're gonna get tired "
                    "of this really quickly.",

                    "The moon loves you",

                    "If you have any complaints about the meme machine, "
                    "please go outside and explain them to the nearest plant."
                    " They will make sure your comments are heard.",

                    "O shit waddup",

                    "You are are more loved than you realize. People look up "
                    "to you, whether you see it or not.",

                    "You are good at your skills/crafts and no one can take "
                    "that from you. You outshine many and improve every day!",

                    "You tunch, I punch."

                    ]
