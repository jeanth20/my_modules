import os
import shutil
import subprocess
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class BackupFolders:
    def __init__(self, user, password, destination, folders, email_recipients):
        self.user = user
        self.password = password
        self.destination = destination
        self.folders = folders
        self.email_recipients = email_recipients
        self.day = datetime.now().strftime('%w')

    def create_destination(self):
        os.makedirs(self.destination, exist_ok=True)

    def backup_folders(self):
        commands = []
        for folder in self.folders:
            dest = os.path.join(folder, self.day, folder)
            os.makedirs(dest, exist_ok=True)
            cmd = f'rsync -av -az --progress {folder} {dest}'
            commands.append(cmd)
            subprocess.call(cmd, shell=True)

        return commands

    def backup_databases(self):
        databases = self.list_databases()
        dir = os.path.join(self.destination, self.day, 'Databases')
        os.makedirs(dir, exist_ok=True)

        for db in databases:
            if db not in ('information_schema', 'performance_schema'):
                dump_file = os.path.join(dir, f'{db}.sql')
                if os.path.isfile(dump_file):
                    os.remove(dump_file)
                cmd = f'mysqldump -u {self.user} {db} >> {dump_file} --password={self.password}'
                subprocess.call(cmd, shell=True)

    def list_databases(self):
        cmd = 'mysql -u {} -p{} -e "SHOW DATABASES"'.format(self.user, self.password)
        output = subprocess.check_output(cmd, shell=True, universal_newlines=True)
        databases = output.strip().split('\n')[1:]
        return [db for db in databases if db not in ('information_schema', 'performance_schema')]

    def send_email(self, subject, message):
        sender = 'sender@example.com'
        smtp_server = 'smtp.example.com'
        smtp_port = 587

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ', '.join(self.email_recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, self.password)
            server.send_message(msg)

    def run_backup(self):
        try:
            self.create_destination()
            commands = self.backup_folders()
            self.backup_databases()

            if not commands:
                raise Exception('No folders to backup')

            success_message = 'Backup completed successfully.\n\nCommands executed:\n' + '\n'.join(commands)
            self.send_email('Backup Success', success_message)

        except Exception as e:
            error_message = f'Error during backup: {str(e)}'
            self.send_email('Backup Error', error_message)


if __name__ == '__main__':
    user = ''
    password = ''
    destination = '/Backup'
    folders = ['/etc', '/root', '/var']
    email_recipients = ['admin@admin.co.za', 'admin2@admin.co.za']

    backup = BackupFolders(user, password, destination, folders, email_recipients)
    backup.run_backup()
