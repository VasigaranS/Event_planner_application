import sys
sys.path.append("..")

from login import Employee
from employeedatabase import EmployeeDatabase

class TestLogin:
	def testClassCreation(self):
		employee = Employee()

	def testLoginSuccessful(self):
		edb = EmployeeDatabase("../employeedatabase.json")
		employee=Employee()
		employeeInfo = employee.login(edb, "jack", "123")
		assert employeeInfo != dict() and employeeInfo.get("name","") == "jack"

	def testLoginFailureFirst3Times(self):
		edb = EmployeeDatabase("../employeedatabase.json")
		employee=Employee()
		employeeInfo = employee.login(edb, "jack", "1234")
		assert employeeInfo == 1 #Return 1 for first login attempt

	def testLoginFailureAfter3Times(self):
		edb = EmployeeDatabase("../employeedatabase.json")
		employee=Employee()
		employeeInfo = employee.login(edb, "jack", "1234")
		employeeInfo = employee.login(edb, "jack1", "1234")
		employeeInfo = employee.login(edb, "jack", "111")
		employeeInfo = employee.login(edb, "jack", "1")
		assert employeeInfo == 2 #Return 2 for first login attempt

