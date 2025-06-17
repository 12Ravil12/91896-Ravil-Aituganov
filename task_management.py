
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

        get_input = options[selection]


def add_task():
    categories = ["Title", "Description", "Assignee", "Priority,", "Status"]
    easygui.msgbox("You are adding a task", "Add Movie")
    new_task = {}
    for field in categories:
        if field() in ["Priority"]:
            value = int_validation(f"Enter the {field} (A number 1-5):", min_val=1, max_val=5)
        else:
            value = string_validation(f"Enter the {field}:")
    
    task_id = generate_task_id()

    tasks[task_id] = new_task

    easygui.msgbox(f"Task '{new_task['Title']}' added with ID {task_id}.", "Task Added")

    output_task(task_id)

    pass



def generate_task_id():

    task_id = f"T{len(tasks)+1}"

    return task_id



def output_task(task_id):

    output = [f"--- {tasks[task_id]['Title']} ---"]
    
    for key, value in tasks[task_id].items():

        output.append(f"{key} : {value}")

    easygui.msgbox("/n".join(output), title=tasks[task_id]["Title"])

    menu()


def output_all_tasks():
    output = []

    for task_id, task in tasks.items():
        output.append(f"--- {task['Title']}---")

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

def string_val():
    if type(value) == str:
        value = str(value)
        return True
    else:
        print("Please enter a string value")

def int_val():
    if type(value) == int:
        if int < 1:
            print("Please enter a value between 1-5")
        
        
def logout():
    choice = easygui.buttonbox("Are you sure you would like to Logout?", "Logout", choices = ["Yes", "No"])
    if choice == "Yes":
        exit()
    else:
        menu()
    
menu()

