from speech import takeCommand
from voice import say
import webbrowser

STOP_WORDS = ["stop", "exit", "quit", "close"]
SITES =[
    ["google","https://www.google.com"],
    ["youtube","https://www.youtube.com"],
    ["linkedin","https://www.linkedin.com"],
    ["whatsapp","https://www.whatsapp.com"]
]

if __name__ == "__main__":
    say("Hello, I am NOVA AI")

    while True:
        command = takeCommand()

        if not command:
            continue

        command = command.lower()

       
        print("User Said:", command)
        say(command)

        if any(word in command for word in STOP_WORDS):
            say("Goodbye nawaz")
            break

        for site in SITES:
            if site[0] in command:
                say(f'opening{site[0]} nawaz...')
                webbrowser.open(site[1])
                break
