import logging, smtplib, os, shutil, sys


smtp = {"sender": "Seanythelad@gmail.com", # elasticemail.com verified sender
"recipient": "30029394@students.sunitafe.edu.au", # elasticemail.com verified recipient
"server": "smtp.elasticemail.com", # elasticemail.com SMTP server
"port": 2525, # elasticemail.com SMTP port
"user": "Seanythelad@gmail.com", # elasticemail.com user
"password": "77DFABCE56C81A3E5E0A9A87F3168888F2A6"} # elasticemail.com password
job1 = {"sourcepath": "./job_files/job1.py", "destination": "./backup_files"}
job2 = {"sourcepath": "./job_files/job2.py", "destination": "./backup_files"}
job3 = {"sourcepath": "./job_files/job3.py", "destination": "./backup_files"}
job5 = {"sourcepath": "./job_files/job5.py", "destination": "./backup_files"}
test_file1 = {"sourcepath": "./job_files/test_file1.txt", "destination": "./backup_files"}
logging.basicConfig(
    filename='backup.log', 
    filemode='a', # 'a' means append (this is the default)
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)