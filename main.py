from login import Employee
from dashboard import Dashboard
from employeedatabase import EmployeeDatabase
from taskassignmentdatabase import TaskAssignmentDatabase
from eventrequestdatabase import EventRequestDatabase
from clientdatabase import ClientDatabase
from recruitmentRequestdatabase import RecruitmentRequestDatabase
from jobapplicationdatabase import JobApplicationDatabase
from employeeactions import *

def login(edb):
	employee=Employee()
	loginResult = 1
	while (loginResult == 1):
		username=input('Enter the username\n')
		password=input('Enter the password\n')
		loginResult = employee.login(edb, username, password)
	if loginResult == 2:
		return ""
	return loginResult

def main():
	#Database initialization
	edb = EmployeeDatabase("employeedatabase.json")
	eventdb=EventRequestDatabase("eventrequestdatabase.json")
	clientdb=ClientDatabase("clientdatabase.json")
	taskdb=TaskAssignmentDatabase("taskassignmentdatabase.json")
	recDb=RecruitmentRequestDatabase("RecruitmentRequestDatabase.json")
	jobDb=JobApplicationDatabase("jobapplicationDatabase.json")
	#Controls initialization
	evReqCtrl = EventReqControl(eventdb, clientdb)
	clReqCtrl = ClientReqControl(eventdb, taskdb, edb)
	recReqCtrl = RecruitmentReqControl(edb,recDb,jobDb)
	finReqCtrl = FinancialReqControl(eventdb)
	
	while(1):
		print("\nEnter 1 to Login")
		print("Enter 2 to exit the application")
		choice = input("Enter your choice\n")
		if choice == '1':
			#Login
			employeeInfo = login(edb)
			if not employeeInfo:
				print("Login attempts exceeded. Please contact System Administrator")
				exit()
			dashboard = Dashboard()
			while(1):
				result = dashboard.assignOptions(employeeInfo.get("role"), employeeInfo.get("name"), evReqCtrl, clReqCtrl, recReqCtrl, finReqCtrl)
				if not result:
					break
		elif choice == '2':
			break
		else:
			print("Invalid choice")
	#Save Database
	edb.saveData()
	eventdb.saveData()
	clientdb.saveData()
	taskdb.saveData()
	recDb.saveData()
	jobDb.saveData()

if __name__ == "__main__":
	main()
