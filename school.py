import json
class School:
  def __init__(self,name_of_school):
      self.name_of_school = name_of_school
      self.classes = []
      self.classes_average_score = {}

  def save_school_to_json(self):
    with open (self.name_of_school + "_info.json","w") as school_info: 
        school_info.write(json.dumps(self.classes_average_score ,indent = 4) )

  def get_school_average(self):
      school_average = -1
      try:
          school_average = sum( class_from_school for class_from_school in self.classes_average_score.values() ) / len(self.classes_average_score)
      except:
          print('No one class is found at school')
      return schoolAverage

  def add_class(self,school_class):
    self.classes.append(school_class)
    self.classes_average_score[school_class.name_of_class] = school_class.class_average_score

  def print_school(self):
    print(self.name_of_school)
    for school_class in self.classes:
      school_class.print_class()

class ClassDiary:
  def __init__(self,name_of_class):
    self.name_of_class = name_of_class
    self.diary = []
    self.class_average_score = 0

  def print_class(self):
    print("Class {}:\nAverage score: {}\n".format(self.name_of_class,self.class_average_score))
    for student in self.diary:
        print("{}\n".format(student))

  def update_class_average_score(self):
      self.class_average_score = sum( student.average_score for student in self.diary ) / len(self.diary)

  def add_student_to_class(self,student):
      self.diary.append(student)
      self.update_class_average_score()




class Student:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.average_score = 0
      self.scores = []
      self.absence = 0

  def update_average_score(self):
    self.average_score = sum( score for score in self.scores ) / len(self.scores)

  def add_score(self,score):
    self.scores.append(score)
    self.update_average_score()

  def add_absence(self):
    self.absence+=1

  def __str__(self):
        student_description = "{} {}\ncount of absences: {}\nscores: {}\naverage score: {}".format(self.name,self.surname,self.absence,self.scores,self.average_score)
        return student_description
