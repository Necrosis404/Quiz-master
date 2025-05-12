"""
************************* NAVY CHILDREN SCHOOL *****************************
******************************* QUIZ MASTER ****************************
*******  Designed and Maintained By :-
*******  SAIKAT SAHA                      -  CLASS XII B  [ 2021-2022 ]
*******  PRAVALLIKA KANDRELA      -  CLASS XII B  [ 2021-2022 ]
*******  PARTIK PRATIHAR               -  CLASS XII B  [ 2021-2022 ]
*******  DEEPAK KUMAR SINGH       -  CLASS XII B  [ 2021-2022 ]
"""

import mysql.connector as mk

# GLOBAL VARIABLES DECLARATION
db_choice = None
db_pwd=None
tot_ques_default = 5

# FOR CONFIG RESET ==================================================================================
#=====================================================================================================
#=====================================================================================================
                 
def create_db_quiz():
      global db_choice
      con= mk.connect(host="localhost",user="root",password=db_pwd)
      cur=con.cursor()
      q1="show databases;"
      cur.execute(q1)
      rs=cur.fetchall()
      print("Checking for existing database quiz.......\n")
      for dname in rs:
            if dname[0]=="quiz":
                  print("Database quiz already exists!!!")
                  f = int(input("press 1 to delete the existing database:- "))
                  if f == 1:
                        query1="drop database quiz; "
                        cur.execute(query1)
                        con.commit()
                        print("\nDATABASE DELETION SUCCESSFUL!!!\n")
                  else:
                        print("***Please try again with valid choice!!!\n")
                        break      # returns to config_panel
      else:
            print("Press 1 to Create database with NEW input questions!!!")
            print("Press 2 to Create database with DEFAULT questions!!!")
            db_choice = int(input("Enter your choice (1-2):- "))
            q2="create database {} ".format("quiz")
            print("Creating database QUIZ......")
            cur.execute(q2)
            print("Database created successfully!")
            q3="use {}".format("quiz")
            cur.execute(q3)
            q4="create table questions(ques_no int(3) primary key , ques_desc varchar(500),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(50))"
            cur.execute(q4)
            print("->Table questions created!!! ")
            q5="create table participants(uid int(3) primary key, uname varchar(50), mailid varchar(50), password varchar(22), pwd_hint varchar(30))"
            cur.execute(q5)
            print("->Table particitants created!!!")
            q6="create table scores(uid int(3) primary key, uname varchar(50), mailid varchar(50), marks int(50))"
            cur.execute(q6)
            print("->Table scores created!\n")
      
            if db_choice == 1: #new input questions
                  tot_ques=int(input("Number of questions to be added: "))
                  for num in range(1,tot_ques+1):
                        sql=num
                        sql1=input("Enter Question: ")
                        sql2=input("Enter the option a: ")
                        sql3=input("Enter the option b: ")
                        sql4=input("Enter the option c: ")
                        sql5=input("Enter the option d: ")
                        sql6=input("The answer is (a,b,c,d): ")
                        sql_in= "insert into questions values({},'{}','{}','{}','{}','{}','{}')".format(sql,sql1,sql2,sql3,sql4,sql5,sql6)
                        print()
                        cur.execute(sql_in)
                        con.commit() 
                  print("All Questions added successfully!!!\n") #returns to config reset
                  
            elif db_choice == 2:  #default questions
                  ques1=[1,"ARPANET stands for ?","Advanced Recheck Projects Agency Internet","Advanced Recheck Projects Agency Network",
                              "Advanced Research Projects Agency Network","Advanced Research Projects Agency Internet","c"]
                  ques2=[2,"Which protocol is commonly used to retrieve email from a mail server?","FTP","IMAP","HTML","TELNET","b"]
                  ques3=[3,"Pick the correct username used for logging in database (sql with Python) :-","root","local","directory","host","a"]
                  ques4=[4,"Which of the following is not a legal method for fetching records from database from within Python?",
                              "fetchone()","fetchtwo()","fetchall()","fetchmany()","b"]
                  ques5=[5," A ____ is property of the entire relation, which ensures through its value that each tuple is unique in a relation",
                             "Rows","Key","Attribute","fields","b"]
                  
                  sql_1= "insert into questions values({},'{}','{}','{}','{}','{}','{}')".format(ques1[0],ques1[1],ques1[2],ques1[3],ques1[4],ques1[5],ques1[6])
                  cur.execute(sql_1)
                  sql_2= "insert into questions values({},'{}','{}','{}','{}','{}','{}')".format(ques2[0],ques2[1],ques2[2],ques2[3],ques2[4],ques2[5],ques2[6])
                  cur.execute(sql_2)
                  sql_3= "insert into questions values({},'{}','{}','{}','{}','{}','{}')".format(ques3[0],ques3[1],ques3[2],ques3[3],ques3[4],ques3[5],ques3[6])
                  cur.execute(sql_3)
                  sql_4= "insert into questions values({},'{}','{}','{}','{}','{}','{}')".format(ques4[0],ques4[1],ques4[2],ques4[3],ques4[4],ques4[5],ques4[6])
                  cur.execute(sql_4)
                  sql_5= "insert into questions values({},'{}','{}','{}','{}','{}','{}')".format(ques5[0],ques5[1],ques5[2],ques5[3],ques5[4],ques5[5],ques5[6])
                  cur.execute(sql_5)
                  print("All Questions added successfully!!!\n")
                  con.commit()  #returns to config reset
                  
            else:
                  print("***Please try again with a valid choice!!!\n")  #returns to config reset
      con.commit()      
      con.close()
        
#==================================================================================================
      
def update_ques():
      #DONE
      con= mk.connect(host="localhost",user="root",password=db_pwd,database="quiz")
      cur=con.cursor()
      print()
      print("->ALL QUESTIONS IN DATABASE :- ")
      d="select * from questions;"
      cur.execute(d)
      sp = cur.fetchall()
      for i in sp:
            print("Q.",i[0],i[1],sep='. ')
      print()
      
      quesno=int(input("Enter the Question Number to be updated: "))
      searchq="select * from questions where ques_no={}".format(quesno)
      cur.execute(searchq)
      rs=cur.fetchone()
      if (rs==None):
            print("***No such question number in the table!!\n") #returns to config reset
      else:
            print("\nQuestion Details are as follows :-")
            print("Question ",rs[0],": ",rs[1])
            print("->Option a :- ",rs[2])
            print("->Option b :- ",rs[3])
            print("->Option c :- ",rs[4])
            print("->Option d :- ",rs[5])
            print("=>ANSWER :- ",rs[6])
            print("-----------------------------------------------------------------------------------------")
            
            ques=input("Enter the NEW question: ")
            a=input("Enter the option a: ")
            b=input("Enter the option b: ")
            c=input("Enter the option c: ")
            d=input("Enter the option d: ")
            answer=input("Enter the correct answer (a,b,c,d): ")
            q="update questions set ques_desc='{}',opt_a='{}',opt_b='{}',opt_c='{}',opt_d='{}',ans='{}' where ques_no={}".format(ques,a,b,c,d,answer,quesno)
            cur.execute(q)
            con.commit()
            print("\nUPDATION SUCCESSFUL!!!\n")
      con.close()
      
#=====================================================================================================
      
def insert_ques():
      con=mk.connect(host="localhost",user="root",password=db_pwd,database="quiz")
      cur=con.cursor()
      print()
      d="select * from questions;"
      cur.execute(d)
      y=cur.fetchall()
      tot_ques=0
      print("->ALL QUESTIONS IN DATABASE :- ")
      for i in y:
            print(i[0],i[1],sep='.')
            tot_ques += 1
      print("***Total questions in database:- ",tot_ques)
      print()
      
      quesno=int(input("Enter the New Question number to be inserted: "))
      searchq="select * from questions where ques_no={}".format(quesno)
      cur.execute(searchq)
      rs=cur.fetchone()
      
      if (rs!=None):
            print("***Question number already exists in the table!!\n")
      else:    
            print("Enter the information to be inserted into the questions Table:- ")
            sql1=input("Enter The Question: ")
            sql2=input("Enter the option a: ")
            sql3=input("Enter the option b: ")
            sql4=input("Enter the option c: ")
            sql5=input("Enter the option d: ")
            sql6=input("The answer is (a,b,c,d): ")
            sql_in= "insert into questions values({},'{}','{}','{}','{}','{}','{}')".format(quesno,sql1,sql2,sql3,sql4,sql5,sql6)
            cur.execute(sql_in)
            con.commit()
            print("\nQUESTION INSERTED SUCCESSFULLY!!!\n")
      con.close() #returns to config reset

#=============================================================================================================

def delete_ques():
      #DONE
      con=mk.connect(host="localhost",user="root",password=db_pwd,database="quiz")
      cur=con.cursor()
      print()
      d="select * from questions;"
      cur.execute(d)
      y=cur.fetchall()
      print("->ALL QUESTIONS IN DATABASE :- ")
      for i in y:
            print(i[0],i[1],sep='.')
      print()
      quesno=int(input("Enter the Question number to be deleted: "))
      searchq="select * from questions where ques_no={}".format(quesno)
      cur.execute(searchq)
      rs=cur.fetchone()
      if (rs==None):
            print("\n***No such Question number in the table!!!\n")
      else:

            dquery="delete from questions where ques_no={}".format(quesno)
            cur.execute(dquery)
            con.commit() 
            print("\nDELETION SUCCESSFUL!!!\n")
      con.close()

#=============================================================================================================

def disp_ques():
      #DONE
      con=mk.connect(host="localhost",user="root",password=db_pwd, database="quiz")
      cur=con.cursor()
      query="select * from questions;"
      cur.execute(query)
      rs=cur.fetchall()
      print()
      if rs==[]:
            print("No Questions Found!!")
      else:        
            for row in rs:
                  print("Question ",row[0],": ",row[1])
                  print("->option a :- ",row[2])
                  print("->option b :- ",row[3])
                  print("->option c :- ",row[4])
                  print("->option d :- ",row[5])
                  print("=>Answer  :- ",row[6])
                  print()
      con.close()
    
#CONFIG RESET FINISHED!! ==============================================================================================
#=====================================================================================================
#=====================================================================================================

def config_reset():
      #DONE
      ask_credentials()
      print("QUIZ MASTER Configuration Panel....")
      key=input("Enter the secret key to configure database: ")
      if key=="boss":
            print("Key Matched!!")
            con=mk.connect(host="localhost",user="root",password=db_pwd)
            print("Connection established with MySQl database!\n")
            
            while True:
                  print("================== MAIN MENU OF CONFIGURATION PANEL ======================")
                  print("""WARNING:- IT IS RECOMMENDED TO DELETE YOUR BACKEND DATABASE QUIZ AND
                        CREATE A NEW DATABASE QUIZ !!!""")
                  print("1. To create database named quiz and add questions! ")
                  print("2. To update the questions in the database quiz! ")
                  print("3. To insert a question in the database quiz! ")
                  print("4. To delete a question in the database quiz! ")
                  print("5. To display all the details of questions in the database quiz! ")
                  print("6. To Exit!")
                  print("==========================================================\n")
                  print("Enter the serial no. for configuration in QM!!!")
                  choice=int(input("Enter your choice (1-6): "))
                  
                  if choice==1:
                        create_db_quiz()
                  elif choice==2:
                        update_ques()
                  elif choice==3:
                        insert_ques()
                  elif choice==4:
                        delete_ques()
                  elif choice==5:
                        disp_ques()
                  elif choice==6:
                        print("Exiting the configuration panel......")
                        break  # jumps to home()
                  else:
                        print("***Try again with a valid choice!!!!!") # continues while loop
      else:
            print("Invalid credentials!!!") # jumps to home()

#=================================================================================

def ask_credentials():
      #DONE
      global db_pwd, db_name
      print("------------------------------------------------------")
      print("Before you start, please provide the following info: ")
      db_pwd=input("Please provide your MySQL database connection password:- ")
      db_name="quiz"  #input("Enter the name of the backend database:")
      print("***Make sure that you have backend database named quiz!!!")
      print("Input cached into system.")
      x=input("Press Enter to continue.... ")
      print()
    
# ****************  REGISTER  ================================================================================================

def register():
      #DONE
      ask_credentials()
      con= mk.connect(host="localhost",user="root",password=db_pwd)
      cur=con.cursor()
      q1="show databases;"
      cur.execute(q1)
      rs=cur.fetchall()
      
      for dname in rs: #checking for database quiz
            if dname[0]=="quiz":
                  print("------------------------- WELCOME TO REGISTRATION PORTAL----------------------------")
                  x=int(input("select an user id: "))
                  searchq1="use quiz;"
                  cur.execute(searchq1)
                  searchq2="select * from participants where uid={}".format(x)
                  cur.execute(searchq2)
                  rs=cur.fetchone()
                  if (rs!=None):
                        print("User id already exists in the table!!")
                        print("Try again with another user id!!!")
                  else:    
                        un=input("Enter the user name: ")
                        mail=input("Enter mail id: ")
                        pswd=input("Enter the password: ")
                        pswd_h=input("Enter a password hint: ")
                        q="insert into participants values({},'{}','{}','{}','{}')".format(x,un,mail,pswd,pswd_h)
                        cur.execute(q)
                        con.commit()
                        print("User registered successfully!")
                  break
      else:
            print("Database quiz not found!!!")  # returns to home()
      con.close()
                 
#===   LOGIN    ==========================================================
                  
def login():
      #DONE
      ask_credentials()
      con= mk.connect(host="localhost",user="root",password=db_pwd)
      cur=con.cursor()
      q1="show databases;"
      cur.execute(q1)
      rs=cur.fetchall()
      
      for dname in rs:
            if dname[0]=="quiz":
                  print("-----------------  LOGIN PORTAL  ------------------")
                  x=int(input("Select an user id to login: "))
                  y=input("Enter your password: ")
                  searchq1="use quiz;"
                  cur.execute(searchq1)
                  searchq="select * from participants where uid={}".format(x)
                  cur.execute(searchq)
                  r=cur.fetchone()
                  if (r==None):
                        print("***No such user registered!!")
                        print("***If not Regsitered, Register first!!!")        
                  else:
                        if r[0]==x and r[3]==y:
                              print("Login Successful!")
                              quiz(r)
                        else:
                              print("Invalid credentials!!")
                  break
      else:
            print("Database quiz not found!!!")
      con.close()
      
#=== QUIZ  =======================================================================
      
def quiz(r):
      #DONE
      con=mk.connect(host="localhost",user="root",password=db_pwd,database="quiz")
      cur=con.cursor()
      print()
      print("================  WELCOME TO QUIZ  =======================")
      print("->There will be total of *FIVE* questions.")
      print("->Each question carries 1 mark.")
      print("->Fill the Answers in (a,b,c,d)")
      z = input("Press ENTER to start the quiz....\n")
      total_marks = 0
      tot_ques = 0
      q5 = "select * from questions"
      cur.execute(q5)
      dp = cur.fetchall()
      print(dp)
      for v in range(1,len(dp)+1):
            tot_ques+=1
      print(tot_ques)
      q7 = "select * from questions"
      cur.execute(q7)
      for i in range(1,tot_ques+1):
            rs=cur.fetchone()
            print(i,".",rs[1])
            print("Option a :- ",rs[2])
            print("Option b :- ",rs[3])
            print("Option c :- ",rs[4])
            print("Option d :- ",rs[5])
            ans = input("Enter your option (a,b,c,d) :- ")
            
            while ans.lower() not in "a,b,c,d":   #checking for alphabets
                  ans = input("Enter your valid answer (a,b,c,d): ")
                  continue
            else:
                  if ans.lower() == rs[6]:   #checking the correct answer
                        total_marks += 1
            print()
            
      print("You Scored",total_marks,"out of",tot_ques,"!!!")
      
      q1 = "select * from scores where uid={}".format(r[0])  
      cur.execute(q1)
      rp = cur.fetchone()
      if (rp == None):
            q2="insert into scores values ({},'{}','{}',{})".format(r[0],r[1],r[2],total_marks)
            cur.execute(q2)
            print("SCORES AND DETAILS INSERTED!!!")
      else:
            q3="update scores set marks={} where uid={}".format(total_marks,r[0])
            cur.execute(q3)
            print("SCORES UPDATED!!!")
      con.commit()
      
      
#=========================================================================================
      
def home():
      while True:
            print()
            print("***************************************************************")
            print("                 ***WELCOME TO QUIZ MASTER***                ")
            print("***************************************************************")
            print("1. To configure/reset backend database (ADMIN ACCESS)")
            print("2. To Register")
            print("3. To Login and Quiz")
            print("4. To Exit")
            print("***************************************************************")
            choice=int(input("Enter your choice (1-4): "))
            if choice==1:
                  config_reset()
            elif choice==2:
                  register()
            elif choice==3:
                  login()
            elif choice==4:
                  print("Exiting....")
                  print("Thank You for using the application!!!")
                  print("********Copyrights reseved to NCS Vizag Group 8 students only !!!*********")
                  print("Have a Great Day..... ")
                  break
            else:
                  print("*** Try again with a valid choice!!!!!")
home()
