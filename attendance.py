class Employee:
    def __init__(self, name, dept, total_days, present_days):
        self.name = name
        self.dept = dept
        self.total_days = total_days
        self.present_days = present_days

    def attendance_percentage(self):
        return (self.present_days / self.total_days) * 100

    def status(self):
        pct = self.attendance_percentage()
        if pct >= 90:
            return "Excellent"
        elif pct >= 75:
            return "Good"
        elif pct >= 50:
            return "Average"
        else:
            return "Poor"


if __name__ == "__main__":
    name = input("Enter employee name: ")
    dept = input("Enter department: ")
    total_days = int(input("Enter total working days: "))
    present_days = int(input("Enter days present: "))

    emp = Employee(name, dept, total_days, present_days)
    print(f"\nEmployee: {emp.name}")
    print(f"Department: {emp.dept}")
    print(f"Attendance %: {emp.attendance_percentage():.2f}")
    print(f"Status: {emp.status()}")



