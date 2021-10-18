import smtplib
import getpass

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#print(user,"has a problem with", program)
#print("Their email address is", useremail, "and best contact number is", tel,". They are free", days ,".")

checkuser = getpass.getuser()
print("Logging into SMTP Server...\n WELCOME " + checkuser + "\n")
email = 'PythonHeatAPI@genesiscare.co.uk'
password = 'B&e*_zrexCy9jL$YXAZ%'
smtpsrv = "smtp.office365.com"
smtpserver = smtplib.SMTP(smtpsrv,587)
send_to_email = 'justin.gates@me.com'
user = input("What is your name? ")
problem = input("What program or device are you using? ")
issue = input("and what is wrong with? ")
telephone = input("Please provide a contact number / ext: ")
centre = input("and finally,  which Centre are you based: ")


body = (" USER EMAIL: " + checkuser + "@genesiscare.co.uk" + " \n PROGRAM OR DEVICE:  " + problem + " \n ISSUE:  " + issue + " \n CONTACT: " + telephone + " \n CENTRE: " + centre)
subject = ("New ticket from " + checkuser)
#useremail = input("What is your email address? ")
# #tel = input("What is your best contact telephone number? ")
# #days = input(" and finally, what days do you work? ")



msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject


# Attach the message to the MIMEMultipart object
plain_text = MIMEText(str(body), _subtype='plain', _charset='UTF-8')
msg.attach(plain_text)

print(' \n Sending ticket to the IT team... \n')

smtpserver.starttls()
smtpserver.login(email, password)
smtpserver.send_message (msg)
smtpserver.close()

print(' Ticket sent! \n')

print("\n Program ended, Press any key to close")
input("")