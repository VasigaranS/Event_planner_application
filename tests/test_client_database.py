import sys
sys.path.append("..")

import json
from clientdatabase import ClientDatabase

class TestClientDatabase:
	fileName = "../clientdatabase.json"
	def testClassCreation(self):
		cdb = ClientDatabase(self.fileName)

	def testAddNewClient(self):
		cdb = ClientDatabase(self.fileName)
		cdb.updateClientDatabase("client", 1)
		clientDetail = cdb.getClientDetail("client")
		assert clientDetail.get("name") == "client" and clientDetail.get("event id") == "1"

	def testAddDetailsForExistingClient(self):
		cdb = ClientDatabase(self.fileName)
		cdb.updateClientDatabase("client1", 1)
		#Client with same name but different ID
		cdb.updateClientDatabase("client1", 2)
		clientDetail = cdb.getClientDetail("client1")
		assert "1" in clientDetail.get("event id") and "2" in clientDetail.get("event id")

	def testAddDetailsForExistingClientExistingId(self):
		cdb = ClientDatabase(self.fileName)
		cdb.updateClientDatabase("client2", 1)
		#Client with same name but different ID
		cdb.updateClientDatabase("client2", 1)
		clientDetail = cdb.getClientDetail("client2")
		eventId = clientDetail.get("event id").split(",")
		if len(eventId) == len(set(eventId)):
			assert True
		else:
			assert False

	def testSaveData(self):
		cdb = ClientDatabase(self.fileName)
		cdb.updateClientDatabase("client3", 1)
		cdb.saveData()
		assert json.load(open(self.fileName)).get("clientDetails") == cdb.getClientDatabase()
