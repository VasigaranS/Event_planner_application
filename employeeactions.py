from forms import *
from clientdatabase import *
from employeedatabase import *
from eventrequestdatabase import *
from taskassignmentdatabase import *

class EventReqControl():
    
    def __init__(self, eventdb, clientdb):
        self.eventdb = eventdb
        self.clientdb = clientdb

    def createNewEvent(self):
        form = EventReqForm()
        formDetails  = form.newForm()
        if formDetails.get("choice") == '1':
            eventDetails = formDetails.get("data")
            eventID = self.eventdb.getLatestEventID() + 1
            eventDetails["eventId"] = str(eventID)
            self.eventdb.addEvent(eventDetails)

    def getEventDetails(self, role):
        return self.eventdb.getEventDetailsByRole(role)

    def updateEventStatus(self, eventId, data, role):
        self.eventdb.updateEventStatus(eventId, data, role)

    def updateClientDatabase(self, custName, eventId):
        self.clientdb.updateClientDatabase(custName, eventId)
    
class ClientReqControl():
    
    def __init__(self, eventdb, taskdb, edb):
        self.eventdb = eventdb
        self.taskdb = taskdb
        self.edb = edb

    def createNewTaskAssignment(self, subTeam, dept):
        form = TaskAssignmentForm()
        employeeNames = self.edb.getAllEmployeeNames(subTeam)
        eventIds = self.eventdb.getEventIdsOfAdminApprovedReq()
        if not eventIds:
            print("\nNo events requiring creation of Tasks")
            return
        formDetails = form.newForm(subTeam, employeeNames, dept, eventIds)
        if formDetails.get("choice") == '1':
            taskId = self.taskdb.getLatestTaskID() + 1
            formDetails["data"]["taskId"] = str(taskId)
            self.taskdb.updateTaskAssignmentDatabase(formDetails['data'])
        elif formDetails.get("choice") == '3':
            print("Invalid Event ID. Task Assignment Not done. Try creating the form again")
        elif formDetails.get("choice") == '4':
            print("Invalid Assignee Name. Task Assignment Not done. Try creating the form again")

    def getTaskDetailsByEmpName(self, employeeName):
        return self.taskdb.getTaskDetailsByEmpName(employeeName)

    def getTaskDetailsByDepartment(self, dept):
        return self.taskdb.getTaskDetailsByDepartment(dept)

    def getEventDetailsUsingId(self, eventId):
        return self.eventdb.getEventDetailsById(eventId)

    def updateTaskStatus(self, taskId, role, data):
        self.taskdb.updateTaskStatus(taskId, role, data)


class RecruitmentReqControl():
    def __init__(self, edb,recDb,jobDb):
        self.edb = edb
        self.recDb=recDb
        self.jobDb=jobDb

    def createNewRecReq(self,dept):
        form = RecruitmentReqForm()
        formDetails = form.newForm(dept)
        if(formDetails['active']=='1'):
            formDetails['active']='Yes'
            latestId=self.recDb.getLatestId()
            formDetails['RecId']=latestId+1
            self.recDb.updateData(formDetails)
        elif(formDetails['active']=='9'):
            print('Invalid choice \n')

    def postJobApplication(self,recR,recId):
        self.recDb.updateHR(recId)
        jobId=self.jobDb.getLatestId()+1
        recR.update({'jobId':jobId})
        self.jobDb.updateDataJD(recR)
    
    def viewApplications(self):
        return self.jobDb.readappnsData()

    def recruitCandidate(self,newEmp):        
        recDet=self.jobDb.getRecId(newEmp['jobId'])
        if recDet:
            self.recDb.updateToRecruited(recDet['RecId'])
            self.jobDb.updateToRecruited(recDet['RecId'])
            Id=self.edb.getLatestId()+1 
            emp={"name": newEmp['name'], "id": Id, "role": recDet['jobTitle'], "dept": recDet['dept']}
            self.edb.addEmployee(emp)
            return True
        return False

    def viewRecruitedCandidatesPm(self,role):
        dept={'serviceManager':'services','productionManager':'production'}
        return self.recDb.viewRecruited(dept[role])

    def closeRecruitedRequestsPm(self,role):
        dept={'serviceManager':'services','productionManager':'production'}
        return self.recDb.closeRequests(dept[role])

    def accessActiveRecReqHR(self):
        return self.recDb.readData()

class FinancialReqControl():
    def __init__(self, eventdb):
        self.eventdb = eventdb

    def createNewFinReq(self, dept, role):
        form = FinancialReqForm()
        eventIds = self.eventdb.getEventIdsOfAdminApprovedReq()
        if not eventIds:
            print("\nNo events requiring creation of Financial Request")
            return
        formDetails = form.newForm(dept, eventIds)
        if formDetails.get("choice") == '1':
            self.eventdb.updateEventStatus(formDetails['data']['eventId'], formDetails['data'], role)
        elif formDetails.get("choice") == '3':
            print("Invalid Event ID. Financial Request Not created, Try creating the request again with correct event ID")

    def getFinRequests(self, dept = ""):
        if not dept:
            return self.eventdb.getPendingFinReq() #accessed by Finance Manager
        else:
            return self.eventdb.getFinReqToClose(dept)

    def updateFinReq(self, eventId, finReq, status, role=""):
        self.eventdb.updateFinReq(eventId, finReq, status, role)