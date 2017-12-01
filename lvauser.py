# modul zawierajcy klase lvuser, ktora ma kod odpowiedzialne za obsuge igt, forkowanie itd.
# -*- coding: utf-8 -*-
from github import Github
import os
import subprocess
import urllib.request
import shutil
from zipfile import ZipFile as zip
import webbrowser as wb


class GHuser:

    def __init__(self, login, password):
        try:
            self.gh = Github(login, password)
            self.gh.get_user().login   #Słuzy tylko sprawdzeniu czy udalo sie zalogowac
        except Exception as e:
            self.log_status = False
            print('Blad: '+str(e))
        else:
            self.log_status = True
            self.gh_user = self.gh.get_user()
            print ("Zalogowano pomyślnie")

    def forkgh(self, gh_master_user, reponame):
        # zforkuj repo z github
        try:
            master = self.gh.get_organization(gh_master_user)
            master_repo = master.get_repo(reponame)
            self.gh_user.create_fork(master_repo)

        except Exception as e:
            print("Nie udało się wykonać \"fork\", Blad"+ e)
            return True
        else:
            return False
class GitUser:
    repos_path="Kody"

    def clone(self,reponame,username,foldername):
        repopath="https://github.com/{}/{}.git".format(username,reponame)
        #-C oznaczna że git pracuje w fodlerze zadania
        folderpath=os.path.join(self.repos_path,foldername)
        cmd = ["git", "clone", repopath, folderpath]
        result=subprocess.run(cmd)
        print("Odpowiedź: " + str(result.returncode))

    def clone_or_pull(self,reponame, username, foldername):
        repopath = "https://github.com/{}/{}.git".format(username, reponame)
        # -C oznaczna że git pracuje w fodlerze zadania
        folderpath = os.path.join(self.repos_path, foldername)
        if os.path.isdir(folderpath):
            cmd=["git","-C",folderpath,"pull",repopath]
            result = subprocess.run(cmd)
        else:
            cmd = ["git", "clone", repopath, folderpath]
            result = subprocess.run(cmd)


    def commit_and_push(self,reponame,username,foldername):
        local_repopath=os.path.join(self.repos_path,foldername)
        repopath = "https://github.com/{}/{}.git".format(username, reponame)
        cmd = ["git", "-C", local_repopath, "add", "--all"]
        subprocess.run(cmd)

        cmd=["git","-C", local_repopath, "config","--local", "user.name", username]
        subprocess.run(cmd)

        cmd = ["git", "-C", local_repopath, "config","--local","user.email", username + "@mail.com"]
        subprocess.run(cmd)

        cmd = ["git", "-C", local_repopath, "config", "--local", "credential.helper", ""]
        subprocess.run(cmd)

        cmd = ["git", "-C", local_repopath, "config", "--local", "credential.username", username]
        subprocess.run(cmd)

        cmd=["git","-C",local_repopath, "commit", "-m", "Dodany z LV Downloader"]
        subprocess.run(cmd)

        cmd=["git","-C", local_repopath,"push",repopath]
        subprocess.run(cmd)

       # cmd = ["git", "-C", "repopath", "commit",]


def download_instruction(url, inst_dirname,filename):
    directory=os.path.join(os.getcwd(),"Instrukcje", inst_dirname)
    filepath=os.path.join(directory,filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with urllib.request.urlopen(url) as response, open(filepath, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    archiwum=zip(filepath)
    archiwum.extractall(directory,pwd=input("Podaj hasło do instrukcji: ").encode())
    archiwum.close()
    os.remove(filepath)


def check_git():
    if not shutil.which("git"):
        print("GIT nie jest zainstalowany, LV Downloader nie bedzie dzialac")
        if input("Przekierowac na strone do pobierania? (t/n)")=="t" :
            wb.open("https://git-scm.com/download/win")
