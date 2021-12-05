import json


class JobApplicationDatabase():
        def __init__(self, fileName):
            database=json.load(open(fileName))
            self.fileName = fileName
            self.jd=database.get("data",list())
            self.latestId=database.get("latestId",0)
            self.applications=database.get("applications",list())

        def getLatestId(self):
            return self.latestId

        def updateDataJD(self,formDetails):
            print(formDetails)
            self.jd.append(formDetails)
            self.latestId=self.latestId+1
            self.saveData()

        def openJobIds(self):
            openJobs=list()
            for i in self.jd:
                if(i["active"]=="Posted"):
                    openJobs.append(i["jobId"])
            return openJobs

        def readappnsData(self):
            jc=dict()
            openJobs=self.openJobIds()
            for data in self.applications:
                if data['jobId'] in openJobs:
                    jc.update({data['appId']:data})
            return jc

        def getRecId(self,JobId):
            recDet = dict()
            for data in self.jd:
                if(data['jobId']==JobId):
                    recDet={"RecId":data['RecId'],'dept':data['dept'],'jobTitle':data['jobTitle']}
            return recDet

        def updateToRecruited(self,RecId):
            for x in self.jd:
                if(int(x['RecId'])==int(RecId)):
                    x['active']='Recruited'
                    self.saveData()     

        def saveData(self):
            fhand=open(self.fileName,'w')
            json.dump({'data':self.jd,'latestId':self.latestId,'applications':self.applications},fhand)

        def getJobDatabase(self, id):
            return [jobDetail for jobDetail in self.jd if jobDetail.get("jobId") == id][0]