student_data = {
    
    "Advik": 88,
    "Jincy": 95,
    "Hridaan": 82,
    "Rohith": 97,
    "Naman": 75,
}
total_score = 0
for score in student_data.values():
  total_score += score

class_average = total_score / len(student_data)
top_scorer = max(student_data, key=student_data.get)
bottom_scorer = min(student_data, key=student_data.get)

search_name = input("Enter the name of the student to look up: ")

grade = student_data.get(search_name)

if grade is not None:
  print(f"{search_name}'s grade is: {grade}")
else:
  print(f"Student '{search_name}' not found in the student data.")


    
