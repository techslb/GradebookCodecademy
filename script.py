# Initial provided code
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Task 1 
subjects = ["physics", "calculus", "poetry", "history"]

# Task 2
grades = [98, 97, 85, 88]

# Task 3
gradebook = [
  ["physics", 98],
  ["calculus", 97],
  ["poetry", 85],
  ["history", 88]
]

# Task 4
gradebook.append(["computer science", 93])

# Task 5
gradebook.append(["visual arts", 93])

# Task 6
gradebook[-1][-1] += 5

# Task 7
gradebook[2].remove(85)

# Task 8
gradebook[2].append("Pass")

# Task 9
full_gradebook = last_semester_gradebook + gradebook

# Final output
print(full_gradebook)
