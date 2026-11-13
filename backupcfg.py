import logging, smtplib, os, shutil, sys

# email config
smtp = {"sender": "bek.j.jones@gmail.com", # Gmail.com verified sender
        "recipient": "Seanythelad@gmail.com", # Gmail.com verified recipient
        "server":    "smtp.gmail.com",# Googlemail SMTP server
        "port":      587, # Gmail.com SMTP port
        "user":      "bek.j.jones@gmail.com",# Gmail.com user
        "password":  "phqc kkks qxst dzix"} # Gmail.com password
# Job file paths and destination file paths. the {"sourcepath" : "./job_files/jobnumber"} indicates the the program where to look for the files to copy.
job1 = {"sourcepath": "./job_files/job1",
         "destination": "./backup_files"} 
job2 = {"sourcepath": "./job_files/job2",
         "destination": "./backup_files"}
job3 = {"sourcepath": "./job_files/job3",
         "destination": "./backup_files"}
job4 = {"Sourcepath": "./job_files/job4",
         "destination": "./backup_files"}
job5 = {"sourcepath": "./job_files/job5",
        "destination": "./backup_files"}
test_file1 = {"sourcepath": "./job_files/test_file1.txt",
               "destination": "./backup_files"}
# log file config
logging.basicConfig(
    filename='backup.log', 
    filemode='a', # 'a' means append (this is the default)
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)