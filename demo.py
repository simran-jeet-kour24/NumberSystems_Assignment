import os
import json

# File to store employee data
FILENAME = "employees.json"

# ---------------- Load and Save Data ----------------

def load_employees():
    """Load employees from JSON file"""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_employees(employees):
    """Save employees to JSON file"""
    with open(FILENAME, "w") as file:
        json.dump(employees, file, indent=4)

# ---------------- CRUD Operations ----------------

def add_employee():
    """Add a new employee"""
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Employee Salary: ")

    employees = load_employees()
    
    # Check if employee ID already exists
    for emp in employees:
        if emp["id"] == emp_id:
            print("\n❌ Employee ID already exists!\n")
            return

    employees.append({"id": emp_id, "name": name, "salary": salary})
    save_employees(employees)
    print("\n✅ Employee added successfully!\n")

def view_employees():
    """View all employees"""
    employees = load_employees()
    if not employees:
        print("\nNo employees found.\n")
        return

    print("\n📋 Employee List:")
    print("-" * 40)
    for i, emp in enumerate(employees, start=1):
        print(f"{i}. ID: {emp['id']} | Name: {emp['name']} | Salary: {emp['salary']}")
    print("-" * 40)

def search_employee():
    """Search employee by ID"""
    emp_id = input("Enter Employee ID to search: ")
    employees = load_employees()
    found = False

    for emp in employees:
        if emp["id"] == emp_id:
            print(f"\n🔍 Found Employee:")
            print(f"ID: {emp['id']}\nName: {emp['name']}\nSalary: {emp['salary']}\n")
            found = True
            break

    if not found:
        print("\n❌ No employee found with that ID.\n")

def update_employee():
    """Update employee details"""
    emp_id = input("Enter Employee ID to update: ")
    employees = load_employees()
    updated = False

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEnter new details (leave blank to keep old values):")
            new_name = input(f"New Name [{emp['name']}]: ") or emp["name"]
            new_salary = input(f"New Salary [{emp['salary']}]: ") or emp["salary"]

            emp["name"], emp["salary"] = new_name, new_salary
            updated = True
            break

    if updated:
        save_employees(employees)
        print("\n✅ Employee updated successfully!\n")
    else:
        print("\n❌ No employee found with that ID.\n")

def delete_employee():
    """Delete employee record"""
    emp_id = input("Enter Employee ID to delete: ")
    employees = load_employees()

    new_employees = [emp for emp in employees if emp["id"] != emp_id]

    if len(new_employees) != len(employees):
        save_employees(new_employees)
        print("\n🗑️ Employee deleted successfully!\n")
    else:
        print("\n❌ No employee found with that ID.\n")

# ---------------- Main Menu ----------------

def main():
    while True:
        print("========== EMPLOYEE MANAGEMENT SYSTEM ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("===============================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("\n👋 Thank you for using Employee Management System!\n")
            break
        else:
            print("\n❌ Invalid choice! Please try again.\n")

# ---------------- Run Program ----------------

if __name__ == "__main__":
    main()