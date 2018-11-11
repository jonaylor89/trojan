
import os

def run(**args):

    print("[+] In dirlsiter module.")
    files = os.listdir(".")

    return str(files)
