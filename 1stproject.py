#1st gmailaccount and 2 factor authentication
#genrate app password
#create a function send the mail
import smtplib
server=smtplib.SMTP('smtp.gmail.com',465)
server.starttls()

server.login('vishnusreedhar2001@gmail.com','tcri lhdh mevx kqcx')

server.sendmail('vishnusreedhar2001@gmail.com','noteveh232@finghy.com',"hi buddy what's up how's this going")

print('mail sent')