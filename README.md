# COSC-4353-Group-17
# 1. Discuss your initial thoughts in details on how you will design this application? (2 points) 
	-We will use django for hosting & front-end
	-We will use MySQL for our database, storing the password, username, location, profit margin, and fuel quote history for each user
	-We will do the quote calculations in a function on the page for the fuel request form 
		
# 2. Discuss what development methodology you will use and why? (2 points)
We will use the Rapid Application Development (RAD) methodology for our project.
- This methodology first starts with the team coming together to plan and map out requirements of the software.
- After planning, we will go through the cycle developing and then prototyping our software, refining the software to meet our needs through each cycle.
- This model allows us to develop the software faster as it requires minimal planning and we can easily change the reqirements of the software as we see fit.


# 3. Provide high level design / architecture of your solution that you are proposing? (6 points)
	-We allow new users to create a profile (username,password,location)
	-There will be some user registration system for logins
	-There will be a page (form) for user to enter/edit details of their profile such as location, profit margin, etc.
	-The user can choose on their page what the company profit margin is (based on login, saved in database)
	-There will be a page (form) for the user to fill out for fuel requests (gallons requested, location,... )	
	-Upon request for fuel, a fuel quote is calculated based on the form details & user details saved in the database 
		and the resulting quote is saved in the database as Fuel Quote History
