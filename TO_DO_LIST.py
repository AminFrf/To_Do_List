class task :
    def __init__(self , name , description , priority) :
        self.name = name
        self.description = description
        self.priority = priority



class to_do_list :
    
    def __init__(self , todolist) :
        self.todolist = todolist
    
    
    def main_menu(self) :
        print("*** TO DO LIST ***")
        print("1. add new task")
        print("2. delete task")
        print("3. see list of tasks")
        print("4. save list")
        print("enter your chois : ")
    
    def add_task(self):
        name = input("pleas enter a title for your : ")
        description = input(f"enter a description about {name}")
        while True :
            priority = int(input("enter a priority for this task : \n1.low\n2.medium\n3.low"))
            if(priority not in [1 , 2 , 3]) :
                print("wrong input !!!")
                print("please try again ") 
            else :
                break
            
        new_task = task(name , description , priority)     
        self.todolist.append(new_task)   
            
    
        
