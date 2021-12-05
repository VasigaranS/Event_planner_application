import json

class ClientDatabase():
    def __init__(self, fileName):
        database=json.load(open(fileName))
        self.fileName = fileName
        self.cd=database["clientDetails"]

    def getClientDatabase(self):
        return self.cd

    def getClientDetail(self, name):
        return [clientDetail for clientDetail in self.cd if clientDetail.get("name") == name][0]

    def getAllClients(self):
        clientnames=list()
        for client in self.cd:  
            clientnames.append(client['name'])
        return clientnames

    def updateClientDatabase(self,clientname,eventid):
        clientnames=self.getAllClients()
        if (clientname in clientnames):
            if not (str(eventid) in self.cd[clientnames.index(clientname)]['event id'] ):
                self.cd[clientnames.index(clientname)]['event id']=self.cd[clientnames.index(clientname)]['event id']+','+str(eventid)
        else:
            self.cd.append({'name':clientname,'event id':str(eventid),'review':'NA'})

    def saveData(self):
        fhand=open(self.fileName,'w')
        json.dump({'clientDetails':self.cd},fhand)


