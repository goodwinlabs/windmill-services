import os


def main():
    print("This script was fired")

    return {"fired": True, "user": os.environ.get("WM_USERNAME")}
