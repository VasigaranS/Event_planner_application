import json

class EmployeeDatabase():
    def __init__(self, fileName):
        self.edb=json.load(open(fileName)).get("employeeDetails")
        self.latestId=json.load(open(fileName)).get("latestId")
        self.fileName = fileName
        #print(self.edb)

    def getLatestId(self):
        return self.latestId
    
    def getEmployeeDatabase(self):
        return self.edb
    
    def getAllEmployeeNamesInLowerCase(self, role=""):
        names = list()
        for emp in self.edb:
            if role == "" or emp.get("role") == role:
                names.append(emp.get("name").lower())
        return names

    def getAllEmployeeNames(self, role=""):
    	names = list()
    	for emp in self.edb:
    		if role == "" or emp.get("role") == role:
    			names.append(emp.get("name"))
    	return names

    def getEmployeeInfo(self, name):
    	for emp in self.edb:
    		if emp.get("name").lower() == name.lower():
    			return emp
    	return dict()

    def addEmployee(self, employeeInfo):
        #if employeeInfo != dict():
        if employeeInfo.get("name").lower() not in self.getAllEmployeeNamesInLowerCase():
            self.edb.append(employeeInfo)
        else:
            print("Duplicate Names")

    def saveData(self):
        fhand=open(self.fileName,'w')
        json.dump({'employeeDetails':self.edb,'latestId':self.latestId},fhand)
