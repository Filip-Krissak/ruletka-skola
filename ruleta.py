import random
import time

cervena = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] 
cierna = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35] 
nula = [0] 
neparna = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35] 
parna = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36] 

class Mojtiket:
    vyhry = {
        'cervena': 2,
        'cierna': 2,
        'parne': 2,
        'neparne': 2,
        'nula': 35,
        'cislo': 35
    }
    moznosti = [
        'cervena',
        'cierna',
        'parne',
        'neparne',
        'nula',
        'cislo']

    def __init__(self):
        self.bets = []

    def vsad(self, bet):
        self.bets.append(bet)
        return self

    @staticmethod
    def vyhodnotenie(cis):
        vysledok = {'cervena': False, 'cierna': False, 'parne': False, 'neparne': False, 'nula': False, 'cislo': cis}
        if cis > 0 and cis < 37:
            if cis % 2:
                vysledok['neparne'] = True
            else:
                vysledok['parne'] = True
            if cis in cierna:
                vysledok['cierna'] = True
            else:
                vysledok['cervena'] = True
        else:
            vysledok['nula'] = True
            vysledok['cislo'] = "0"
        
        return vysledok

class stavka:
    def __init__(self, typ, kolko, cislo=None):
            self.typ = typ
            self.kolko = kolko
            self.cislo = cislo

hra = True
ano = False
while hra == True:
    if ano == False:
        balanc = int(input('vyber si vklad:'))
        ticket = Mojtiket()
        ano = True
        print('Vitaj')

    print(f'tvoj balanc: {balanc}')
    print('1 = zadaj stavku')
    print('2 = pozri si svoje stavky')
    print('3 = zatoc koleso')
    print('4 = koniec')

    vyber = input('co chces spravit? ' )
    if vyber ==  '4':
        hra = False

    if vyber == '1':
        if balanc <= 0:
            print('nemas peniaze')
            continue
        i = 1
        for k in ticket.moznosti:
            print(f"{i} {k}")
            i+=1
        k_vyber = int(input('vyber si kam vsadit: ' ))
        typ = ticket.moznosti[k_vyber -1]
        print(f'vybral si si: {typ} ' )
        num = None
        if typ == 'cislo':
            while num == None:
                cs = int(input('vyber cislo: (1-36) '))
                if cs < 1 or cs > 36:
                    print('napis cislo (1-36)')
                else:
                    num = cs

        stauka = 0
        while stauka == 0:
            vs = int(input('kolko chces vsadit? ' ))
            if vs > balanc:
                print('nemas dost penazi')
            else:
                stauka = vs
        ticket.vsad(stavka(typ, stauka, num))
        balanc -= stauka
    if vyber == '2':
        print('tvoje stavky: ' )
        for bet in ticket.bets:
            print(f'{bet.typ}: ${bet.kolko}', end =' ')
            if bet.cislo:
                print(f'na: {bet.cislo}')
            else:
                print('')

    if vyber == '3':
        vysl = ticket.vyhodnotenie(random.randint(0,36))
        print(f"padlo: {vysl['cislo']}")
        k_stavky = 0
        k_vysl = 0
        for bet in ticket.bets:
            win = False
            k_stavky += bet.kolko
            if bet.typ == 'cislo':
                if vysl['cislo'] == bet.cislo:
                    win = True

            elif vysl[bet.typ]:
                win = True
            if win:
                vyhra = bet.kolko * Mojtiket.vyhry[bet.typ]
                print(f'vyhralo: {bet.typ}, vsadil si: {bet.kolko}, vyhral si: {vyhra}')
                if bet.typ == 'cislo':
                    print(f'(vsadene na {bet.cislo})')
                else:
                    print('')
                k_vysl += vyhra
            else:
                print(f'{bet.typ}: -${bet.kolko}', end = ' ')
                if bet.typ == 'cislo':
                    print(f'(vsadene na: {bet.cislo})')
                else:
                    print('')
        print(f'celkovo vsadene: {k_stavky}, celkova vyhra: {k_vysl}, profit: {k_vysl - k_stavky}')
        balanc += k_vysl
        print(f'balanc: {balanc}')
        if balanc <= 0:
            hra = False
            print('prehral si')
        else:
            pokracovat = input('chces pokracovat? (0 = nie / 1 = ano)')
            if pokracovat == '1':
                ticket = Mojtiket()
                continue
            else:
                time.sleep(2)
                hra = False
                print('dohral si')
