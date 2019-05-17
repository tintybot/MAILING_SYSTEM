#!/usr/bin/env python
# coding: utf-8

import time 
from tkinter import *
#for gui frontend
import os 
import smtplib
#here we send birthday greetings to the people
def birthday():
    today = time.strftime('%m%d')
    #extract today's date
    mail=smtplib.SMTP('smtp.gmail.com',587)
    #for gmail the host server and port
    mail.ehlo()
    mail.starttls()
    mail.login('<your-email-id>',"<your-password>")
    #remember you need to allow access from your mailing administrator
    birthdayFile = 'recipients.txt'
    #the recivers details are written
    #birthmonthbirthday emailid
    fileName = open(birthdayFile, 'r')
    #reading the file details
    for line in fileName: 
    #for each person in the file
        if today in line: 
        	#if there is anyone with a birthday today
            line = line.split(' ')
            #accessing the email-id
            content='<your name> WISHES YOU A VERY HAPPY AND PROSPEROUS BIRTHDAY'
            #the message you want to send
            mail.sendmail('<your email-id',f"{line[1]}",content)
            #the first parameter helps the recipient to see from whom the mail is coming, please dont spam with it.
            mail.close()
            #closing the connection
    screen.destroy()
    #destroys the gui window after the work is done
            
def main():
	#I used a gui front end for the maiing system
    global screen
    screen=Tk()
    screen.geometry("300x100")
    screen.resizable(0,0)
    screen.title("TINTY APPLICATION")
    Label(text="GOOD MORNING SIR",bg="orange",font=("calibri",20)).pack()
    Label(text="").pack()
    Button(text="WISH ALL",command=birthday).pack()
    screen.mainloop()
main()
#you can use the default calling option as well
#thank you

