"""
RECORD CHECK  -  my version
===========================

Name  : Aahil Mustafa Nias
Lane  :  AI     
Date  :18/10/2026

Run it:   python template.py
"""

def check_record(value, limit):
    """Check whether a value is over its limit."""
    difference = value - limit
    percent = (value / limit) * 100
    status = "OVER LIMIT" if value > limit else "WITHIN LIMIT"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a report for one record."""
    print(f"Label: {label}")
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference}")
    print(f"Percent: {percent:.1f}%")
    print(f"Status: {status}")
    print("-" * 30)


records = [
    {"label": "Electricity", "value": 120, "limit": 100},
    {"label": "Water", "value": 80, "limit": 100},
    {"label": "Internet", "value": 110, "limit": 100}
]


over_count = 0

with open("results.txt", "w") as file:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"])
        print_report(record["label"],record["value"],record["limit"],difference,percent,status)
        
        if status == "OVER LIMIT":
            over_count += 1
        file.write(f"{record['label']}, {status}\n")

print(f"Records over limit: {over_count}")