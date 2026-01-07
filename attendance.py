class Employee:
    def __init__(self, name, department, total_days, present_days):
        self.name = name
        self.department = department
        self.total_days = total_days
        self.present_days = present_days

    def attendance_percentage(self):
        return int((self.present_days / self.total_days) * 100)

    def status(self):
        p = self.attendance_percentage()
        if p >= 90:
            return "Excellent"
        elif p >= 75:
            return "Good"
        elif p >= 50:
            return "Average"
        else:
            return "Poor"


# 👇 THIS IS VERY IMPORTANT
if __name__ == "__main__":
    name = input("Enter employee name: ")
    dept = input("Enter department: ")
    total = int(input("Enter total working days: "))
    present = int(input("Enter present days: "))

    emp = Employee(name, dept, total, present)
    print("Attendance %:", emp.attendance_percentage())
    print("Status:", emp.status())
