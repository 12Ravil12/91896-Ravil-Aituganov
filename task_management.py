
import easygui
tasks = {
    "T1" : {
        "Title": "Design Homepage",
        "Description" : "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": 3,
        "Status" : "In Progress"
    },
    
    "T2" : {
        "Title": "Implement Login page",
        "Description" : "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": 3,
        "Status" : "Blocked"
    },

    "T3" : {
        "Title": "Fix navigation menu",
        "Description" : "Fix the navigation menu to be more user-freindly",
        "Assignee": "None",
        "Priority": 1,
        "Status" : "Not started"
    },

    "T4" : {
        "Title": "Add payment processing",
        "Description" : "Implement payment processing for the website",
        "Assignee": "JLO",
        "Priority": 2,
        "Status" : "In progress"
    },

    "T5" : {
        "Title": "Create an About Us page",
        "Description" : "Create a page with information about the company",
        "Assignee": "BDI",
        "Priority": 1,
        "Status" : "Blocked"
    }
}

team_member = {

    "JSM":{
        "Name": "Jhon Smith",
        "Email": "John@techvision.com",
        "Task assigned": ["T1", "T2"]
    },

    "JLO":{
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Task assigned": ["T4"]
    },

    "BDI":{
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Task assigned": ["T5"]
    }

}


def menu():
    options = {
        "Add a new task": add_task,
        "Update a task": update_task,
        "Search for a task": search_task,
        "Search for a team member": search_team_member,
        "Generate a progress report": generate_report,
        "Logout": logout
    }

    get_input = None

    while get_input != "Logout":

        msg = "Welcome to the progress checker! What woudl you like to do?"
        title = "Progress Checker Home"

        choices = []

        for action in options:
            choices.append(action)

        selection = easygui.buttonbox(msg, title, choices)

        if selection is None:
            selection = "Logout"

        get_input = options[selection]()



def add_task():
    pass

def output_task():
    pass

def update_task():
    pass

def search():
    pass

def search_task():
    pass

def search_team_member():
    pass

def output_team_member():
    pass

def generate_report():
    pass

def logout():
    choice = easygui.buttonbox("Are you sure you would like to Logout?", "Logout", choices = ["Yes", "No"])
    if choice == "Yes":
        exit
    else:
        menu()
    

menu()
