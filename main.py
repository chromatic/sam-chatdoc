try:
    import gnureadline as readline
except ImportError:
    import readline

from hashlib import sha256

readline.parse_and_bind("tab: complete")
readline.parse_and_bind("set editing-mode vi")

QUIT_PROMPT = "lolol"

DIAGNOSES = [
    "Have you tried not being sick?",
    "Rub some dirt on it.",
    "Sounds gross. Try not to die.",
    "Go touch grass.",
    "Stop being poor."
]

def parse_and_diagnose(input: str) -> str:
    m = sha256()
    m.update(input.encode("utf-8"))
    llm_summary = m.hexdigest()
    llm_value   = int(llm_summary, 16)
    llm_index   = llm_value % len(DIAGNOSES)
    return DIAGNOSES[llm_index]


def main() -> int:
    while True:
        try:
            line = input(f"Enter your symptoms (or {QUIT_PROMPT} to quit): ")

            if line == QUIT_PROMPT:
                break
            elif line.lower() == QUIT_PROMPT.lower():
                print("If you can't bother to follow directions, how is AGI supposed to diagnose you?")
            elif line:
                print("Hmm... thinking... Got it!")
                print(parse_and_diagnose(line) + "\n")
        except Exception as e:
            print(f"I said to type {QUIT_PROMPT} to quit. What's wrong with you? ({e})")

    print("Thanks for using AGI to diagnose and solve your health problems! Good luck!")

    return(0)

if __name__ == "__main__":
    exit(main())
