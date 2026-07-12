import os

FILE = "sent_links.txt"

def load_sent():
    if not os.path.exists(FILE):
        return set()

    with open(FILE, "r") as f:
        return set(line.strip() for line in f)

def save_sent(link):
    with open(FILE, "a") as f:
        f.write(link + "\n")
