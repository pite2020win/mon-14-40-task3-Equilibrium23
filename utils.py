from urllib import request
from school import Student
import random

def getNamesFromWebSite(url,startLine,EndLine):
    response = request.urlopen(url)
    usefulContent = response.read().decode('utf-8').split("\n")[startLine:EndLine]
    usefulContent[0] = usefulContent[0][8:] # bcs the first line is -> <div><p>ANTONI - 9329<br />
    names = [ line.split(" ")[0] for line in usefulContent ]
    return names

grades = [2,2.5,3,3.5,4,4.5,5]
maleNames = getNamesFromWebSite("https://www.gov.pl/web/cyfryzacja/najpopularniejsze-imiona-dla-chlopcow-2018-ranking-ogolnopolski",331,1121)
maleSurnames = ["Kowalski","Nowak","Jedraski","Jasinski"]
femaleNames = getNamesFromWebSite("https://www.gov.pl/web/cyfryzacja/najpopularniejsze-imiona-dla-dziewczynek-2018-ranking-ogolnopolski",331,1083)
femaleSurnames = ["Kowalska","Nowak","Jedraska","Jasinska"]


def student_generator():
  while True:
      if random.randint(0,1) == 0:
          student = Student(random.choice(maleNames),random.choice(maleSurnames))
      else:
          student = Student(random.choice(femaleNames),random.choice(femaleSurnames))
      for _ in range(0, random.randint(0,20)):
          student.add_score(random.choice(grades))
          student.add_absence()
      yield student