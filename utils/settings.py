import json
import os


def get_settings() -> dict:
    settings = {}

    if os.path.exists("settings.json"):
        with open("settings.json", "r") as file:
            settings = json.load(file)
    else:
        settings = {"work": 5, "short_break": 10, "long_break": 20}

    return settings


def saved_settings(new_settigns: dict):
    if os.path.exists("settings.json"):
        with open("settings.json", "w") as file:
            json.dump(new_settigns, file)
    else:
        with open("settings.json", "x") as file:
            json.dump(new_settigns, file)
