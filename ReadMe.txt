Python modules required to run the application:
	1) pytest
	2) json

To run the application:
	1) Go to the directory of the project (Same directory as this file)
	2) Run "python main.py"
Job applications which are applied by external people need to be entered manually in the json at the start of the application. Any update in json when the program is running will not be taken into consideration.
	-> Job Applications which have been applied needs to be entered manually in jobapplicationdatabase.json
	-> They need to be of the format {"appId": "1", "name": "caesar", "exp": 7, "jobId": 1, "position": "photographerSubTeam", "dept": "production"}
	-> The job applications should be in an array with the key "applications"
	-> Only if the jobapplication's jobId matches with the JobAdvertisement's jobId, the applications will be displayed to the HR Manager

To run the tests:
	1) Go to the "./tests" directory
	2) Run pytest in the ./tests directory (Make sure all databases (except employeedatabase.json) are empty before running the test. Otherwise, the test will not pass as there will be redundant data saved in the database)

Login Information for the application:
Password: 123
Usernames in the employee database:
	1) Customer Service Executive - sarah, sam, judy, carine
	2) Senior Customer Service Executive - janet
	3) Financial Manager - alice
	4) Admin Manager - mike
	5) Production Manager - jack
	6) Service Manager - natalie
	7) Chef SubTeam - helen, diana, chris, daniel, marilyn
	8) Waitress SubTeam - kate, lauren, johnny, brad, meryl
	9) Photographer SubTeam - tobias, magdalena
	10) Audio Specialist SubTeam - antony, adam
	11) Graphic Designer SubTeam - julia, raymond
	12) Decorating Architect SubTeam - angelina, magy, don, tom
	13) Network Engineer SubTeam - christian, nicolas, michael, robert
	14) HR Manager - simon
	15) HR Assistant - maria
	16) Marketing Officer - david
	17) Marketing Assistant - emma
	18) Accountant - fredrik, sophia
