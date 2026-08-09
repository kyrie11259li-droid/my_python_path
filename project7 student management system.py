def menu():
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Delete Student")
    print("5.Update Student")
    print("6.Exit")

students = []

while True:

    menu()

    choice = int(input("Choose:"))

    if choice == 1:
        print("Add mode selected")
        name = input("Enter name:")
        score = float(input("Enter score:"))
        student = {
            "name": name,
            "score": score
            }
        students.append(student)

    elif choice == 2:
        for student in students:
            print("Name:",student["name"])
            print("Score:",student["score"])
            print()

    elif choice == 3:
        print("Search mode selected")
        search_name = input("Search name:")
        found = False
        for student in students:

            if search_name == student["name"]:
                print("name:",student["name"])
                print("score:",student["score"])
                found = True

        if found == False:
            print("Student not found.")
            print()

    elif choice == 4:

        delete_name = input("Delete name:")

        found = False
        
        for student in students:

            if student["name"] == delete_name:
                students.remove(student)
                print("Deleted")
                found = True
                break

        if found == False:
            print("No this student")
        
    elif choice == 5:

        update_name = input("Enter student's name:")

        found = False

        for student in students:

            if student["name"] == update_name:
                new_score = float(input("New score:"))
                student["score"] = new_score
                found = True
                break
        if found == False:
            print("Student not found.")
            
    elif choice == 6:
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")
