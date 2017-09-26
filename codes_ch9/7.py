# 7.py

template = """
From: <{from_email}>
To: <{to_email}>
Subject: {subject}
{message}
"""

print(template.format(
    from_email="someone@domain.com",
    to_email="anyone@example.com",
    message="\nThis is a test email.\n\nI hope this be helpful!",
    subject="This email is urgent")
)
