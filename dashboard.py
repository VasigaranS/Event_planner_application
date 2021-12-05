from employeeactions import *

class Dashboard():

    def __init__(self):
        pass
        
    def assignOptions(self, role, employeeName, evReqCtrl, clReqCtrl, recReqCtrl, finReqCtrl):
        productionTeamMembers = ["photographerSubTeam", "audioSpecialistSubTeam", "graphicDesignerSubTeam", "decoratingArchitectSubTeam", "networkEngineerSubTeam"]
        serviceTeamMembers = ["chefSubTeam", "waitress"]
        if role == 'custservice':
            return self.custServiceExecutiveOptions(evReqCtrl)
        elif role == 'seniorCustManager':
            return self.seniorCustomerServiceExec(evReqCtrl)
        elif role == 'financeManager':
            return self.financialManagerOptions(evReqCtrl, finReqCtrl, role)
        elif role == 'adminManager':
            return self.adminManagerOptions(evReqCtrl)
        elif role == 'serviceManager' or role == 'productionManager':
            return self.managerOptions( role, clReqCtrl, recReqCtrl, finReqCtrl)
        elif role in productionTeamMembers or role in serviceTeamMembers:
            return self.teamMemberOptions(role, employeeName, clReqCtrl)
        elif role =='seniorHRManager':
            return self.hrManagerOptions(recReqCtrl)
        else:
            return self.logoutOption()
            

    def custServiceExecutiveOptions(self, evReqCtrl):
        print('\nEnter 1 For new event creation\t')
        print('Enter 9 to logout\t')
        choice=input('Enter your choice\n')
        
        if choice == '1':
            evReqCtrl.createNewEvent()
            return True
        if choice == '9':
            return False
        else:
            print("Invalid choice")
            return True
    
    def seniorCustomerServiceExec(self, evReqCtrl):
        print('\nEnter 1 to check new events\t')
        print('Enter 9 to logout\t')
        choice=input('Enter your choice\n')
        
        if choice == '1':
            return self.seniorCustomerServiceExecCheckEvents(evReqCtrl)
        if choice == '9':
            return False
        else:
            print("Invalid choice")
            return True

    def seniorCustomerServiceExecCheckEvents(self, evReqCtrl):
        eventDetails = evReqCtrl.getEventDetails('seniorCustManager')
        if eventDetails:
            print("\n")
            for event in eventDetails:
                evReqCtrl.updateClientDatabase(event['custName'], event['eventId'])
                print('Event Id: '+event['eventId']+'    Customer name: '+event['custName']+'    Event Date: '+event['eventDate']+'    Event Type: '+event['eventType'])
            print('Select an option by entering Event Id\t')
            eventId=input('Enter Event Id\n')
            event = [event for event in eventDetails if event["eventId"] == eventId]
            if len(event) == 1:
                eventStatus = self.seniorCustomerServiceExecAppRejEvent(event[0])
                if eventStatus:
                    evReqCtrl.updateEventStatus(eventId, eventStatus, 'seniorCustManager')
        else:
            print("No New events present")
        return True

    def seniorCustomerServiceExecAppRejEvent(self, event):
        print("\nEvent Details for event with Event ID "+event["eventId"])
        print("Customer name: "+event['custName']+"\t")
        print("Event Date: "+event['eventDate']+"\t")
        print("Event Type: "+event['eventType']+"\t")
        print("Proposed Budget: "+event["propBudget"]+"\t")
        print("Enter 1 to approve the event request\t")
        print("Enter 2 to reject the event request\t")
        print("Enter 3 to cancel\t")
        choice = input("Enter your choice \n")
        if choice == '1':
            return "Approved"
        elif choice == '2':
            return "Rejected"
        return ""

    def financialManagerOptions(self, evReqCtrl, finReqCtrl, role):
        print('\nEnter 1 to check events requiring comments\t')
        print("Enter 2 to check Financial Requests\t")
        print('Enter 9 to logout\t')
        choice=input('Enter your choice\n')
        
        if choice == '1':
            self.financialManagerCheckEvents(evReqCtrl)
            return True
        if choice == '2':
            self.financialManagerUpdateBudgetStatus(finReqCtrl, role)
            return True
        if choice == '9':
            return False
        else:
            print("Invalid choice")
            return True
    
    def financialManagerCheckEvents(self, evReqCtrl):  
        eventDetails = evReqCtrl.getEventDetails('financeManager')
        if eventDetails:
            print("\n")
            for event in eventDetails:
                print('Event Id: '+event['eventId']+'    Customer name: '+event['custName']+'    Event Date: '+event['eventDate']+'    Event Type: '+event['eventType'])
            print('Select an option by entering Event Id\t')
            eventId=input('Enter Event Id\n')
            event = [event for event in eventDetails if event["eventId"] == eventId]
            if len(event) == 1:
                comments = self.financialManagerCommentEvent(event[0])
                if comments:
                    evReqCtrl.updateEventStatus(eventId, comments, 'financeManager')
        else:
            print("No events requiring comments")
        return True

    def financialManagerCommentEvent(self, event):
        print("\nEvent Details for event with Event ID "+event["eventId"])
        print("Customer name: "+event['custName']+"\t")
        print("Event Date: "+event['eventDate']+"\t")
        print("Event Type: "+event['eventType']+"\t")
        print("Proposed Budget: "+event["propBudget"]+"\t")
        comments=input('Enter your review comments\n')
        print('Enter 1 to save the review comments\t')
        print('Enter 2 to cancel \t')
        choice = input("Enter your choice \n")
        if choice == '1':
            return comments
        return ""

    def financialManagerUpdateBudgetStatus(self, finReqCtrl, role):
        finRequests = finReqCtrl.getFinRequests()
        if finRequests:
            print("\n")
            for index,req in enumerate(finRequests):
                print(str(index+1)+'. Event Id: '+req['eventId']+'    ExtraBudget: '+req['extraBudget']+'    Reason: '+req['reason']+'    Department: '+req['dept'])
            print('Select an option by entering Index\t')
            index=input('Enter Index\n')
            if (not index.isnumeric()) or int(index)-1 >= len(finRequests) or int(index)-1 < 0:
                print ("Enter correct index for selection\n")
                return
            print("Enter 1 to update Extra Budget Status Resolved")
            print("Enter 2 to update Extra Budget Status Unsuccessful")
            print("Enter 3 to cancel")
            choice=input('Enter your choice\n')
            if choice == '1':
                finReqCtrl.updateFinReq(finRequests[int(index)-1]['eventId'], finRequests[int(index)-1], "Resolved", role)
            if choice == '2':
                finReqCtrl.updateFinReq(finRequests[int(index)-1]['eventId'], finRequests[int(index)-1], "Unsuccessful", role)
        else:
            print("No Financial Requests Remaining")

    
    def adminManagerOptions(self, evReqCtrl):
        print('\nEnter 1 to check events requiring approval\t')
        print('Enter 9 to logout\t')
        choice=input('Enter your choice\n')
        
        if choice == '1':
            return self.adminManagerCheckEvents(evReqCtrl)
        if choice == '9':
            return False
        else:
            print("Invalid choice")
            return True

    def adminManagerCheckEvents(self, evReqCtrl):
        eventDetails = evReqCtrl.getEventDetails('adminManager')
        if eventDetails:
            print("\n")
            for event in eventDetails:
                print('Event Id: '+event['eventId']+'    Customer name: '+event['custName']+'    Event Date: '+event['eventDate']+'    Event Type: '+event['eventType'])
            print('Select an option by entering Event Id\t')
            eventId=input('Enter Event Id\n')
            event = [event for event in eventDetails if event["eventId"] == eventId]
            if len(event) == 1:
                eventStatus = self.adminManagerAppRejEvent(event[0])
                if eventStatus:
                    evReqCtrl.updateEventStatus(eventId, eventStatus, 'adminManager')
        else:
            print("No events requiring approval")
        return True

    def adminManagerAppRejEvent(self, event):
        print("\nEvent Details for event with Event ID "+event["eventId"])
        print("Customer name: "+event['custName']+"\t")
        print("Event Date: "+event['eventDate']+"\t")
        print("Event Type: "+event['eventType']+"\t")
        print("Proposed Budget: "+event["propBudget"]+"\t")
        print("Finance Manager Comments: "+event["fmComments"]+"\t")
        print("Enter 1 to approve the event request\t")
        print("Enter 2 to reject the event request\t")
        print("Enter 3 to cancel\t")
        choice = input("Enter your choice \n")
        if choice == '1':
            return "Approved"
        elif choice == '2':
            return "Rejected"
        return ""

    def managerOptions(self, role, clReqCtrl, recReqCtrl, finReqCtrl):
        print('\nEnter 1 to create new task assignment\t')
        print('Enter 2 to review task assignment comments from sub teams\t')
        print('Enter 3 to create Recruitment Request\t')
        print('Enter 4 to create Financial Request\t')
        print('Enter 5 to view Recruitment Requests to be closed\t')
        print('Enter 6 to view Financial Requests to be closed\t')
        print('Enter 9 to logout\t')
        choice=input('Enter your choice\n')

        if choice == '1':
            if role == "serviceManager":
                self.serviceManagerChooseSubTeam(clReqCtrl)
            elif role == "productionManager":
                self.productionManagerChooseSubTeam(clReqCtrl)
            return True
        elif choice == '2':
            if role == "serviceManager":
                self.managerReviewComments(clReqCtrl, "services", role)
            elif role == "productionManager":
                self.managerReviewComments(clReqCtrl, "production", role)
            return True
        elif choice == '3':
            if role=="serviceManager":
                recReqCtrl.createNewRecReq("services")
            elif role=="productionManager":
                recReqCtrl.createNewRecReq("production")
            return True
        elif choice =='4':
            if role == "serviceManager":
                finReqCtrl.createNewFinReq("services", role)
            elif role == "productionManager":
                finReqCtrl.createNewFinReq("production", role)
            return True
        elif choice == '5':
            self.viewCloseRecruitmentRequest(recReqCtrl, role)
            return True
        elif choice == '6':
            if role == "serviceManager":
                self.managerCloseFinRequests(finReqCtrl, "services")
            elif role == "productionManager":
                self.managerCloseFinRequests(finReqCtrl, "production")
            return True
        elif choice == '9':
            return False
        else:
            print("Invalid choice")
            return True
 

    def serviceManagerChooseSubTeam(self, clReqCtrl, dept="services"):
        print("\n1. Chef\t")
        print("2. Waitress\t")
        choice = input("Enter your choice 1 or 2\n")

        if choice == '1':
            clReqCtrl.createNewTaskAssignment("chefSubTeam", dept)
        elif choice == '2':
            clReqCtrl.createNewTaskAssignment("waitress", dept)
        else:
            print("Invalid choice")
            

    def productionManagerChooseSubTeam(self, clReqCtrl, dept="production"):
        print("\n1. Photographer\t")
        print("2. Audio Specialist\t")
        print("3. Graphic Designer\t")
        print("4. Decorating Architect\t")
        print("5. Network Engineer\t")
        choice = input("Enter your choice 1 to 5\n")

        if choice == '1':
            clReqCtrl.createNewTaskAssignment("photographerSubTeam", dept)
        elif choice == '2':
            clReqCtrl.createNewTaskAssignment("audioSpecialistSubTeam", dept)
        elif choice == '3':
            clReqCtrl.createNewTaskAssignment("graphicDesignerSubTeam", dept)
        elif choice == '4':
            clReqCtrl.createNewTaskAssignment("decoratingArchitectSubTeam", dept)
        elif choice == '5':
            clReqCtrl.createNewTaskAssignment("networkEngineerSubTeam", dept)
        else:
            print("Invalid choice")
    
    def managerReviewComments(self, clReqCtrl, dept, role):
        taskDetails = clReqCtrl.getTaskDetailsByDepartment(dept)
        if taskDetails:
            print("\n")
            for task in taskDetails:
                print('Task Id: '+task['taskId']+'    Task Budget: '+task['taskBudget']+'    Task Description: '+task['taskDesc'])
            print('Select an option by entering Task Id to view Task Details\t')
            taskId=input('Enter Task Id\n')
            task = [task for task in taskDetails if task["taskId"] == taskId]
            if len(task) == 1:
                self.managerTaskClosure(clReqCtrl, task[0], role)
        else:
            print("No tasks with comments/plan for review")
        return True
    
    def managerTaskClosure(self, clReqCtrl, task, role):
        print("\nTask Details for task with Task ID "+task["taskId"])
        print("Budget allocated for the task: "+task['taskBudget']+"\t")
        print("Task Description: "+task['taskDesc']+"\t")
        print("Plan for Task: "+task['plan']+"\t")
        print("Comments by SubTeam: "+task['teamMemberComments']+"\t")
        print("Plan and Comments by: "+task["assignedTo"]+"\t")
        print('Enter 1 for task closure\t')
        print('Enter 2 to cancel \t')
        choice = input("Enter your choice \n")
        if choice == '1':
            clReqCtrl.updateTaskStatus(task["taskId"], role, "Closed")
    
    def managerCloseFinRequests(self, finReqCtrl, dept):
        requests = list()
        requests = finReqCtrl.getFinRequests(dept)
        if requests:
            print("\n")
            for index,req in enumerate(requests):
                print(str(index+1)+'. Event Id: '+req['eventId']+'    ExtraBudget: '+req['extraBudget']+'    Reason: '+req['reason']+'    Status: '+req['budgetStatus'])
            print('Select an option by entering Index\t')
            index=input('Enter Index\n')
            if (not index.isnumeric()) or int(index)-1 >= len(requests) or int(index)-1 < 0:
                print ("Enter correct index for selection\n")
                return
            print("Enter 1 to close the Financial Request")
            print("Enter 2 to cancel")
            choice=input('Enter your choice\n')
            if choice == '1':
                finReqCtrl.updateFinReq(requests[int(index)-1]['eventId'], requests[int(index)-1], "Closed")
        else:
            print("No Financial requests to be closed")


    def teamMemberOptions(self, clReqCtrl, role, employeeName):
        print('\nEnter 1 to view and comment task assignments\t')
        print('Enter 9 to logout\t')
        choice=input('Enter your choice\n')

        if choice == '1':
            self.teamMemberTaskAssignment(clReqCtrl, role, employeeName)
            return True
        elif choice == '9':
            return False
        else:
            print("Invalid choice")
            return True

    def teamMemberTaskAssignment(self, role, employeeName, clReqCtrl):
        taskDetails = clReqCtrl.getTaskDetailsByEmpName(employeeName)
        if taskDetails:
            print("\n")
            for task in taskDetails:
                print('Task Id: '+task['taskId']+'    Task Budget: '+task['taskBudget']+'    Task Description: '+task['taskDesc'])
            print('Select an option by entering Task Id\t')
            taskId=input('Enter Task Id\n')
            task = [task for task in taskDetails if task["taskId"] == taskId]
            if len(task) == 1:
                event = clReqCtrl.getEventDetailsUsingId(task[0]["eventId"])
                planAndComment = self.teamMemberPlanAndComments(task[0], event)
                if planAndComment:
                    clReqCtrl.updateTaskStatus(taskId, role, planAndComment)
        else:
            print("No tasks requiring plan and comments")
        return True

    def teamMemberPlanAndComments(self, task, event):
        planAndComment = {"plan":"NA", "comments":"NA"}
        print("\nTask Details for task with Task ID "+task["taskId"])
        print("Budget allocated for the task: "+task['taskBudget']+"\t")
        print("Task Description: "+task['taskDesc']+"\t")
        if event:
            print("Event Details for event with Event ID "+event["eventId"])
            print("Customer name: "+event['custName']+"\t")
            print("Event Date: "+event['eventDate']+"\t")
            print("Event Type: "+event['eventType']+"\t")
            print("Proposed Budget for Event: "+event["propBudget"]+"\t")
        plan=input('Enter your expected plan\n')
        print('Enter 1 to save the plan\t')
        print('Enter 2 to cancel \t')
        choice = input("Enter your choice \n")
        if choice == '1':
            planAndComment["plan"] = plan
        comments=input('Enter your review comments\n')
        print('Enter 1 to save the review comments\t')
        print('Enter 2 to cancel \t')
        choice = input("Enter your choice \n")
        if choice == '1':
            planAndComment["comments"] = comments
        return planAndComment

    def viewCloseRecruitmentRequest(self, recReqCtrl, role):
        Recruited=recReqCtrl.viewRecruitedCandidatesPm(role)
        Recruits=list()
        for x in Recruited:
            print('Recruitment Request Id:  '+ str(x['RecId'])+'     Department: '+x['dept']+'   Years of experience: '+ str(x['exp'])+'  Contract Type: '+x['contractType']+'  Job Description:  '+x['jobDesc'] )
            Recruits.append(x['RecId'])
        if not Recruits:
            print('No Recruitments requests to be closed\n')
            return True
        print('\nEnter 1 to close the above recruitment requests')
        print('Enter 2 to cancel')
        choice = input("Enter your choice \n")
        if(choice=='1'):
            recReqCtrl.closeRecruitedRequestsPm(role)
        elif(choice=='2'):
            pass
        else:
            print("invalid choice \n")

        return True

    def hrManagerOptions(self, recReqCtrl):
        print('\nEnter 1 to check Recruitment Requests\t')
        print('Enter 2 to view job applications\t')
        print('Enter 9 to logout\t')
        choice=input('Enter your choice\n')
        
        if choice == '1':
            dc=recReqCtrl.accessActiveRecReqHR()
            recIds=list()
            for x in dc:
                print('Recruitment Request Id:  '+ str(dc[x]['RecId'])+'     Department: '+dc[x]['dept']+'   Years of experience: '+str(dc[x]['exp'])+'  Contract Type: '+dc[x]['contractType']+'  Job Description:  '+dc[x]['jobDesc'] )
                recIds.append(str(dc[x]['RecId']))
            if not recIds:
                print('No Pending Recruitment Requests\n')
                return True
            recId=input('Enter Recruitment Request Id to post as job application\n')
            if(recId  not in recIds):
                print('Invalid choice \n')
                return True
            recId=int(recId)
            print('Recruitment Request Id:  '+ str(dc[recId]['RecId'])+'     Department: '+dc[recId]['dept']+'   Years of experience: '+str(dc[recId]['exp'])+'  Contract Type: '+dc[recId]['contractType']+'  Job Description:  '+dc[recId]['jobDesc'] )
            print('\nEnter 1 to post the request as job application\t')
            print('Enter 2 to cancel')
            inp=input('Enter your choice\n')
            if(inp =='1'):
                recReqCtrl.postJobApplication(dc[recId],recId)
                print('Posted successfully')
            elif(inp=='2'):
                pass
            else:
                print('Invalid input')
                pass
            return True
        elif choice == '9':
            return False
        elif(choice=='2'):
            jc=recReqCtrl.viewApplications()
            aIds=list()
            for x in jc:
                print("Application Id: "+str(jc[x]['appId'])+"   Applicant Name: "+jc[x]['name']+"  Years of Experience:  "+str(jc[x]['exp'])+"  jobid:  "+str(jc[x]['jobId']) +"    position: "+str(jc[x]['position']) )
                aIds.append(str(jc[x]['appId']))
            if not aIds:
                print('No job applications received\n')
                return True
            aId=input('Enter application id to review the job application\n')
            if(aId  not in aIds):
                print('Invalid choice \n')
                return True
            print("Application Id: "+str(jc[aId]['appId'])+"   Applicant Name: "+jc[aId]['name']+"  Years of Experience:  "+str(jc[aId]['exp'])+"  jobid:  "+str(jc[aId]['jobId'])+"    position: "+str(jc[aId]['position']) )
            print('\nEnter 1 to recruit the candidate\t')
            print('Enter 2 to cancel')
            inp=input('Enter your choice\n')
            if(inp=='1'):
                recruited = recReqCtrl.recruitCandidate(jc[aId])
            elif(inp=='2'):
                pass
            else:
                print('Invalid input')
        else:
            print("Invalid choice")
        return True          


    def logoutOption(self):
        print("\nYou do not have any functionalities\t")
        print('Enter 9 to logout\t')
        choice=input('Enter your choice\n')
        if choice == '9':
            return False
        else:
            print("Invalid choice")
        return True