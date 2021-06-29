from tkinter import *
import tkinter.messagebox
import mysql.connector
import math
import operator
from PIL import Image, ImageTk

root=Tk()
root.title("MobiExpert")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()

root.geometry("%dx%d+0+0"%(w,h))
root.resizable(0,0)

mydb=mysql.connector.connect(host="localhost",user="root",passwd="ash@123",database="MobiExpert")

mycursor=mydb.cursor()


def RGBAImage(path):
	return Image.open(path).convert("RGBA")


welcome=RGBAImage("Resources/welcome.png")
background_image=RGBAImage("Resources/bg5.png")

background_image.paste(welcome,(0,0),welcome)

final_bg=ImageTk.PhotoImage(background_image)

bg=Label(root,image=final_bg)
bg.place(x=0,y=0,relwidth=1,relheight=1)

login_frame=Frame(root,bg="white")
login_frame.grid(row=0,column=0,padx=450,pady=100,ipadx=40,ipady=20)
#login_frame.pack(fill=Y)

def euclidean_distance(a,b):
	distance=0
	for i in [0,1,2]:
		distance+=pow((a[i]-b[i]),2)
	return math.sqrt(distance)

def action():
	if(ans8.get()==1):
		mycursor.execute("""Select Gaming,Entertainment,Camera from Users where Name = %s""",(n.get(),))
		r4=mycursor.fetchall()
		ans1=r4[0][0]
		ans2=r4[0][1]
		ans3=r4[0][2]
		knn(1)
	else:
		ques1(5)
def choice():
	frame0.destroy()
	global c_frame
	c_frame=Frame(root,bg="white")
	global ans8,ans9
	ans8=IntVar()
	ans9=IntVar()
	c_frame.grid(row=0,column=0,padx=455,pady=300,ipadx=10,ipady=10)
	l7=Label(c_frame,text="\n\tWork with previously entered choices?\n\n\t",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=0,column=0,pady=5,columnspan=2)
	r11=Radiobutton(c_frame,text="Yes",bg="white",variable=ans8,value=1,command=action,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=1,column=0,pady=5,padx=10)
	r12=Radiobutton(c_frame,text="No",bg="white",variable=ans9,value=2,command=action,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=1,column=1,pady=5,padx=10)

def check(frame_no):
	if(ans4.get()<1000 or ans5.get()<1000 or ans4.get()>200000 or ans5.get()>200000 or ans4.get()>ans5.get()):
		tkinter.messagebox.showerror("Error","Invalid or not Practical Budget Range !")
	else:
		if(frame_no==5):
			choice()
		else:
			ques1(1)

def result(frame_no):
	if(frame_no==3):
		frame3.destroy()
	else:
		c_frame.destroy()
	frame4=Frame(root,bg="white")
	frame4.grid(row=0,column=0,padx=305,pady=50,ipadx=20,ipady=20)
	sno=[]
	prices=[]

	if(len(neighbours)==0):
		l20=Label(frame4,text="No phones in this budget range!",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=0,columnspan=2,padx=20,pady=20)
	else:
		for x in neighbours:
			for y in index:
				if(x==y[0]):
					sno.append(y[1])
					prices.append(y[2])

		
		
		
		#print(path)
		if(len(neighbours)>0):
			path1="Resources/"+"%s"%(sno[0])+".png"
			pic1=PhotoImage(file=path1)
			l13=Label(frame4,text=(neighbours[0]),bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=0,column=1,columnspan=2,pady=10)
			
			str1="Best Match!\nPrice : "+"%s"%(prices[0])+"/-"
			l19=Label(frame4,text=str1,bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=1,column=3,pady=10)
			l14=Label(frame4,image=pic1,border=0)
			l14.grid(row=1,column=1,columnspan=2,pady=10)
			l14.image=pic1

			if(len(neighbours)>1):
				path2="Resources/"+"%s"%(sno[1])+".png"
				pic2=PhotoImage(file=path2)
				l15=Label(frame4,text=(neighbours[1]),bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=2,column=0,padx=20,pady=10)
				
				str2="Price : "+"%s"%(prices[1])+"/-"
				l19=Label(frame4,text=str2,bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=3,column=1,padx=20,pady=10)
				l16=Label(frame4,image=pic2,border=0)
				l16.grid(row=3,column=0,padx=20,pady=10)
				l16.image=pic2

				if(len(neighbours)>2):
					path3="Resources/"+"%s"%(sno[2])+".png"
					pic3=PhotoImage(file=path3)
					l17=Label(frame4,text=(neighbours[2]),bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=2,column=2,padx=20,pady=10)
					
					str3="Price : "+"%s"%(prices[2])+"/-"
					l19=Label(frame4,text=str3,bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=3,column=3,padx=20,pady=10)
					l18=Label(frame4,image=pic3,border=0)
					l18.grid(row=3,column=2,padx=20,pady=10)
					l18.image=pic3

	print("Successfully Terminated...\nBye!")
 
def knn(frame_no):
	
	#print(ans4.get())
	#print(ans5.get())
	mycursor.execute("""Select * from Mobiles where Price > %s and Price < %s """,(ans4.get(),ans5.get(),))
	result1=mycursor.fetchall()
	data=[11-ans1.get(),11-ans2.get(),11-ans3.get()]
	if(nn.get()==""):
		mycursor.execute("""Update Users set Gaming=%s where Name = %s""",(data[0],n.get(),))
		mycursor.execute("""Update Users set Entertainment=%s where Name = %s""",(data[1],n.get(),))
		mycursor.execute("""Update Users set Camera=%s where Name = %s""",(data[2],n.get(),))
		mydb.commit()
	else:
		mycursor.execute("""Update Users set Gaming=%s where Name = %s""",(data[0],nn.get(),))
		mycursor.execute("""Update Users set Entertainment=%s where Name = %s""",(data[1],nn.get(),))
		mycursor.execute("""Update Users set Camera=%s where Name = %s""",(data[2],nn.get(),))
		mydb.commit()
	distances=[]
	global index
	index=[]
	for i in result1:
		data2=[i[1],i[2],i[3]]
		dist=euclidean_distance(data2,data)
		distances.append((i[5],dist))
		index.append((i[5],i[0],i[4]))

	distances.sort(key=operator.itemgetter(1))

	#print(len(distances))

	global neighbours 
	neighbours=[]

	for j in [0,1,2]:
		if(j>=len(distances)):
			break
		else:
			neighbours.append(distances[j][0])

	
	result(frame_no)

def ques0(frame_no):
	login_frame.destroy()
	global frame0
	frame0=Frame(root,bg="white")
	global ans4,ans5
	ans5=IntVar()
	ans4=IntVar()
	frame0.grid(row=0,column=0,padx=305,pady=200,ipadx=10,ipady=10)
	l7=Label(frame0,text="\n\tIn what budget range are you looking for your new smartphone ?\n\n\t",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=0,column=0,pady=5,columnspan=4)
	l8=Label(frame0,text="Minimum Price :",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=1,column=0,padx=10,pady=10)
	e3=Entry(frame0,textvariable=ans4)
	e3.grid(row=1,column=1,padx=10,pady=10)
	l8=Label(frame0,text="Maximum Price :",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=1,column=2,padx=10,pady=10)
	e4=Entry(frame0,textvariable=ans5)
	e4.grid(row=1,column=3,padx=10,pady=10)
	b3=Button(frame0,text="Next -->",bg="white",command=lambda: check(frame_no),font=("AnjaliOldLipi Bold",12)).grid(row=2,columnspan=4,padx=10,pady=10)
		


def ques1(frame_no):
	 if(frame_no==5):
	 	c_frame.destroy()
	 else:
	 	frame0.destroy()
	 global frame1
	 frame1=Frame(root,bg="white")
	 
	 frame1.grid(row=0,column=0,padx=300,pady=200,ipadx=10,ipady=10)
	 l6=Label(frame1,text="\n\tHow much will you prefer to use your mobile phone for Gaming ?\n\t",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=0,column=0,pady=5)
	 r1=Radiobutton(frame1,text="Strongly Prefered",bg="white",variable=ans1,value=1,command=ques2,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=1,column=0,pady=5)
	 r2=Radiobutton(frame1,text="Moderately Prefered",bg="white",variable=ans1,value=2,command=ques2,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=2,column=0,pady=5)
	 r3=Radiobutton(frame1,text="Weakely Prefered",bg="white",variable=ans1,value=3,command=ques2,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=3,column=0,pady=5)
	 r4=Radiobutton(frame1,text="Less Prefered",bg="white",variable=ans1,value=4,command=ques2,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=4,column=0,pady=5)
	 r5=Radiobutton(frame1,text="Not Prefered",bg="white",variable=ans1,value=5,command=ques2,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=5,column=0,pady=5)

def ques2():
	frame1.destroy()
	global frame2
	frame2=Frame(root,bg="white")
	
	frame2.grid(row=0,column=0,padx=225,pady=200,ipadx=10,ipady=10)
	l7=Label(frame2,text="\n\tHow much will you prefer to use your mobile phone for Watching Movies or Videos ?\n\t",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=0,column=0,pady=5)
	r6=Radiobutton(frame2,text="Strongly Prefered",bg="white",variable=ans2,command=ques3,value=1,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=1,column=0,pady=5)
	r7=Radiobutton(frame2,text="Moderately Prefered",bg="white",variable=ans2,command=ques3,value=2,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=2,column=0,pady=5)
	r8=Radiobutton(frame2,text="Weakely Prefered",bg="white",variable=ans2,command=ques3,value=3,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=3,column=0,pady=5)
	r9=Radiobutton(frame2,text="Less Prefered",bg="white",variable=ans2,command=ques3,value=4,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=4,column=0,pady=5)
	r10=Radiobutton(frame2,text="Not Prefered",bg="white",variable=ans2,command=ques3,value=5,padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=5,column=0,pady=5)

def ques3():
	 frame2.destroy()
	 global frame3
	 frame3=Frame(root,bg="white")
	 
	 frame3.grid(row=0,column=0,padx=200,pady=200,ipadx=10,ipady=10)
	 l6=Label(frame3,text="\n\tHow much will you prefer to use your mobile phone for Clicking Pictures or making Videos etc. ?\n\t",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=0,column=0)
	 r1=Radiobutton(frame3,text="Strongly Prefered",bg="white",variable=ans3,value=1,command=lambda: knn(3),padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=1,column=0,pady=5)
	 r2=Radiobutton(frame3,text="Moderately Prefered",bg="white",variable=ans3,value=2,command=lambda: knn(3),padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=2,column=0,pady=5)
	 r3=Radiobutton(frame3,text="Weakely Prefered",bg="white",variable=ans3,value=3,command=lambda: knn(3),padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=3,column=0,pady=5)
	 r4=Radiobutton(frame3,text="Less Prefered",bg="white",variable=ans3,value=4,command=lambda: knn(3),padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=4,column=0,pady=5)
	 r5=Radiobutton(frame3,text="Not Prefered",bg="white",variable=ans3,value=5,command=lambda: knn(3),padx=5,pady=10,font=("AnjaliOldLipi Bold",15)).grid(row=5,column=0,pady=5)

def sign_up():
	#print(nn.get())
	#print(np.get())
	try:
		mycursor.execute("""Insert into Users(Name,Password) values (%s,%s)""",(nn.get(),np.get(),))
		mydb.commit()
		ques0(1)
	except(mysql.connector.Error) as e:
		print(e)
		tkinter.messagebox.showerror("Integrity Error","User Already Exist")
	
	


def login():
	mycursor.execute("""Select Password from Users where Name = %s""",(n.get(),))
	result=mycursor.fetchall()
	if(len(result)==0):
		tkinter.messagebox.showinfo("Error","Wrong Credentials")
	else:
		sqlpass="%s"%(result[0])
		if(sqlpass==p.get()):
			ques0(5)
		else:
			tkinter.messagebox.showerror("Error","Wrong Credentials")


n=StringVar()
p=StringVar()
nn=StringVar()
np=StringVar()
ans1=IntVar()
ans2=IntVar()
ans3=IntVar()

user=PhotoImage("Resources/user.png")
l5=Label(login_frame,image=user)
l5.image=user


l1=Label(login_frame,text="\nLogin with your details..\n",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=0,columnspan=2,padx=5,pady=25)
l2=Label(login_frame,text="UserName :",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=1,column=0,padx=85,pady=5)
e1=Entry(login_frame,textvariable=n)
e1.grid(row=1,column=1,padx=5,pady=5,ipady=3)
l3=Label(login_frame,text="Password :",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=2,column=0,padx=10,pady=10)
e2=Entry(login_frame,show="*",textvariable=p)
e2.grid(row=2,column=1,padx=5,pady=5,ipady=3)
l11=Label(login_frame,text="",bg="white").grid(row=4,columnspan=2,pady=10)
b2=Button(login_frame,text="Login",bg="white",font=("AnjaliOldLipi Bold",12),command=login)
b2.grid(row=5,columnspan=2,pady=5,ipadx=50)
l4=Label(login_frame,text="----------OR----------",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=6,columnspan=2,padx=5,pady=5)

def create_user():
	b2.destroy()
	b1.destroy()
	e1.config(state='disabled')
	e2.config(state='disabled')
	n=e1.get()
	Label(login_frame,text="Enter Name :",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=8,column=0,padx=5,pady=5)
	e5=Entry(login_frame,textvariable=nn)
	e5.grid(row=8,column=1,ipady=3)
	Label(login_frame,text="Set Password :",bg="white",font=("AnjaliOldLipi Bold",15)).grid(row=9,column=0,padx=5,pady=5)
	e6=Entry(login_frame,show="*",textvariable=np)
	e6.grid(row=9,column=1,ipady=3)
	b7=Button(login_frame,text="Sign Up",bg="white",font=("AnjaliOldLipi Bold",12),command=sign_up).grid(row=11,columnspan=2,ipadx=50,pady=5,padx=5)
	l12=Label(login_frame,text="",bg="white").grid(row=10,columnspan=2,pady=10)
	
	


b1=Button(login_frame,text="Create New Account",border=0,bg="white",font=("Arial Bold",10),command=create_user)
b1.grid(row=11,columnspan=2,ipadx=50,padx=5,pady=5)

root.mainloop()
