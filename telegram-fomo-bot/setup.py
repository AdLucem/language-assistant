"""This script creates a directory, `.config`, which stores all the config variables required for the app. Config folder is not uploaded to the github; this is to prevent the config variables being made public."""

from os.path import isfile, isdir, join
from os import mkdir
import json


def readConfigs(configInputList):

    configs = {}

    for question in configInputList:

        answer = input(question + " : ")
        configs[question] = answer

    return configs


def writeConfigs(configs, dirname):

    dirExists = isdir(dirname)

    if not dirExists:
        mkdir(dirname)

    with open(join(dirname, "config.json"), "w+") as f:
        json.dump(configs, f)
        return 0

    return 1


def main():

    configInputList = [
        "Bot API token",
    ]

    configs = readConfigs(configInputList)
    success = writeConfigs(configs, "./.config")
    print(success)


# --------- run the whole damn thing --------------------
main()

    