
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
        "Search": search,
        "Generate a progress report": generate_report,
        "Logout": logout,
        "Output all tasks" : output_all_tasks
    }

    get_input = None

    while get_input != "Logout":

        msg = "Welcome to the progress checker! What would you like to do?"
        title = "Progress Checker Home"

        choices = []

        for action in options:
            choices.append(action)
        selection = easygui.buttonbox(msg, title, choices)
        if selection is None:
            selection = "Logout"
        get_input = options[selection]()

def update_task():
    status_options = ["Blocked", "In progress", "not started", "completed"]
    status = [field for field in status_options]
    categories = ["Title", "Description", "Assignee", "Priority", "Status"]
    task_id = search_task()
    print(task_id)

    
    if not task_id:
        return
    
    task = tasks[task_id]
    updatable_fields = [field for field in categories]


    field_to_edit = easygui.buttonbox("Which field do you want to edit?", "Edit Task", updatable_fields)

    if not field_to_edit:
        easygui.msgbox("No field selected. Edit cancelled.")
        return
    
  
    if field_to_edit in ["Priority"]:
        new_value = int_val(f"Enter new {field_to_edit.lower()}:")

    elif field_to_edit.lower() == "assignee":
        member_id = search_team_member()
        if member_id:
            new_value = member_id
            team_member[member_id]["Task assigned"].append(task_id)
            

        
            
    elif field_to_edit.lower() == "status":
            new_value = easygui.buttonbox("Pick what status you want to assign", "Pick a Status", status)
            if new_value == "completed":
                selected_member = tasks[task_id]["Assignee"]
                team_member[selected_member]["Task assigned"].remove(task_id)

    else:
        new_value = string_val(field_to_edit)

    task[field_to_edit] = new_value
    easygui.msgbox(f"{field_to_edit} updates successfully.", "Edit Complete")
    output_task(task_id)
    

def add_task():
    status_options = ["Blocked", "In progress", "not started", "completed"]
    status = [field for field in status_options]
    categories = ["Title", "description", "assignee", "priority", "status"]
    new_task = {}
    assignees = ["JSM", "JLO", "BDI", "None"]



    for field in categories:
        if field.lower() == "priority":
            value = int_val(1, 3, f"Enter the {field.lower()}")

        elif field.lower() == "assignee":
            value = easygui.choicebox("Pick the member you want to assign the task too", "Pick Assignee", assignees)
            if value != "None":
                task_id = generate_task_id()
                team_member[value]["Task assigned"].append(task_id) #Document 21/07 adding the prblem with the task not assigning to the member (update as well)

            

                    
        elif field.lower() == "status":
            value = easygui.buttonbox("Pick what status you want to assign", "Pick a Status", status)
        else:
            value = string_val(f"Enter the {field}")
            new_task[field] = value
        new_task[field] = value
    
    task_id = generate_task_id()
    tasks[task_id] = new_task
    easygui.msgbox(f"Task '{new_task['Title']}' added with ID {task_id}.", "Task Added")
    output_task(task_id)

def int_val(min_val, max_val, value):

    while True:
        int_check = easygui.integerbox(value)
        if int_check is None:
            menu()
        elif int_check == "":
            easygui.msgbox("Please enter a value")
        elif int_check < min_val or int_check > max_val:
            easygui.msgbox("Please enter a value between 1-3")
        else:
            return int_check

def string_val(value):
    while True:
        str_check = easygui.enterbox(value)
        if str_check is None:
            menu()
        else:
            return str_check.strip()
        



def generate_task_id():
    task_id = f"T{len(tasks)+1}"
    return task_id


def output_task(task_id):
    output = [f"--- {tasks[task_id]['Title']} ---"]
    for key, value in tasks[task_id].items():
        output.append(f"{key} : {value}")
    easygui.msgbox("\n".join(output), title=tasks[task_id]["Title"])



def output_all_tasks():

    output = []

    for task_id, task in tasks.items():
        output.append(f"--- {task['Title']}---")
        for key, value in task.items():
            if key != "title":
                output.append(f"{key}: {value}")
        output.append("")
    easygui.msgbox("\n".join(output), title = "All Tasks")




def search():
    options = {
        "Search for a Task": search_task,
        "Search for a team member": search_team_member
    }

    get_input = None

    while get_input != "exit":

        msg = "What would you like to search for?"
        title = "Search"

        choices = []

        for action in options:
            choices.append(action)
        selection = easygui.buttonbox(msg, title, choices)
        if selection is None:
            menu()
        get_input = options[selection]()
    return







def search_task(): 
    task_titles = []
    
    for task_id, task_data in tasks.items():
        task_titles.append(task_data["Title"])


    selected_title = str(easygui.choicebox("\nPick a task to veiw", "Task search", task_titles))

    if selected_title is None:
        menu()



    for task_id, task_data in tasks.items():
        if task_data["Title"] == selected_title:
            output_task(task_id)
            return task_id 



def output_team_member(member_id):
    output = [f"--- {team_member[member_id]['Name']} ---"]
    for key, value in team_member[member_id].items():
        output.append(f"{key} : {value}")
    easygui.msgbox("\n".join(output), title=team_member[member_id]["Name"])





def search_team_member():

    team_names = []
    for member_id, member_info in team_member.items():
        team_names.append(member_info["Name"])

    selected_name = str(easygui.choicebox("\nPick a task to veiw", "Task search", team_names))

    if selected_name is None:
        menu()

    else:
        for member_id, member_info in team_member.items():
            if member_info["Name"] == selected_name:
                output_team_member(member_id)
                return member_id


def generate_report():
    not_started_tasks = 0
    completed_tasks = 0
    in_progress_tasks = 0
    blocked_tasks = 0
    output = []

    for task_id, task in tasks.items():
        for key, value in task.items():
            if key == "Status":
                if value.lower() == "in progress":
                    in_progress_tasks += 1
                if value.lower() == "blocked":
                    blocked_tasks += 1
                if value.lower() == "completed":
                    completed_tasks += 1
                if value.lower() == "not started":
                    not_started_tasks += 1
            report = [completed_tasks, blocked_tasks, in_progress_tasks, not_started_tasks]
    easygui.msgbox(f"There are {completed_tasks} completed tasks", title="Report")
    easygui.msgbox(f"There are {in_progress_tasks} in progress tasks", title="Report")
    easygui.msgbox(f"There are {not_started_tasks} not started tasks", title="Report")
    easygui.msgbox(f"There are {blocked_tasks} blocked tasks", title="Report")

   

def logout():
    choice = easygui.buttonbox("Are you sure you would like to Logout?", "Logout", choices = ["Yes", "No"])
    if choice == "Yes":
        exit()
    else:
        menu()
    
menu()

