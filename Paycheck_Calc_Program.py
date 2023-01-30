import sqlite3
from Paycheck_Calc_Module import *
#from Paycheck_Calc_DB import *

conn = sqlite3.connect('records.db')

crsr = conn.cursor()


def select_name(name):
    crsr.execute("SELECT USER_NAME FROM Paycheck_Info WHERE USER_NAME=:name",{"name":info.name})
    return crsr.fetchone()
    

def select_hours(name):
    crsr.execute("SELECT HOURS FROM Paycheck_Info WHERE USER_NAME=:name",{"name":info.name})
    return crsr.fetchone()
    

def select_pay(user):
    crsr.execute("SELECT PAY FROM Paycheck_Info WHERE USER_NAME=:name",{"name":user})
    return crsr.fetchall()

def select_target(user):
    crsr.execute("SELECT TARGET_PAY FROM Paycheck_Info WHERE USER_NAME=:name",{"name":user})
    return crsr.fetchall()

def select_gross(user):
    crsr.execute("SELECT GROSS_PAY FROM Paycheck_Info WHERE USER_NAME=:name",{"name":user})
    return crsr.fetchall()

def select_net(user):
    crsr.execute("SELECT NET_PAY FROM Paycheck_Info WHERE USER_NAME=:name",{"name":user})
    return crsr.fetchall()



def insert_info():
    with conn:
        crsr.execute("INSERT INTO Paycheck_Info VALUES(:USER_NAME,:HOURS,:PAY,:TARGET_PAY,:GROSS_PAY,:NET_PAY)",
        {"USER_NAME":info.name,"HOURS":info.hours,"PAY":info.pay, "TARGET_PAY":info.target, "GROSS_PAY":info.gross, "NET_PAY":info.net})

def insert_totals():
    with conn:
        crsr.execute("INSERT INTO Paycheck_Info VALUES(:GROSS_PAY, NET_PAY)")

def info_print():
    print ("Name:","[(",info.name,",)]", "Hours Worked:",info.hours, "Hourly Pay:",
     info.pay,)

#
#SETTING A BASE VALUE TO VARIABLES

#info.name = input("What is your name?: ")
info.name = input("What is your name?: ")
#
#
#GET NAME OF USER


#select_hours()
#select_pay()
#select_target()
#
#
#CHECK VALUES IN DATABASE


if (len(select_name(info.name))) > 0:

    #return_info(info.name, info.hours, info.pay, info.target)
    info.name = (select_name(info.name))
    print (info.name)
    info.hours = (select_hours(info.name))
    info.pay = (select_pay(info.name))
    info.target = select_target
    #info.gross == select_gross

    user_choice = input("Your USER INFO is found! Please enter 'Y' for a new calculation or 'N' to view last calculation: ")

    if user_choice == "N":
        #info.gross == select_gross()
        #info.net == select_net()
        info_print()
    else:
        print()

else:
    info.hours = float(input("How many hours did you work this week?: "))
    info.pay = float(input("How many dollars per hour do you recieve?: "))
    info.target = int(input("What is your target income this paycheck?: "))

    #IF NAME IS ALREADY FOUND, USE SAVED DATA
    #IF NEW NAME, ASK FOR NEW INFORMATION

    info.gross = gross_income()

    med = medicare()

    ss = social_sec()

    info.net = find_taxes()

    #FUNCTIONS TO FIND GROSS, TAXES, AND NET

    insert_info()

    #SAVE NEW INFO TO DATABASE

    if info.net < info.target:
        print("You will not reach target income")
    else:
        print("You will reach your target income")
    

        #print(info.gross)

        #print(med)

        #print (ss)

        #print (net_pay)



