def input_record():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    grade = input("Enter Student Grade: ")

    record = {
        "Student ID": student_id,
        "Name": name,
        "Age": age,
        "Grade": grade
    }
    return record


def display_record(record):
    print("\nStudent Record:")
    print(f"Student ID: {record['Student ID']}")
    print(f"Name: {record['Name']}")
    print(f"Age: {record['Age']}")
    print(f"Grade: {record['Grade']}")


def display_all_records(records):
    if not records:
        print("No records found.")
        return
    print(f"\n--- All Student Records ({len(records)}) ---")
    for record in records:
        display_record(record)
        print("-" * 30)


def find_record(records, student_id):
    for record in records:
        if record['Student ID'] == student_id:
            return record
    return None


def update_Stu_record(record):
    print("\nUpdate Student Record:")
    record['Name'] = input(f"Enter new name (current: {record['Name']}): ") or record['Name']
    record['Age'] = input(f"Enter new age (current: {record['Age']}): ") or record['Age']
    record['Grade'] = input(f"Enter new grade (current: {record['Grade']}): ") or record['Grade']
    print("Record updated successfully.")


def delete_Stu_record(records, record):
    confirm = input("Are you sure you want to delete this record? (yes/no): ")
    if confirm.lower() == 'yes':
        records.remove(record)
        print("Record deleted successfully.")
    else:
        print("Deletion canceled.")


def main():
    records = []  # list of student dictionaries

    while True:
        print("\n===== Student Record Menu =====")
        print("1. Add New Record")
        print("2. Display All Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            new_record = input_record()
            if find_record(records, new_record['Student ID']):
                print("A record with this Student ID already exists.")
            else:
                records.append(new_record)
                print("Record added successfully.")

        elif choice == '2':
            display_all_records(records)

        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            record = find_record(records, student_id)
            if record:
                update_Stu_record(record)
            else:
                print("No record found with that Student ID.")

        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            record = find_record(records, student_id)
            if record:
                delete_Stu_record(records, record)
            else:
                print("No record found with that Student ID.")

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()