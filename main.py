# -*- coding: utf-8 -*-

from lvauser import GHuser,GitUser
import messages as msg
import re
repo_prefix="LVLab"
org_name="wemif-lva"
folder_prefix="Laboratorium "
print(msg.welcome)
gh_login=input("Uzytkownik GitHub: ")

while 1:

    cmd=input("Wybór: ")
    if cmd=="f":
        ghuser=GHuser(gh_login,msg.logowanie_gh())
        if ghuser.log_status:
            prompt=input("podaj numer ćwiczenia (1-10):")
            if re.fullmatch("^[1-9]|10$",prompt):
                reponame=repo_prefix+prompt
                ghuser.forkgh(org_name,reponame)
                gu = GitUser()
                gu.clone(reponame, gh_login, folder_prefix + prompt)
            else:
                print("Zly numer cwiczenia!")
    elif cmd=="c":
        prompt = input("podaj numer ćwiczenia (1-10):")
        if re.fullmatch("^[1-9]|10$", prompt):
            reponame = repo_prefix + prompt
            gu=GitUser()
            gu.clone(reponame,gh_login,folder_prefix+prompt)
        else:
            print("Zly numer cwiczenia")

    elif cmd=="z":
        prompt = input("podaj numer ćwiczenia (1-10):")
        if re.fullmatch("^[1-9]|10$", prompt):
            reponame = repo_prefix + prompt
            gu = GitUser()
            gu.commit_and_push(reponame, gh_login, folder_prefix + prompt)
        else:
            print("Zly numer cwiczenia")
    elif cmd=="p":
        pass
    elif cmd=="w":
        break
    else:
        print("Blędna komenda")

