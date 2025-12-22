#Smart Student Result Management System

import pandas as pd
import os





file_name = "studentdetails.csv"
if not os.path.exists(file_name):
    subjects=input("enter subjects (comma separated): ").split()
    subjects=[sub.strip() for sub in subjects]

    columns = pd.MultiIndex.from_tuples(
    [("Rollnumber",""),("studentname","")]+
    [("Marks",sub)for sub in subjects]+
    [("Total",""),("Result","")]
    )
    df=pd.DataFrame(columns=columns)
    df.to_csv(file_name, index=False)
    print("file created successfully")
        
else:
    df = pd.read_csv(file_name, header=[0,1])
    print("Existing file loaded success.")

    subjects = list(df["Marks"].columns)
    print("subjects found in file: ",subjects)

student={}
    
while True:
    choice = input("Enter want you want add student(or'enter Marks','view result','total','Update','delete',Exit'): ").lower()

    if choice == 'exit':
        print("Successfully Store The Data")
        break

    
    if choice == "add student":
        
        while True:
            studentname=input("enter student name: ").strip()
            rollnumber=input("enter roll number: ").strip()
            student[rollnumber] = {
                "name": studentname,
                "subjects": subjects,
                "marks": {},
                "total": {},
            }

            a= input("Do you want add more student? (yes/no): ").lower()
            if a == "no":
                break
        print(student)


    elif  choice == "enter marks":
        while True:
            roll = input("Enter roll number to enter marks: ").strip()
            if roll in student:
                print(f"\nSubjects for {student[roll]['name']}: {student[roll]['subjects']}")
                while True:
                    for sub in subjects:
                        m = int(input(f"Enter marks for {sub}: "))
                        student[roll]['marks'][sub]= m
                    break
            else:
                print("roll number Not Found!")

            next_students = input("Do you want to enter marks for another student? (yes/no): ").lower()
            if next_students == "no":
                break
        print(student)


    elif choice == "total":
        while True:
            option = input("enter 'rollnumber' or 'studentname' (or 'exit'): ").lower()

            if option == "exit":
                break

            elif option == "rollnumber":
                roll = input("enter rollnumber: ").strip()
                if roll in student:
                    total=sum(student[roll]['marks'].values())
                    print("Total Marks:", total)
                else:
                    print("rollnumber Not Found")

            elif option == "studentname":
                name = input("enter studentname: ").strip()
                found = False
                for roll, info in student.items():
                    if info["name"].lower() == name.lower():
                        total = sum(info["marks"].values())
                        print(f"\nTotal marks for {info['name']} ({roll}): {total}")
                        found = True
                        break
                if not found:
                    print("Student name not found!")

            j = input("Do you want get more student total? (yes/no): ").lower()
            if j == "no":
                break


    elif choice == "update":
        file_name = "studentdetails.csv"
        df = pd.read_csv(file_name, header=[0,1])
        df.columns = [(col[0], "" if "Unnamed" in str(col[1]) else col[1]) for col in df.columns]
        df.columns = pd.MultiIndex.from_tuples(df.columns)
        print(df.columns)

        df[("Rollnumber", "")] = df[("Rollnumber", "")].astype(str)
        df[("studentname", "")] = df[("studentname", "")].astype(str)
        while True:
            n = input("enter 'rollnumber' or 'studentname' or 'exit': ").lower()
            if n == "exit":
                print("Marks Updated")
                break
                
            if n == "rollnumber":
                roll = input("enter rollnumber: ").strip()
                if roll not in df["Rollnumber"].values:
                    print("Rollnumber not found!")
                    continue
                subject = input("Enter subject to update: ").strip()
                if subject not in subjects:
                    print("Subject not found!")
                    continue
                new_marks = int(input("Enter new marks: "))
                df.loc[df["Rollnumber"] == roll, ("Marks", subject)] = new_marks
                total = sum([df.loc[df["Rollnumber"] == roll, ("Marks", s)].values[0] for s in subjects])
                df.loc[df["Rollnumber"] == roll, ("Total", "")] = total
                if total >= 180:
                    grade = "A+"
                elif total >= 150:
                    grade = "A"
                elif total >= 120:
                    grade = "B+"
                elif total >= 100:
                    grade = "B"
                elif total >= 80:
                    grade = "C"
                else:
                    grade = "Fail"

                df.loc[df["Rollnumber"] == roll, ("Result", "")] = grade
                df.to_csv(file_name, index=False)
                print("Marks updated successfully!")
            elif n == "studentname":
                name = input("enter studentname: ").strip()
                if name not in df["studentname"].values:
                    print("Studentname not found!")
                    continue
                subject = input("Enter subject to update: ").strip()
                if subject not in subjects:
                    print("Subject not found!")
                    continue
                new_marks = int(input("Enter new marks: "))
                df.loc[df["studentname"] == name, ("Marks", subject)] = new_marks
                total = sum([df.loc[df["studentname"] == name, ("Marks", s)].values[0] for s in subjects])
                df.loc[df["studentname"] == name, ("Total", "")] = total
                if total >= 180:
                    grade = "A+"
                elif total >= 150:
                    grade = "A"
                elif total >= 120:
                    grade = "B+"
                elif total >= 100:
                    grade = "B"
                elif total >= 80:
                    grade = "C"
                else:
                    grade = "Fail"

                df.loc[df["studentname"] == name, ("Result", "")] = grade
                df.to_csv(file_name, index=False)
                print("Marks updated successfully!")
        cont = input("Update another student? (yes/no): ").lower()
        if cont == "no":
            break

    elif choice == "delete":
        file_name = "studentdetails.csv"
        df = pd.read_csv(file_name, header=[0,1])
        df.columns = [(col[0], "" if "Unnamed" in str(col[1]) else col[1]) for col in df.columns]
        df.columns = pd.MultiIndex.from_tuples(df.columns)
        print(df.columns)

        df[("Rollnumber", "")] = df[("Rollnumber", "")].astype(str)
        df[("studentname", "")] = df[("studentname", "")].astype(str)
        while True:
            option = input("enter 'rollnumber' or 'studentname' (or 'exit'): ").lower()

            if option == 'exit':
                print("exit deletion process")
                break

            elif option == "rollnumber":
                roll = input("enter roll number: ").strip()
                df = df[df[("Rollnumber", "")] != roll]

            elif option == "studentname":
                name_to_delete = input("Enter studentname: ").strip().lower()
                df = df[df[("studentname", "").str.lower() != name_to_delete]]
            else:
                print("Invalid option.")

            df = df.reset_index(drop=True)
            df.to_csv(file_name, index=False)
            print("Delete successfully")
            print(df)
        cont_delete = input("Delete another student? (yes/no): ").lower()
        if cont_delete == 'no':
            break
        print(student)


                
        
    elif choice == "view result":
        while True:
            option = input("enter 'rollnumber' or 'studentname'  (or 'exit'): ").lower()

            if option == 'exit':
                print("no more data")
                break


            elif option == "rollnumber":
                roll=input("enter rollnumber: ").strip()
                if roll in student:
                    total=sum(student[roll]['marks'].values())
                    if total >= 90:
                        grade = "A+"
                    elif total >=80:
                        grade = "A"
                    elif total >= 70:
                        grade = "B+"
                    elif total >= 60:
                        grade = "B"
                    elif total >= 50:
                        grade = "C"
                    else:
                        print("fail")
                    print("Marks:", student[roll]['marks'])
                    print("Total Marks:", total)
                    print("REsult:", grade)
                else:
                    print("rollnumber Not Found")


            elif option == "studentname":
                name=input("enter studentname: ").strip()
                found = False
                for roll, info in student.items():
                    if info["name"].lower() == name.lower():
                        total=sum(student[roll]['marks'].values())
                        if total >= 90:
                            grade = "A+"
                        elif total >=80:
                            grade = "A"
                        elif total >= 70:
                            grade = "B+"
                        elif total >= 60:
                            grade = "B"
                        elif total >= 50:
                            grade = "C"
                        else:
                            print("fail")
                        print("Marks:", student[roll]['marks'])
                        print("Total Marks:", total)
                        print("Result:", grade)
                    else:
                        print("student name  Not Found")


        new_row ={
            ("Rollnumber", ""): roll,
            ("studentname", "") : student[roll]['name'],
        }
        for sub in subjects:
            new_row[("Marks",sub)]= student[roll]['marks'][sub]

        new_row[("Total", "")] = total
        new_row[("Result", "")] = grade


        new_data = pd.DataFrame([new_row])


        new_data.to_csv(file_name, mode='a', header=False, index=False)
        print("Data added successfully")


        
df = pd.read_csv(file_name, header=[0,1])
print(df)



    

                    
                    
            
                


    
            

        




    
            
                



    

        

    

 
        

    
