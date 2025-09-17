#University Management System

from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, college_name, id_no):
        self.name = name
        self.college = college_name
        self.id_no = id_no

    @abstractmethod
    def get_role(self):
        pass

    def basic_details(self):
        print(f"Name : {self.name}")
        print(f"College : {self.college}")
        print(f"ID : {self.id_no}")

class Student(Person):

    def __init__(self,name, college_name, id_no, dept):
        super().__init__(name, college_name, id_no)
        self.dept = dept

    
    def get_role(self):
        print("Role : Student")

    def student_details(self):
        super().basic_details()
        self.get_role()
        print(f"Dept : {self.dept}")
        
class TeachingStaff(Person):

    def __init__(self,name, college_name, id_no, dept, subject):
        super().__init__(name, college_name, id_no)
        self.dept = dept
        self.subject = subject

    def get_role(self):
        print("Role : Professor")


    def staff_details(self):
        super().basic_details()
        self.get_role()
        print(f"Dept : {self.dept}")
        print(f"Subject : {self.subject}")


class NonteachingStaff(Person):

    def __init__(self,name, college_name, id_no, dept):
        super().__init__(name, college_name, id_no)
        self.dept = dept
        
    
    def get_role(self):
        print("Role : Non teaching Staff")

    def staff_details(self):
        super().basic_details()
        self.get_role()
        print(f"Dept : {self.dept}")
        

class University:

    university_name = "Codegnan University"

    def __init__(self):
        self.students = []
        self.teaching_staff = []
        self.nonteaching_staff = []

    def add_person(self,person):
        if isinstance(person, Student):
            self.students.append(person)
        if isinstance(person, TeachingStaff):
            self.teaching_staff.append(person)
        if isinstance(person, NonteachingStaff):
            self.nonteaching_staff.append(person)


    def remove_person(self,person):
        if isinstance(person, Student):
            self.students.remove(person)
        if isinstance(person, TeachingStaff):
            self.teaching_staff.remove(person)
        if isinstance(person, NonteachingStaff):
            self.nonteaching_staff.remove(person)


    def candidates_details(self):
        print("***STUDENTS***")
        if self.students:
            for student in self.students:
                student.student_details()
                print("=========================")
        else:
            print("No students yet")

        print("***TEACHING STAFF***")
        if self.teaching_staff:
            for staff in self.teaching_staff:
                staff.staff_details()
                print("=========================")
        else:
            print("No staff yet")


        print("***NON-TEACHING STAFF***")
        if self.nonteaching_staff:
            for staff in self.nonteaching_staff:
                staff.staff_details()
                print("=========================")
        else:
            print("No staff yet")
        
    @classmethod
    def university_details(cls):
        print(f" University : {cls.university_name}")


    @staticmethod
    def greet():
        print("Welcome to University Management System")


def main():

    u = University()
    u.greet()
    while True:

        print("Choose any option from the following: ")
        print("1.Student Registration")
        print("2.Faculty Registration")
        print("3.Non-teaching staff Registration")
        print("4.Remove candidates with ID")
        print("5.Candidates info")
        print("6.Exit")

        choice = int(input("Please enter your choice "))

        if choice == 1:

            name = input("Enter the name of the student: ")
            clg_name = input("Enter the name of the College: ")
            id_number = input("Enter the ID number of student: ")
            dept = input("Enter the department: ")

            student = Student(name, clg_name, id_number, dept)

            u.add_person(student)
            print("STUDENT DETAILS ADDED SUCCESSFULLY")

        elif choice == 2:
            name = input("Enter the name of the staff: ")
            clg_name = input("Enter the name of the College: ")
            id_number = input("Enter the ID number of staff: ")
            dept = input("Enter the department: ")
            subject = input("Enter the subject: ")
            staff = TeachingStaff(name, clg_name, id_number, dept, subject)
            u.add_person(staff)
            print("STAFF DETAILS ADDED SUCCESSFULLY")

        elif choice == 3:
            name = input("Enter the name of the staff: ")
            clg_name = input("Enter the name of the College: ")
            id_number = input("Enter the ID number of staff: ")
            dept = input("Enter the department: ")
            staff = NonteachingStaff(name, clg_name, id_number, dept)
            u.add_person(staff)
            print("STAFF DETAILS ADDED SUCCESSFULLY")

        elif choice == 4:
            print("SELECT THE CATEGORY :")
            print("1. STUDENT")
            print("2. TEACHING STAFF")
            print("3. NON-TEACHING STAFF")


            category = int(input("Enter your choice: "))

            if category == 1:
                input_id = input("Enter the ID number: ")

                for i in u.students:

                    if i.id_no == input_id:
                        u.remove_person(i)
                        print("DETAILS REMOVED SUCCESSFULLY")
                        break

                else:
                    print("NO STUDENT WITH THAT ID NUMBER")

            if category == 2:
                input_id = input("Enter the ID number: ")

                for i in u.teaching_staff:

                    if i.id_no == input_id:
                        u.remove_person(i)
                        print("DETAILS REMOVED SUCCESSFULLY")
                        break

                else:
                    print("NO STAFF WITH THAT ID NUMBER")

            if category == 3:
                input_id = input("Enter the ID number: ")

                for i in u.nonteaching_staff:

                    if i.id_no == input_id:
                        u.remove_person(i)
                        print("DETAILS REMOVED SUCCESSFULLY")
                        break

                else:
                    print("NO STAFF WITH THAT ID NUMBER")

            
        elif choice == 5:
            u.candidates_details()

        
        elif choice == 6:
            print("========Thank you========")
            break
            
        else:

            print("Invalid choice")
main()



