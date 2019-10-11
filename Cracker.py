#!/usr/bin/python3
# Author: Brad Roberts

# TODO:
# 1. This can easily be multi-threaded in several ways
# 2. Prolly should error check
# 3. Ya know, handle args

import os
import time

hash_file = "hash.txt"
wordlist = "wordlist2.txt"

start = time.time()
count = 0
with open(hash_file, "r") as shadow:
    for line in shadow:
        count += 1
        name = line.split(':')[0]
        hash = line.split(':')[1]
        hash_algo = hash.split('$')[1]
        salt = hash.split('$')[2]
        print("Starting password for", name)

        with open(wordlist, "r") as wl:
            print("Searching...", flush=True)
            for word in wl:
                response = os.popen("/usr/bin/openssl passwd -{} -salt {} {}".format(hash_algo, salt, word)).read()

            if response.strip() == hash:
                print("[+] Password found: {}".format(word))
                end = time.time()
                print("Execution time: %s", str(end-start))
                exit(0)

print("[-] Password was not in the provided wordlist.")

end = time.time()
print("Execution time: %s", str(end-start))
