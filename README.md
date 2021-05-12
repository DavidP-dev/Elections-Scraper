# Elections-Scraper
This code is my third Engeto Academy project. It can download election data from selected distritct from Czech statistic bureau in this page https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ and export it to "csv" file.

LIBRARIES INSTALLATION

Libraries used in this code are described in included requirements.txt file. It is recommended to use new virtual enviroment for running this code. You can install libraries from command line this way:

$ pip3 --version                     # for version check
$ pip3 install -r requirements.txt   # for libraries installation

LAUNCHING PROGRAM

It is required to use two arguments for launching this program. The first is name of selected district and the second is chosen name of .csv file that you want to create for storing results. Command looks like this:

$ python Elections Scraper.py <name of district> <chosen name of .csv file>
  
USING CODE EXAMPLE

Launching code:

$ python Elections Scraper.py Kladno Kladno.csv

Runnig code:

Hello. Scrapping elections results for Kladno

Found district link for Kladno: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103
Found city link for Běleč #535010: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=535010&xvyber=2103
RESULT: ['535010', 'Běleč', 262, 181, 181, 'Občanská demokratická strana|Česká str.sociálně demokrat.|STAROSTOVÉ A NEZÁVISLÍ|Komunistická str.Čech a Moravy|Strana zelených|ROZUMNÍ-stop migraci,diktát.EU|Česká pirátská strana|TOP 09|ANO 2011|Křesť.demokr.unie-Čs.str.lid.|REALISTÉ|SPORTOVCI|Dělnic.str.sociální spravedl.|Svob.a př.dem.-T.Okamura (SPD)|Strana Práv Občanů']
...
Found city link for Žižice #533157: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=533157&xvyber=2103
RESULT: ['533157', 'Žižice', 487, 298, 296, 'Občanská demokratická strana|Řád národa - Vlastenecká unie|Česká str.sociálně demokrat.|STAROSTOVÉ A NEZÁVISLÍ|Komunistická str.Čech a Moravy|Strana zelených|ROZUMNÍ-stop migraci,diktát.EU|Strana svobodných občanů|Blok proti islam.-Obran.domova|Česká pirátská strana|TOP 09|ANO 2011|SPR-Republ.str.Čsl. M.Sládka|SPORTOVCI|Dělnic.str.sociální spravedl.|Svob.a př.dem.-T.Okamura (SPD)']

Final result:

Final result of this code is creation of Kladno.csv file. This file is stored in this repository.  
