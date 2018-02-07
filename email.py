import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("shreyas.patil0602@gmail.com", "*********")
 
msg = "YOUR MESSAGE!"
server.sendmail("shreyas.patil0602@gmail.com", "prateekkovalli7@gmail.com", msg)
server.quit()
