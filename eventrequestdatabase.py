import json

class EventRequestDatabase():
    def __init__(self, fileName):
        database=json.load(open(fileName))
        self.fileName = fileName
        self.ed=database.get("eventDetails",list())
        self.latestEventID = database.get("latestEventID",0)

    def getEventRequestDatabase(self):
        return self.ed

    def getLatestEventID(self):
        return int(self.latestEventID)
    
    def setLatestEventID(self, latestEventID):
        self.latestEventID = latestEventID

    def addEvent(self, eventDetails):
        self.ed.append(eventDetails)
        self.latestEventID += 1

    def getEventDetailsByRole(self, role):
        details = list()
        if(role=='seniorCustManager'):
            details= [event for event in self.ed if (event["scseApproval"] == "NA")]
        if(role=='financeManager'):
            details= [event for event in self.ed if (event["scseApproval"] != "NA" and event["scseApproval"] != "Rejected" and event["fmComments"] == "NA")]
        if(role=='adminManager'):
            details= [event for event in self.ed if (event["scseApproval"] != "NA" and event["scseApproval"] != "Rejected" and event["fmComments"] != "NA" and event["amApproval"] == "NA")]
        return details

    def getEventDetailsById(self, eventId):
        return [event for event in self.ed if eventId==event["eventId"]][0]
    
    def getEventIdsOfAdminApprovedReq(self):
        return [event["eventId"] for event in self.ed if event["amApproval"] == "Approved"]

    def getPendingFinReq(self):
        finRequests = list()
        for event in self.ed:
            if event.get("finRequest",""):
                for req in event.get("finRequest"):
                    if req["budgetStatus"] == "NA":
                        finRequests.append(req)
        return finRequests

    def getFinReqToClose(self, dept):
        finRequests = list()
        for event in self.ed:
            if event.get("finRequest",""):
                for req in event.get("finRequest"):
                    if req["budgetStatus"] != "NA" and req["reqStatus"] != "Closed" and req["dept"] == dept:
                        finRequests.append(req)
        return finRequests


    def updateEventStatus(self, eventId, data, role):
        if(role=='seniorCustManager'):
            [event for event in self.ed if eventId==event["eventId"]][0]["scseApproval"] = data 
        if(role=='financeManager'):
            [event for event in self.ed if eventId==event["eventId"]][0]["fmComments"] = data
        if(role=='adminManager'):
            [event for event in self.ed if eventId==event["eventId"]][0]["amApproval"] = data
        if role=='serviceManager' or role == 'productionManager':
            event = [event for event in self.ed if eventId==event["eventId"]][0]
            if not event.get("finRequest", ""):
                event["finRequest"] = []
            event["finRequest"].append(data)

    def updateFinReq(self, eventId, finReq, status, role):
        event = self.getEventDetailsById(eventId)
        for req in event["finRequest"]:
            if req == finReq:
                if role == "financeManager":
                    req["budgetStatus"] = status
                else:
                    req["reqStatus"] = status
                break

    def saveData(self):
        fhand=open(self.fileName,'w')
        json.dump({'eventDetails':self.ed,'latestEventID':self.latestEventID},fhand)

    
