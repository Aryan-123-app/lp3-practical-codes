import re
from collections import defaultdict
from datetime import datetime

LOG_FILE = "system.log"

# Sample log data
sample_logs = """2026-10-04 10:00:01 LOGIN_SUCCESS user=admin ip=192.168.1.10
2026-10-04 10:01:12 LOGIN_FAILED user=admin ip=192.168.1.20
2026-10-04 10:01:45 LOGIN_FAILED user=admin ip=192.168.1.20
2026-10-04 10:02:10 LOGIN_FAILED user=admin ip=192.168.1.20
2026-10-04 10:03:05 LOGIN_SUCCESS user=user1 ip=192.168.1.15
2026-10-04 10:04:20 FILE_ACCESS user=user1 ip=192.168.1.15
2026-10-04 10:05:30 LOGIN_FAILED user=guest ip=192.168.1.30
"""

# Create sample log file
with open(LOG_FILE, "w") as file:
    file.write(sample_logs)


def capture_logs():

    events = []

    with open(LOG_FILE, "r") as file:

        for line in file:

            line = line.strip()

            pattern = (
                r"(\d{4}-\d{2}-\d{2} "
                r"\d{2}:\d{2}:\d{2}) "
                r"(\S+) user=(\S+) ip=(\S+)"
            )

            match = re.match(pattern, line)

            if match:

                timestamp = datetime.strptime(
                    match.group(1),
                    "%Y-%m-%d %H:%M:%S"
                )

                event = match.group(2)
                user = match.group(3)
                ip = match.group(4)

                events.append({
                    "time": timestamp,
                    "event": event,
                    "user": user,
                    "ip": ip
                })

    return events


def correlate_events(events):

    ip_events = defaultdict(list)

    for event in events:
        ip_events[event["ip"]].append(event)

    print("\n----- EVENT CORRELATION -----")

    for ip, records in ip_events.items():

        failed_count = sum(
            1 for event in records
            if event["event"] == "LOGIN_FAILED"
        )

        print("\nIP Address:", ip)
        print("Total Events:", len(records))
        print("Failed Login Attempts:", failed_count)

        for event in records:

            print(
                event["time"],
                "|",
                event["event"],
                "| User:",
                event["user"]
            )

        # Detect suspicious activity
        if failed_count >= 3:

            print(
                "STATUS: SUSPICIOUS ACTIVITY DETECTED"
            )

        else:

            print(
                "STATUS: Normal Activity"
            )


def main():

    print("==============================")
    print(" LOG CAPTURING TOOL")
    print("==============================")

    print("\nCapturing logs...")

    events = capture_logs()

    print(
        "Total log events captured:",
        len(events)
    )

    print("\n----- CAPTURED LOGS -----")

    for event in events:

        print(
            event["time"],
            "|",
            event["event"],
            "| User:",
            event["user"],
            "| IP:",
            event["ip"]
        )

    correlate_events(events)


if __name__ == "__main__":
    main()