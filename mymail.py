import smtplib
smtpUser ='Your Email@gmail.com'
smtpPass ='Your Password'

toAdd ='gadgetguy.gadgetguy@gmail.com'
fromAdd =smtpUser

subject ='Raspberry pi Turned on!!!'
header ='To:' + toAdd + '\n' + 'From:' + fromAdd + '\n' + 'Subject:' 
body = 'Raspberry pi has succcessfully booted up and is connected to the  internet  ***This is an auto generated mail pls dont reply***'

print header + '\n' + body 
 
s= smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser,smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n' + body )

s.quit()
