from copy import copy, deepcopy

class Person:
    """
    Parent class representing a person with a name and age.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self):
        """Print the person's name and age in the specified format."""
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    """
    Child class representing a student, inherits from Person.
    Adds student_id, courses list, and school_name class variable.
    """
    school_name = "Generic University"

    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name: str):
        """Enroll the student in a new course by adding to the courses list."""
        self.courses.append(course_name)

    def display_info(self):
        """Print all student details, including courses."""
        courses_str = ", ".join(self.courses)
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, School: {Student.school_name}, Courses: [{courses_str}]")


def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    # Accessing class variable through class and instances
    print(f"Accessing via class (Student.school_name): {Student.school_name}")
    
    s1 = Student("Alice", 20, "S101")
    s2 = Student("Bob", 22, "S102")
    
    print(f"Accessing via instance s1: {s1.school_name}")
    
    # Add a new attribute to only one object after creation
    s1.major = "Computer Science"
    
    print("\nDisplaying s1 namespace (__dict__):")
    print(s1.__dict__)
    
    print("\nDisplaying s2 namespace (__dict__):")
    print(s2.__dict__)


def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    # Create an object with nested mutable data
    original_student = Student("Charlie", 23, "S103")
    original_student.metadata = {"grades": [90, 85]}

    # Shallow copy vs Deep copy
    shallow_stu = copy(original_student)
    deep_stu = deepcopy(original_student)

    # Modify nested mutable data (the grades list) in the original
    original_student.metadata["grades"].append(95)

    print("Original grades:", original_student.metadata["grades"])
    print("Shallow copy grades (shares reference to nested list):", shallow_stu.metadata["grades"])
    print("Deep copy grades (independent copy):", deep_stu.metadata["grades"])


def main():
    print("=== Unit 1 OOP Assignment ===")

    # Creating and displaying a Person
    p = Person('Cleo', 45)
    p.display_info()
    print()

    # Creating and displaying a Student
    s = Student('Dana', 22, 'S9876')
    s.enroll_course('Biology')
    s.enroll_course('Chemistry')
    s.display_info()
    print()

    # Changing the class variable
    Student.school_name = 'Tech Institute'
    s2 = Student('Eli', 21, 'S2222')
    s2.display_info()
    s.display_info()
    print()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()