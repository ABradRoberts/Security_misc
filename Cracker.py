#!/bin/python3

# Author: Allen Bradley Roberts

import os
import time

start = time.time()

with open("hash.txt", "r") as shadow:
    hash=shadow.readline().split(':')[1]

hash_algo = hash.split('$')[1]
salt = hash.split('$')[2]

with open("wordlist.txt", "r") as wordlist:
    print("Searching...", flush=True)
    for word in wordlist:
        response = os.popen("/usr/bin/openssl passwd -{} -salt {} {}".format(hash_algo, salt, word)).read()

        if response.strip() == hash:
            print("[+] Password found: {}".format(word))
            end = time.time()
            print("Execution time: %s", str(end-start))
            exit(0)

print("[-] Password was not in the provided wordlist.")

end = time.time()
print("Execution time: %s", str(end-start))
