import json

class TaskAssignmentDatabase():
    def __init__(self, fileName):
        database=json.load(open(fileName))
        self.fileName = fileName
        self.td=database.get("data",list())
        self.latestTaskID = database.get("latestTaskID",0)

    def getLatestTaskID(self):
        return int(self.latestTaskID)
    
    def setLatestTaskID(self, latestTaskID):
        self.latestTaskID = latestTaskID
    
    def getTaskDatabase(self):
        return self.td

    def updateTaskAssignmentDatabase(self,data):
        self.td.append(data)
        self.latestTaskID += 1
    
    def getTaskDetailsByEmpName(self, employeeName):
        return [task for task in self.td if ((task["assignedTo"] == employeeName) and (task["teamMemberComments"] == "NA") and (task["plan"] == "NA"))]

    def getTaskDetailsByDepartment(self, dept):
        return [task for task in self.td if (task["dept"] == dept) and (task["teamMemberComments"] != "NA" or task["plan"] != "NA") and task["managerTaskClosure"] == "NA"]

    def updateTaskStatus(self, taskId, role, data):
        if role != "serviceManager" and role != "productionManager":
            task = [task for task in self.td if taskId==task["taskId"]][0]
            task["teamMemberComments"] = data["comments"]
            task["plan"] = data["plan"]
        else:
            task = [task for task in self.td if taskId==task["taskId"]][0]
            task["managerTaskClosure"] = data
    
    def saveData(self):
        fhand=open(self.fileName,'w')
        json.dump({'data':self.td,'latestTaskID':self.latestTaskID}, fhand)