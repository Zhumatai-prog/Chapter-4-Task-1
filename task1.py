class Student():
	def __init__(self, name, lastname, department, year_of_entrance):
		self.name = name
		self.lastname = lastname
		self.department = department
		self.year_of_entrance = year_of_entrance

	def get_student_info(self):
		return(f"{self.name} {self.lastname} entered in {self.year_of_entrance} to department {self.department}")

student1 = Student(
	'Zhumatai', 'Daniiar uulu', 'Computer Science', '2016')
print(student1.get_student_info())