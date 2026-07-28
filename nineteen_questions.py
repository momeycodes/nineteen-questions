import random

"""
Score.
A. Screening: 
    Frank Scheffer's "John Cage From Zero: 19 Questions Interview"
    (22 minute film)
B. Explanation & pick terms (about 10 minutes). Example explanation
from 2017, which will do for the explanation of the rules.
> Imagining a social world that would imitate John Cage here
> notice that he is not using his time to say whatever comes into
> his head, but to think of how to speak with as much economy as
> he can, and then finally to say it
> 
> it seems very difficult to me. i wanted to see if anybody would
> be good at it.
> 
> We will pick the terms. i have written a program to select them
> at random and set the time at random
> 
> we will do it for 8 minutes, with no commentaries during and
> between attempts to do the task. take the chair to volunteer.
> while the chair is empty, we wait, and we do not converse.
> then 5 minutes to converse about modifying the rules, not about
> the content.
> 
> it will be a conversation about the historical present. we will
> talk about culture and politics. let's try to talk really about
> 2017 and not about 2015 or 2011. knowing that, let's now pick
> the terms that all fall within this, so that although commentary
> and conversation are not going to be possible, the attempts to
> play the game will enter into some relation with each other.
> let's try to come up with 3 each.
> if you have to talk it out to come up with them, do not say them
> loudly so that most of them can say unknown to the majority.
C. Iterations:
    - 8 minutes of chair-only discourse
    - 5 minutes of discussing and modifying the rules
    - 8 minutes of chair-only
    - 5 minutes rules
    - etc.
    - Note: This was the plan. However, in no concrete cases has it
      ever seemed appropriate to engage in the 5-minute interludes.
      Thus no timer is required for the 8-minute segments either;
      the whole thing can be given a longer timer, e.g. 35', to clip
      the exercise.
"""

TOPIC_STRINGS = """
Topic
Topic
Topic
"""

# In the first run-through, players proposed the following topics:
"""
Feminist Project
Emotional Labour
Death of Adama Traore
fake news
american elections
democratic confederalism
beyonce's twins
muslim ban
irony
Berlin
Social democracy
healing
micro-breweries
populism
Bowie Prince George Michael
when does europe end?
Beyonce
Panama Papers
coup in Turkey
neorationalism
what to do with north corea
security
educational turn
highschool education without subjects
kanye west
potatoes
somaticized body
Je suis Je suis
to pimp a butterfly
Erdogan
chechnia gay oppression
empathy
lies
being sincere
facebook hacking
hollywood
decolonizing science
irony
Erdogan
humorless
lazy
careerism
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_dots():
    dots = ""
    for i in range(0, random.randint(280, 310)):
        dots += bcolors.FAIL + "." + bcolors.ENDC
        dots += bcolors.HEADER + "." + bcolors.ENDC
        dots += bcolors.OKBLUE + "." + bcolors.ENDC
        dots += bcolors.OKGREEN + "." + bcolors.ENDC
        for j in range(0, random.randint(0, 40)):
            dots += " "
        dots += bcolors.HEADER + "." + bcolors.ENDC
        dots += bcolors.OKBLUE + "." + bcolors.ENDC
        dots += bcolors.OKGREEN + "." + bcolors.ENDC
        for j in range(0, random.randint(0, 2)):
            dots += " "
        dots += bcolors.WARNING + "." + bcolors.ENDC
        dots += bcolors.FAIL + "." + bcolors.ENDC
        dots += bcolors.HEADER + "." + bcolors.ENDC
        dots += bcolors.OKBLUE + "." + bcolors.ENDC
        dots += bcolors.OKGREEN + "." + bcolors.ENDC
        for j in range(0, random.randint(0, 40)):
            dots += " "
        dots += bcolors.OKBLUE + "." + bcolors.ENDC
        dots += bcolors.OKGREEN + "." + bcolors.ENDC
        dots += bcolors.WARNING + "." + bcolors.ENDC
    print(dots)
    print()
    print()
    print()

def prompt_to_continue():
    user_input = input("Run again? [Y/n]  ")
    if user_input in ["Y", "y"]:
        return True
    elif user_input == "n":
        return False
    else:
        return prompt_to_continue()

def output_result():
    topics = TOPIC_STRINGS.split('\n')
    topics = list(filter(None, topics))
    print("          " + random.choice(topics))
    time = None
    length_of_time = random.choice([
        "long", "short", "short", "normal", "normal",
    ])
    if length_of_time == "long":
        time = random.randint(50, 80)
    elif length_of_time == "short":
        time = random.randint(1, 10)
    else:
        time = random.randint(20, 45)
    print("         " + str(time) + " seconds")
    print()
    print()
    print()

def run_once():
    print_dots()
    output_result()
    run_again = prompt_to_continue()
    if run_again:
        run_once()
    else:
        return

if __name__ == "__main__":
    run_once()
