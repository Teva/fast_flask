import os, time

stamp = time.ctime()

while True:
    os.system("git add .")
    os.system("git status")
    os.system("git commit -m "+'{}{}{}'.format('"',stamp,'"'))
    os.system("git push")
    print("repo is updated")
    time.sleep(600)
