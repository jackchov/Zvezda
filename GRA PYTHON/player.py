class Player:
    def __init__(self):
        self.kartka1=False
        self.kartka2=False
        self.kartka3=False
        self.kartka4=False
        self.lina=False

        self.plansza1=False
        self.plansza2=False
        self.plansza3=False
        self.plansza4=False
        self.plansza5=False
        self.plansza6=False
        self.plansza7=False
        self.plansza8=False
        self.plansza9=False

'''
class player:

    def __init__(self):
        self.kartki = 1
        self.lina = 0


    def zbierz_kartke(self):
        self.kartki+=1

    def zbierz_line(self):
        self.lina+=1

    def stan_kartek(self):
        return self.kartki

    def stan_liny(self):
        return self.lina

gracz=player()

#przykład lokacji zdobycia liny

los=random.randint(1,3)
if los > 1:
    gracz.zbierz_line()
    textsurface = myfont.render('Somehow you menage to harvest what is left of the rope and put it to your backpack.', False,
                                (255, 255, 255))
    screen.blit(textsurface, (10, 650))
if los =1:
    textsurface = myfont.render('As you reach for the rope you hear worrying sound of something falling down. Afraid'
                                'of what it may be attached to, you abandon your attempt to take the rope.',
                                False,
                                (255, 255, 255))
    screen.blit(textsurface, (10, 650))
    '''
