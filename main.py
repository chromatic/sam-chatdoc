try:
    import gnureadline as readline
except ImportError:
    import readline
from random import choice

readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode vi")

diagnoses = [
    "Have you tried not being sick?",
    "Rub some dirt on it.",
    "Sounds gross. Try not to die.",
    "Go touch grass.",
    "Stop being poor."
]

def main():
    while True:
        try:
            line = input("Enter your symptoms (or UGH to quit): ")

            if line == "UGH":
                break
            elif line == "ugh":
                print("If you can't bother to follow directions, how is AGI supposed to diagnose you?")
            elif line:
                print("Hmm... thinking... Got it!\n" + choice(diagnoses))
        except:
            print("I said to type UGH to quit. What's wrong with you?")

    print("Thanks for using AGI to diagnose and solve your health problems! Good luck!")

if __name__ == "__main__":
    main()
