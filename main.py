import ftplib
import sys
import os
from progress_bar import printProgressBar

ftp_server = '-'
ftp_user = '-'
ftp_pass = '-'


session = ftplib.FTP(ftp_server, ftp_user, ftp_pass)

file_addresse = sys.argv[1]
file_name = file_addresse.split('/')[-1]

# Init
sizeWritten = 0
totalSize = os.path.getsize(file_addresse)

# Initial call to print 0% progress
printProgressBar(0, totalSize, prefix='Progress:',
                 suffix='Complete', length=50)

# Define a handle to print the percentage uploaded

oldComplete = 0


def handle(block):
    # this line fail because sizeWritten is not initialized.
    global sizeWritten
    sizeWritten += 1024
    global percentComplete
    global oldComplete
    percentComplete = int(((sizeWritten / totalSize)*100))
    if percentComplete > oldComplete+2:
        printProgressBar(sizeWritten, totalSize,
                         prefix='Progress:', suffix='Complete', length=50)


# open file
file = open(file_addresse, 'rb')

command = f"STOR {file_name}"

session.storbinary(command, file, 1024, handle)

file.close()
session.quit()
