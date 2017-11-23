# -*- coding: utf-8 -*-

import getpass

welcome=u"""******** LabVIEW Downlader WEMiF ********
Zarządzaj kodem i instrukcjami do laboratorium programowania w LabVIEW
Autor:B.Paszkiewicz,  Uwagi i bledy: bartlomiej.paszkiewicz@pwr.edu.pl
Wybierz co chcesz zrobic?
1) [f]ork i clone kodu do laboratorium (pierwsze pobranie)
2) {c]lone kodu do laboratorium (kod juz jest przypisany do Twojego konta GitHub)
3) [z]apisz i zaladuj (push) kod do repozytorium
4) [p]obierz instrukcje do laboratorium
5) [w]yjdz
"""


def logowanie_gh():
    password=getpass.getpass(prompt="Hasło GitHub: ")
    return password

