from sys import stdin
import re


# coding: utf-8

# De här funktionerna ska returnera reguljära uttryck som löser uppgifterna på övningen.

def dna():  # uppgift 1
    return "^[ACGT]+$"


def sorted():  # uppgift 2
    return "^9*8*7*6*5*4*3*2*1*0*$"


def hidden1(x):  # uppgift 3
    # Input x är strängen som vi vill söka efter.
    return x


def hidden2(x):  # uppgift 4
    # Input x är strängen som vi vill söka efter.
    return ".*".join(list(x))


def equation():  # uppgift 5
    return "^[-+]?(\d+[-+*/])*\d+(=[-+]?(\d+[-+*/])*\d+)?$"


# Här är lite kod som du kan använda för att provköra dina
# reguljära uttryck. Koden definierar en main-metod som läser
# rader från standard input och kollar vilka reguljära uttryck
# som matchar indata-raden. För de två hidden-uppgifterna
# används söksträngen x="test" (kan lätt ändras).
#
# För att provköra från terminalen, skriv:
# > python s1.py
# Skriv in teststrängar:
# [skriv här]
# ...

def main():
    def hidden1_test():
        return hidden1('test')

    def hidden2_test():
        return hidden2('test')

    tasks = [dna, sorted, hidden1_test, hidden2_test, equation]
    print('Skriv in teststrängar:')
    while True:
        line = stdin.readline().rstrip('\r\n')
        if line == '':
            break
        for task in tasks:
            result = '' if re.search(task(), line) else 'INTE '
            print('%s(): "%s" matchar %suttrycket "%s"' % (task.__name__, line, result, task()))


if __name__ == '__main__':
    main()
