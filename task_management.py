
import easygui

"""
This nested dictionary holds all the tasks, and their key information
and also their assignees, priority and status.
"""
tasks = {
   

    "T1" : {
        "Title": "Design Homepage",
        "Description" : "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": 3,
        "Status" : "In progress"
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

"""
    This nested dictionary holds all the team members, and their key \
information
    and also their tasks assigned in a list
    """
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

#Both of these are constant I have defined
max_val = 3

min_val = 1

def menu():
    """
    The menu function, allows the users to pick what they would like to do
    and when the user presses a button the menu calls that specific fucntion
    to perform what the user wants to do.
    """
    #This is the options for the menu, and the functions that are called
    #that correspond to the options.
    options = {
        "Add a new task": add_task,
        "Update a task": update_task,
        "Search": search,
        "Generate a progress report": generate_report,
        "Exit": exit_program,
        "Output all tasks" : output_all_tasks
    }

    get_input = None

    while get_input != "Logout":
        #This easygui.buttonbox displays the options for the user to 
        #choose.
        msg = "Welcome to the progress checker! What would you like to do?"
        title = "Progress Checker Home"

        choices = []
        #This loops through the options and appends them to the choices 
        #list.
        for action in options:
            choices.append(action)
        selection = easygui.buttonbox(msg, title, choices)
        if selection is None:
            exit_program()
        get_input = options[selection]()



def update_task():
    """
    This update function allows the user to edit the existing 
    tasks and their assignees, or values
    """
    #This easygui.buttonbox displays the options for the user to choose.
    status_options = ["Blocked", "In progress", "Not started", "Completed"]
    status = [field for field in status_options]
    categories = ["Title", "Description", "Assignee", "Priority", "Status"]
    task_id = search_task()
    #This checks if the user has selected a task, and if not it returns 
    #to the menu.
    if not task_id:
        return
    task = tasks[task_id]
    updatable_fields = [field for field in categories]
    field_to_edit = easygui.buttonbox("Which field do you want to edit?",\
"Edit Task", updatable_fields)
    #this block of code, contains if statements that check what field 
    #the user inputtted, and then performs the corresponding action 
    #to edit the task.
    if not field_to_edit:
        easygui.msgbox("No field selected. Edit cancelled.")
        return
    if field_to_edit in ["Priority"]:
        new_value = int_val(1, 3, f"Enter new {field_to_edit.lower()}:")
    #This statement checks it the assignee does exist, and then calls 
    #the searech_team_member function to allow the user to select a 
    #team member Then the program checks if the user has selected a 
    #team member, and if not it returns to the menu, otherwise 
    #it updates the assignee.
    elif field_to_edit.lower() == "assignee":
        member_id = search_team_member()
        if member_id is None:
            easygui.msgbox("Edit has been cancelled,")
            return
        new_value = member_id
        if tasks[task_id]["Assignee"] == "None":
            team_member[member_id]["Task assigned"].append(task_id)  
        else:
            assignee = tasks [task_id]["Assignee"]
            if tasks[task_id]["Status"] != "Completed":
                team_member[assignee]["Task assigned"].remove(task_id)
            elif tasks[task_id]["Status"] == "Completed":
                #This checks if the task is completed, and if it is, it
                # displays a message to the user that they can't change
                # the assignee of a completed task.
                easygui.msgbox("You can't change the assignee of a\
completed task.")
                return
            team_member[member_id]["Task assigned"].append(task_id)

            #assignee = tasks[task_id]["Assignee"]
            #team_member[assignee]["Task assigned"].remove(task_id)
            #team_member[member_id]["Task assigned"].append(task_id)
            
#This statement checks if the user has selected a status, and then 
#updates the status of the task, and also removes the task from the 
#previous assignee only if the status is completed.
    elif field_to_edit.lower() == "status":
            new_value = easygui.buttonbox("Pick what status you want to\
assign", "Pick a Status", status)
            if new_value.lower() == "completed":
                selected_member = tasks[task_id]["Assignee"]
                assignee = tasks[task_id]["Assignee"]
                if assignee != "None":
                    if tasks[task_id]["Status"] != "Completed":
                        team_member[selected_member]["Task\
 assigned"].remove(task_id)
                        tasks[task_id]["Assignee"] = "None" 
                    else:
                        easygui.msgbox("You can't change a completed \
task to completed again")
                        return
            
            else:
                easygui.msgbox("You can't change a status task to\
 the same status again")
                return
    elif field_to_edit == None:
        return
    else:
        new_value = string_val(field_to_edit)
    #This updates the task with the new value for the field that was 
    #edited.
    task[field_to_edit] = new_value
    easygui.msgbox(f"{field_to_edit} updates successfully.", "Edit Complete")
    output_task(task_id)
    
    
def add_task():
    """
    This function allows the user to add a task and customise its properties
    to suit the users needs. It also allows the user to assign the task to a
    team member
    """
    #This easygui.buttonbox displays the options for the user to choose.
    status_options = ["Blocked", "In progress", "Not started", "Completed"]
    status = [field for field in status_options]
    categories = ["Title", "Description", "Assignee", "Priority", "Status"] 
    new_task = {}
    assignees = ["JSM", "JLO", "BDI", "None"]

    for field in categories:
        #This is to ensure that the user inputs a value by having the 
        # "" which is an empty string.
        if field == "": 
            easygui.msgbox("Please enter a value")
        #This is to ensure that the user inputs a value between 1-3 and
        # that it is an integer through the int_val function.
        if field.lower() == "priority":
            value = int_val(1, 3, f"Enter the {field.lower()}")
        #This is to ensure that the user inputs a value from the list of
        #assignees.
        elif field.lower() == "assignee":
            value = easygui.choicebox("Pick the member you want to assign the\
 task too", "Pick Assignee", assignees)
            if value is None:
                menu()
            if value != "None": 
                task_id = generate_task_id()
                team_member[value]["Task assigned"].append(task_id)
            
            
        #This allows the user to choose what exact status they want to 
        # pick using the easygui.buttonbox.
        elif field.lower() == "status":
            value = easygui.buttonbox("Pick what status you want to assign",\
"Pick a Status", status)
            if value is None:
                menu()
        #Otherwise the user can input any string value they want, and 
        # it will be added to the new_task dictionary.
        else:
            value = string_val(f"Enter the {field}")
            new_task[field] = value
        new_task[field] = value
    #This generates a new task ID for the new task.
    task_id = generate_task_id()
    tasks[task_id] = new_task
    #This easygui.msgbox outputs the task that was added and its ID.
    easygui.msgbox(f"Task '{new_task['Title']}' added with ID {task_id}.",\
"Task Added")
    output_task(task_id)

def int_val(min_val, max_val, value): 
    """
    This function validates the users input to ensure it is an integer, and is 
    within the set boundaries required (1-3), and ensure sthe user inputs a
    value
    """
    while True:
        #This loop validates the users input using the passed min and
        # max values. And also checks if the user has inputted a value.
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
    """
    This function validates the users string inputs to ensure they are valid
    and that they put in a value
    """
    #This loop validates the users input to ensure it is a string, and
    # that the user has inputted a value.
    while True:
        str_check = easygui.enterbox(value)
        if str_check == "":
            easygui.msgbox("Please enter a value")
        elif str_check is None:
            menu()
        else:
            return str_check.strip()
        
def generate_task_id():
    """
    This function generates an ID for a new task
    """
    #This generates a new task ID by counting the number of tasks and
    # adding one, and then adding 1, and then returns the task_id.
    task_id = f"T{len(tasks)+1}"
    return task_id

def output_task(task_id):
    """
    This function outputs the task, and its key information by accesing the
    information in the nested dictionary
    """
    #This function outputs the task, and its key information by 
    # accesing the task dictionary.
    output = [f"--- {tasks[task_id]['Title']} ---"]
    for key, value in tasks[task_id].items():
        output.append(f"{key} : {value}")
    easygui.msgbox("\n".join(output), title=tasks[task_id]["Title"])

def output_all_tasks():
    """
    This function outputs all the tasks and their key information by also
    accesing the information in the nested dictionary
    """
    output = []
    #This loops through the tasks and appends the task title and its
    # key.
    for task_id, task in tasks.items():
        output.append(f"--- {task['Title']}---")
        for key, value in task.items():
            if key != "title":
                output.append(f"{key}: {value}")
        output.append("")
    easygui.msgbox("\n".join(output), title = "All Tasks")

def search(): 
    """
    This function allows the user to select what search fucntion they 
    would like to use, and then calls the selected search function
    """
    #This is the options for the search function, and the functions 
    # that are called when the user selects an option.
    options = {
        "Search for a Task": search_task,
        "Search for a team member": search_team_member,
        "Exit": exit_search
    }

    get_input = False
    #This loop allows the user to select what search function they
    # would like to use, and then calls the selected search function.
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

def exit_search():
    """
    This allows the user to exit the search function
    """
    menu()

def search_task(): 
    """
    This function allows the user to search for a task by accesing the 
    information in the nested dictionary
    """
    
    task_titles = []
    #This loops through the tasks and appends the titles to the 
    # task_titles list This is so that the user can select a 
    # task by its title.
    for task_id, task_data in tasks.items():
        task_titles.append(task_data["Title"])


    selected_title = str(easygui.choicebox("\nPick a task to veiw",\
"Task search", task_titles))

    if selected_title is None:
        menu()

        #This loops through the tasks and checks if the title matches
        # the selected title
        # If it does it outputs the task information.
    for task_id, task_data in tasks.items():
        if task_data["Title"] == selected_title:
            output_task(task_id)
            return task_id 

def output_team_member(member_id):
    
    """
    This function outputs the team members name and information by 
    accesing the information in the nested dictionary
    """
    #This function outputs the team member, and their key information 
    # by accesing the information in the nested dictionary.
    output = [f"--- {team_member[member_id]['Name']} ---"]
    for key, value in team_member[member_id].items():
        output.append(f"{key} : {value}")
    easygui.msgbox("\n".join(output), title=team_member[member_id]["Name"])

def search_team_member():
    """
    This function allows the user to search for a team member by their name
    and outputs their information by accesing the information in the nested 
    dictionary
    """
    #This loops through the team members and appends their names to the 
    # team_names list This is so that the user can select a team member.
    team_names = []
    for member_id, member_info in team_member.items():
        team_names.append(member_info["Name"])
    #This easygui.choicebox allows the user to select a team member by 
    # their name.
    selected_name = str(easygui.choicebox("\nPick a team member to \
veiw","Task search", team_names))
    if selected_name == "None":
        return
    else:
        #This loops through the team members and checks if the name 
        # matches the selected name If it does it outputs 
        # the team member information.
        for member_id, member_info in team_member.items():
            if member_info["Name"] == selected_name:
                output_team_member(member_id)
                return member_id

def generate_report():
    """
    This function generates a report of the tasks and their statuses
    and outputs the report in a message box
    """
    not_started_tasks = 0
    completed_tasks = 0
    in_progress_tasks = 0
    blocked_tasks = 0
    #This loops through the tasks and counts the number of tasks 
    # in each status and increments the counters for each status.
    for task_id, task in tasks.items():
        for key, value in task.items():
            if key == "Status":
                if value == "In progress":
                    in_progress_tasks += 1
                if value == "Blocked":
                    blocked_tasks += 1
                if value == "Completed":
                    completed_tasks += 1
                if value == "Not started":
                    not_started_tasks += 1
    

    #This easygui.msgbox outputs the report of the tasks and their 
    # statuses and the number of tasks in each status.

    easygui.msgbox(f"There are {completed_tasks} completed tasks\n\
There are {in_progress_tasks} in progress tasks\n\
There are {not_started_tasks} not started tasks\n\
There are {blocked_tasks} blocked tasks", title="Report")

def exit_program():
    """
    This function allows the user to logout of the application
    and asks the user if they are sure they want to logout
    and if they are sure it exits the application
    """
     #This easygui.buttonbox asks the user if they are sure they 
     # want to logout If they are sure it exits the application, 
     # otherwise it returns to the menu.
    choice = easygui.buttonbox("Are you sure you would like to Exit",\
        "logout", choices = ["Yes", "No"])
    if choice == "Yes":
        exit()
    else:
        menu()
    
menu()