import sys
sys.path.append("..")
import json
from jobapplicationdatabase import JobApplicationDatabase


class TestRecruitmentRequestDatabase:
    fileName = "../jobapplicationdatabase.json"

    def testClassCreation(self):
        jdb = JobApplicationDatabase(self.fileName)

    def testupdateDataJD(self):
        jdb = JobApplicationDatabase(self.fileName)
        job1={'RecId': 1, 'dept': 'production', 'jobTitle': 'audioSpecialistSubTeam', 'exp': '1', 'contractType': 'Part Time', 'jobDesc': 'audio comm', 'active': 'Posted', 'jobId': 1}
        jdb.updateDataJD(job1)
        jobRequest=jdb.getJobDatabase(1)
        assert jobRequest==job1
    
    def testopenJobIds(self):
        jdb = JobApplicationDatabase(self.fileName)
        openJobs=jdb.openJobIds()
        assert openJobs==[1]

    def testgetRecId(self):
        jdb = JobApplicationDatabase(self.fileName)
        recDet=jdb.getRecId(1)
        rec1={"RecId":1,'dept':'production','jobTitle':'audioSpecialistSubTeam'}
        assert recDet==rec1

    def testupdateToRecruited(self):
        jdb = JobApplicationDatabase(self.fileName)
        job1={'RecId': 1, 'dept': 'production', 'jobTitle': 'audioSpecialistSubTeam', 'exp': '1', 'contractType': 'Part Time', 'jobDesc': 'audio comm', 'active': 'Recruited', 'jobId': 1}
        jdb.updateToRecruited(1)
        jobRequest=jdb.getJobDatabase(1)
        assert jobRequest==job1


    



