"""
RECORD CHECK  -  my version
===========================

Name  : Aahil Mustafa nias
Lane  :  AI / Cyber / IT 
Date  :21/10/2026
"""

class Record:
    """Stores a record label, value, and limit."""
    over_limit_count = 0
    def __init__(self, label, value, limit):
        """record attributes."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Returns the status based on value and limit."""
        if self.value >= self.limit * 1.0:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif self.value >= self.limit * 0.9:
            return "WARNING"
        else:
            return "OK"
records = [
    Record("r-09", 105, 100),
    Record("R-06", 95, 100),
    Record("r-05", 70, 100),
    Record("R-04", 120, 100),
    Record("R-01", 92, 100)
]
for record in records:
    print()
    print("=" * 34)
    print(f" RECORD CHECK - {record.label}")
    print("=" * 34)

    print(f"Label : {record.label}")
    print(f"Value : {record.value}")
    print(f"Limit : {record.limit}")
    print(f"Status: {record.status()}")

    print("=" * 34)

print()
print(f"Total OVER LIMIT records: {Record.over_limit_count}")
