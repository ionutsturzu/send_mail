import smtplib
to = ''
gmail_user = ''
gmail_pwd = '*******'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print header
msg = header + '\n this is test msg \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()
