"""
RECORD CHECK  -  my version
===========================

Name  :Aahil mustafa nias
Lane  :  AI
Date  : 2026-10-02

Run it:   python template.py

"""
count_over=0
while True:
    label = input("Enter label: ")     
    if label=="quit":
        break

    value = float(input("Enter value: "))    
    limit = float(input("Enter limit: "))     
    difference = value - limit   
    percent = value/limit * 100      

    if value> limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    if percent>=100:
        status = "OVER LIMIT"
    elif percent>=90:
        status = "WARNING"
    else:
        status = "OK"
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  - {label}")
    print("=" * 34)

    print(f"Value   :{value:>10.2f}")
    print(f"Limit   :{limit:>10.2f}")
    print(f"Difference: {difference:>10.2f}")
    print(f"Percent :{percent:>10.2f}%")
    print(f"Status  :{status}")

    print("=" * 34)
    print()
