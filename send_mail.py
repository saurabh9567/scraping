import smtplib

from_add = 'saurabh956@gmail.com'
to_add = 'saurabhverma956@gmail.com'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_add, 'rqozbryqteixhgjg')

message = 'Hi this is saurabh verma from saurabh956@gmail.com'
server.sendmail(from_add, to_add, message)

server.quit()