class University:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    def add_department(self, department):
        self.__departments.append(department)

    def display_details(self):
        print(f"University: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            print(f"- {department.get_name()}")

class Department(University):
    def __init__(self, name, location, head_of_department):
        super().__init__(name, location)
        self.__head_of_department = head_of_department
        self.__courses_offered = []

    def add_course(self, course):
        self.__courses_offered.append(course)

    def get_name(self):
        return f"{self.__head_of_department}'s Department of {self._University__name}"

    def display_details(self):
        super().display_details()
        print(f"Head of Department: {self.__head_of_department}")
        print("Courses Offered:")
        for course in self.__courses_offered:
            print(f"- {course}")


if __name__ == "__main__":
    # Create University
    university = University("ABC University", "City XYZ")

    # Create Departments
    department1 = Department("Computer Science", "Building A", "Prof. John Doe")
    department2 = Department("Electrical Engineering", "Building B", "Prof. Jane Smith")

    # Add Courses to Departments
    department1.add_course("Data Structures")
    department1.add_course("Algorithms")
    department2.add_course("Circuit Analysis")
    department2.add_course("Power Systems")

    # Add Departments to University
    university.add_department(department1)
    university.add_department(department2)

    # Display University and Department Details
    university.display_details()
    print()
    department1.display_details()
    print()
    department2.display_details()
