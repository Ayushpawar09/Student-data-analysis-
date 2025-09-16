students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks1 = float(input("Enter Marks for Subject 1 (out of 100): "))
    marks2 = float(input("Enter Marks for Subject 2 (out of 100): "))
    marks3 = float(input("Enter Marks for Subject 3 (out of 100): "))
    
    students[roll_no] = {
        "name": name,
        "marks": [marks1, marks2, marks3],
        "average": (marks1 + marks2 + marks3) / 3
    }
    print(f"Student {name} added successfully!\n")

def analyze_performance():
    if not students:
        print("No students added yet!")
        return
    
    print("\n--- Student Performance Report ---")
    for roll_no, details in students.items():
        name = details["name"]
        marks = details["marks"]
        avg = details["average"]
        status = "Pass" if avg >= 40 else "Fail" 
        
        print(f"Roll No: {roll_no}")
        print(f"Name: {name}")
        print(f"Marks: Subject 1: {marks[0]}, Subject 2: {marks[1]}, Subject 3: {marks[2]}")
        print(f"Average Marks: {avg:.2f}")
        print(f"Status: {status}")
        print("-------------------")

def top_performer():
    if not students:
        print("No students added yet!")
        return
    
    top_student = max(students.items(), key=lambda x: x[1]["average"])
    roll_no = top_student[0]
    name = top_student[1]["name"]
    avg = top_student[1]["average"]
    
    print("\n--- Top Performer ---")
    print(f"Roll No: {roll_no}")
    print(f"Name: {name}")
    print(f"Average Marks: {avg:.2f}")

def main():
    while True:
        print("\n--- Student Data Analysis System ---")
        print("1. Add Student")
        print("2. Analyze Performance")
        print("3. Find Top Performer")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            analyze_performance()
        elif choice == "3":
            top_performer()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()