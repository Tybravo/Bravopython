# Input the number of students and subjects
num_of_students = int(input("Enter number of students: "))
num_of_subjects = int(input("Enter number of subjects: "))

reg_student = []

for student in range(num_of_students):
    scores = []
    print(f"\nEntering scores for Student {student + 1}:")
    for subject in range(num_of_subjects):
        score = int(input(f"Enter score for subject {subject + 1}: "))
        scores.append(score)
    reg_student.append(scores)

total_scores = []
average_scores = []

for scores in reg_student:
    total = sum(scores)
    average = total / num_of_subjects
    total_scores.append(total)
    average_scores.append(average)

positions = sorted(range(len(total_scores)), key=lambda x: total_scores[x], reverse=True)
positions = [positions.index(i) + 1 for i in range(len(total_scores))]

print("\nResults:")
print(f"{'Student':<10}{'Subjects':<20}{'Total Score':<15}{'Average Score':<15}{'Position':<10}")

for i in range(num_of_students):
    student_subjects = ' '.join(map(str, reg_student[i]))
    print(f"{'Student ' + str(i + 1):<10}{student_subjects:<20}{total_scores[i]:<15}{average_scores[i]:<15.2f}{positions[i]:<10}")
