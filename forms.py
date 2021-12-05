class Form():
	def __init__(self):
		pass

	def newForm(self):
		pass


class EventReqForm(Form):
	def __init__(self):
		pass

	def newForm(self):
		custName=input('Enter customer name\n')
		eventDate=input('Enter event date\n')
		propBudget=input('Enter clients proposed budget\n')
		eventType=input('Enter type of event\n')
		print('Enter 1 to confirm\t')
		print('Enter 2 to cancel\t')
		choice = input('Waiting for input\n')
		return {"data": {"custName":custName, "eventDate":eventDate, "propBudget":propBudget, "eventType":eventType, 
      	"eventId":"", "scseApproval":"NA", "fmComments":"NA", "amApproval":"NA"},
		 "choice": choice}

class TaskAssignmentForm():
	def __init__(self):
		pass

	def newForm(self, subTeam, employeeNames, dept, eventIds):
		print("Following Event Ids are available for Task Assignment")
		print(",".join(eventIds))
		eventID=input('Enter from the above event ids\n')
		if not (eventID in eventIds):
			return {"data":{}, "choice": '3'}
		taskBudget=input('Enter the task budget\n')
		taskDesc=input('Add task detailed description\n')
		print("Assignee Options:\t")
		for employee in employeeNames:
			print(employee)
		assignedTo=input('Choose Assignee by Name\n')
		if not (assignedTo in employeeNames):
			return {"data":{}, "choice": '4'}
		print('Enter 1 to confirm\t')
		print('Enter 2 to cancel\t')
		choice = input('Waiting for input\n')
		return  {"data": {"taskId": "", "eventId": eventID, "taskBudget": taskBudget, "dept": dept, "subTeam": subTeam,
		 "taskDesc": taskDesc, "assignedTo": assignedTo, "teamMemberComments": "NA", "plan":"NA", "managerTaskClosure":"NA"},"choice": choice}

class FinancialReqForm():
	def __init__(self):
		pass

	def newForm(self, dept, eventIds):
		print("Following Event Ids are available for Financial Request Creation")
		print(",".join(eventIds))
		eventId = input("Enter from the above, Event ID for the event requiring new budget\n")
		if not eventId in eventIds:
			return {"data":{}, "choice": '3'}
		extraBudget=input('Enter the extra budget required for the event\n')
		reason=input('Add reason for the extra budget\n')
		print('Enter 1 to confirm\t')
		print('Enter 2 to cancel\t')
		choice = input('Waiting for input\n')
		return  {"data": {"eventId": eventId, "extraBudget": extraBudget, "dept": dept, "reason": reason,
		 "budgetStatus": "NA", "reqStatus": "InProgress"},"choice": choice}


class RecruitmentReqForm():
	def __init__(self):
		pass

	def newForm(self,dept):
		if (dept=="services"):	
			print('Choose the job title\n')	
			print("1. Chef\t")
			print("2. Waitress\t")
			jobTitle = input('Enter your choice\n')
			if not (jobTitle in ['1','2']):
				return {"active":'9'}
			d={"1":'chefSubTeam','2':'waitress'}

			jobTitle=d[jobTitle]
			exp=input('Enter the years of experience\n')
			print('Choose the type of contract\n')	
			print("1. Full time\t")
			print('2. Part Time\t')
			f={"1":'Full time',"2":"Part Time"}
			contractType=input('Enter your choice\n')
			if not (contractType in ['1','2']):
				return {"active":'9'}

			contractType=f[contractType]
			jobDesc=input('Enter the job description\n')
			print('Enter 1 to confirm\t')
			print('Enter 2 to cancel\t')
	
			active = input('Waiting for input\n')
			if not (active in ['1','2']):
				return {"active":'9'}	
			return { "RecId":"NA","dept":dept,"jobTitle":jobTitle,"exp":exp,"contractType":contractType,"jobDesc":jobDesc,"active":active}

		if(dept=='production'):
			print('Choose the job title\n')	
			print("1. Photographer\t")
			print("2. Audio Specialist\t")
			print("3. Graphic Designer\t")
			print("4. Decorating Architect\t")
			print("5. Network Engineer\t")
			jobTitle = input('Enter your choice\n')
			if not (jobTitle in ['1','2','3','4','5']):
				return {"active":'9'}
			d={"1":'photographerSubTeam',"2":'audioSpecialistSubTeam','3':'graphicDesignerSubTeam','4':'decoratingArchitectSubTeam','5':'networkEngineerSubTeam'}
			jobTitle=d[jobTitle]

			exp=input('Enter the years of experience\n')
			f={"1":'Full time',"2":"Part Time"}
			print('Choose the type of contract\n')	
			print("1. Full time\t")
			print('2. Part Time\t')
			contractType=input('Enter your choice\n')
			if not (contractType in ['1','2']):
				return {"active":'9'}

			contractType=f[contractType]
			jobDesc=input('Enter the job description\n')
			print('Enter 1 to confirm\t')
			print('Enter 2 to cancel\t')
			active = input('Waiting for input\n')
			if not (active in ['1','2']):
				return {"active":'9'}
			return { "RecId":"NA","dept":dept,"jobTitle":jobTitle,"exp":exp,"contractType":contractType,"jobDesc":jobDesc,"active":active}

		return