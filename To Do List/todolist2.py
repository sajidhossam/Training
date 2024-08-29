def main():
    tasks=[]

    while True:
        print("\n --------------TO DO LIST-------------")  
        print("1. Add Task")
        print("2. Show Task")
        print("3. Mark as done")
        print("4. Exit")

        choice = int(input("Enter Number of your choice: "))

        if choice == 1:
            print()
            n_tasks = int(input("How many tasks do you want?: ") )
            
            for i in range(n_tasks):
               task = input("Enter your Task: ")
               tasks.append({"task" : task , "done" : False})
               print("Task Added!")

        elif choice == 2:
            print("\n-------------------TASK LIST-----------------")
            for index, task in enumerate(tasks):
                status = "Done" if task ["done"] else "not done"
                print(f"{index + 1}. {task['task']} - {status}")


        elif choice == 3:
            task_index = int(input("Enter number of task you want to mark as done: ")) -1
            if 0 <= task_index <  len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number")
        
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
