# findMyPropertySite
ISQA 8220 - Assignment 1. A real estate website.

To use this application: Clone the application from GitHub and then follow the below steps to run the application locally
 
Open the Terminal Window: 
1. Create a virtual environment: Run the command 'Python -m venv virtualEnv'
     -   “virtualEnv” is the name set for your virtual environment.
2. Now run your virtual environment by running the activation script we need to navigate to the venv\Scripts directory: Run the command 'cd venv\Scripts' 
 
3. Now activate the scripts: Run the command 'activate' 
 
4. Navigate back to the repository directory: Run the command 'cd..' twice 
 
5. Install the required packages: Run the command 'pip install -r requirements.txt' 
This command will install the required packages to run the application. 
 
6. Make the migrations for the database model: Run the command 'python manage.py migrate' 
 
7. Create a superuser: Run the command 'python manage.py createsuperuser' 
Enter the username, Email and password for the superuser. 
 
8. Run the server: Run the command 'python manage.py runserver' 
 
9. Click on the link that is displayed in the terminal window to launch the application. 
 
To deactivate the virtual environment. Navigate to the venv\Script directory (use the command of Step 1) and run the command 'deactivate'
