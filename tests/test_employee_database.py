import sys
sys.path.append("..")

import json
from employeedatabase import EmployeeDatabase

class TestEmployeeDatabase:
	fileName = "../employeedatabase.json"
	def testClassCreation(self):
		edb = EmployeeDatabase(self.fileName)

	def testGetEmployeeInfo(self):
		edb = EmployeeDatabase(self.fileName)
		assert edb.getEmployeeInfo("jack").get("name","") == "jack"

	def testGetEmployeeInfoWithWrongName(self):
		edb = EmployeeDatabase(self.fileName)
		assert edb.getEmployeeInfo("emp1") == dict() and edb.getEmployeeInfo("emp1").get("name","") == ""

	def testAddEmployee(self):
		edb = EmployeeDatabase(self.fileName)
		employeeInfo = {"name": "emp2", "id": 123, "role": "custservice"}
		edb.addEmployee(employeeInfo)
		assert edb.getEmployeeInfo("emp2") == employeeInfo

	def testAddEmployeeWithSameName(self):
		edb = EmployeeDatabase(self.fileName)
		employeeInfo = {"name": "emp3", "id": 123, "role": "waitress"}
		edb.addEmployee(employeeInfo)
		#Employee with same name
		employeeInfo = {"name": "emp3", "id": 111, "role": "custservice"}
		edb.addEmployee(employeeInfo)
		assert edb.getEmployeeInfo("emp3") != employeeInfo

	def testSaveData(self):
		edb = EmployeeDatabase(self.fileName)
		employeeInfo = {"name": "emp4", "id": 1, "role": "custservice"}
		edb.addEmployee(employeeInfo)
		edb.saveData()
		assert json.load(open(self.fileName)).get("employeeDetails") == edb.getEmployeeDatabase()
