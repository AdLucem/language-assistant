#!/usr/bin/env python
# coding: utf-8

import numpy as np 
import pandas as pd
import re
import json

# check if data directory exists
from subprocess import check_output
print(check_output(["ls", "../data/"]).decode("utf8"))

emails = pd.read_csv("../data/emails.csv")

msg = emails['message'][1].split("\n")

headers = ["Message-ID", "Date", "From", "To", "Subject",
           "Mime-Version", "Content-Type", "Content-Transfer-Encoding",
           "X-From", "X-To", "X-cc", "X-bcc", "X-Folder", "X-Origin", 
           "X-FileName"]

def get_text(message, headers):
    """Get only the text of the email"""

    clean = []

    for line in message:

        is_head = False

        for header in headers:

            h = header + ":"

            if h in line:
                #print(line)
                is_head = True

        if not is_head:
            if line != "":
                clean.append(line)

    return clean

if __name__ == "__main__":
    
    msgs = emails["message"]
    text = ""
    num_files = 0

    texts = []

    for index, email in enumerate(msgs):
        if not index % 10000:
            print(index)
        msg = email.split("\n")
        clean = get_text(msg, headers)
        temp = "\n".join(clean)
        if (len(text) + len(temp)) > 1000000:
            #print("CHECKPOINT: ", str(len(text)))
            #print("Saving...")
            texts.append(text)
            num_files += 1
            text = ""
            #print("Text container emptied: ", str(len(text)))
        text += temp
        
    with open("data.json", "w+") as f:
        json.dump(texts, f)
