marks=[72,45,88,61,39]
for mark in marks:
    if mark >= 50:
        print(mark, "pass")
    else:
        print(mark, "fail")

        passed = 0

        for mark in marks:
            if mark >= 50:
                passed += 1
print("Number of students passed:",passed) 

heighst = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print("Highst mark:", heighst)
print("Lowest mark:", lowest)
print("Average mark:", average)

        
