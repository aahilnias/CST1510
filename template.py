
label = input("Label : ")
first = float(input("First : "))
second = float(input("Second : "))  
difference = first - second   
percent = (first / second * 100) 
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)
print(f"First:    {first:>10.2f}")
print(f"Second:   {second:>10.2f}")
print(f"Difference: {difference:>10.2f}")
print(f"Percent:   {percent:>10.2f}%")
print("=" * 34)