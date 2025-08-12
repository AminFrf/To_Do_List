import csv
import emoji

class helper :
    
    def creat_task(self) :
        
        name = input("pleas enter a title for your task : ")
        description = input(f"enter a description about {name} : ")
        while True :
            priority = int(input("enter a priority for this task : \n1.low\n2.medium\n3.high\n: "))
            if(priority not in [1 , 2 , 3]) :
                    
                print()
                print("wrong input !!!")
                print("please try again ")
                print() 
            else :
                break
        
                
        new_task = task(name , description , priority)
        return new_task
  
    def edit_task(self , my_todolist) :
        
        def edit_info_menu() :
                print_again = True
                choice = 0 
                while(print_again):
                    print("Which task features would you like to change?")
                    print("1. task name")
                    print("2. task description")
                    print("3. task priority")
                    choice = input("enter your choice :")
                    if choice not in ["1" , "2" , "3"] :
                        print()
                        print("wrong input !!!")
                        print()
                    else :
                        print_again = False
                        
                return choice  
        
        def change_task_name(target_task) :
                
                    newname = input("enter new name : ")
                    target_task.set_task_name(newname)
                    print()
                    print("rename done successfully")
                    print()
                

        def change_task_description(target_task) :
                
            new_description = input("enter new description : ")
            target_task.set_task_description(new_description)
            print()
            print("description changed successfully")
            print()
                
        
        def change_task_priority(target_task) :
            
            while(True):
                new_priority = int(input("enter new priority (1 , 2 , 3) : "))
                if (new_priority not in [1 , 2 , 3]) :
                    continuee = True
                    print("try again")
                else :
                    continuee = False
                if continuee == False :
                    break
                        
            target_task.set_task_priority(new_priority)
            print()
            print("priority changed successfully")
            print()
                
        oldname = input("enter name of task you want to edit : ")
        target_task = None
        for t in my_todolist.todolist :
            if t.get_task_name() == oldname :
                target_task = t 
                break  
        if target_task != None :
            choice = edit_info_menu()
            if choice == "1" :
                change_task_name(target_task)
            if choice == "2" :
                change_task_description(target_task)
            if choice == "3" :
                change_task_priority(target_task)
                my_todolist.sort_tasks_list()
        else :
            print()
            print(f"task {oldname} not found")
            print()
              
        

class task :
    
    def __init__(self , name , description , priority) :
        
        self.name = name
        self.description = description
        self.priority = priority

    def get_task_name (self):
        return self.name
        
    def get_task_description(self):
        return self.description
        
    def get_task_priority(self) :
        return self.priority  
      
    def set_task_name(self , name) :
        self.name = name
    
    def set_task_description(self , description) :
        self.description = description
    
    def set_task_priority(self , priority) :
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
            print("3. edit task")
            print("4. see list of tasks")
            print("5. save list")
            print("6. load list")
            print("7. exite")
            choice = input("enter your chois : ")
            
            if choice not in ["1" , "2" ,"3" ,"4" ,"5" , "6" , "7"]:
                print()
                print("wrong input !!!")
                print()
            else : 
                print_again = False
        return choice      
    
    def add_task_to_list(self , new_task) :
        
        
        self.todolist.append(new_task)
        self.sort_tasks_list()
            
        print()
        print("task added successfully !")   
        print()
            
    def delete_task_from_list(self) :
        
        name = input("enter the name of the task you want to delete : ")
        find = False
        for t in self.todolist :
            if t.name == name :
                self.todolist.remove(t)
                
                print()
                print(f"task {name} deleted successfully !")
                print()
                
                find = True
                break        
        
        if find == False :
            print()
            print(f"task {name} not found") 
            print()
            
    def sort_tasks_list(self) :
        for i in range(len(self.todolist)-1) :
            for j in range(len(self.todolist)-1-i):
                if(self.todolist[j].get_task_priority() < self.todolist[j+1].get_task_priority() ) :
                    temp = self.todolist[j]
                    self.todolist[j] = self.todolist[j+1]
                    self.todolist[j+1] = temp
                    
    def see_list_of_tasks(self) :
        
        if not self.todolist :
            print()
            print("no task to show !!!")
            print()
            return
        print()
        print("******************************************")
        for t in self.todolist :
            
            print("name : " + t.get_task_name())
            print("description : " + t.get_task_description())
            num_priority = t.get_task_priority()
            priority = ""
            if num_priority == 1 :
                priority = emoji.emojize("LOW :blue_circle:" , language="alias")
            elif num_priority == 2 :
                priority = emoji.emojize("MEDIUM :yellow_circle:" , language="alias")
            else :
                priority = emoji.emojize("HIGH :red_circle:" , language="alias")
            print("priority : " + priority)
            print("******************************************")
        print()
        
    def save_list(self) :
        
        name = input("enter the file name to save your TO_DO_LIST : ")
        my_file = open(f"{name}.csv" , "w")
        writer = csv.writer(my_file)
        
        for task in self.todolist :
            task_name = task.get_task_name()
            task_description = task.get_task_description()
            task_priority = task.get_task_priority()
            writer.writerow([task_name , task_description , task_priority])
        my_file.close()
        
        print()
        print("file saved successfully !")
        print()
        
    def load_file(self) :
        
        try :
            name = input("please enter the filename you want to open : ")
            my_file = open(f"{name}.csv" , "r")
            self.todolist.clear()
            reader = csv.reader(my_file)
            
            for line in reader :
                if len(line) < 3 :
                    continue
                task_name = line[0]
                task_description = line[1]
                task_priority = int(line[2])
                newtask = task(task_name , task_description , task_priority)
                self.todolist.append(newtask)
                
            print()
            print(f"{name} loaded successfully !")
            print() 
            
        except FileNotFoundError :
            print()
            print(f"{name} not found")
            print()
            
if __name__ == "__main__" :
    
    my_todo_list = to_do_list()
    the_help = helper()
    running = True
    
    while(running) :
        
        choice = my_todo_list.main_menu()
        
        if choice == "1":
            new_task = the_help.creat_task()
            my_todo_list.add_task_to_list(new_task)
        elif choice == "2":
            my_todo_list.delete_task_from_list()
        elif choice == "3" :
            the_help.edit_task(my_todo_list)
        elif choice == "4":
            my_todo_list.see_list_of_tasks()
        elif choice == "5" :
            my_todo_list.save_list()
        elif choice == "6" :
            my_todo_list.load_file()
        else :
            running = False