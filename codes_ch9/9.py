# 9.py

header = {"emails": ["me@example.com", "you@example.com"],
         "subject": "Look at this email."}

message = {"text": "Sorry this is not important."}

template = """
From: <{0[emails][0]}>
To: <{0[emails][1]}>
Subject: {0[subject]}
{1[text]}"""

print(template.format(header, message))
