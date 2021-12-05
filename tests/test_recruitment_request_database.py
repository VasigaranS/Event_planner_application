import sys
sys.path.append("..")
import json
from recruitmentRequestdatabase import RecruitmentRequestDatabase

class TestRecruitmentRequestDatabase:
    fileName = "../RecruitmentRequestDatabase.json"
	
    def testClassCreation(self):
        rdb = RecruitmentRequestDatabase(self.fileName)

    def testAddNewRecrutiment(self):
        rdb = RecruitmentRequestDatabase(self.fileName)
        Rec1={'RecId': 1, 'dept': 'production', 'jobTitle': 'audioSpecialistSubTeam', 'exp': '1', 'contractType': 'Part Time', 'jobDesc': 'audio comm', 'active': 'Yes'}
        rdb.updateData(Rec1)
        RecruitmentRequest = rdb.readData()[1]
        assert RecruitmentRequest== Rec1

    def testupdateHR(self):
        rdb = RecruitmentRequestDatabase(self.fileName)
        Rec1={'RecId': 99, 'dept': 'production', 'jobTitle': 'audioSpecialistSubTeam', 'exp': '1', 'contractType': 'Part Time', 'jobDesc': 'audio comm', 'active': 'Yes'}
        rdb.updateData(Rec1)
        rdb.updateHR('99')
        RecruitmentRequest =rdb.getRecDatabase(99)              
        assert RecruitmentRequest.get("active")=='Posted' and RecruitmentRequest.get('RecId')==99

    def testupdateToRecruited(self):
        rdb = RecruitmentRequestDatabase(self.fileName)
        #Rec1={'RecId': 98, 'dept': 'production', 'jobTitle': 'audioSpecialistSubTeam', 'exp': '1', 'contractType': 'Part Time', 'jobDesc': 'audio comm', 'active': 'Posted'}
        #rdb.updateData(Rec1)
        rdb.updateToRecruited('99')
        RecruitmentRequest =rdb.getRecDatabase(99)              
        assert RecruitmentRequest.get("active")=='Recruited' and RecruitmentRequest.get('RecId')==99

    def testviewRecruited(self):
        rdb = RecruitmentRequestDatabase(self.fileName)
        #Rec1={'RecId': 96, 'dept': 'production', 'jobTitle': 'audioSpecialistSubTeam', 'exp': '1', 'contractType': 'Part Time', 'jobDesc': 'audio comm', 'active': 'Recruited'}
        #rdb.updateData(Rec1)
        Recruited=rdb.viewRecruited('production')
        RecruitmentRequest =rdb.getRecDatabase(99)  
        assert Recruited==[RecruitmentRequest]

    def testcloseRequests(self):
        rdb = RecruitmentRequestDatabase(self.fileName)
        #Rec1={'RecId': 97, 'dept': 'production', 'jobTitle': 'audioSpecialistSubTeam', 'exp': '1', 'contractType': 'Part Time', 'jobDesc': 'audio comm', 'active': 'Recruited'}
        #rdb.updateData(Rec1)
        rdb.closeRequests('production')
        RecruitmentRequest =rdb.getRecDatabase(99)              
        assert RecruitmentRequest.get("active")=='Closed' and RecruitmentRequest.get('RecId')==99



