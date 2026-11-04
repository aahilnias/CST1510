"""
RECORD CHECK  -  my version
===========================

Name  : Aahil Mustafa Nias
Lane  :  AI / Cyber / IT      (delete two)
Date  :07/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    if percent>=100:
        return "OVER LIMIT"
    elif percent<=90:
        return "WARNING"
    else:
        return "OK"

def check(value,limit):
    difference=value - limit
    percentage=value/limit*100
    return difference,percentage
def print_report(label,value,limit,difference,percent,status):
    print("Label",label)
    print("Value:",value)
    print("Limit:",limit)
    print("Difference:",difference)
    print("percentage:",percent)
    print("Status:",status)
    

count=0
while True:
    label = input("enter label:")    
    if label=="quit":
        break
    value = float(input("enter number:")) 
    limit = float(input("enter number:"))   
    difference,percent=check(value,limit)
    status=status_of(percent)
    if status=="OVER LIMIT":
        count+=1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print_report(label,value,limit,difference,percent,status)

    print("=" * 34)
print(f"OVERLIMIT:{count}")




