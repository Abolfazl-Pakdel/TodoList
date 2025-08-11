#""""
# To do list programm
import termcolor
import termcolor2
import pyfiglet
# import json

# black, red, green, yellow, blue, magenta, cyan, white,
# light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
# light_magenta, light_cyan.

show_work = []
# show_work_2 = []
try:
    with open('data_work_list.txt', 'r') as file:
        for line in file:
            show_work.append(line.strip())
except FileNotFoundError:
    pass

def save_to_file():
    with open('data_work_list.txt', 'w') as file:
        for item in show_work:
            file.write(item+ "\n")

print(termcolor2.colored("Wellcome to my program!!", "yellow"))
print(termcolor2.colored("Please Chose bettwen the items below ||", "red"))
while True:
    print(termcolor2.colored("1. Add to list", "green"))
    print(termcolor2.colored("2. Remove from list", "green"))
    print(termcolor2.colored("3. Mark as Done", "green"))
    print(termcolor2.colored("4. View Task", "green"))
    print(termcolor2.colored("5. Exit", "green"))
    first_entery = int(input("Enter your choice: "))
    if first_entery == 5:
        print(termcolor2.colored("Goodbye!,come back soon :)", "green"))
        break
    elif first_entery == 1:
        print(termcolor2.colored("== Add to list ==", "blue"))
        show_yes_or_no = input("Do you wish to add item to your list? (Y/N): ")
        if show_yes_or_no == "Y":
            Adder = input("Enter your Works: ")
            show_work.append(Adder)
            save_to_file()
        #     # show_work_2.append(Adder)
        #     file_man = open("data_work_list_chert.txt", "a")
        #     for i, item in enumerate(show_work, start=1):
        #         #
        #         file_man.write(f"{i}. {item} \n")
        #     file_man.close()
        # else:
        #     continue
        print(termcolor2.colored("== Done ==", "blue"))
    elif first_entery == 2:
        print(termcolor2.colored("== Remove from list of Works ==", "cyan"))
        print(termcolor2.colored(f"your work until now => {show_work}", "light_grey"))
        delter = int(input("Which item do you want to remove?[Notice!!! items sterted from zero!!]"))
        show_work.pop(delter)
        save_to_file()
        print(termcolor2.colored("== Removed Successfully :) ==", "blue"))
    elif first_entery == 3:
        print(termcolor2.colored("== Mark as Done ==", "blue"))
        for i, item in enumerate(show_work, start=1):
            print(termcolor2.colored(f"{i}. {item}", "light_yellow"))
        donner = int(input("Which Work you done ? "))
        show_work[donner - 1] = termcolor2.colored("DONE !!!", "magenta")
        print("== Done ==")
    elif first_entery == 4:
        print(termcolor2.colored("== Your Work ==", "blue"))
        file_man = open("data_work_list.txt", "r")
        for i, item in enumerate(show_work, start=1):
            print(termcolor2.colored(f"{file_man.read()}", "magenta"))
        file_man.close()
        print(termcolor2.colored("== Done ==", "blue"))
    else:
        print(termcolor2.colored("Please enter a valid choice ERROR!!", "light_red"))


""""
tasks = ["Read book", "Do homework", "Exercise", "Meditate"]
for i, item in enumerate(tasks, start=1):
    print(f"{i}. {item}")

task_done = int(input(("Which task number did you finish? ")))
tasks[task_done - 1]= "DONE !!!"
print("== Updateed list work ==")
for i, item in enumerate(tasks, start=1):
    print(f"{i}. {item}")

"""
# file_object = open("data_work_list_chert.txt", "w")
# for i, item in enumerate(show_work, start=1):
#     file_object.write(f"{i}. {item}\n")
# file_object = open("data_work_list_chert.txt", "r")
# print(file_object.read())

# file_object = open("data_work_list_chert.txt", "r")
# print(file_object.read())
# file_object.close()