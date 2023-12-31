class tasks:
    def __init__(self,task,time,date,completion):
        self.task = task
        self.time = time
        self.date = date
        self.completion = completion
    def view(self,task_list):
        task_list = []
        with open('ToDoTasks.txt','r') as file:
            tasks = file.readlines()
        for task_line in tasks:
            pairs = task_line.split(', ')
            task_dict = {}
            for pair in pairs:
                key, value = pair.split(': ')
                task_dict[key.strip()] = value.strip()
            task_list.append(task_dict)
        return task_list
    def new(self):
        line = f'Task: {self.task}, Time: {self.time}, Date: {self.date}, Completion: {self.completion}\n'
        with open('ToDoTasks.txt','a') as file:
            file.write(line)
    def dele(self,task_list):
        filtered_tasks = [task for task in task_list if task['Task'].lower() != self.task.lower()]
        with open('ToDoTasks.txt', 'w') as file:
            for task in filtered_tasks:
                line = f'Task: {task["Task"]}, Time: {task["Time"]}, Date: {task["Date"]}, Completion: {task["Completion"]}\n'
                file.write(line)
    def edit_t(self,tasl_list):
        for task in task_list: 
            if task['Task'].lower() == self.task.lower():
                task['Time'] = self.time
                break
        with open('ToDoTasks.txt', 'w') as file:
            for task in task_list:
                line = f'Task: {task["Task"]}, Time: {task["Time"]}, Date: {task["Date"]}, Completion: {task["Completion"]}\n'
                file.write(line)
    def edit_d(self,task_list):
        for task in task_list: 
            if task['Task'].lower() == self.task.lower():
                task['Date'] = self.date
                break
        with open('ToDoTasks.txt', 'w') as file:
            for task in task_list:
                line = f'Task: {task["Task"]}, Time: {task["Time"]}, Date: {task["Date"]}, Completion: {task["Completion"]}\n'
                file.write(line)
    def edit_c(self,task_list):
        for task in task_list: 
            if task['Task'].lower() == self.task.lower():
                task['Completion'] = self.completion
                break
        with open('ToDoTasks.txt', 'w') as file:
            for task in task_list:
                line = f'Task: {task["Task"]}, Time: {task["Time"]}, Date: {task["Date"]}, Completion: {task["Completion"]}\n'
                file.write(line)
    
                

               
print('Select Option Below:\n','A. Create New Task\n','B. Delete Task\n','C. Edit Task\n','D. View Tasks')

c = input('Enter Option:')
if c.upper() == 'A':
    task = input('Enter New Task:')
    time = input('Enter The time:')
    date = input('Enter Date:')
    new_task = tasks(task = task,time = time, date = date, completion='not done')
    new_task.new()

elif c.upper() == 'B':
    task = input('Enter Delete Task:')
    del_task = tasks(task = task, time= '', date='',completion='')
    task_list = del_task.view([])
    del_task.dele(task_list)

elif c.upper() == 'C':
    task = input('Enter Task to Edit:')
    print('Choose Following Option:\n','A.Time\n','B.Date\n','C.Completion')
    u = input('Enter Option:')
    if u.upper( ) == 'A':
        time = input('Enter new time:')
        update_task = tasks(task = task,time = time, date = '', completion='')
        task_list = update_task.view([])
        update_task.edit_t(task_list)
    elif u.upper() == 'B':
        date = input('Enter new date:')
        update_task = tasks(task = task,time = '', date = date, completion='')
        task_list = update_task.view([])
        update_task.edit_d(task_list)
    elif u.upper() == 'C':
        completion = input('Enter Completion:')
        update_task = tasks(task = task,time = '', date = '', completion= completion)
        task_list = update_task.view([])
        update_task.edit_c(task_list)
    else:
        print('ERROR')
elif c.upper() == 'D':
    view_task = tasks(task = '',time = '', date = '', completion= '')
    task_list = view_task.view([])
