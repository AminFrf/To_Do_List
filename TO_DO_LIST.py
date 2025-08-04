class task :
    
    def __init__(self , name , description , priority) :
        self.name = name
        self.description = description
        self.priority = priority
        


class to_do_list :
    
    def __init__(self , todolist) :
        self.todolist = todolist
    
    
    def main_menu(self) :
        
        print_again = True
        choice = 0 
        
        while(print_again) :
            
            print("*** TO DO LIST ***")
            print("1. add new task")
            print("2. delete task")
            print("3. see list of tasks")
            print("4. save list")
            print("5. exite")
            choice = input("enter your chois : ")
            
            if choice not in ["1" , "2" ,"3" ,"4" ,"5" ]:
                print("wrong input !!!")
            else : 
                print_again = False
        return choice 
        
    
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
            
    def delete_task(self) :
        name = input("enter the name of the task you want to delete")
        find = False
        for t in self.todolist :
            if t.name == name :
                self.todolist.remove(t)
                print(f"task {name} deleted successfully")
                find = True
                break        
        
        if find == False :
            print(f"task {name} not found")    
            
    def see_list_of_tasks(self) :
        
        if not self.todolist :
            print("no task to show !!!")
            return
        
        for t in self.todolist :
            
            print("name : " + t.name)
            print("description : " + t.description)
            print("priority : " + t.priority)
            print("******************************************")
            
            
if __name__ == "__main__" :
    
    my_todo_list = to_do_list([])
    running = True
    
    while(running) :
        
        my_todo_list.main_menu()