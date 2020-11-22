"""This script creates a directory, `.config`, which stores all the config variables required for the app. Config folder is not uploaded to the github; this is to prevent the config variables being made public."""

configInputList = [
    "Bot API token",
]

if __name__ == "__main__":

    configInputs = {}

    for question in configInputList:

        answer = input(question + " : ")
        configInputs[question] = answer

    print(configInputs) 