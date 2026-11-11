"""
RECORD CHECK  -  my version
===========================

Name  : Aahil Mustafa Nias
Lane  :  AI 
Date  :09/11/2026

Run it:   python template.py
"""

def parse_line(raw_line):

    parts = raw_line.strip().split(",")

    server = parts[0].strip()

    data = {
        "server": server,
        "used": None,
        "total": None
    }

    for part in parts[1:]:
        key, value = part.strip().split("=")

        key = key.strip().lower()
        value = value.strip()

        if key in ["used", "total"]:
            data[key] = int(value)

    return data

def status_of(record):


    used = record["used"]
    total = record["total"]

    percentage = (used / total) * 100

    if percentage > 100:
        return "OVER LIMIT"
    elif percentage >= 80:
        return "WARNING"
    else:
        return "OK"



with open("servers.txt", "w") as file:
    file.write("  Srv-01 , used=87 , total=100  \n")
    file.write("SRV-02,USED=45,TOTAL=100\n")
    file.write("  srv-03, Used = 95, Total = 100 \n")
    file.write("Srv-04 , USED=120 , TOTAL=100\n")
    file.write("  SRV-05 , used=30 , total=100  \n")
    file.write("srv-06, USED=80 , TOTAL=100\n")


raw_records = []

with open("servers.txt", "r") as file:
    for line in file:
        raw_records.append(line)

total_records = 0
flagged_records = 0

for raw_record in raw_records:
    parsed = parse_line(raw_record)

    status = status_of(parsed)

    print("Cleaned:", parsed)
    print("Status:", status)
    print("----------------------")

    total_records += 1

    if status != "OK":
        flagged_records += 1

print("Total records:", total_records)
print("Flagged records:", flagged_records)
