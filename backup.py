#!/usr/bin/python3
"""
backup.py
This program is used to backup files and alert the user if any error occurs
This program was created Sean Hosking, and was created on the 11/11/2026 09:45
"Sean Hosking" <30029394@students.sunitafe.edu.au>
version 1.0
"""

import shutil, os, sys, datetime, logging, smtplib
from datetime import datetime
from zoneinfo import ZoneInfo
from backupcfg import smtp, logging

def ClearLog():
    """
    Clears the contents of the backup.log file entered like any other job into the command line interface.
    """
    log_file_path = 'backup.log'
    if os.path.exists(log_file_path):
        with open(log_file_path, 'w') as log_file:
            log_file.write('')
        print(f"Cleared the contents of {log_file_path}.")
        logging.info("Cleared the contents of backup.log.")
    else:
        print(f"{log_file_path} does not exist.")
        logging.warning(f"{log_file_path} does not exist.")

def CreateBackup(source_path, destination_dir): 
    """
    This code is responsible for the functionality of creating the backup using the source path and destination directory
    """
    # used to ensure the source path is correct
    if not os.path.exists(source_path):
        print(f"Error: ",{source_path}," does not exist.")
        logging.error(f'FAIL: {source_path} located within the Config file but no such file exists.')
        SendEmail(f'Copy attempt Failed: {source_path} located in the config file but no such file exists.')
        return
    os.makedirs(destination_dir, exist_ok=True)
    now = datetime.now
    time_zone = ZoneInfo("Australia/Melbourne")
    timestamp = now().astimezone(time_zone).strftime("%Y%m%d-%H%M%S")
    base_name = os.path.basename(os.path.normpath(source_path))
    
    # This section of the code is used to identify if the back up is file directory
    if os.path.isdir(source_path):
        backup_name = f'{base_name}_backup_{timestamp}'
        target_path = os.path.join(destination_dir, backup_name)

        shutil.copytree(source_path, target_path)
        print(f"Successfully backed up to: ",{target_path})
        logging.info(f'SUCCESS: backup completed successfully.')
    #This code is used to identify if the file to back up is a file
    elif os.path.isfile(source_path):
        file_name, file_ext =os.path.splitext(base_name)  
        backup_name = f"{file_name}_{timestamp}{file_ext}"  
        target_path = os.path.join(destination_dir, backup_name)

        shutil.copy2(source_path, target_path)
        print(f'Successfully backed up file to: ',{target_path})
        logging.info("SUCCESS:  backup completed successfully.")
        print("Check backup.log for details.")    

def SendEmail(message):
    """
    This code is responsible for sending an email to the user if any error occurs during the backup process
    """
    try:
        with smtplib.SMTP(smtp["server"], smtp["port"]) as server:
            server.starttls()
            server.login(smtp["user"], smtp["password"])
            server.sendmail(smtp["sender"], smtp["recipient"], message)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
        logging.error(f"FAIL: Error sending email: {e}")

def main():
    # this code is used to check for the command line argument and check if the file is included within the config file. If it is, it will proceed to backup the file.
    if len(sys.argv) < 2:
        print("Error: Please provide a job name.")
        print("Usage: python script.py <job name>")
        sys.exit(1)
    target_file = sys.argv[1]
    if target_file == "clearlog": 
        #This code handles the ability to clear the log file if the user enters "clearlog" into the command line interface. This is useful for clearing the log file if it becomes too large or if the user wants to start fresh with a new log.
        ClearLog()
        sys.exit(0)
    elif target_file == "backup_files":
        # This code handles the ability to backup all the files in the backup_files Directory if the user enters the right code. This is useful to quickly backup all the backup files.
        print("Backing up all files in the backup_files directory.")
        source_dir = "./backup_files"
        destination_dir = "./backup_files"
        CreateBackup(source_dir, destination_dir)
        sys.exit(0)    
    else:
        print('Searching for: '+ target_file)
        Search_word = target_file
    
    Search_word = target_file
    with open("backupcfg.py", "r") as file:
        if Search_word in file.read():
            print(target_file + ' included within the Config File. Proceeding to backup.')
            target_file = "./job_files/" + target_file
            Destination = "./backup_files"            
            CreateBackup(target_file, Destination)            
        else:
            print('Error: '+ target_file + ' not included within the Config File. Ensure command line has full file name. Make sure to Type the full file name including its extension (.txt, .py)')
            logging.error("FAIL: Backup failed, "+ target_file+ " not in the config file. Ensure command is written correctly and that the job is valid")
            SendEmail("Backup failed, " + target_file + " not in the config file. Ensure command is written correctly and that the job is valid")

if __name__ == "__main__":
    main()
