class Employee():
    def __init__(self):
        self.loginAttempt = 0
        self.employeeInfo = dict()

    def login(self, edb, username, password):
        employeeNames = edb.getAllEmployeeNamesInLowerCase()
        if (username.lower() in employeeNames) and (password=='123'):
            self.employeeInfo = edb.getEmployeeInfo(username)
            print('\nWelcome '+self.employeeInfo['name']+'. Your role is '+self.employeeInfo['role']+'\n')
            return self.employeeInfo
        else:
            print('Invalid Credentials\n')
            self.loginAttempt += 1
            if self.loginAttempt >= 3:
                return 2 # 3 loginAttempts failed
            return 1 #Can retry again


