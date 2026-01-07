class Employee:
    def __init__(self, name, department, total_days, present_days):
        self.name = name
        self.department = department
        self.total_days = total_days
        self.present_days = present_days

    def attendance_percentage(self):
        return (self.present_days / self.total_days) * 100

    def status(self):
        percent = self.attendance_percentage()
        if percent >= 90:
            return "Excellent"
        elif percent >= 75:
            return "Good"
        elif percent >= 50:
            return "Average"
        else:
            return "Poor"

# Only run this if executed directly, not during tests
if __name__ == "__main__":
    name = input("Enter employee name: ")
    dept = input("Enter department: ")
    total = int(input("Enter total working days: "))
    present = int(input("Enter number of days present: "))
    emp = Employee(name, dept, total, present)
    print(f"Attendance %: {emp.attendance_percentage():.2f}")
    print(f"Status: {emp.status()}")
