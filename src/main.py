from student import UnderGrad, Graduate

if __name__ == "__main__":
    students = [UnderGrad("John", "jown@ucdenver.edu", 2.0), UnderGrad("Alice", "alice@ucdenver.edu", 2.0),
                UnderGrad("Norman", "alice@ucdenver.edu", 2.0), Graduate("Elise", "elise@ucdenver.edu", "master"),
                Graduate("Laura", "elice@ucdenver.edu", "phd")]

    for u in students:
        print(u)







    # university = University("University of Denver")
    # student1 = Student("Josh", "testemail@ucdenver.edu")
    # print(student1.__str__())
    # university.add_undergrad(student1.name, student1.email, 4)
    #
    # print(student1.__str__())
    # print(university.get_students("bob", 2, "string"))
    # student2 = Student("Josh", "testemail@ucdenver.edu")
    # student3 = Student("Josh", "testemail@ucdenver.edu")
    # university.add_graduate(student1.name, student1.email, "phd")
    # print(student3.__str__())
    # student3 = UnderGrad(student3.name, student3.email, 3)
    # #print(student3.__str__())


