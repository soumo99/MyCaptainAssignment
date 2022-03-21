import csv

def write_into_csv(info_list):
    with open('student_info_csv','a',newline='')as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0 :
            writer.writerow(["Name", "Age","Contact-No","Email-id"])

        writer.writerow(info_list)

if __name__ == '__main__':

    Condition = True
    student_num=1

    while(Condition):
        student_info = input("Enter some student information for student #{} in the following format(Name , Age , Contact no., Email): ".format(student_num))
        # print(student_info)

        student_info_list = student_info.split(' ')
        # print("Entered split up information is : " ,str(student_info_list))

        print("\n The entered information is -\nName: {}\nAge: {}\nContact_number : {}\nE-mail ID: {}"
            .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check = input("Is the entered information correct ? (yes/no):")
        if choice_check == "yes":
            write_into_csv(student_info_list)

            Condition_check = input("Enter (yes/no) if you want to enter another student information : ")
            if Condition_check == "yes":
                Condition = True
                student_num = student_num+1
            elif Condition_check == "no":
                Condition = False
            elif choice_check =="no":
                print("\n Please re-enter the values")
