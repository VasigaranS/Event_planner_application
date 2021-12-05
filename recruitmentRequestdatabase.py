import json


class RecruitmentRequestDatabase():
        def __init__(self, fileName):
            database=json.load(open(fileName))
            self.fileName = fileName
            self.rd=database.get("data",list())
            self.latestId=database.get("latestId",0)

        def getLatestId(self):
            return self.latestId

        def updateData(self,formDetails):
            
            self.rd.append(formDetails)
            self.latestId=self.latestId+1
            self.saveData()

        def readData(self):
            dc=dict()
            for data in self.rd:
                if data['active']=='Yes':
                    dc.update({data['RecId']:data})
            return dc

        def updateHR(self,recId):
            for x in self.rd:
                if(int(x['RecId'])==int(recId)):
                    #self.rd[i]['active']='Posted'
                    x['active']='Posted'
                    self.saveData()

        def updateToRecruited(self,RecId):
            for x in self.rd:
                if(int(x['RecId'])==int(RecId)):
                    x['active']='Recruited'
                    self.saveData()

        def viewRecruited(self,dept):
            recruited=list()
            for i in self.rd:
                if(i['active']=='Recruited' and i['dept']==dept):
                    recruited.append(i)
            return recruited

        def closeRequests(self,dept):
            
            for i in self.rd:
                if(i['active']=='Recruited' and i['dept']==dept):
                    i['active']='Closed'
            self.saveData()
            return 
        
        def getRecDatabaser(self):
            return self.rd

        def getRecDatabase(self, id):
            return [recDetail for recDetail in self.rd if recDetail.get("RecId") == id][0]
            #return [clientDetail for clientDetail in self.cd if clientDetail.get("name") == name][0]
        
        def saveData(self):
            fhand=open(self.fileName,'w')
            json.dump({'data':self.rd,'latestId':self.latestId},fhand)