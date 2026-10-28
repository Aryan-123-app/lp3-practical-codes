from email import policy
from email.parser import Parser
import re

# Sample email header
header = """From: sender@example.com
To: receiver@example.com
Subject: Important Account Update
Date: Tue, 08 Sep 2026 09:15:00 +0530
Message-ID: <12345@example.com>
Received: from mail.sender.com (192.168.1.10)
 by mail.receiver.com with ESMTP;
 Tue, 08 Sep 2026 09:15:00 +0530
Received: from smtp.example.com (203.0.113.25)
 by mail.sender.com with ESMTP;
 Tue, 08 Sep 2026 09:14:30 +0530
"""

# Parse email header
msg = Parser(policy=policy.default).parsestr(header)

print("----- EMAIL HEADER ANALYSIS -----")

print("\nFrom :", msg.get("From"))
print("To :", msg.get("To"))
print("Subject :", msg.get("Subject"))
print("Date :", msg.get("Date"))
print("Message-ID :", msg.get("Message-ID"))

# Analyze Received headers
received = msg.get_all("Received", [])

print("\n----- EMAIL ROUTING INFORMATION -----")

if received:
    for i, route in enumerate(received, 1):

        print("\nReceived Header", i, ":")
        print(route)

        # Extract IPv4 addresses
        ips = re.findall(
            r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
            str(route)
        )

        if ips:
            print("IP Address(es):", ", ".join(ips))
        else:
            print("No IP address found.")
else:
    print("No Received header found.")

print("\n----- ANALYSIS COMPLETE -----")