tasks = []
print(tasks)
def show_menu():
    print("\n1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    


while True:
   show_menu()
   choice = input("Enter Your Choice(1-5): ")

   if choice == '1':
       task = input("Enter the task:")
       tasks.append({'task': task, 'done': False})
       print("Task added")
   
   elif choice == '2':
       for i, t in enumerate(tasks):
           status = 'Done' if t['done'] else 'Not Done'

   elif choice == '3':
       index = int(input("Enter task number to mark done: ")) - 1
       if 0 <=index < len(tasks):
           tasks[index]['done'] = True
           print("Task marked as done.")

   elif choice == '4':
       index = int(input("Enter task number to delete: ")) - 1
       if 0 <= index < len(tasks):
           tasks.pop(index)
           print("Task deleted.") 

   elif choice == '5':
       break          
   
