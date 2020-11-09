# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
from school import School,Student,ClassDiary
from utils import student_generator

if __name__ == "__main__":
  school = School("AGH")

  class_A = ClassDiary("A")
  class_B = ClassDiary("B")
  class_C = ClassDiary("C")

  student_gen = student_generator()

  for _ in range(5):
    class_A.add_student_to_class(next(student_gen))
    class_B.add_student_to_class(next(student_gen))
    class_C.add_student_to_class(next(student_gen))

  school.add_class(class_A)
  school.add_class(class_B)
  school.add_class(class_C)

  school.print_school()
  school.save_school_to_json()


# it is ok to get content of utils.py from my previos labs ?
# its ok to reuse your own code yes
# ok :D