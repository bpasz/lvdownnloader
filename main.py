# -*- coding: utf-8 -*-

from lvauser import GHuser,GitUser, download_instruction,check_git
import messages as msg
import re
import string
repo_prefix="adv_LVLab"
org_name="wemif-lva"
folder_prefix="Laboratorium "
url=string.Template("http://labview.wemif.pwr.edu.pl/student/advlab${nr}.zip")
url_ins=string.Template("http://labview.wemif.pwr.edu.pl/instruktor/advlab${nr}_ins.zip")
print(msg.welcome)
gh_login=input("Uzytkownik GitHub: ")
check_git()

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
    elif cmd=="s":
        prompt = input("podaj numer ćwiczenia (1-10):")
        if re.fullmatch("^[1-9]|10$", prompt):
            reponame = repo_prefix + prompt
            gu=GitUser()
            gu.clone_or_pull(reponame,gh_login,folder_prefix+prompt)
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
        prompt = input("podaj numer ćwiczenia (1-10):")
        if re.fullmatch("^[1-9]|10$", prompt):
            download_instruction(url.substitute(nr=prompt),"Laboratorium {}".format(prompt),"lab{}.zip".format(prompt))
        else:
            print("Zły numer ćwiczenia")
    elif cmd == "i":
        prompt = input("podaj numer ćwiczenia (1-10):")
        if re.fullmatch("^[1-9]|10$", prompt):
            download_instruction(url_ins.substitute(nr=prompt), "Laboratorium {}".format(prompt),
                                 "lab{}.zip".format(prompt))
        else:
            print("Zły numer ćwiczenia")

    elif cmd=="w":
        break
    else:
        print("Blędna komenda")

