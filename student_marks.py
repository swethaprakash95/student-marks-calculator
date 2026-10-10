
name = input("Enter your name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

total = mark1 + mark2 + mark3
percentage = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
  
