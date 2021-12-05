import sys
sys.path.append("..")

import json
from taskassignmentdatabase import TaskAssignmentDatabase

class TestTaskAssignmentDatabase:
	fileName = "../taskassignmentdatabase.json"

	def testClassCreation(self):
		tdb = TaskAssignmentDatabase(self.fileName)

	def testAddNewTask(self):
		task = {"taskId": "1", "eventId": "2", "taskBudget": "5000", "dept": "services", "subTeam": "waitress",
		 "taskDesc": "Sample", "assignedTo": "kate", "teamMemberComments": "NA", "plan":"NA", "managerTaskClosure":"NA"}
		tdb = TaskAssignmentDatabase(self.fileName)
		tdb.updateTaskAssignmentDatabase(task)
		taskData = tdb.getTaskDatabase()
		assert task == taskData[len(taskData)-1] #As new task will be added to the end of the database

	def testGetTaskDetailForTeamMember(self):
		tdb = TaskAssignmentDatabase(self.fileName)
		task1 = {"taskId": "1", "eventId": "2", "taskBudget": "5000", "dept": "services", "subTeam": "waitress",
		 "taskDesc": "Sample", "assignedTo": "kate", "teamMemberComments": "NA", "plan":"NA", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task1)
		task2 = {"taskId": "2", "eventId": "3", "taskBudget": "5000", "dept": "services", "subTeam": "waitress",
		 "taskDesc": "Sample", "assignedTo": "lauren", "teamMemberComments": "NA", "plan":"NA", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task2)
		task3 = {"taskId": "3", "eventId": "1", "taskBudget": "1000", "dept": "services", "subTeam": "waitress",
		 "taskDesc": "Sample", "assignedTo": "kate", "teamMemberComments": "NA", "plan":"NA", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task3)
		tasks = tdb.getTaskDetailsByEmpName("kate")
		inputTasks = [task1, task3] 
		assert inputTasks == tasks #Testing if we get kate tasks properly

	def testGetTaskDetailForManager(self): #Get Details by Department which are commented/planned by team member
		tdb = TaskAssignmentDatabase(self.fileName)
		task = {"taskId": "2", "eventId": "3", "taskBudget": "5000", "dept": "services", "subTeam": "chefSubTeam",
		 "taskDesc": "Sample", "assignedTo": "helen", "teamMemberComments": "NA", "plan":"Takes 2 days", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task)
		task1 = {"taskId": "1", "eventId": "2", "taskBudget": "5000", "dept": "production", "subTeam": "photographerSubTeam",
		 "taskDesc": "Sample", "assignedTo": "tobias", "teamMemberComments": "NA", "plan":"NA", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task1)
		task2 = {"taskId": "2", "eventId": "3", "taskBudget": "5000", "dept": "services", "subTeam": "waitress",
		 "taskDesc": "Sample", "assignedTo": "lauren", "teamMemberComments": "NA", "plan":"NA", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task2)
		task3 = {"taskId": "3", "eventId": "1", "taskBudget": "1000", "dept": "services", "subTeam": "chefSubTeam",
		 "taskDesc": "Sample", "assignedTo": "diana", "teamMemberComments": "Extra budget 100 required", "plan":"NA", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task3)
		tasks = tdb.getTaskDetailsByDepartment("services")
		inputTasks = [task, task3] #These are the services tasks which have comments/plan from the members
		assert inputTasks == tasks #Testing if we get services tasks which are commented/planned

	def testTaskStatusUpdateForTeamMember(self):
		tdb = TaskAssignmentDatabase(self.fileName)
		task = {"taskId": "2", "eventId": "3", "taskBudget": "5000", "dept": "services", "subTeam": "chefSubTeam",
		 "taskDesc": "Sample", "assignedTo": "helen", "teamMemberComments": "NA", "plan":"Takes 2 days", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task)
		tdb.updateTaskStatus("2","chefSubTeam",{"comments":"", "plan":"ABC"})
		tasks = tdb.getTaskDatabase()
		task["teamMemberComments"] = ""
		task["plan"] = "ABC"
		assert task == tasks[len(tasks)-1]
	
	def testTaskClosureForManager(self):
		tdb = TaskAssignmentDatabase(self.fileName)
		task = {"taskId": "2", "eventId": "3", "taskBudget": "5000", "dept": "services", "subTeam": "chefSubTeam",
		 "taskDesc": "Sample", "assignedTo": "helen", "teamMemberComments": "NA", "plan":"Takes 2 days", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task)
		tdb.updateTaskStatus("2","serviceManager","Closed")
		tasks = tdb.getTaskDatabase()
		task["managerTaskClosure"] = "Closed"
		assert task == tasks[len(tasks)-1]

	def testSaveData(self):
		tdb = TaskAssignmentDatabase(self.fileName)
		task = {"taskId": "2", "eventId": "3", "taskBudget": "5000", "dept": "production", "subTeam": "photographerSubTeam",
		 "taskDesc": "Sample", "assignedTo": "Juan", "teamMemberComments": "NA", "plan":"NA", "managerTaskClosure":"NA"}
		tdb.updateTaskAssignmentDatabase(task)
		tdb.saveData()
		assert json.load(open(self.fileName)).get("data") == tdb.getTaskDatabase()
