total_seconds = int(input("Enter the total number of seconds: "))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print("hours", hours)
print('minutes', minutes)
print('seconds', seconds)
