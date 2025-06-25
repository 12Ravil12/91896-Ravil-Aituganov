
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
        "Logout": logout,
        "Find Task": output_task,
        "Output all tasks" : output_all_tasks
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

    categories = ["title", "description", "assignee", "priority", "status"]
    new_task = {}

    for field in categories:
        if field.lower() == ["priority"]:
            value = int_val(1, 5, f"Enter the {field.lower()}")
        elif field.lower() == ["assignee"]:
                value = easygui.enterbox(f"Assignee (you can choose to leave this blank)")
                if value is None:
                    menu()
                value = value.strip()
                if value == "":
                    value = "Not Assigned"
        else:
            value = string_val(f"Enter the {field}")
            new_task[field] = value
        new_task[field] = value
    
    task_id = generate_task_id()
    tasks[task_id] = new_task
    easygui.msgbox(f"Task '{new_task['title']}' added with ID {task_id}.", "Task Added")
    output_task(task_id)


def string_val(value):
    while True:
        str_check = easygui.enterbox(value)
        if str_check is None:
            menu()
        else:
            return str_check.strip()
        

def int_val(min_val, max_val, value):

    while True:
        int_check = easygui.integerbox(value)

        if int_check is None:
            easygui.msgbox("Please enter a number")
        elif int_check < min_val or int_check > max_val:
            easygui.msgbox("Please enter a value between 1-5")
        else:
            return int_check


def generate_task_id():
    task_id = f"T{len(tasks)+1}"

    return task_id


def output_task(task_id):

    output = [f"--- {tasks[task_id]['title']} ---"]
    
    for key, value in tasks[task_id].items():

        output.append(f"{key} : {value}")

    easygui.msgbox("\n".join(output), title=tasks[task_id]["title"])

    menu()


def output_all_tasks():

    output = []

    for task_id, task in tasks.items():
        output.append(f"--- {task['title']}---")
        for key, value in task.items():
            if key != "Title":
                output.append(f"{key}: {value}")
        output.append("")
    easygui.msgbox("\n".join(output), title = "All Tasks")

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
        exit()
    else:
        menu()
    
menu()

