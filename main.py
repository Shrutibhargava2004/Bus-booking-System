from tkinter import *
from tkinter.messagebox import *
import sqlite3
from datetime import date 
con=sqlite3.Connection('Python1')
cur=con.cursor()

cur.execute('create table if not exists operator(op_id int, op_name varchar(20), op_address varchar(50), op_phone numeric, op_email varchar(30))')
cur.execute('create table if not exists bus(bus_id int, bus_type varchar(30), capacity int, fare numeric, op_id int, route_id int)')
cur.execute('create table if not exists route(route_id int, station_name varchar(20), station_id int,bus_id int, running_date date, seat_available int)')
cur.execute('create table if not exists passenger(Booking_ref int, name varchar(30),gender varchar(20), No_of_seats int, Mobile_number numeric, Age int , Fare numeric, bus_details varchar(20), travel_on_date date, booked_on_date date, boarding_point varchar(20), destination_point varchar(20))')
con.commit()

cur.execute("insert into operator values(1, 'kamla', 'Guna', 1122334455, 'kamla@gmail.com'), (2, 'Rayeen', 'bhopal', 1112223330, 'rayeen@gmail.com'),(3, 'Atul', 'Bus Stand Multai', 1234567890, 'atul@gmail.com') ")
cur.execute("insert into bus values (1,'AC 2X2', 30, 800, 1, 1), (2,'AC 3X2', 30, 700, 1, 2),(3,'Non AC 2X2', 30, 500, 2, 1), (4,'Sleeper 2X2', 30, 810, 2, 2)")
cur.execute("insert into route values (1,'bhopal',1,1,'2023-11-10',25), (1,'biawara',2,1,'2023-11-10',25) , (1,'guna',3,1,'2023-11-10',25) ")
cur.execute("insert into route values (1,'bhopal',1,1,'2023-11-11',27), (1,'biawara',2,1,'2023-11-11',27) , (1,'guna',3,1,'2023-11-11',27) ")
cur.execute("insert into route values (1,'bhopal',1,3,'2023-11-10',26), (1,'biawara',2,3,'2023-11-10',26) , (1,'guna',3,3,'2023-11-10',26) ")
cur.execute("insert into route values (1,'bhopal',1,3,'2023-11-11',24), (1,'biawara',2,3,'2023-11-11',24) , (1,'guna',3,3,'2023-11-11',24) ")
cur.execute("insert into route values (2,'guna',1,2,'2023-11-10',23) ,(2,'biawara',2,2,'2023-11-10',23) ,(2,'bhopal',3,2,'2023-11-10',23) ")
cur.execute("insert into route values (2,'guna',1,2,'2023-11-11',30) ,(2,'biawara',2,2,'2023-11-11',30) ,(2,'bhopal',3,2,'2023-11-11',30) ")
cur.execute("insert into route values (2,'guna',1,4,'2023-11-10',30) ,(2,'biawara',2,4,'2023-11-10',30) ,(2,'bhopal',3,4,'2023-11-10',30) ")

cur.execute("select * from route")
x=cur.fetchall()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class python_project:
    def main(self):
        root=Tk()
        #setting window height and width
        width=root.winfo_screenwidth()
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('Main')#title of main page

        #FRAME
        fr=Frame(root)
        fr.grid(row=0,column=0, padx=450,columnspan=3)
        #python bus image
        busImage=PhotoImage(file = 'python_bus.png')
        Label(fr, image=busImage).grid(row=0,column=1)

        #label=online bus booking system
        Label(fr, text='Online Bus Booking System',font = ('arial', 20, 'bold'), bg='LightBlue1', fg='red').grid(row=1,\
                                                                                                column=1)

        #student details
        Label(root, text='Name : Shruti Bhargava', font=('arial',12,'bold'),fg='medium blue').grid(row=2, column = 1,pady=20)
        Label(root, text='Er: 221B374', font=('arial',12, 'bold'), fg='medium blue').grid(row=3, column = 1)
        Label(root, text='Mobile : 8989591018', font=('arial',12, 'bold'), fg='medium blue').grid(row=4, column = 1,pady=20)
        Label(root, text='Submitted To : Mahesh Kumar',font = ('arial', 14, 'bold'), bg='LightBlue1', fg='red').grid(row=5,\
                                                                                                column = 1,pady=14)
        Label(root, text='Project Based Learning',font=('arial',13,'bold'),fg='red').grid(row=6, column=1)
        def direct_new_page(e=0):
            root.destroy()
            self.home()
        root.bind("<Key>",direct_new_page)
        root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def home(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('Home')#title of home page

        #FRAME
        fr=Frame(root)
        fr.grid(row=0,column=0, padx=450,pady=18,columnspan=3)
        #python bus image
        busImage=PhotoImage(file = 'python_bus.png')
        Label(fr, image=busImage).grid(row=0,column=1)

        #label=online bus booking system
        Label(fr, text='Online Bus Booking System',font = ('arial', 20, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=1)
        #defining functions
        def destroy1():
            root.destroy()
            self.seat_booking()
        def destroy2():
            root.destroy()
            self.check_booked_seat()
        def destroy3():
            root.destroy()
            self.add_bus_details()

        #BUTTONS
        Button(root, text='Seat Booking', font=('arial', 15, 'bold'), bg='green2', command=destroy1).grid(row=2,column=0) #seat booking
        Button(root, text='Check Booked Seat',font=('arial', 15, 'bold'),bg='green2', command=destroy2).grid(row=2,column=1) #check booked seat
        Button(root, text='Add Bus Details',font=('arial', 15, 'bold'),bg='green2', command=destroy3).grid(row=2,column=2) #add bus details
        Label(root, text='For Admin Only',font=('arial', 12), fg='red').grid(row=3, column=2,pady=10)
        root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

    def seat_booking(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('Seat Booking')#title of home page
         #FRAME
        fr=Frame(root)
        fr.grid(row=0,column=0, padx=450,columnspan=13)
                #python bus image
        busImage=PhotoImage(file = 'python_bus.png')
        Label(fr, image=busImage).grid(row=0,column=1)
                #label=online bus booking system
        Label(fr, text='Online Bus Booking System',font = ('arial', 18, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=1)
        Label(fr, text='Enter Jourey Details',font = ('arial', 15, 'bold'), bg='green2', fg='green4').grid(row=2,column=1, pady=10,columnspan=12)

        Label(root,text="From : ",font="Arial 11 bold").grid(row=3,column=1)
        From=Entry(root,font="Arial 11 bold",width=15)
        From.grid(row=3,column=2)
                
        Label(root,text=" ").grid(row=3,column=0)
        Label(root,text="To : ",font="Arial 11 bold").grid(row=3,column=3)
        To=Entry(root,font="Arial 11 bold",width=15)
        To.grid(row=3,column=4)
                
        Label(root,text="Journey Date : ",font="Arial 11 bold").grid(row=3,column=5)
        Date=Entry(root,font="Arial 11 bold",width=12)
        Date.grid(row=3,column=6)

        Label(root,text="Example:from",font="Arial 8 bold",fg='grey').grid(row=4,column=1,columnspan=2)
        Label(root,text="Example:to ",font="Arial 8 bold",fg='grey').grid(row=4,column=3,columnspan=2)
        Label(root,text="Example:YYYY-MM-DD",font="Arial 8 bold",fg='grey').grid(row=4,column=5,columnspan=2)

        

#---------------------------------------------------------------------------------------------------------------------------------------------------------
        def show_bus():
            from_place=From.get()
            to_place=To.get()
            journey_date=Date.get()

            from_place=from_place.lower()
            to_place= to_place.lower()


            if(len(from_place)==0 or len(to_place)==0 or len(journey_date)==0): #show error if all the details are not filled
                showerror("Error", "You have not filled all the details")
                return 1

            if(from_place==to_place):             #show error if to and from are same
                showerror("Same Record", 'You have entered same details')
                return 1

            dash=0
            for i in range(len(journey_date)):
                if (journey_date[i]=='-'):
                    dash=dash+1

            if(dash!=2):
                showerror("invalid","use '-' as YYYY-MM-DD")
                return 1

                
            split_date=journey_date.split("-")
            ly=len(split_date[0])
            lm=len(split_date[1])
            ld=len(split_date[2])
            #print(ly)
            #print(lm)
            #print(ld)

            if(ly!=4 or lm!=2 or ld!=2):
                showerror("Invalid Detail","Enter the date YYYY-MM-DD")
                return 1
            if(int(split_date[1]) >= 13):
                showerror("Invalid Detail","You have Entered Invalid Month")
                return 1
            if(int(split_date[2]) >= 32):
                showerror("Invalid Detail","You have Entered Invalid Date(DD)")
                return 1

  
           
            cur.execute("select distinct route_id from route where station_name=(?) or station_name=(?)",(from_place,to_place))
            rid=cur.fetchall()
            #print("rid")
            #print(rid)

        
            for i in range(len(rid)):
                a=rid[i][0]
                #print(a)
                cur.execute("select distinct station_id from route where station_name=(?) and route_id=(?) and running_date=(?)",(from_place,a,journey_date))
                fid=cur.fetchall()
                id1=fid[0][0]
                #print("id1")
                #print(id1)
                cur.execute("select distinct station_id from route where station_name=(?) and route_id=(?) and running_date=(?)",(to_place,a,journey_date))
                tid=cur.fetchall()
                id2=tid[0][0]
                #print("id2")
                #print(id2)

                if(id1<id2):
                    stfid=id1
                    sttid=id2
                    #print("stfid")
                    #print(stfid)
                    #print("sttid")
                    #print(sttid)
                    final_route=a

            cur.execute("select distinct route_id from route where route_id=(?) and station_name=(?) and station_id=(?)",(final_route,from_place,stfid))
            catch=cur.fetchall()
            r1=catch[0][0]
            #print("r1")
            #print(r1)

            cur.execute("select distinct route_id from route where route_id=(?) and station_name=(?) and station_id=(?)",(final_route,to_place,sttid))
            catch1=cur.fetchall()
            r2=catch1[0][0]
            #print("r2")
            #print(r2)
            
            if(r1==r2):
                final_route_id=r1
            #print("final route id")
            #print(final_route_id)


            count=0
            bus=0
            select_bus=IntVar()
            select_bus.set(0)

            
            cur.execute("select distinct bus_id from route where route_id=(?) and running_date=(?)",(final_route_id,journey_date))
            distinct_busid=cur.fetchall() #GIVES THE BUS ID WHICH RUNS ON REQUIRED ROUTE
            #print(distinct_busid)
                    
            for i in range(len(distinct_busid)):
                b=distinct_busid[i][0]
                #print(b)

                bus=bus+1
                Radiobutton(root,text="Bus"+" "+str(bus),variable=select_bus,value=b,font='arial 10 bold',bg='sky blue',indicator=0).grid(row=7+count,column=2)

                cur.execute("select op_name from operator inner join bus where bus_id = (?) and bus.op_id = operator.op_id",(b,))
                operator_name=cur.fetchall()
                Label(root, text=operator_name[0][0] ,font=('arial',10),fg='blue').grid(row=7+count,column=3)

                cur.execute("select bus_type from bus where bus_id=(?)",(b,))
                bus_type=cur.fetchall()
                Label(root, text=bus_type[0][0] ,font=('arial',10),fg='blue').grid(row=7+count,column=4)

                cur.execute("select seat_available from route where bus_id=(?) and running_date=(?)",(b,journey_date))
                seat_available=cur.fetchall()
                cur.execute("select capacity from bus where bus_id=(?)",(b,))
                bus_capacity=cur.fetchall()
                Label(root, text=str(seat_available[0][0]) + "/" + str(bus_capacity[0][0]),font=('arial',10),fg='blue').grid(row=7+count,column=5)


                cur.execute("select fare from bus where bus_id=(?)",(b,))
                bus_fare=cur.fetchall()
                Label(root, text=bus_fare[0][0],font=('arial',10),fg='blue').grid(row=7+count,column=6)
#---------------------------------------------------------------------------------------------------------------------------------------------------------


                def proceed_to_book():
                    seat=0
                    value=select_bus.get()
                    if value==0:
                        showerror("No bus selected", "Select the bus.")
                        return 1
                    
                    Label(root,text='Fill Passenger Details to book the bus ticket',font = ('arial', 14, 'bold'), bg='LightBlue1', fg='red').grid(row=10,column=3,columnspan=4,pady=15)

                    Label(root, text='Name :',font=('arial',11,'bold')).grid(row=11, column=1)#NAME
                    pass_name = Entry(root, width=18)
                    pass_name.grid(row=11, column=2)
        
                    Label(root, text='Gender :',font=('arial',11,'bold')).grid(row=11, column=3)#GENDER
                    gender=StringVar()
                    gender.set('Gender')
                    gender_option=['Male','Female','Third Gender']
                    OptionMenu(root,gender,*gender_option).grid(row=11, column=4)
                                    
                    Label(root, text='No of Seats :',font=('arial',11,'bold')).grid(row=11, column=5)#NUMBER OF SEATS
                    no_of_seats= Entry(root, width=8)
                    no_of_seats.grid(row=11, column=6)
                    
                    Label(root, text='Mobile No :',font=('arial',11,'bold')).grid(row=11, column=7)#MOBILE NUMBER
                    pass_mobile_no = Entry(root, width=18)
                    pass_mobile_no.grid(row=11, column=8 )

                    Label(root, text='Age :',font=('arial',11,'bold')).grid(row=11, column=9)#AGE
                    pass_age= Entry(root, width=6)
                    pass_age.grid(row=11, column=10)

                    #print(select_bus.get())

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
                    def book_seat():
                        
                        p_name=pass_name.get()
                        p_gender=gender.get()
                        p_seats=no_of_seats.get()
                        p_mobile_no=pass_mobile_no.get()
                        p_age=pass_age.get()

                        if(p_name.isdigit()==False):
                            showerror("Invalid Details","Name should only contain alphabets")
                            return 1

                        if(p_seats.isdigit()==False):
                            showerror("Invalid Details","No. of seats should be a number")
                            return 1
                        
                        if(int(p_age) <= 0):
                            showerror("Invalid Details","Age can neither be negative nor Zero")
                            return 1
                        
                        if(len(p_name)==0 or len(p_gender)==0 or len(p_seats)==0 or len(p_mobile_no)==0 or len(p_age)==0):
                            showerror("Incomplete Information", "Kindly fill all the details.")
                            return 1

                        if(int(p_seats)>seat_available[0][0]):
                            showerror("Not Available", "Seats are not available")
                            return 1

                        if(len(p_mobile_no)!=10):
                            showerror("Invalid Number", "Please enter correct mobile number")
                            return 1

                        cur.execute("select Mobile_number,boarding_point,destination_point from passenger")
                        distinct_mobile_no = cur.fetchall()
                        for i in range(len(distinct_mobile_no)):
                            if((distinct_mobile_no[i][0] == int(p_mobile_no)) and (distinct_mobile_no[i][1]==from_place) and (distinct_mobile_no[i][2]==to_place)):
                                showerror("Already Booked", "Ticket is booked with this Mobile No.")
                                return 1
                            
                        selected_bus_id=select_bus.get()
                        cur.execute("select fare from bus where bus_id=(?)",(selected_bus_id,))
                        fare_per_seat=cur.fetchall()
                        #print(fare_per_seat[0][0])
                        total_fare= (fare_per_seat[0][0]) * int(p_seats)
                        #print(total_fare)

                        booked_on_date = date.today()
                        #print(booked_on_date)

                        cur.execute("select op_name from operator cross join bus where bus_id = (?) and bus.op_id = operator.op_id",(selected_bus_id,))
                        oper_name=cur.fetchall()
                        

                        QUE=askyesno('FARE CONFIRM',("Total Amount To Be Paid is Rs. " + str(total_fare)))
                        if(QUE):
                            cur.execute("insert into passenger(Booking_ref,name,gender,No_of_seats,Mobile_number,Age,Fare,bus_details,travel_on_date,booked_on_date,boarding_point,destination_point) values (?,?,?,?,?,?,?,?,?,?,?,?)",(selected_bus_id , p_name, p_gender,p_seats, p_mobile_no, p_age, total_fare,oper_name[0][0], journey_date, booked_on_date, from_place, to_place))
                            #cur.execute("select * from passenger")
                            #passenger_detail=cur.fetchall()
                            #print(passenger_detail)

                            #print(final_route_id)
                            #print(selected_bus_id)
                            #print(journey_date)
                            cur.execute("select * from route where route_id=(?) and bus_id=(?)and running_date=(?)",(final_route_id,selected_bus_id,journey_date))
                            rd=cur.fetchall()
                            #print(rd)

                            cur.execute("select distinct station_id from route where route_id=(?) and bus_id=(?)and running_date=(?)",(final_route_id,selected_bus_id,journey_date))
                            z=cur.fetchall()
                            z_len=len(z)

                            if(z_len==sttid):
                                for i in range(stfid,sttid+1):
                                    #print(i)
                                    #print("inside if")
                                    cur.execute("select seat_available from route where route_id=(?) and bus_id=(?) and running_date=(?) and station_id=(?)",(final_route_id,selected_bus_id,journey_date,i))
                                    s1=cur.fetchall()
                                    updated_seat = s1[0][0] - int(p_seats)
                                    #print("seat avail = " + str(seat_available[0][0]))
                                    #print("p_seat = " + p_seats)
                                    #print("updated = " + str(updated_seat))
                                    cur.execute("update route set seat_available=(?) where route_id=(?) and bus_id=(?) and running_date=(?) and station_id=(?)",(updated_seat,final_route_id,selected_bus_id,journey_date,i))
                            else:                                    
                                for i in range(stfid,sttid):
                                    #print(i)
                                    #print("inside else")
                                    cur.execute("select seat_available from route where route_id=(?) and bus_id=(?) and running_date=(?) and station_id=(?)",(final_route_id,selected_bus_id,journey_date,i))
                                    s1=cur.fetchall()
                                    updated_seat = s1[0][0] - int(p_seats)
                                    #print("seat avail = " + str(seat_available[0][0]))
                                    #print("p_seat = " + p_seats)
                                    #print("updated = " + str(updated_seat))
                                    cur.execute("update route set seat_available=(?) where route_id=(?) and bus_id=(?) and running_date=(?) and station_id=(?)",(updated_seat,final_route_id,selected_bus_id,journey_date,i))
                            
                            cur.execute("select * from route where route_id=(?) and bus_id=(?)and running_date=(?)",(final_route_id,selected_bus_id,journey_date))
                            rd1=cur.fetchall()
                            #print(rd1)
                                
                            con.commit()
                            root.destroy()
                            self.ticket()

                    Button(root,text='Book Seat',font="Arial 11 bold", bg='green2',command=book_seat).grid(row=11,column=11)


                if(seat_available[0][0] != 0):    
                    Button(root, text='Proceed to Book',font="Arial 9 bold", bg='green2',command=proceed_to_book).grid(row=7+count, column=7,columnspan=2)#PROCEED TO BOOK BUTTON
                count=count+1
               
                        
           
            Label(root, text='Select Bus',font=('arial',11),fg='green4').grid(row=5,column=2)
            Label(root, text='Operator',font=('arial',11),fg='green4').grid(row=5,column=3)
            Label(root, text='Bus Type',font=('arial',11),fg='green4').grid(row=5,column=4)
            Label(root, text='Available  Capacity',font=('arial',11),fg='green4').grid(row=5,column=5)
            Label(root, text='Fare',font=('arial',11),fg='green4').grid(row=5,column=6)
            Label(root, text=' ').grid(row=5,column=0)

        Button(root, text='Show Bus',font="Arial 11 bold", bg='green2',command=show_bus).grid(row=3, column=7)#SHOW BUS BUTTON

        def back_to_home():#Function to go back to home page
            root.destroy()
            self.home()
        Button(root, text= 'Home',font="Arial 11 bold", command=back_to_home).grid(row=3,column=8)# back to home page button

        root.mainloop()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def ticket(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('Ticket')#title of home page
        #FRAME
        fr=Frame(root)
        fr.grid(row=0,column=0, padx=450,columnspan=3)
        #python bus image
        busImage=PhotoImage(file = 'python_bus.png')
        Label(fr, image=busImage).grid(row=0,column=1)

        #label=online bus booking system
        Label(fr, text='Online Bus Booking System',font = ('arial', 18, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=1)
        Label(fr, text='Bus Ticket',font = ('arial', 14,'bold'),fg='blue').grid(row=2,column=1)

        
        cur.execute("select * from passenger")
        detail_passen=cur.fetchall()
        l=len(detail_passen)

        # 0-busId,1-Name,2-gender,3-no.of seats, 4-mobile no., 5-age, 6-fare, 7-op_name, 8-travel date, 9-booked date, 10-from place, 11-to place
        frame=Frame(root,relief="ridge",bd=8)
        frame.grid(row=1,column=0,columnspan=1,padx=450)
        Label(root,text=" ").grid(row=4,column=0)
        Label(frame,text="Passengers : " + detail_passen[l-1][1],font="Arial 15 bold").grid(row=5,column=0,columnspan=3)
        Label(frame,text="No. of seats : " + str(detail_passen[l-1][3]) ,font="Arial 15 bold").grid(row=8,column=0)
        Label(frame,text="Phone : "+ str(detail_passen[l-1][4]),font="Arial 15 bold").grid(row=6,column=0)
        Label(frame,text="Age : " + str(detail_passen[l-1][5]),font="Arial 15 bold").grid(row=6,column=1)
        Label(frame,text="Bus Id : " + str(detail_passen[l-1][0]),font="Arial 15 bold").grid(row=7,column=0)
        Label(frame,text="Fare Rs : " + str(detail_passen[l-1][6]),font="Arial 15 bold").grid(row=8,column=1)
        Label(frame,text="Travel On : " + detail_passen[l-1][8],font="Arial 15 bold").grid(row=9,column=0)
        Label(frame,text="Booked On : " + detail_passen[l-1][9],font="Arial 15 bold").grid(row=9,column=1)
        Label(frame,text="Bus Details : "+ detail_passen[l-1][7],font="Arial 15 bold").grid(row=7,column=1)
        Label(frame,text="To : "+ detail_passen[l-1][11],font="Arial 15 bold").grid(row=10,column=1)
        Label(frame,text="From : "+ detail_passen[l-1][10],font="Arial 15 bold").grid(row=10,column=0)
        Label(frame,text="*Total amount Rs "+ str(detail_passen[l-1][6]) +" to be paid at the time of boarding the bus",font="Arial 12 italic",).grid(row=14,column=0,columnspan=3)
        Label(frame,text=" ").grid(row=15,column=0)
        showinfo("Success" , "Seat Booked...")
        def confirm_exit():
            ans=askyesnocancel(title='Exit',message='Exit: Yes \nHome: No \nRemain here: Cancel ')
            if ans==False:#no
                root.destroy()
                self.home()
            elif(ans):#yes
                showinfo("Thanks" , "Thank You for using Python bus service")
                root.destroy()
            
                
        root.protocol("WM_DELETE_WINDOW",confirm_exit)
        root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def check_booked_seat(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('Check Booked Seat')#title of home page
        #python bus image
        img=PhotoImage(file='.\\python_bus.png')#ADD BUS IMAGE
        Label(root,image=img).grid(row=0,column=0,padx=width//2.8,columnspan=width//50)
        #label=online bus booking system
        Label(root,text="Online Bus Booking System",font = ('arial', 18, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=0,columnspan=width//50)
        Label(root,text="Check Your Booking",font="Arial 14 bold",fg="Green",bg="Light Green").grid(row=3,column=0,columnspan=width//50,pady=7)

        Label(root,text=" ").grid(row=5,column=0,padx=width//7.9)
        Label(root,text="Enter your mobile number :",font="bold 11 bold").grid(row=5,column=1)
        mobile_number=Entry(root,font=" Arial 11 bold",width=15)
        mobile_number.grid(row=5,column=2)
#---------------------------------------------------------------------------------------------------------------------------------------------------------
      
        def check_booking():
            
            check_mobile=mobile_number.get()
            if(len(check_mobile)==0):
                showerror("Invalid", "Enter the mobile number!")
                return 1
            if(len(check_mobile)!=10):
                showerror("Invalid", "Incorrect mobile number")
                
            if(check_mobile.isdigit()==False):
                showerror("Invalid Details","Mobile number should be a number")
                return 1
            
            cur.execute("select Mobile_number from passenger")
            all_mobile_passen=cur.fetchall()
            present=0
            for k in range(len(all_mobile_passen)):
                if(int(check_mobile) in all_mobile_passen[k]):
                    present+=1

            if(present==0):
                ans=askyesno("NO DATA", "There is no ticket booked with this number. \nDo you want to book now?")
                if(ans):
                    root.destroy()
                    self.seat_booking()
                else:
                    root.destroy()
                    self.check_booked_seat()

            
            if(present!=0):
                cur.execute("select * from passenger where Mobile_number=(?)",(check_mobile,))
                detail_passen=cur.fetchall()
                l=len(detail_passen)
            
            Label(root,text=" ").grid(row=6,column=0)#CREATE SPACE BETWEEN ROWS
            Label(root,text=" ").grid(row=7,column=0)#CREATE SPACE BETWEEN ROWS
            frame=Frame(root,relief="ridge",bd=8)#CAN ALSO USE GROOVE OR RAISED INSTEAD OF RIDGE
            frame.grid(row=8,column=0,columnspan=width//50)



            Label(frame,text="Passengers : " + detail_passen[0][1],font="Arial 15 bold").grid(row=8,column=0,columnspan=3)
            Label(frame,text="Phone : "+ str(detail_passen[0][4]),font="Arial 15 bold").grid(row=9,column=0)
            Label(frame,text="Age : " + str(detail_passen[0][5]),font="Arial 15 bold").grid(row=9,column=1)
            Label(frame,text="Bus Id : " + str(detail_passen[0][0]),font="Arial 15 bold").grid(row=10,column=0)
            Label(frame,text="Bus Details : "+ detail_passen[0][7],font="Arial 15 bold").grid(row=10,column=1)
            Label(frame,text="No. of seats : " + str(detail_passen[0][3]) ,font="Arial 15 bold").grid(row=11,column=0)
            Label(frame,text="Fare Rs : " + str(detail_passen[0][6]),font="Arial 15 bold").grid(row=11,column=1)
            Label(frame,text="Travel On : " + detail_passen[0][8],font="Arial 15 bold").grid(row=12,column=0)
            Label(frame,text="Booked On : " + detail_passen[0][9],font="Arial 15 bold").grid(row=12,column=1)
            Label(frame,text="To : "+ detail_passen[0][11],font="Arial 15 bold").grid(row=13,column=1)
            Label(frame,text="From : "+ detail_passen[0][10],font="Arial 15 bold").grid(row=13,column=0)
            Label(frame,text="*Total amount Rs "+ str(detail_passen[0][6]) +" to be paid at the time of boarding the bus",font="Arial 12 italic",).grid(row=14,column=0,columnspan=3)
            Label(frame,text=" ").grid(row=15,column=0)

        
        Button(root, text='Check Booking',command=check_booking,font="Arial 8 bold").grid(row=5,column=3)#button to search for ticket using mobile number
        
        def back_to_home():#Function to go back to home page
            root.destroy()
            self.home()
        Button(root, text= 'Home',font="Arial 8 bold", command=back_to_home).grid(row=5,column=4)# back to home page button
        
        root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def add_bus_details(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('Add Bus Details')#title of home page

        #python bus image
        for i in range(4):
            Label(root, text=" ").grid(row=0, column=i, padx=47)
        busImage=PhotoImage(file = 'python_bus.png')
        Label(root, image=busImage).grid(row=0,column=4,columnspan=4)
        #label=online bus booking system
        Label(root, text='Online Bus Booking System',font = ('arial',19, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=4,columnspan=4)
        Label(root, text='Add New Details To Database',font = ('arial', 14, 'bold'), fg='green4', borderwidth=1,relief="solid").grid(row=2,column=4, pady=17,columnspan=4)


        def destroy1():  #DESTROY THE CURRENT PAGE AND OPEN THE NEXT PAGE
            root.destroy()
            self.new_operator()
        def destroy2():
            root.destroy()
            self.new_bus()
        def destroy3():
            root.destroy()
            self.new_route()
        def destroy4():
            root.destroy()
            self.new_run()


        for i in range(4):
            Label(root, text=" ").grid(row=3, column=i)
        Button(root, text='New Operator', bg='green2',font = ('arial',12, 'bold'),command=destroy1).grid(row= 3, column=4,pady=10)
        Button(root, text='New Bus', bg='orange',width=12,font = ('arial',12, 'bold'),command=destroy2).grid(row=3 , column= 5,padx=20)
        Button(root, text='New Route', bg='sky blue',width=12,font = ('arial',12, 'bold'),command=destroy3).grid(row=3 , column= 6)
        Button(root, text='New Run', bg='brown2',width=12,font = ('arial',12, 'bold'),command=destroy4).grid(row=3, column=7,padx=20)

        def back_to_home():#Function to go back to home page
            root.destroy()
            self.home()
        Button(root, text= 'Home',font="Arial 11 bold", command=back_to_home).grid(row=3,column=8)# back to home page button
        
        root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def new_operator(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('New Operator')#title of home page
        #FRAME
        fr=Frame(root)
        fr.grid(row=0,column=0, padx=450,columnspan=15)
        #python bus image
        busImage=PhotoImage(file = 'python_bus.png')
        Label(fr, image=busImage).grid(row=0,column=1)
        #label=online bus booking system
        Label(fr, text='Online Bus Booking System',font = ('arial', 14, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=1)
        Label(fr, text='Add Bus Operator Details',font = ('arial', 14, 'bold'), fg='green4', borderwidth=1,relief="solid").grid(row=2,column=1, pady=17)

        #INPUT DETAILS   
        Label(root, text='Operator id :',font=('arial',12)).grid(row=1, column=0) #OPERATOR ID
        op_id = Entry(root, width=6)
        op_id.grid(row=1, column=1)
        
        Label(root, text='Name :',font=('arial',12)).grid(row=1, column=2)#NAME
        op_name = Entry(root, width=15)
        op_name.grid(row=1, column=3)

        Label(root, text='Address :',font=('arial',12)).grid(row=1, column=4)#ADDRESS
        op_address = Entry(root, width=15)
        op_address.grid(row=1, column=5)

        Label(root, text='Phone :',font=('arial',12)).grid(row=1, column=6)#PHONE
        op_phone= Entry(root, width=15)
        op_phone.grid(row=1, column=7)

        Label(root, text='Email :',font=('arial',12)).grid(row=1, column=8)#EMAIL
        op_email = Entry(root, width=15)
        op_email.grid(row=1, column=9)

        ################### FUNCTION- ADD and EDIT  #####################
        def operator_add():
            opid=op_id.get()
            opname=op_name.get()
            opaddress=op_address.get()
            opphone=op_phone.get()
            opemail=op_email.get()
            if(len(opid)==0 or len(opname)==0 or len(opaddress)==0 or len(opphone)==0 or len(opemail)==0):
                showerror("Incomplete Information","Kindly fill all the feilds")
                return 1
##            if(len(opphone)!=10):
##                showerror("Invalid Details", "Enter the correct mobile number")
##                return 1
            
            cur.execute("select * from operator")
            op=cur.fetchall()
            for i in range(len(op)):
                if(int(opid)==op[i][0] or opname==op[i][1] or opaddress==op[i][2] or int(opphone)== op[i][3] or opemail==op[i][4]):
                    showerror("DUPLICATE DATA","Data Already Exists.....")
                    return 1

            cur.execute("insert into operator(op_id, op_name, op_address, op_phone, op_email) values (?,?,?,?,?)",(opid,opname,opaddress,opphone,opemail))
            cur.execute("select * from operator where op_id=(?)",(opid,))
            catch=cur.fetchall()
            Label(root,text=catch[0],font="Arial 12 bold",fg='gray46').grid(row=3,column=0,columnspan=13)
            showinfo ("Operator Entry","Operator Added Successfully...")

            con.commit()

            
        def operator_edit():
            opid=op_id.get()
            opname=op_name.get()
            opaddress=op_address.get()
            opphone=op_phone.get()
            opemail=op_email.get()
            if(len(opid)==0 or len(opname)==0 or len(opaddress)==0 or len(opphone)==0 or len(opemail)==0):
                showerror("Incomplete Information","Kindly fill all the feilds")
                return 1
            cur.execute("select distinct(op_id) from operator")
            op=cur.fetchall()
            not_exist=0

            
            for i in range(len(op)):
                if(int(opid) in op[i]):
                    not_exist+=1
            if(not_exist==0):
                showerror("NO DATA FOUND","No data exists...")
                return 1
            else:
                cur.execute("update operator set op_id=(?) , op_name=(?), op_address=(?), op_phone=(?), op_email=(?) where op_id=(?)",(opid,opname,opaddress,opphone,opemail,opid))
                cur.execute("select * from operator where op_id=(?)",(opid,))
                catch=cur.fetchall()
                Label(root,text=catch[0],font="Arial 12 bold",fg='gray46').grid(row=3,column=0,columnspan=13)
                showinfo ("Operator Entry Updated","Operator updated Successfully...")

                con.commit()


        Button(root, text='Add',font=('arial',11,'bold'),bg='green2',command=operator_add).grid(row=1, column=10) #ADD BUTTON
        Button(root, text='Edit',font=('arial',11,'bold'),bg='green2',command=operator_edit).grid(row=1, column=11) #EDIT BUTTON
        def back_to_home():#Function to go back to home page
                root.destroy()
                self.add_bus_details()
        Button(root, text= 'Back',font="Arial 11 bold", command=back_to_home).grid(row=1,column=12)# back to home page button
        root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def new_bus(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('New Bus')#title of home page
        #FRAME
        fr=Frame(root)
        fr.grid(row=0,column=0, padx=450,columnspan=15)
        #python bus image
        busImage=PhotoImage(file = 'python_bus.png')
        Label(fr, image=busImage).grid(row=0,column=1)
        #label=online bus booking system
        Label(fr, text='Online Bus Booking System',font = ('arial', 14, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=1)
        Label(fr, text='Add Bus Details',font = ('arial', 14, 'bold'), fg='green4', borderwidth=1,relief="solid").grid(row=2,column=1, pady=17)
        #INPUT DETAILS   
        Label(root, text='Bus Id :',font=('arial',12)).grid(row=1, column=0) #OPERATOR ID
        bus_id = Entry(root, width=6)
        bus_id.grid(row=1, column=1)
        
        Label(root, text='Bus Type :',font=('arial',12)).grid(row=1, column=2)#NAME
        bus_type = StringVar()
        bus_type.set('Bus Type')
        bus_type_option=['AC 2X2', 'AC 3X2', 'Non AC 2X2' ,'Non AC 3X2' ,'AC Sleeper 2X1' ,'Non-AC Sleeper 2X1']
        OptionMenu(root,bus_type,*bus_type_option).grid(row=1, column=3)


        Label(root, text='Capacity :',font=('arial',12)).grid(row=1, column=4)#ADDRESS
        bus_capacity = Entry(root, width=15)
        bus_capacity.grid(row=1, column=5)

        Label(root, text='Fare Rs :',font=('arial',12)).grid(row=1, column=6)#PHONE
        bus_fare= Entry(root, width=15)
        bus_fare.grid(row=1, column=7)

        Label(root, text='Operator Id :',font=('arial',12)).grid(row=1, column=8)#EMAIL
        bus_op_id = Entry(root, width=15)
        bus_op_id.grid(row=1, column=9)
        
        Label(root, text='Route Id :',font=('arial',12)).grid(row=1, column=10)#EMAIL
        bus_route_id = Entry(root, width=15)
        bus_route_id.grid(row=1, column=11)

        ################### FUNCTION- ADD and EDIT  #####################
        def bus_add():
            busid = bus_id.get()
            bustype = bus_type.get()
            buscapa = bus_capacity.get()
            busfare = bus_fare.get()
            busOpId = bus_op_id. get()
            busRouteId = bus_route_id.get()
            if(len(busid)==0 or len(bustype)==0 or len(buscapa)==0 or len(busfare)==0 or len(busOpId)==0 or len(busRouteId)==0):
                showerror("Incomplete information", "Kindly fill all the feilds")
                return 1
            
            if(buscapa.isdigit()==False):
                showerror("Invalid details", "Capacity should be a number")
                return 1
            
            cur.execute("select distinct(bus_id) from bus")
            bus=cur.fetchall()
            for i in range(len(bus)):
                #print("i" + str(i))
                if(int(busid)==bus[i][0]):
                    showerror("Duplicate Entry","Data already exists..")
                    return 1
                
            cur.execute("select distinct(op_id) from operator")
            avail_opId=cur.fetchall()
            opid_present=0
            for i in range(len(avail_opId)):
                if(int(busOpId)==avail_opId[i][0]):
                    opid_present+=1
            if(opid_present==0):
                ans=askyesno("No Record", "This operator does not exist.\nDo you want to add operator?")
                if(ans):
                    root.destroy()
                    self.new_operator()

            cur.execute("select distinct(route_id) from route")
            avail_routeId=cur.fetchall()
            routeid_present=0
            for i in range(len(avail_routeId)):
                if(int(busRouteId)==avail_routeId[i][0]):
                    routeid_present+=1
            if(routeid_present!=0):
                ans=askyesno("No Record", "This route does not exist.\nDo you want to add route?")
                if(ans):
                    root.destroy()
                    self.new_route()
                        
            cur.execute("insert into bus(bus_id,bus_type,capacity,fare,op_id,route_id) values(?,?,?,?,?,?)", (busid,bustype,buscapa,busfare,busOpId,busRouteId))
            cur.execute("select * from bus where bus_id=(?)",(busid,))
            added_bus=cur.fetchall()
            Label(root,text= added_bus[0],font="Arial 12 bold",fg='gray46').grid(row=21,column=0,columnspan=13)
            showinfo ("Bus Entry","Bus Details Added Successfully. ")
            con.commit()
#---------------------------------------------------------------------------------------------------------------------------------------------------------
            
            
        def bus_edit():
            busid = bus_id.get()
            bustype = bus_type.get()
            buscapa = bus_capacity.get()
            busfare = bus_fare.get()
            busOpId = bus_op_id.get()
            busRouteId = bus_route_id.get()

            busid, bustype,buscapa,busfare,busOpId,busRouteId
            if(len(busid)==0 or len(bustype)==0 or len(buscapa)==0 or len(busfare)==0 or len(busOpId)==0 or len(busRouteId)==0):
                showerror("Incomplete information", "Kindly fill all the feilds")
                return 1
            if(buscapa.isdigit()==False):
                showerror("Invalid details", "Capacity should be a number")
                return 1

            cur.execute("select distinct(op_id) from operator")
            avail_opId=cur.fetchall()
            opid_present=0
            for i in range(len(avail_opId)):
                if(int(busOpId)==avail_opId[i][0]):
                    opid_present+=1
            if(opid_present!=0):
                ans=askyesno("No Record", "This operator does not exist.\nDo you want to add operator?")
                if(ans):
                    root.destroy()
                    self.new_operator()
                    return 1

            cur.execute("select distinct(route_id) from route")
            avail_routeId=cur.fetchall()
            routeid_present=0
            for i in range(len(avail_routeId)):
                if(int(busRouteId)==avail_routeId[i][0]):
                    routeid_present+=1
            if(routeid_present!=0):
                ans=askyesno("No Record", "This route does not exist.\nDo you want to add route?")
                if(ans):
                    root.destroy()
                    self.new_route()
        


            
            
            cur.execute("select distinct(bus_id) from bus")
            bus=cur.fetchall()
            not_exist=0
            for i in range(len(bus)):
                if(int(busid) in bus[i]):
                    not_exist+=1
            if(not_exist==0):
                showerror("NO DATA FOUND","No data exists...")
                return 1
            else:
                cur.execute("update bus set bus_id=(?),bus_type=(?),capacity=(?),fare=(?),op_id=(?),route_id=(?)",(busid, bustype,buscapa,busfare,busOpId,busRouteId))
                cur.execute("select * from bus where bus_id=(?)",(busid,))
                catch=cur.fetchall()
                Label(root,text = str(catch[0][0])+','+str(catch[0][1])+', '+str(catch[0][3])+', '+str(catch[0][4])+', '+str(catch[0][2])+', '+str(catch[0][5]),font="Arial 12 bold",fg='gray46').grid(row=21,column=0,columnspan=13)
                showinfo ("Bus Entry Update ","Bus  Updated Successfully...")
                return 1
            con.commit()
 
        Button(root, text='Add Bus',font=('arial',10,'bold'),bg='green2',command=bus_add ).grid(row=20, column=8) #ADD BUTTON
        Button(root, text='Edit Bus',font=('arial',10,'bold'),bg='green2',command=bus_edit).grid(row=20, column=9) #EDIT BUTTON
        def back_to_home():#Function to go back to home page
                root.destroy()
                self.add_bus_details()
        Button(root, text= 'Back',font="Arial 10 bold", command=back_to_home).grid(row=20,column=10)# back to home page button
        root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def new_route(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('New Route')#title of home page
        #FRAME
        fr=Frame(root)
        fr.grid(row=0,column=0, padx=450,columnspan=15)
        #python bus image
        busImage=PhotoImage(file = 'python_bus.png')
        Label(fr, image=busImage).grid(row=0,column=1)
        #label=online bus booking system
        Label(fr, text='Online Bus Booking System',font = ('arial', 14, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=1)
        Label(fr, text='Add Bus Route Details',font = ('arial', 14, 'bold'), fg='green4', borderwidth=1,relief="solid").grid(row=2,column=1, pady=17)

        Label(root, text='Route Id :',font=('arial',12)).grid(row=1, column=0)#EMAIL
        new_route_id = Entry(root, width=15)
        new_route_id.grid(row=1, column=1)

        Label(root, text='Station Name:',font=('arial',12)).grid(row=1, column=2)#NAME
        station_name = Entry(root, width=15)
        station_name.grid(row=1, column=3)

        Label(root, text='Station Id :',font=('arial',12)).grid(row=1, column=4)#NAME
        station_id = Entry(root, width=15)
        station_id.grid(row=1, column=5)

        def add_route():
            route_id = new_route_id.get()
            st_name = station_name.get()
            st_id = station_id.get()
            

            #print(route_id)
            #print(st_name)
            #print(st_id)
        

            if(len(route_id)==0 or len(st_name)==0 or len(st_id)==0):
                showerror("INCOMPLETE","You have not filled all fields")
                return 1
            cur.execute("select distinct(route_id),station_name , station_id from route")
            catch=cur.fetchall()
            count=0
            
            #print("-----------------")
            #print(catch)
            
            for i in range(len(catch)):
                if(int(route_id)==catch[i][0] and st_name==catch[i][1] and (int(st_id)==catch[i][0])):
                    count+=1
            if(count!=0):
                showerror("DUPLICATE DATA","This route id already exists....")
                return 1
            else:
                cur.execute("insert into route(route_id,station_name,station_id,bus_id,running_date,seat_available) values(?,?,?,NULL,NULL,NULL)",(route_id,st_name,st_id))

                
                cur.execute("select route_id,station_name,station_id from route where route_id=(?) and station_name=(?)",(route_id,st_name))
                catchbus=cur.fetchall()
                Label(root,text = str(catchbus[0][0])+','+str(catchbus[0][1])+', '+str(catchbus[0][2]),font="Arial 12 bold",fg='gray46').grid(row=21,column=0,columnspan=13)
                showinfo("Route Added","New Route Added Successfully....")
                con.commit()

            #cur.execute("select * from route")
            #catchdisplay1=cur.fetchall()    
            #cur.execute("select * from route where bus_id is NULL")
            #catchdisplay=cur.fetchall()
            #print(catchdisplay1)
            #print("-----------------")
            #print(catchdisplay)
                
        def delete_route():
            route_id = new_route_id.get()
            st_name = station_name.get()
            st_id = station_id.get()
            

            if(len(route_id)==0 or len(st_name)==0 or len(st_id)==0):
                showerror("INCOMPLETE","You have not filled all fields")
                return 1
            
            cur.execute("select distinct(route_id) from route")
            catch1=cur.fetchall()
            count_route=0
            for i in range(len(catch1)):
                if(int(route_id) in catch1[i]):
                    count_route+=1

            cur.execute("select distinct(station_name) from route")
            catch1=cur.fetchall()
            count_st=0
            for i in range(len(catch1)):
                if(st_name in catch1[i]):
                    count_st+=1

            cur.execute("select distinct(station_id) from route")
            catch1=cur.fetchall()
            count_st_id=0
            for i in range(len(catch1)):
                if(int(st_id) in catch1[i]):
                    count_st_id+=1

            
            if(count_route!=0 and count_st!=0 and count_st_id!=0):
                    cur.execute("delete from route where route_id=(?) and station_name=(?) and station_id=(?)",(route_id,st_name,st_id))
                    #cur.execute("delete from route where route_id=(?) and station_name=(?) and station_id=(?)",(route_id,st_to,st_to_id))

            else:
                showerror("NOT EXISTS","This run does not exists....")
                return 1
            con.commit()
            
            showinfo ("Route Deletion","Route Record Deleted Successfully...")

        Button(root, text='Add Route',font=('arial',10,'bold'),bg='green2',command=add_route).grid(row=1, column=10) #ADD BUTTON
        Button(root, text='Delete Route',font=('arial',10,'bold'),bg='green2',command=delete_route).grid(row=1, column=11) #EDIT BUTTON
        
        def back_to_home():#Function to go back to home page
                root.destroy()
                self.add_bus_details()
        Button(root, text= 'Back',font="Arial 10 bold", command=back_to_home).grid(row=1,column=12)# back to home page button
        
        root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
    def new_run(self):
        root=Tk()
        width=root.winfo_screenwidth()#setting window height and width
        height=root.winfo_screenheight()
        root.geometry("%dx%d"%(width,height))
        root.title('New Run')#title of home page
        #FRAME
        fr=Frame(root)
        fr.grid(row=0,column=0, padx=450,columnspan=15)
        #python bus image
        busImage=PhotoImage(file = 'python_bus.png')
        Label(fr, image=busImage).grid(row=0,column=1)
        #label=online bus booking system
        Label(fr, text='Online Bus Booking System',font = ('arial', 14, 'bold'), bg='LightBlue1', fg='red').grid(row=1,column=1)
        Label(fr, text='Add Bus Running Details',font = ('arial', 14, 'bold'), fg='green4', borderwidth=1,relief="solid").grid(row=2,column=1, pady=17)
        
        Label(root, text='Bus Id :',font=('arial',12)).grid(row=1, column=3)#EMAIL
        new_run_bus_id = Entry(root, width=6)
        new_run_bus_id.grid(row=1, column=4)

        Label(root, text='Route Id :',font=('arial',12)).grid(row=1, column=5)#EMAIL
        new_run_bus_route_id = Entry(root, width=6)
        new_run_bus_route_id.grid(row=1, column=6)

        Label(root, text='Seat Available :',font=('arial',12)).grid(row=1, column=7)#EMAIL
        new_run_seat_avail = Entry(root, width=15)
        new_run_seat_avail.grid(row=1, column=8)
        
        Label(root, text='Running Date :',font=('arial',12)).grid(row=1, column=9)#NAME
        new_run_running_data = Entry(root, width=15)
        new_run_running_data.grid(row=1, column=10)



        def add_run():
            #cur.execute("select * from route")
            #se=cur.fetchall()
            #print(se)
            #print("---------------------------------------------------------------")
            

            
            bid=new_run_bus_id.get()
            brouteid = new_run_bus_route_id.get()
            bseat=new_run_seat_avail.get()
            brun=new_run_running_data.get()
            if(len(bid)==0 or len(brouteid)==0 or len(bseat)==0 or len(brun)==0):
                showerror("Incomplete Information", "Kindly fill all the details")
                return 1
            
            cur.execute("select distinct(bus_id),route_id,running_date from route")
            catch=cur.fetchall()
            #print(catch)
            for i in range(len(catch)):
                if(int(bid)==catch[i][0] and int(brouteid)==catch[i][1] and brun==catch[i][2]):
                    showerror("DUPLICATE ERROR","This bus run already exists.....")
                    return 1
            if(bid.isdigit()==False):
                showerror("Invalid", "Bus id is numeric..")
                return 1
            

            a=0
            cur.execute("select distinct(bus_id) from bus")
            catch1=cur.fetchall()
            for i in range(len(catch1)):
                if(int(bid)==catch1[i][0]):
                    a=a+1
            if(a==0):
                ans=askyesno("Bus Error", "bus id does not exist.\nDo you want to add bus?")
                if(ans):
                    root.destroy()
                    self.new_bus()
                else:
                    return 1

            
            b=0
            cur.execute("select distinct(route_id) from route")
            catch2=cur.fetchall()
            for i in range(len(catch2)):
                if(int(brouteid)==catch2[i][0]):
                    b=b+1
            if(b==0):
                ans1=askyesno("Route Error","This route does not exits.\nDo you want to add route")
                if(ans1):
                    root.destroy()
                    self.new_route()
                else:
                    return 1

            cur.execute("select * from route where bus_id is NULL and route_id=(?)",(brouteid,))
            empty_tuple=cur.fetchall()
            print(empty_tuple)
            l_empty_tuple = len(empty_tuple)
            if(l_empty_tuple!=0):#if no bus is running on this route
                print("inside - if")
                for i in range(l_empty_tuple):
                    cur.execute("update route set bus_id=(?),running_date=(?),seat_available=(?) where route_id=(?)",(bid,brun,bseat,brouteid))
                
            else:###if you want to run a exisiting bus on existing route on another date also
                print("inside else")
                cur.execute("select distinct station_name,station_id from route where route_id=(?)",(brouteid,))
                st=cur.fetchall()
                #print(st)
                for i in range(len(st)):
                    stname=st[i][0]
                    stid=st[i][1]
                    #print(stname + " " + str(stid))
                    cur.execute("insert into route(route_id,station_name,station_id,bus_id,running_date,seat_available) values(?,?,?,?,?,?)",(brouteid,stname,stid,bid,brun,bseat))
           
            Label(root,text=' ').grid(row=11,column=0)
            Label(root,text=bid +', '+ brouteid +', ' + bseat+', ' + brun ,font="Arial 12 bold",fg='gray64').grid(row=10,column=0,columnspan=14)
                
            showinfo("New Run","New Run Added Successfully...")
            con.commit()
       
        def delete_run():
            bid=new_run_bus_id.get()
            brouteid = new_run_bus_route_id.get()
            bseat=new_run_seat_avail.get()
            brun=new_run_running_data.get()
            
            if(len(bid)==0 or len(brouteid)==0 or len(bseat)==0 or len(brun)==0):
                showerror("Incomplete Information", "Kindly fill all the details")
            else:
                cur.execute("Select distinct(route_id) from route ")
                catch_3=cur.fetchall()
                count_1=0
                for i in range(len(catch_3)):
                    if( int(brouteid) in catch_3[i]):
                        count_1+=1
                    
                cur.execute("Select distinct(running_date) from route ")
                catch_3=cur.fetchall()
                count_2=0
                for i in range(len(catch_3)):
                    if( brun in catch_3[i]):
                        count_2+=1
                    
                cur.execute("Select distinct(seat_available) from route")
                catch_3=cur.fetchall()
                count_3=0
                for i in range(len(catch_3)):
                    if( int(bseat) in catch_3[i]):
                        count_3+=1
                    
                cur.execute("Select distinct(bus_id) from route ")
                catch_3=cur.fetchall()
                count_4=0
                for i in range(len(catch_3)):
                    if( int(bid) in catch_3[i]):
                        count_4+=1

                if(count_1!=0 and count_2!=0 and count_3!=0 and count_4!=0):
                    cur.execute("delete from route where route_id=(?) and bus_id=(?) and seat_available=(?) and running_date=(?)",(brouteid,bid,bseat,brun))
                else:
                    showerror("NOT EXISTS","This run does not exists....")
                    return 1
                con.commit()
                
                cur.execute("select * from route")
                updated=cur.fetchall()
                print(updated)
                
                Label(root,text=' ').grid(row=11,column=0)
                showinfo ("Run Deletion","Run Record Deleted Successfully...")
        Button(root, text='Add Run',font=('arial',10,'bold'),bg='green2',command=add_run ).grid(row=1, column=11) #ADD BUTTON
        Button(root, text='Delete Run',font=('arial',10,'bold'),bg='green2',command=delete_run).grid(row=1, column=12) #EDIT BUTTON
        
        def back_to_home():#Function to go back to home page
                root.destroy()
                self.add_bus_details()
        Button(root, text= 'Back',font="Arial 10 bold", command=back_to_home).grid(row=1,column=13)# back to home page button
        
        root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
p=python_project()
p.main()
