def task():
    task=[]
    print(".......... WELCOME TO THE TASK MANAGEMENT APP ..........")

    total_task = int(input(" how many kast you want to enter "))
    for i in range(total_task):
        user = input(f'Enter task {i+1} ')
        task.append(user)
    print("Your task is ",task)

    while True:
        operation = int(input(" 1. Add \n 2. Update \n 3. Delete \n 4. View \n Exist"))
        if operation == 1:
            add = input("Enter New task ")
            task.append(add)
            print(f'Your Task {add} Has Been Successful Added. ')

        elif operation ==2:
            update = input("Which item you want to update ")
            if update in task:
                update_val = input("Enter New Task: ")
                index = task.index(update)
                task[index]= update_val
                print(f'your Task {update_val} has Been Successfully Updated ')

        elif operation ==3:
                dlt = input("Which Item You Want to Delete : ")
                if dlt in task:
                     index= task.index(dlt)
                     del task[index]
                     print(f'Your Task {dlt} has Been Successfully Deleted..')
                
        elif operation == 4:
             print("Total task is ",task)

        elif operation ==5 :
             print("program closed...")
             break
        else:
             print("Invalid Input ")
task()
  