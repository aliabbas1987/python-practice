import smtplib
#from email.mime.text import *
body = 'Test email'

msg = body

msg['From'] = "ali.logician@gmail.com"
msg['To'] = "ali.logician@gmail.com"
msg['Subject'] = 'Hello'

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()
server.login("ali.logician@gmail.com", 'aliabbas786"!')

server.send_message(msg)
print("Mail Sent")

server.quit()
