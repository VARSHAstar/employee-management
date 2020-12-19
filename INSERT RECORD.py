print()
print()
print()
print('*************************************************************************************************')
print('           W E L C O M E   T O   E M P L O Y E E   M A N A G E M E N T   S Y S T E M             ')
print('*************************************************************************************************')
print()
print()
print('                    ..................Choose your module................')
print()
print()
print('                    ----------------------------------------------------')
print('                   |                 MODULE               | MODULE CODE |')
print('                    ----------------------------------------------------')
print('                   | 1.Employee Metails Management Module |      1      |')
print('                   | 2.Employee Salary Managemant Module  |      2      |')
print('                   | 3.Search Module                      |      3      |')
print('                    ----------------------------------------------------')

print()
print()

#__________________E M P L O Y E E   D E T A I L S   M A N A G E M E N T   M O D U L E____________________



#____________________________ PROGRAM TO INSERT RECORD TO THE DATABASE_____________________________________
ans='y'
def insert_record():
    i=0
    while i<1 or (ans=='Y'or"y"):
            import mysql.connector as m
            mycon=m.connect(host='localhost',user='varsha',passwd='Var@123#',database='emp_mgmt')
            cur=mycon.cursor()
            q=input('employee id                   : ' )
            w=input('employee name                 : ')
            e=input('employee department           : ')
            r=input('employee salary               : ')
            t=input('employee designation          : ')
            y=input('employee date of birth        : ')
            u=input('employee date of joining job  : ')
            i=int(input('employee contact number       : '))
            o=input('employee blood group          : ')
            p=input('employee marital status       : ')
            a=input('employee city                 : ')
            s=input('employee country              : ')
            d=input('employee email                : ')
            f=input('employee address              : ')
            st="insert into emp_mgmt values('{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}','{}','{}','{}')".format(q,w,e,r,t,y,u,i,o,p,a,s,d,f)
            cur.execute(st)
            mycon.commit()
            mycon.close()
            print(q,'details have been saved :) ')
            i+=1
            ans=input('Do you want to enter more records \n if yes then press y \n otherwise enter any key ')
insert_record()

    
