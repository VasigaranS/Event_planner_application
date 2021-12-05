import sys
sys.path.append("..")

import json
from eventrequestdatabase import EventRequestDatabase

class TestEventRequestDatabase:
	fileName = "../eventrequestdatabase.json"
	def testClassCreation(self):
		erdb = EventRequestDatabase(self.fileName)

	def testAddNewEvent(self):
		erdb = EventRequestDatabase(self.fileName)
		latestEventId = erdb.getLatestEventID()
		eventDetails = {"custName": "Cust1", "eventDate": "24/07/2022", "propBudget": "5000", 
					"eventType": "Music Concert", "eventId": "", 
					"scseApproval": "NA", "fmComments": " NA", "amApproval": "NA"}
		eventDetails["eventId"] = str(latestEventId + 1)
		erdb.addEvent(eventDetails)
		eventsData = erdb.getEventRequestDatabase()
		assert eventsData[len(eventsData)-1] == eventDetails #As new event will be added to the end of the db

	def testGetEventByEventId(self):
		erdb = EventRequestDatabase(self.fileName)
		latestEventId = erdb.getLatestEventID()
		eventDetails = {"custName": "Cust1", "eventDate": "24/11/2021", "propBudget": "1000", 
					"eventType": "Music Concert", "eventId": "", 
					"scseApproval": "NA", "fmComments": " NA", "amApproval": "NA"}
		eventDetails["eventId"] = str(latestEventId + 1)
		erdb.addEvent(eventDetails)
		assert erdb.getEventDetailsById(eventDetails["eventId"]) == eventDetails #The obtained event should be of same ID as the added event

	def eventsAddedForTesting(self, erdb):
		event1 = {"custName": "Cust1", "eventDate": "24/11/2021", "propBudget": "1000", 
					"eventType": "Music Concert", "eventId": "1", 
					"scseApproval": "NA", "fmComments": "NA", "amApproval": "NA"}
		erdb.addEvent(event1)
		event2 = {"custName": "Cust2", "eventDate": "24/11/2021", "propBudget": "5000", 
					"eventType": "Conference", "eventId": "2", 
					"scseApproval": "Approved", "fmComments": "NA", "amApproval": "NA"}
		erdb.addEvent(event2)
		event3 = {"custName": "Cust2", "eventDate": "24/11/2021", "propBudget": "2000", 
					"eventType": "Party", "eventId": "3", 
					"scseApproval": "NA", "fmComments": "NA", "amApproval": "NA"}
		erdb.addEvent(event3)
		event4 = {"custName": "Cust4", "eventDate": "24/11/2021", "propBudget": "3000", 
					"eventType": "Party", "eventId": "4", 
					"scseApproval": "Rejected", "fmComments": "NA", "amApproval": "NA"}
		erdb.addEvent(event4)
		event5 = {"custName": "Cust4", "eventDate": "24/11/2021", "propBudget": "3000", 
					"eventType": "Party", "eventId": "5", 
					"scseApproval": "Approved", "fmComments": "Good", "amApproval": "Approved"}
		erdb.addEvent(event5)
		event6 = {"custName": "Cust6", "eventDate": "24/11/2021", "propBudget": "3000", 
					"eventType": "Party", "eventId": "6", 
					"scseApproval": "Approved", "fmComments": "Good", "amApproval": "NA"}
		erdb.addEvent(event6)
		event7 = {"custName": "Cust6", "eventDate": "24/11/2021", "propBudget": "3000", 
					"eventType": "Party", "eventId": "7", 
					"scseApproval": "Approved", "fmComments": "Good", "amApproval": "Approved"}
		erdb.addEvent(event7)
		return [event1, event2, event3, event4, event5, event6, event7]

	def finReqAddedForTesting(self, erdb, events):
		finReq1 = {"eventId": "5", "extraBudget": "1000", "dept": "services", "reason": "Required",
				 "budgetStatus": "Resolved", "reqStatus": "InProgress"}
		erdb.updateEventStatus(finReq1["eventId"], finReq1, "serviceManager")
		finReq2 = {"eventId": "7", "extraBudget": "1000", "dept": "production", "reason": "Required",
				 "budgetStatus": "Resolved", "reqStatus": "InProgress"}
		erdb.updateEventStatus(finReq2["eventId"], finReq2, "productionManager")
		finReq3 = {"eventId": "5", "extraBudget": "1000", "dept": "production", "reason": "Required",
				 "budgetStatus": "NA", "reqStatus": "InProgress"}
		erdb.updateEventStatus(finReq3["eventId"], finReq3, "productionManager")
		finReq4 = {"eventId": "7", "extraBudget": "1000", "dept": "services", "reason": "Required",
				 "budgetStatus": "NA", "reqStatus": "InProgress"}
		erdb.updateEventStatus(finReq4["eventId"], finReq4, "serviceManager")
		events[4]["finRequest"] = list()
		events[4]["finRequest"].append(finReq1)
		events[4]["finRequest"].append(finReq3)
		events[6]["finRequest"] = list()
		events[6]["finRequest"].append(finReq2)
		events[6]["finRequest"].append(finReq4)

	def testGetEventByRole(self):
		erdb = EventRequestDatabase(self.fileName)
		events = self.eventsAddedForTesting(erdb)
		assert erdb.getEventDetailsByRole("seniorCustManager") == [events[0], events[2]]
		assert erdb.getEventDetailsByRole("financeManager") == [events[1]]
		assert erdb.getEventDetailsByRole("adminManager") == [events[5]]

	def testUpdateEventStatusByRole(self):
		erdb = EventRequestDatabase(self.fileName)
		events = self.eventsAddedForTesting(erdb)
		data = "Approved"
		erdb.updateEventStatus("1", data, "seniorCustManager")
		events[0]["scseApproval"] = data
		assert erdb.getEventDetailsById("1") == events[0]
		data = "Good"
		erdb.updateEventStatus("2", data, "financeManager")
		events[1]["fmComments"] = data
		assert erdb.getEventDetailsById("2") == events[1]
		data = "Rejected"
		erdb.updateEventStatus("6", data, "adminManager")
		events[5]["amApproval"] = data
		assert erdb.getEventDetailsById("6") == events[5]
		data = {"eventId": "5", "extraBudget": "1000", "dept": "services", "reason": "Required",
				 "budgetStatus": "NA", "reqStatus": "InProgress"}
		erdb.updateEventStatus("5", data, "serviceManager")
		if not events[4].get("finRequest",""):
			events[4]["finRequest"] = []
		events[4]["finRequest"].append(data)
		assert erdb.getEventDetailsById("5") == events[4]
		data = {"eventId": "5", "extraBudget": "2000", "dept": "production", "reason": "Photography",
				 "budgetStatus": "NA", "reqStatus": "InProgress"}
		erdb.updateEventStatus("5", data, "productionManager")
		if not events[4].get("finRequest",""):
			events[4]["finRequest"] = []
		events[4]["finRequest"].append(data)
		assert erdb.getEventDetailsById("5") == events[4]

	def testGetEventIdsOfAdminAppReq(self):
		erdb = EventRequestDatabase(self.fileName)
		events = self.eventsAddedForTesting(erdb)
		assert erdb.getEventIdsOfAdminApprovedReq() == ["5", "7"]

	def testGetPendingFinReq(self):
		erdb = EventRequestDatabase(self.fileName)
		events = self.eventsAddedForTesting(erdb)
		self.finReqAddedForTesting(erdb, events)
		#Getting request for Financial Manager if budgetStatus is "NA"
		finRequests = [events[4]["finRequest"][1], events[6]["finRequest"][1]]
		assert finRequests == erdb.getPendingFinReq()

	def testGetFinReqToBeClosed(self):
		erdb = EventRequestDatabase(self.fileName)
		events = self.eventsAddedForTesting(erdb)
		self.finReqAddedForTesting(erdb, events)
		#Getting request for Service Manager if budgetStatus is not "NA" and request is not closed
		finRequestsForService = [events[4]["finRequest"][0]]
		assert finRequestsForService == erdb.getFinReqToClose("services")
		#Getting request for Production Manager if budgetStatus is not "NA" and request is not closed
		finRequestsForProduction = [events[6]["finRequest"][0]]
		assert finRequestsForProduction == erdb.getFinReqToClose("production")

	def testUpdateFinReq(self):
		erdb = EventRequestDatabase(self.fileName)
		events = self.eventsAddedForTesting(erdb)
		self.finReqAddedForTesting(erdb, events)
		#Test for Financial Manager
		finRequestsForFinMan = [events[4]["finRequest"][1], events[6]["finRequest"][1]]
		erdb.updateFinReq("5", finRequestsForFinMan[0], "Resolved", "financeManager")
		events[4]["finRequest"][1]["budgetStatus"] = "Resolved"
		assert events[4] == erdb.getEventDetailsById("5")
		#Test for others (Production/Service Manager)
		finRequestsForPM = [events[6]["finRequest"][0]]
		erdb.updateFinReq("7", finRequestsForPM[0], "Closed", "productionManager")
		events[6]["finRequest"][1]["reqStatus"] = "Closed"
		assert events[6] == erdb.getEventDetailsById("7")

	def testSaveData(self):
		erdb = EventRequestDatabase(self.fileName)
		events = self.eventsAddedForTesting(erdb)
		erdb.saveData()
		assert json.load(open(self.fileName)).get("eventDetails") == erdb.getEventRequestDatabase()
