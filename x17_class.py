class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print "%s: %s" % (self.name, self.score)
        print "aaaaaaaaaaaaaaaaaaa"
if __name__ == '__main__':
  student = Student("Hugh", 99)
  student.print_score
  print student.name
  print student.score
