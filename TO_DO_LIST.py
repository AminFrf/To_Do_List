import csv


class task :
    
    def __init__(self , name , description , priority) :
        self.name = name
        self.description = description
        self.priority = priority
        


class to_do_list :
    
    def __init__(self) :
        self.todolist = []
    
    
    def main_menu(self) :
        
        print_again = True
        choice = 0 
        
        while(print_again) :
            
            print("*** TO DO LIST ***")
            print("1. add new task")
            print("2. delete task")
            print("3. see list of tasks")
            print("4. save list")
            print("5. load list")
            print("6. exite")
            choice = input("enter your chois : ")
            
            if choice not in ["1" , "2" ,"3" ,"4" ,"5" , "6"]:
                print("wrong input !!!")
            else : 
                print_again = False
        return choice 
        
    
    def add_task(self):
        name = input("pleas enter a title for your task : ")
        description = input(f"enter a description about {name} : ")
        while True :
            priority = int(input("enter a priority for this task : \n1.low\n2.medium\n3.high\n: "))
            if(priority not in [1 , 2 , 3]) :
                print("wrong input !!!")
                print("please try again ") 
            else :
                break
            
        new_task = task(name , description , priority)     
        self.todolist.append(new_task)
        print("task added successfully !")   
        
    def delete_task(self) :
        name = input("enter the name of the task you want to delete : ")
        find = False
        for t in self.todolist :
            if t.name == name :
                self.todolist.remove(t)
                print(f"task {name} deleted successfully !")
                find = True
                break        
        
        if find == False :
            print(f"task {name} not found") 
            
    def see_list_of_tasks(self) :
        
        if not self.todolist :
            print()
            print("no task to show !!!")
            print()
            return
        print()
        print("******************************************")
        for t in self.todolist :
            
            print("name : " + t.name)
            print("description : " + t.description)
            print("priority : " + str(t.priority))
            print("******************************************")
        print()
    def save_list(self) :
        
        name = input("enter the file name to save your TO_DO_LIST : ")
        my_file = open(f"{name}.csv" , "w")
        writer = csv.writer(my_file)
        
        for task in self.todolist :
            task_name = task.name
            task_description = task.description
            task_priority = task.priority
            writer.writerow([task_name , task_description , task_priority])
        my_file.close()
        print("file saved successfully !")
        
    def load_file(self) :
        
        try :
            name = input("please enter the filename you want to open : ")
            my_file = open(f"{name}.csv" , "r")
            self.todolist.clear()
            reader = csv.reader(my_file)
            for line in reader :
                task_name = line[0]
                task_description = line[1]
                task_priority = line[2]
                newtask = task(task_name , task_description , task_priority)
                self.todolist.append(newtask)
            print(f"{name} loaded successfully !")
        except FileNotFoundError :
            print(f"{name} not found")

            
if __name__ == "__main__" :
    
    my_todo_list = to_do_list()
    running = True
    
    while(running) :
        
        choice = my_todo_list.main_menu()
        
        if choice == "1":
            my_todo_list.add_task()
        elif choice == "2":
            my_todo_list.delete_task()
        elif choice == "3":
            my_todo_list.see_list_of_tasks()
        elif choice == "4" :
            my_todo_list.save_list()
        elif choice == "5" :
            my_todo_list.load_file()
        elif choice == "6":
            running = False