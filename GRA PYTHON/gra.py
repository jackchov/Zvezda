import pygame
from player import Player
import random

class GameState():


    def __init__(self):
        #self.state='congratulations' #TESTY
        self.state='intro_menu' #REAL GAME
        self.player=Player()


    ''' Tutaj są metody do sprawdzania czy gracz był na danej planszy,
    zmieńcie nazwy self.state na własne, bo różnie się nazywają, a to szablon'''

    def check_plansza1(self):
        if self.player.plansza1==False:
            self.state='plansza_1_1'
        else:
            self.state='plansza_1_again'

    def check_plansza2(self):
        if self.player.kartka1==True and self.player.kartka2==True and self.player.kartka3==True and self.player.kartka4==True:
            self.state='plansza_finish'

        else:
            if self.player.plansza2==False:
                self.state='plansza_2'
            else:
                self.state='plansza_2_again'

    def check_plansza3(self):
        if self.player.plansza3==False:
            self.state='plansza_3'
        else:
            self.state='plansza_3_again'

    def check_plansza4(self):
        if self.player.plansza4==False:
            self.state='plansza_4'
        else:
            self.state='plansza_4_again'

    def check_plansza5(self):
        if self.player.plansza5==False:
            self.state='plansza_5_1'
        else:
            self.state='plansza_5_again'
    def check_plansza6(self):
        if self.player.plansza6==False:
            self.state='plansza_6'
        else:
            self.state='plansza_6_again'
    def check_plansza7(self):
        if self.player.plansza7==False:
            self.state='plansza_7'
        else:
            if self.player.most==False:
                self.state=='plansza_7_again_m2'
            else:
                self.state=='plansza_7_again_m1'
    def check_plansza8(self):
        #Plansza 8 nie potrzebuje check, tam się nic nie dzieje
        self.state='plansza_8'
    def check_plansza9(self):
        if self.player.plansza9==False:
            self.state='plansza_9'
        else:
            self.state='plansza_9_again'


    ''' Plansze początkowe - kokpit, animacja spadania statku'''

    def intro_menu(self):
        #print(pygame.mouse.get_pos()) #Wyświetlanie aktualnej pozycji myszy do testów
        alarm = pygame.mixer.Sound('alarm.wav')
        pygame.mixer.Sound.play(alarm)
        buttn_click=0
        danger_flag=0
        while buttn_click==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(658) and pygame.mouse.get_pos()[0]<=(658+94):
                        if pygame.mouse.get_pos()[1]>=(550) and pygame.mouse.get_pos()[1]<=(550+65):
                            buttn_click=1
                            self.state='plansza_awaria'

        #screen.fill((0,0,0)) #screen.fill((R,G,B)), kolor tła, późniejsza wersja - dodoać obraz
            if danger_flag==0:
                screen.blit(background_menu_resized,(0,0))#(nazwa obrazu, pozycja 0,0 - lewy dolny róg)
                screen.blit(danger,(SCREEN_WIDTH/2-201,SCREEN_HEIGHT/3-62+30))
                screen.blit(emergency_txt,(SCREEN_WIDTH/2-327,SCREEN_HEIGHT-80))
                pygame.display.update()
                danger_flag=1
                clock.tick(1)
            else:
                screen.blit(background_menu_resized,(0,0))#(nazwa obrazu, pozycja 0,0 - lewy dolny róg)
                screen.blit(emergency_txt,(SCREEN_WIDTH/2-327,SCREEN_HEIGHT-80))
                pygame.display.update()
                danger_flag=0
                clock.tick(2)
        #pygame.display.flip()



    def plansza_awaria(self):
        imageX= 0; # x coordnate of image
        imageY= 0; # y coordinate of image
        while imageX<=1400:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
            imageX =imageX + 10;
            imageY= imageY + 6.4;
            screen.blit(background_resized,(0,0))#(nazwa obrazu, pozycja 0,0 - lewy dolny róg)
            screen.blit(statek_rotated,(0+imageX,0+ imageY)) # paint to screen
            pygame.display.update()
            clock.tick(20)
            if imageX==1400:
               self.state='plansza_2'

    ''' PLANSZA 2 '''

    def plansza_2(self):
        self.player.plansza2=True
        for event in pygame.event.get():
            if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                pygame.quit()
        screen.blit(background_plansza2_resize,(0,0))
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)
        pygame.mixer.music.play(-1)

            #zawijanie tekstu okazało się bardziej skomplikowane, na razie wypisuje każda linjke osobno
        textsurface = myfont.render('"I am alive."', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface2 = myfont.render('You said and looked around. You were surrounded only by sand and the burnt remains of a spaceship.', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 675))

        textsurface2 = myfont.render('"But who am I? And where am I?"', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 700))

        textsurface3 = myfont.render('You put your hands in your pockets. You felt a piece of paper under your fingers.', False, (255, 255, 255))
        screen.blit(textsurface3, (10, 725))

        textsurface3 = myfont.render('"Let\'s see what do we got there."', False, (255, 255, 255))
        screen.blit(textsurface3, (10, 750))

        textsurface4 = myfont.render('NEXT >>', False, (255, 255, 255))
        screen.blit(textsurface4, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))

        pygame.display.update()

        next=0
        while next==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH-120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.state='plansza_2_2'
    def plansza_2_2(self):
        screen.blit(background_plansza2_resize,(0,0))
        screen.blit(kartka_resize,(0,0))
        screen.blit(cross,(SCREEN_WIDTH/2+287-110,SCREEN_HEIGHT/2-400+40))
        pygame.display.update()
        cancel=0
        while cancel==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+287-110) and pygame.mouse.get_pos()[0]<=(SCREEN_WIDTH/2+287-110+81):
                        if pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT/2-400+40) and pygame.mouse.get_pos()[1]<=(SCREEN_HEIGHT/2-400+40+122):
                            cancel=1
                            self.state='plansza_2_3'
    def plansza_2_3(self):
        self.player.kartka1=True
        screen.blit(background_plansza2_resize,(0,0))
        pygame.display.update()
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render('"It seems that I am a wizard. Maybe I can find more pages from the diary."', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface2 = myfont.render('Where do you want to go now?', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 675))

        textsurface3 = myfont.render('SOUTH >>', False, (255, 255, 255))
        screen.blit(textsurface3, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))

        textsurface4 = myfont.render('<< WEST', False, (255, 255, 255))
        screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))
        pygame.display.update()

        next=0
        while next==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza1()
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH-300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza4()

    def plansza_2_again(self):
        screen.blit(background_plansza2_resize,(0,0))
        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 150))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-150))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render('"My ship is broken. I need to find every piece of my diary and come back here."', False, (255, 255, 255))
        screen.blit(textsurface, (10, 750))

        textsurface2 = myfont.render('Only then I will be able to go home', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 775))

        textsurface3 = myfont.render('SOUTH >>', False, (255, 255, 255))
        screen.blit(textsurface3, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))

        textsurface4 = myfont.render('<< WEST', False, (255, 255, 255))
        screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))
        pygame.display.update()

        next=0
        while next==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza1()
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH-300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza4()
    #def plansza_finish(self):
    def plansza_startowanie(self):
        imageX= 1400; # x coordnate of image
        imageY= 900; # y coordinate of image
        while imageX<=1400:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
            imageX =imageX - 10;
            imageY= imageY - 6.4;
            screen.blit(background_resized,(0,0))#(nazwa obrazu, pozycja 0,0 - lewy dolny róg)
            screen.blit(statek_rotated2,(imageX,imageY)) # paint to screen
            pygame.display.update()
            clock.tick(20)
            if imageX==0:
               self.state='congratulations'

    ''' PLANSZA 1 '''

    def plansza_1_1(self):
        self.player.plansza1=True
        screen.blit(plansza_zwykla_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

            #zawijanie tekstu okazało się bardziej skomplikowane, na razie wypisuje każda linjke osobno
        textsurface = myfont.render('As you go forward, in the darkness you hear an unfamiliar whisper.', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface2 = myfont.render('"South from here danger awaits, it is standing in the way of what you are trying to obtain"', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 675))

        textsurface2 = myfont.render('You look around trying to make sense of the situation but there is no one to be seen. The voice seems to just appear directly in your head. It laughs, softly.', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 700))

        textsurface3 = myfont.render('"Indulge me. I will give you a hint, provided you solve one of my riddles"', False, (255, 255, 255))
        screen.blit(textsurface3, (10, 725))

        textsurface3 = myfont.render('"If it is too much for you say- "i give up""', False, (255, 255, 255))
        screen.blit(textsurface3, (10, 750))


        pygame.display.update()

        #nie wiem czemu MOUSEBUTTONDOWN kiepsko dzialalo (50/50 szansa na zawieszenie u mnie), wiec po czasie automatycznie przelaczy sie do nastepnego "slajdu"
        pygame.time.delay(11000)

        self.state = 'plansza_1_2'




    def plansza_1_2(self):
        screen.blit(plansza1, (0,0))
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        myfont1 = pygame.font.SysFont('Times New Roman', 16)
        riddlefont = pygame.font.SysFont('Times New Roman', 40)

        textsurface4 = riddlefont.render("WHAT LIVES ON IT'S OWN SUBSTANCE,", False, (255, 255, 255))
        screen.blit(textsurface4, (100, 200))

        textsurface5 = riddlefont.render("BUT DIES AS SOON AS IT DEVOURS ITSELF ?", False, (255, 255, 255))
        screen.blit(textsurface5, (100, 250))

        textsurface = myfont.render('You think for a bit and what comes to mind is:', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface0 = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface0, (10, 675))

        textsurface6 = myfont1.render('(REMEMBER TO PRESS ENTER AFTER THE ANSWER)', False, (255, 255, 255))
        screen.blit(textsurface6, (500, 850))

        textsurface7 = myfont1.render('(IF YOU DO NOT KNOW THE ANSWER WRITE "I GIVE UP")', False, (255, 255, 255))
        screen.blit(textsurface7, (487, 875))

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)

        if user_text == 'candle' or user_text == 'a candle':
            textsurface6 = myfont.render('"Correct! As reward, as promised, you get a hint."', True, (255, 255, 255))
            screen.blit(textsurface6, (10, 700))
            textsurface7 = myfont.render('"South from here something new awaits. You should not expect kindness. Stealth is your best bet', True, (255, 255, 255))
            screen.blit(textsurface7, (10, 725))
            textsurface8 = myfont.render('"Now go, adventurer..."', True, (255, 255, 255))
            screen.blit(textsurface7, (10, 725))
            pygame.display.flip()
            pygame.time.delay(4000)
            self.state = 'move_from1'

        elif user_text == 'i give up' or user_text == 'give up':
            textsurface6 = myfont.render('"Too bad. Good luck without knowing the hint. You are gonna need it"', True, (255, 255, 255))
            screen.blit(textsurface6, (10, 700))
            textsurface7 = myfont.render('The voice disappers, but its omnious sound still rings in your head', True, (255, 255, 255))
            screen.blit(textsurface7, (10, 725))
            textsurface8 = myfont.render('Still, you need to move forward', True, (255, 255, 255))
            screen.blit(textsurface7, (10, 725))
            pygame.display.flip()
            pygame.time.delay(4000)
            self.state = 'move_from1'
        pygame.display.flip()

    def plansza_1_again(self): #plansza 1 gdzie nic sie nie dzieje, uruchamiana gdy gracz ponownie wejdzie na pole 1
        screen.blit(plansza_zwykla_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render('You find yourself again in this place where you encountered the mysterious voice', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface0 = myfont.render('Nothing is happening. You decide to continue moving', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 625))

        pygame.time.delay(4000)
        self.state = 'move_from1'

    def move_from1(self):
        screen.fill((0, 0, 0))
        riddlefont = pygame.font.SysFont('Times New Roman', 40)

        textsurface = riddlefont.render("It seems you could only go east or south from here.", False, (255, 255, 255))
        screen.blit(textsurface, (100, 200))

        textsurface1 = riddlefont.render("You decide to go:", False, (255, 255, 255))
        screen.blit(textsurface1, (100, 250))

        textsurface2 = riddlefont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface2, (100, 300))



        if user_text == 'east' or user_text == 'the east':
            textsurface3 = riddlefont.render("You decided to move towards the East", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 350))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.check_plansza2()

        elif user_text == 'south' or user_text == 'the south':
            textsurface3 = riddlefont.render("You decided to move towards the South", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 350))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.check_plansza4()

        pygame.display.flip()

    ''' PLANSZA 3 '''
#self.player.plansza3=True
    def plansza_3_1(self):
        self.player.plansza3=True
        screen.blit(plansza1, (0, 0))

        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect = surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2 - 700, SCREEN_HEIGHT - 250))
        myfont = pygame.font.SysFont('Times New Roman', 22)

        textsurface1 = myfont.render('It seems that you can go inside or go back south:', False, (255, 255, 255))
        screen.blit(textsurface1, (100, 675))

        textsurface1 = myfont.render('You decide to go:', False, (255, 255, 255))
        screen.blit(textsurface1, (100, 700))

        textsurface2 = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface2, (100, 725))

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(100)

        if user_text == 'south' or user_text == 'the south':
            textsurface3 = myfont.render("You decided to move towards the South", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 675))
            pygame.display.flip()

            pygame.time.delay(3000)
            self.state = 'plansza_6_1'

        if user_text == 'inside' or user_text == 'go inside':
            textsurface3 = myfont.render("You decided to go inside", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 750))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.state='inside'

    def inside(self):
        screen.blit(plansza1, (0, 0))
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect = surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2 - 700, SCREEN_HEIGHT - 250))
        myfont = pygame.font.SysFont('Times New Roman', 22)

        textsurface3 = myfont.render("As you enter the cave you see three tunnels.", False, (255, 255, 255))
        screen.blit(textsurface3, (100, 675))

        textsurface22 = myfont.render("Which tunnel you decide to enter? Left, center or right?", False, (255, 255, 255))
        screen.blit(textsurface22, (100, 700))
        textsurface2 = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface2, (100, 725))

        pygame.display.flip()

        pygame.time.delay(100)

        if user_text == 'left' or user_text == 'go left':
            textsurface33 = myfont.render("You go inside the left tunnel but unfortunately it ends with a dead end. You decide to go back", False,
                                                (255, 255, 255))
            screen.blit(textsurface33, (100, 750))
            pygame.display.flip()
            pygame.time.delay(5000)
            self.state = 'plansza_3_1'
        if user_text == 'right' or user_text == 'go right':
            textsurface18 = myfont.render("You go inside the right tunnel but unfortunately it ends with a dead end. You decide to go back", False,
                                                (255, 255, 255))

            screen.blit(textsurface18, (100, 750))
            pygame.display.flip()
            pygame.time.delay(5000)
            self.state = 'plansza_3_1'
        if user_text == 'center':
            textsurface3 = myfont.render("You decided to go through the center tunnel", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 750))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.state = 'center'
    def center(self):
        screen.blit(plansza1, (0, 0))
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect = surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2 - 700, SCREEN_HEIGHT - 250))
        myfont = pygame.font.SysFont('Times New Roman', 22)

        textsurface9 = myfont.render(
            "You walk forward for a while, until you reach an underground dome. From here you can either go up or go down",
            False,
            (255, 255, 255))
        screen.blit(textsurface9, (100, 675))
        textsurface10 = myfont.render(
            "Go up or go down?",
            False,
            (255, 255, 255))
        screen.blit(textsurface10, (100, 700))
        textsurface2 = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface2, (100, 725))
        pygame.display.flip()
        pygame.time.delay(100)
        if user_text == 'down' or user_text == 'go down':
            textsurface20 = myfont.render(
                            'You get yourself really lost in the underground tunnels but luckily you manage to find a way back to the beginning of the cave complex',
                            False,
                            (255, 255, 255))
            screen.blit(textsurface20, (100, 650))
            pygame.display.flip()
            pygame.time.delay(5000)
            self.state = 'plansza_3_1'
        if user_text == 'up' or user_text == 'go up':
            textsurface3 = myfont.render("You decided to go up", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 750))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.state = 'up'
    def up(self):
        screen.blit(plansza1, (0, 0))
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect = surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2 - 700, SCREEN_HEIGHT - 250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        textsurface7 = myfont.render(
                            'You climb to the top of the dome on some rocks and boulders, and find a small hole that leads you to a chamber with, '
                            'another set of tunnels.',
                            False,
                            (255, 255, 255))
        screen.blit(textsurface7, (100, 675))
        textsurface8 = myfont.render(
            'One of them is next to dead tree, second tunnel is next to glowing boulder, and last'
            ' one is next to large skull. ',
            False,
            (255, 255, 255))
        screen.blit(textsurface8, (100, 700))
        textsurface12 = myfont.render(
                            'Which tunnel you decide to check? One next to dead tree, glowing boulder or large skull?',
                            False,
                            (255, 255, 255))
        screen.blit(textsurface12, (100, 725))
        pygame.display.flip()

        textsurface11 = myfont.render(
                            user_text,
                            False,
                            (255, 255, 255))
        screen.blit(textsurface11, (100, 750))
        pygame.display.flip()
        pygame.time.delay(100)
        if user_text == 'glowing boulder' or user_text == 'large skull':

            textsurface10 = myfont.render(
                                'After few minutes  of walking around uncanny, same looking rocky corridors you magicaly find yourself at the beggining of the cave',
                                False,
                                (255, 255, 255))
            screen.blit(textsurface10, (100, 775))
            pygame.display.flip()
            pygame.time.delay(1000)
            self.state = 'plansza_3_1'
        if user_text == 'dead tree':
            textsurface3 = myfont.render("You decided to go through the tunnel next to dead tree", False, (255, 255, 255))
            screen.blit(textsurface3, (100,775))

            pygame.display.flip()
            pygame.time.delay(3000)
            self.state = 'tree'
    def tree(self):
        screen.blit(plansza1, (0, 0))
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect = surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2 - 700, SCREEN_HEIGHT - 250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        textsurface26= myfont.render('One step into the tunnel you find yourself falling through the mansized hole'
                            'you prepare for the worst ',
                            False, (255, 255, 255))
        screen.blit(textsurface26, (100, 675))
        textsurface26 = myfont.render('but luckily you land on piles of bones and clothes'
                                      'also, you find here another note from your journal!',
                                      False, (255, 255, 255))
        screen.blit(textsurface26, (100, 700))
        textsurface26 = myfont.render(
                                    'after you read a magic spell written on it you teleport to front of the cave',
                                      False, (255, 255, 255))
        screen.blit(textsurface26, (100, 725))
        pygame.display.update()
        pygame.time.delay(10000)
        self.player.kartka3 = True
        self.state = 'plansza_3_1'
    ''' PLANSZA 4 '''

    def plansza_4(self):
        self.player.plansza4=True
        screen.blit(plansza_kosmita_resize, (0,0))

        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        myfont1 = pygame.font.SysFont('Times New Roman', 16)

        textsurface = myfont.render('Now you realize you are in some serious trouble. You freeze completly trying to find the best way out of the situation.', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface2 = myfont.render('The situation being a weird intimidating alien right in front of you. Of course, with your luck, you would not crash on a planet with nice looking aliens.', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 675))

        textsurface2 = myfont.render('You feel like you have only two options.', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 700))

        textsurface3 = myfont.render('You could hide behind a boulder- you are not sure if it is big enough to be a good hiding spot or...', False, (255, 255, 255))
        screen.blit(textsurface3, (10, 725))

        textsurface3 = myfont.render('You could say hi to the alien and hopefully make a new exotic fun frienship.', False, (255, 255, 255))
        screen.blit(textsurface3, (10, 750))

        textsurface3 = myfont.render('You decide to: (write "hide" or "say hi")', False, (255, 255, 255))
        screen.blit(textsurface3, (10, 775))

        textsurface0 = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface0, (10, 800))

        textsurface6 = myfont1.render('(REMEMBER TO PRESS ENTER AFTER THE ANSWER)', False, (255, 255, 255))
        screen.blit(textsurface6, (500, 875))

        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(1000)

        if user_text == 'say hi':
            textsurface7 = myfont.render('You decided to say hi. What could go wrong.', False, (255, 255, 255))
            screen.blit(textsurface7, (10, 825))

            pygame.display.flip()
            pygame.time.delay(2000)
            self.state = 'plansza_4_hi'

        elif user_text == 'hide':
            textsurface7 = myfont.render('You decided to try and hide.', False, (255, 255, 255))
            screen.blit(textsurface7, (10, 825))

            pygame.display.flip()
            pygame.time.delay(2000)
            self.state = 'plansza_4_hide'

    def plansza_4_hi(self):
        screen.blit(plansza_kosmita_resize, (0,0))

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)

        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        myfont1 = pygame.font.SysFont('Times New Roman', 16)

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render('You move towards the alien with an optimistic attitude.', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface2 = myfont.render('"Hi" you say "Could I-" ', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 675))

        textsurface2 = myfont.render('Before you can finish everything goes black', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 700))

        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(8000)

        self.state = 'game_over'

    def plansza_4_hide(self):
        screen.blit(plansza_kosmita_resize, (0,0))

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)

        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        myfont1 = pygame.font.SysFont('Times New Roman', 16)

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render('You moved very slowly towards the boulder hoping the alien will not notice.', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface2 = myfont.render('You stayed behind a boulder for a while and when you heard their steps fading you could finally let your breath out', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 675))

        textsurface2 = myfont.render('You were safe. You decided to continue movig forward', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 700))

        pygame.display.update()
        pygame.time.delay(11000)

        self.state = 'move_from4'



    def plansza_4_again(self):
        screen.blit(plansza_zwykla_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render('This is the place you encountered the alien. Well, technically you are the alien here.', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface0 = myfont.render('Nothing is happening. You decide to continue moving', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 675))

        pygame.display.flip()
        pygame.event.pump()

        pygame.time.delay(4000)
        self.state = 'move_from4'

    def move_from4(self):
        screen.fill((0, 0, 0))
        riddlefont = pygame.font.SysFont('Times New Roman', 40)

        textsurface = riddlefont.render("It seems you could go north, east or south from here.", False, (255, 255, 255))
        screen.blit(textsurface, (100, 200))

        textsurface1 = riddlefont.render("You decide to go:", False, (255, 255, 255))
        screen.blit(textsurface1, (100, 250))

        textsurface2 = riddlefont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface2, (100, 300))


        if user_text == 'east' or user_text == 'the east':
            textsurface3 = riddlefont.render("You decided to move towards the East", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 350))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.check_plansza5()

        elif user_text == 'south' or user_text == 'the south':
            textsurface3 = riddlefont.render("You decided to move towards the South", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 350))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.check_plansza7()

        elif user_text == 'north' or user_text == 'the north':
            textsurface3 = riddlefont.render("You decided to move towards the North", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 350))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.check_plansza1()


        pygame.display.flip()

    ''' PLANSZA 5 '''


    def plansza_5_1(self):
        self.player.plansza5=True
        screen.blit(plansza_zwykla_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

            #zawijanie tekstu okazało się bardziej skomplikowane, na razie wypisuje każda linjke osobno
        textsurface = myfont.render('On this site you encounter a weird boulder with some words carved in it', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface2 = myfont.render('It did not look like any language you knew, yet the meaning somhow came effortlessly to you.', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 675))

        textsurface2 = myfont.render('"Hm. A riddle."- you say to yourself- "what a weird place for a boulder with a riddle"', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 700))

        textsurface3 = myfont.render('You decided to give it a try', False, (255, 255, 255))
        screen.blit(textsurface3, (10, 725))

        pygame.display.update()

        pygame.time.delay(11000)

        self.state = 'plansza_5_2'

    def plansza_5_2(self):
        screen.blit(plansza_zwykla_resize, (0,0))
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        myfont1 = pygame.font.SysFont('Times New Roman', 16)
        riddlefont = pygame.font.SysFont('Times New Roman', 40)

        textsurface4 = riddlefont.render("WHAT IS ALWAYS COMING, BUT NEVER ARRIVES?", False, (255, 255, 255))
        screen.blit(textsurface4, (100, 200))

        textsurface = myfont.render('You think for a bit and what comes to mind is:', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface0 = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface0, (10, 675))


        textsurface6 = myfont1.render('(REMEMBER TO PRESS ENTER AFTER THE ANSWER)', False, (255, 255, 255))
        screen.blit(textsurface6, (500, 850))

        textsurface7 = myfont1.render('(IF YOU DO NOT KNOW THE ANSWER WRITE "I GIVE UP")', False, (255, 255, 255))
        screen.blit(textsurface7, (487, 875))

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)

        if user_text == 'tommorow' or user_text == 'a next day' or user_text == 'the next day':
            textsurface6 = myfont.render('You carve in your answer to spoil the fun for other shipwreck survivors with memory loss', True, (255, 255, 255))
            screen.blit(textsurface6, (10, 700))
            textsurface7 = myfont.render('You smile proudly at your doing. Weirdly enough, another writing appears on the stone. it says:', True, (255, 255, 255))
            screen.blit(textsurface7, (10, 725))
            textsurface8 = myfont.render('"What lives here is fast but cannot see what moves slow"', True, (255, 255, 255))
            screen.blit(textsurface8, (10, 750))
            textsurface9 = myfont.render('A thought, that if dinosaurs lived here you would surely notice appears in your head.', True, (255, 255, 255))
            screen.blit(textsurface9, (10, 775))
            textsurface10 = myfont.render('You shrug and decide to keep that information in mind anyway. Just in case.', True, (255, 255, 255))
            screen.blit(textsurface10, (10, 800))
            pygame.display.flip()
            pygame.time.delay(17000)
            self.state = 'move_from5'

        elif user_text == 'i give up' or user_text == 'give up':
            textsurface6 = myfont.render('You wanted to solve the riddle for some fun but the answer did not come to you', True, (255, 255, 255))
            screen.blit(textsurface6, (10, 700))
            textsurface7 = myfont.render('Annoyed, you kick the boulder, but it does nothing but hurt your feet.', True, (255, 255, 255))
            screen.blit(textsurface7, (10, 725))
            textsurface8 = myfont.render('You mumble something about not wanting to do the riddle anyway and pick your next destination', True, (255, 255, 255))
            screen.blit(textsurface8, (10, 750))
            pygame.display.flip()
            pygame.time.delay(10000)
            self.state = 'move_from5'
        pygame.display.flip()

    def move_from5(self):
                screen.fill((0, 0, 0))
                riddlefont = pygame.font.SysFont('Times New Roman', 40)
                myfont1 = pygame.font.SysFont('Times New Roman', 16)

                textsurface = riddlefont.render("It seems you could go in any derection from here. North, east, south or west.", False, (255, 255, 255))
                screen.blit(textsurface, (100, 200))

                textsurface1 = riddlefont.render("You decide to go:", False, (255, 255, 255))
                screen.blit(textsurface1, (100, 250))

                textsurface2 = riddlefont.render(user_text, True, (255, 255, 255))
                screen.blit(textsurface2, (100, 300))

                textsurface6 = myfont1.render('(REMEMBER TO PRESS ENTER AFTER THE ANSWER)', False, (255, 255, 255))
                screen.blit(textsurface6, (500, 850))

                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(1000)

                if user_text == 'east' or user_text == 'the east':
                    textsurface3 = riddlefont.render("You decided to move towards the East", False, (255, 255, 255))
                    screen.blit(textsurface3, (100, 350))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    #self.check_plansza6()

                elif user_text == 'south' or user_text == 'the south':
                    textsurface3 = riddlefont.render("You decided to move towards the South", False, (255, 255, 255))
                    screen.blit(textsurface3, (100, 350))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    #self.check_plansza8()

                elif user_text == 'north' or user_text == 'the north':
                    textsurface3 = riddlefont.render("You decided to move towards the North", False, (255, 255, 255))
                    screen.blit(textsurface3, (100, 350))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    #self.check_plansza2()

                elif user_text == 'west' or user_text == 'the west':
                    textsurface3 = riddlefont.render("You decided to move towards the West", False, (255, 255, 255))
                    screen.blit(textsurface3, (100, 350))
                    pygame.display.flip()
                    pygame.time.delay(3000)
                    #self.check_plansza4()
    def plansza_5_again(self): #plansza 1 gdzie nic sie nie dzieje, uruchamiana gdy gracz ponownie wejdzie na pole 1
        screen.blit(plansza1, (0,0)) # zmień obraz na to co potem w 5
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render('You find yourself again in the place with the weird looking stone. It still looks out of place.', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface0 = myfont.render('Nothing is happening. You decide to continue moving', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 675))

        pygame.time.delay(4000)
        self.state = 'move_from5'

    ''' PLANSZA 6 '''
    def plansza_6(self):
        self.player.plansza6=True
        screen.blit(tlo_zwykle_resize, (0,0)) # zmień obraz na to co potem w 5
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)
        if self.player.plansza7==True or self.player.plansza8==True:

            textsurface = myfont.render('You keep moving forward, although you are only accompanied by sand.', False, (255, 255, 255))
            screen.blit(textsurface, (10, 650))

            textsurface0 = myfont.render('But wait, something like a rope is hanging from that rock', False, (255, 255, 255))
            screen.blit(textsurface0, (10, 675))

            textsurface1 = myfont.render('You could use it to repair a bridge.', False, (255, 255, 255))
            screen.blit(textsurface1, (10, 700))

            textsurface2 = myfont.render('"I just have to reach out...""', False, (255, 255, 255))
            screen.blit(textsurface2, (10, 720))

            textsurface3 = myfont.render('RISK', False, (255, 255, 255))
            screen.blit(textsurface3, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))

            textsurface4 = myfont.render('LEAVE IT', False, (255, 255, 255))
            screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))

            pygame.display.update()

            next=0
            while next==0:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                        pygame.quit()
                    if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                        if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH-120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.state='plansza_6_risk'
                        elif pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.state='plansza_6_leave'
        else:
            textsurface = myfont.render('You keep moving forward, although you are only accompanied by sand.', False, (255, 255, 255))
            screen.blit(textsurface, (10, 650))

            textsurface0 = myfont.render('But wait, something like a rope is hanging from that rock', False, (255, 255, 255))
            screen.blit(textsurface0, (10, 675))

            textsurface1 = myfont.render('"It might be useful."', False, (255, 255, 255))
            screen.blit(textsurface1, (10, 700))

            textsurface2 = myfont.render('"I just have to reach out...""', False, (255, 255, 255))
            screen.blit(textsurface2, (10, 720))

            textsurface3 = myfont.render('RISK', False, (255, 255, 255))
            screen.blit(textsurface3, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))

            textsurface4 = myfont.render('LEAVE IT', False, (255, 255, 255))
            screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))

            pygame.display.update()

            next=0
            while next==0:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                        pygame.quit()
                    if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                        if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.state='plansza_6_risk'
                        elif pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.state='plansza_6_leave'

    def plansza_6_risk(self):
        screen.blit(tlo_zwykle_resize, (0,0)) # zmień obraz na to co potem w 5
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)
        textsurface = myfont.render('You decided to reach for the rope.', False, (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface0 = myfont.render('You stand on the tips of your toes, reach out your hand and...', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 675))

        los=random.randint(1,3)
        if los > 1:
            self.player.lina=True
            textsurface1 = myfont.render('Somehow you menage to harvest what is left of the rope and put it to your backpack.', False,
                                (255, 255, 255))
            screen.blit(textsurface1, (10, 700))
        elif los ==1:
            textsurface1 = myfont.render('As you reach for the rope you hear worrying sound of something falling down.',False,(255, 255, 255))
            screen.blit(textsurface1, (10, 700))
            textsurface2 = myfont.render('Afraid of what it may be attached to, you abandon your attempt to take the rope.',False,(255, 255, 255))
            screen.blit(textsurface2, (10, 725))
        textsurface4 = myfont.render('NEXT >>', False, (255, 255, 255))
        screen.blit(textsurface4, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))

        pygame.display.update()
        next=0
        while next==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.state='plansza_6_leave'


    def plansza_6_leave(self):
        screen.fill((0, 0, 0))
        riddlefont = pygame.font.SysFont('Times New Roman', 40)
        myfont1 = pygame.font.SysFont('Times New Roman', 16)
        textsurface = riddlefont.render("It seems you could go north, south or west from here", False, (255, 255, 255))
        screen.blit(textsurface, (100, 200))

        textsurface1 = riddlefont.render("You decide to go:", False, (255, 255, 255))
        screen.blit(textsurface1, (100, 250))

        textsurface2 = riddlefont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface2, (100, 300))

        textsurface6 = myfont1.render('(REMEMBER TO PRESS ENTER AFTER THE ANSWER)', False, (255, 255, 255))
        screen.blit(textsurface6, (500, 850))

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(1000)

        if user_text == 'south' or user_text == 'the south':
            textsurface3 = riddlefont.render("You decided to move towards the South", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 350))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.check_plansza9()

        elif user_text == 'north' or user_text == 'the north':
            textsurface3 = riddlefont.render("You decided to move towards the North", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 350))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.check_plansza3()

        elif user_text == 'west' or user_text == 'the west':
            textsurface3 = riddlefont.render("You decided to move towards the West", False, (255, 255, 255))
            screen.blit(textsurface3, (100, 350))
            pygame.display.flip()
            pygame.time.delay(3000)
            self.check_plansza5()

    def plansza_6_again(self):
        screen.blit(tlo_zwykle_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)
        textsurface0 = myfont.render('I have been there before. Nothing to do for me', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 650))
        textsurface = myfont.render('Where do you want to go now?', False, (255, 255, 255))
        screen.blit(textsurface, (10, 675))
        textsurface3 = myfont.render('NORTH', False, (255, 255, 255))
        screen.blit(textsurface3, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))

        textsurface4 = myfont.render('WEST', False, (255, 255, 255))
        screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))

        textsurface5 = myfont.render('SOUTH', False, (255, 255, 255))
        screen.blit(textsurface5, (SCREEN_WIDTH/2-30, SCREEN_HEIGHT-60))

        pygame.display.update()
        #pygame.time.delay(11000)
        #self.state='plansza_2_2'
        next=0
        while next==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH-120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza3()
                    if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza5()
                    if pygame.mouse.get_pos()[0]<=(SCREEN_WIDTH/2-30) and pygame.mouse.get_pos()[0]<=(SCREEN_WIDTH/2+30) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza9()
    ''' PLANSZA 7 '''
    def plansza_7(self):
        self.player.plansza7=True
        screen.blit(tlo_z_mostem_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)
        textsurface0 = myfont.render('There is something strange about this planet. The sand shines like glass.', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 650))
        textsurface1 = myfont.render('You look down and a piece of paper lies by your foot. Yes, it is a page from your diary.', False, (255, 255, 255))
        screen.blit(textsurface1, (10, 675))
        textsurface2 = myfont.render('It has come all the way here.', False, (255, 255, 255))
        screen.blit(textsurface2, (10, 700))
        textsurface3 = myfont.render('NEXT >>', False, (255, 255, 255))
        screen.blit(textsurface3, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))

        pygame.display.update()

        next=0
        while next==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH-120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.state='plansza_7_kartka'
    def plansza_7_kartka(self):
        screen.blit(tlo_z_mostem_resize,(0,0))
        screen.blit(kartka_resize,(0,0)) #WSTAWIĆ KARTKE DO PLANSZY 7
        screen.blit(cross,(SCREEN_WIDTH/2+287-110,SCREEN_HEIGHT/2-400+40))
        pygame.display.update()
        cancel=0
        while cancel==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+287-110) and pygame.mouse.get_pos()[0]<=(SCREEN_WIDTH/2+287-110+81):
                        if pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT/2-400+40) and pygame.mouse.get_pos()[1]<=(SCREEN_HEIGHT/2-400+40+122):
                            cancel=1
                            self.state='plansza_7_1'
    def plansza_7_1(self):
        self.player.lina=True #DO TESTÓW

        screen.blit(tlo_z_mostem_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)
        textsurface0 = myfont.render('As you continue walking, you notice a broken bridge.', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 650))
        if self.player.lina==1:
            textsurface = myfont.render('"I can use that rope i gained earlier" you said.', False, (255, 255, 255))
            screen.blit(textsurface, (10, 675))
            textsurface2 = myfont.render('You can also go back north.', False, (255, 255, 255))
            screen.blit(textsurface2, (10,700))
            textsurface5 = myfont.render('TRY TO REPAIR THE BRIDGE', False, (255, 255, 255))
            screen.blit(textsurface5, (SCREEN_WIDTH/2+120, SCREEN_HEIGHT-60))
            textsurface4 = myfont.render('NORTH', False, (255, 255, 255))
            screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))
            pygame.display.update()
            next=0
            while next==0:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                        pygame.quit()
                    if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                        if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.state='gra_most'
                        if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.check_plansza4()
        else:
            textsurface = myfont.render('"I wish I had a piece of rope" you said.', False, (255, 255, 255))
            screen.blit(textsurface, (10, 675))
            textsurface2 = myfont.render('Nothing more to do here, you have to go back north', False, (255, 255, 255))
            screen.blit(textsurface2, (10,700))
            textsurface4 = myfont.render('NORTH', False, (255, 255, 255))
            screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))
            pygame.display.update()
            next=0
            while next==0:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                        pygame.quit()
                    if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                        if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.check_plansza4()

    def gra_most(self):
        self.angle1=90
        self.angle2=90
        self.angle3=0
        self.angle4=0
        self.angle5=0
        self.angle6=0
        self.angle7=90
        self.angle8=0
        self.angle9=180
        self.angle10=0
        self.angle11=0
        self.angle12=90
        self.state1=0
        self.state2=0
        self.state6=0
        self.state10=0
        self.state11=1
        self.state12=0
        self.wyjscie=False

        screen.blit(tlo_z_mostem_resize,(0,0))
        screen.blit(gra_most_tlo_resized,(0,0))
        '''
        POLA GRY    1  2  3  4
                    5  6  7  8
                    9 10 11 12
        Ścieżka     1 2 6 10 11 12
        '''
        linap1=pygame.transform.rotate(lina1,self.angle1)
        linap2=pygame.transform.rotate(lina2,self.angle2)
        linap3=pygame.transform.rotate(lina2,self.angle3)
        linap4=pygame.transform.rotate(lina1,self.angle4)
        linap5=pygame.transform.rotate(lina2,self.angle5)
        linap6=pygame.transform.rotate(lina1,self.angle6)
        linap7=pygame.transform.rotate(lina1,self.angle7)
        linap8=pygame.transform.rotate(lina2,self.angle8)
        linap9=pygame.transform.rotate(lina2,self.angle9)
        linap10=pygame.transform.rotate(lina2,self.angle10)
        linap11=pygame.transform.rotate(lina1,self.angle11)
        linap12=pygame.transform.rotate(lina1,self.angle12)
        screen.blit(linap1,(300,150))
        screen.blit(linap2,(500,150))
        screen.blit(linap3,(700,150))
        screen.blit(linap4,(900,150))

        screen.blit(linap5,(300,350))
        screen.blit(linap6,(500,350))
        screen.blit(linap7,(700,350))
        screen.blit(linap8,(900,350))

        screen.blit(linap9,(300,550))
        screen.blit(linap10,(500,550))
        screen.blit(linap11,(700,550))
        screen.blit(linap12,(900,550))
        pygame.display.update()

        petla=True
        while petla==True:
            if self.state1==1 and self.state2==1 and self.state6==1 and self.state10==1 and self.state11==1 and self.state12==1:
                petla=False
                self.player.most=True
                self.state='plansza_7_2'
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(300) and pygame.mouse.get_pos()[0]<=(500):
                        if pygame.mouse.get_pos()[1]>=(150) and pygame.mouse.get_pos()[1]<=(350):
                            #POLE 1
                            if self.angle1==0:
                                self.angle1=90
                                self.state1=0
                            else:
                                self.angle1=0
                                self.state1=1
                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap1=pygame.transform.rotate(lina1,self.angle1)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()

                        elif pygame.mouse.get_pos()[1]>(350) and pygame.mouse.get_pos()[1]<=(550):
                            #POLE 5
                            if self.angle5==0:
                                self.angle5=90
                            elif self.angle5==90:
                                self.angle5=180
                            elif self.angle5==180:
                                self.angle5=270
                            else:
                                self.angle5=0

                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap5=pygame.transform.rotate(lina2,self.angle5)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                        elif pygame.mouse.get_pos()[1]>(550) and pygame.mouse.get_pos()[1]<=(750):
                            #POLE 9
                            if self.angle9==0:
                                self.angle9=90
                            elif self.angle9==90:
                                self.angle9=180
                            elif self.angle9==180:
                                self.angle9=270
                            else:
                                self.angle9=0

                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap9=pygame.transform.rotate(lina2,self.angle9)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                    elif pygame.mouse.get_pos()[0]>(500) and pygame.mouse.get_pos()[0]<=(700):
                        if pygame.mouse.get_pos()[1]>=(150) and pygame.mouse.get_pos()[1]<=(350):
                            #POLE 2
                            if self.angle2==0:
                                self.angle2=90
                                self.state2=0
                            elif self.angle2==90:
                                self.angle2=180
                            elif self.angle2==180:
                                self.angle2=270
                            else:
                                self.angle2=0
                                self.state2=1

                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap2=pygame.transform.rotate(lina2,self.angle2)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                        elif pygame.mouse.get_pos()[1]>(350) and pygame.mouse.get_pos()[1]<=(550):
                            #POLE 6
                            if self.angle6==0:
                                self.angle6=90
                                self.state6=1
                            else:
                                self.angle6=0
                                self.state6=0
                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap6=pygame.transform.rotate(lina1,self.angle6)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                        elif pygame.mouse.get_pos()[1]>(550) and pygame.mouse.get_pos()[1]<=(750):
                            #POLE 10
                            if self.angle10==0:
                                self.angle10=90
                                self.state10=0
                            elif self.angle10==90:
                                self.angle10=180
                                self.state10=1
                            elif self.angle10==180:
                                self.angle10=270
                                self.state10=0
                            else:
                                self.angle10=0
                                self.state10=0

                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap10=pygame.transform.rotate(lina2,self.angle10)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                    elif pygame.mouse.get_pos()[0]>(700) and pygame.mouse.get_pos()[0]<=(900):
                        if pygame.mouse.get_pos()[1]>=(150) and pygame.mouse.get_pos()[1]<=(350):
                            #POLE 3
                            if self.angle3==0:
                                self.angle3=90
                            elif self.angle3==90:
                                self.angle3=180
                            elif self.angle3==180:
                                self.angle3=270
                            else:
                                self.angle3=0

                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap3=pygame.transform.rotate(lina2,self.angle3)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                        elif pygame.mouse.get_pos()[1]>(350) and pygame.mouse.get_pos()[1]<=(550):
                            #POLE 7
                            if self.angle7==0:
                                self.angle7=90
                            else:
                                self.angle7=0
                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap7=pygame.transform.rotate(lina1,self.angle7)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                        elif pygame.mouse.get_pos()[1]>(550) and pygame.mouse.get_pos()[1]<=(750):
                            #POLE 11
                            if self.angle11==0:
                                self.angle11=90
                                self.state11=0
                            else:
                                self.angle11=0
                                self.state11=1
                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap11=pygame.transform.rotate(lina1,self.angle11)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                    elif pygame.mouse.get_pos()[0]>(900) and pygame.mouse.get_pos()[0]<=(1100):
                        if pygame.mouse.get_pos()[1]>=(150) and pygame.mouse.get_pos()[1]<=(350):
                            #POLE 4
                            if self.angle4==0:
                                self.angle4=90
                            else:
                                self.angle4=0
                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap4=pygame.transform.rotate(lina1,self.angle4)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                        elif pygame.mouse.get_pos()[1]>(350) and pygame.mouse.get_pos()[1]<=(550):
                            #POLE 8
                            if self.angle8==0:
                                self.angle8=90
                            elif self.angle8==90:
                                self.angle8=180
                            elif self.angle8==180:
                                self.angle8=270
                            else:
                                self.angle8=0

                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap8=pygame.transform.rotate(lina2,self.angle8)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
                        elif pygame.mouse.get_pos()[1]>(550) and pygame.mouse.get_pos()[1]<=(750):
                            #POLE 12
                            if self.angle12==0:
                                self.angle12=90
                                self.state12=0
                            else:
                                self.angle12=0
                                self.state12=1
                            screen.blit(tlo_z_mostem_resize,(0,0))
                            screen.blit(gra_most_tlo_resized,(0,0))
                            linap12=pygame.transform.rotate(lina1,self.angle12)

                            screen.blit(linap1,(300,150))
                            screen.blit(linap2,(500,150))
                            screen.blit(linap3,(700,150))
                            screen.blit(linap4,(900,150))

                            screen.blit(linap5,(300,350))
                            screen.blit(linap6,(500,350))
                            screen.blit(linap7,(700,350))
                            screen.blit(linap8,(900,350))

                            screen.blit(linap9,(300,550))
                            screen.blit(linap10,(500,550))
                            screen.blit(linap11,(700,550))
                            screen.blit(linap12,(900,550))
                            pygame.display.update()
    def plansza_7_2(self):
        screen.blit(tlo_z_mostem_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)
        textsurface0 = myfont.render('The bridge looks strong enough to walk through.', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 650))
        textsurface = myfont.render('You can go east now', False, (255, 255, 255))
        screen.blit(textsurface, (10, 675))

        textsurface4 = myfont.render('NORTH', False, (255, 255, 255))
        screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))
        textsurface5 = myfont.render('EAST', False, (255, 255, 255))
        screen.blit(textsurface5, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))
        pygame.display.update()

        next=0
        while next==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza8()
                    if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza4()
    def plansza_7_again_m1(self):
        #Most zbudowany
        screen.blit(tlo_z_mostem_resize, (0,0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect= surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)
        textsurface0 = myfont.render('The bridge looks strong enough to walk through.', False, (255, 255, 255))
        screen.blit(textsurface0, (10, 650))
        textsurface4 = myfont.render('NORTH', False, (255, 255, 255))
        screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))
        textsurface5 = myfont.render('EAST', False, (255, 255, 255))
        screen.blit(textsurface5, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))
        pygame.display.update()

        next=0
        while next==0:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                    pygame.quit()
                if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                    if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza8()
                    if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                        next=1
                        self.check_plansza4()

    def plansza_7_again_m2(self):
        #Most niezbudowany
        self.state=='plansza_7_1'
    ''' PLANSZA 8 '''
    def plansza_8(self):
        self.player.plansza8=True
        if self.player.most==True:
            screen.blit(tlo_z_mostem_resize, (0,0))
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(800)
            surf = pygame.Surface((1400, 250))
            surf.fill((0, 0, 0))
            rect= surf.get_rect()
            screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
            myfont = pygame.font.SysFont('Times New Roman', 22)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(500)
            textsurface0 = myfont.render('The bridge looks strong enough to walk through... Where would you like to go?', False, (255, 255, 255))
            screen.blit(textsurface0, (10, 650))
            textsurface4 = myfont.render('NORTH', False, (255, 255, 255))
            screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))
            textsurface5 = myfont.render('EAST', False, (255, 255, 255))
            screen.blit(textsurface5, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))
            textsurface6 = myfont.render('WEST', False, (255, 255, 255))
            screen.blit(textsurface6, (SCREEN_WIDTH/2-60, SCREEN_HEIGHT-60))
            pygame.display.update()
            next=0
            while next==0:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                        pygame.quit()
                    if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                        if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.check_plansza9()
                        if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.check_plansza5()
                        if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2-60) and pygame.mouse.get_pos()[0]<=(SCREEN_WIDTH/2+60) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.check_plansza7()
        else:
            screen.blit(tlo_z_mostem_resize, (0,0))
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(800)
            surf = pygame.Surface((1400, 250))
            surf.fill((0, 0, 0))
            rect= surf.get_rect()
            screen.blit(surf, (SCREEN_WIDTH / 2-700, SCREEN_HEIGHT-250))
            myfont = pygame.font.SysFont('Times New Roman', 22)
            pygame.display.flip()
            pygame.event.pump()
            pygame.time.delay(500)
            textsurface0 = myfont.render('The bridge is broken and you cannot go through it.', False, (255, 255, 255))
            screen.blit(textsurface0, (10, 650))
            textsurface0 = myfont.render('You could try to build it from the other side.', False, (255, 255, 255))
            screen.blit(textsurface0, (10, 675))
            textsurface4 = myfont.render('NORTH', False, (255, 255, 255))
            screen.blit(textsurface4, (10, SCREEN_HEIGHT-60))
            textsurface5 = myfont.render('EAST', False, (255, 255, 255))
            screen.blit(textsurface5, (SCREEN_WIDTH-120, SCREEN_HEIGHT-60))
            pygame.display.update()
            next=0
            while next==0:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:#Krzyżyk okna wyłącza grę
                        pygame.quit()
                    if event.type==pygame.MOUSEBUTTONDOWN: #Dwie następne linijki sprawdzają, czy mysz jest na przycisku
                        if pygame.mouse.get_pos()[0]>=(SCREEN_WIDTH/2+120) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.check_plansza9()
                        if pygame.mouse.get_pos()[0]<=(300) and pygame.mouse.get_pos()[1]>=(SCREEN_HEIGHT-60):
                            next=1
                            self.check_plansza5()

    ''' PLANSZA 9 '''

    def plansza_9(self):
        self.player.plansza9 = True
        screen.blit(plansza_kosmita, (0, 0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect = surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2 - 700, SCREEN_HEIGHT - 250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render(
            'After wandering for long distance you notice an alien standing next to what appears to be page from your notebook',
            False,
            (255, 255, 255))
        screen.blit(textsurface, (10, 650))

        textsurface2 = myfont.render(
            'How will you recover your knowledge?  You can attack the alien with a stone you or you can aprroach it slowly',
            False,
            (255, 255, 255))
        screen.blit(textsurface2, (10, 675))

        textsurface2 = myfont.render(
            'Attack or approach slowly? which one it wil be?',
            False,
            (255, 255, 255))
        screen.blit(textsurface2, (10, 700))

        textsurface3 = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface3, (10, 725))

        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(100)
        pygame.display.update()
        if user_text == 'attack':
            textsurface5 = myfont.render('It seems that your attack did little to no damage. Aliens\' turn', False,
                                         (255, 255, 255))
            screen.blit(textsurface5, (10, 750))
            pygame.display.flip()
            self.state = game_over
        if user_text == 'approach slowly':
            textsurface5 = myfont.render('It worked! The alien did not see you coming at all.', False,
                                         (255, 255, 255))
            screen.blit(textsurface5, (10, 750))
            pygame.display.flip()
            self.player.kartka4 = True
            self.state = 'plansza_9_1'

    def plansza_9_1:
        screen.blit(plansza_kosmita, (0, 0))
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(800)
        surf = pygame.Surface((1400, 250))
        surf.fill((0, 0, 0))
        rect = surf.get_rect()
        screen.blit(surf, (SCREEN_WIDTH / 2 - 700, SCREEN_HEIGHT - 250))
        myfont = pygame.font.SysFont('Times New Roman', 22)
        pygame.display.flip()
        pygame.event.pump()
        pygame.time.delay(500)

        textsurface = myfont.render(
            'Where to go now? From here you can go north and west',
            False,
            (255, 255, 255))
        screen.blit(textsurface, (10, 650))
        textsurface3 = myfont.render(user_text, True, (255, 255, 255))
        screen.blit(textsurface3, (10, 675))
        if user_text == 'north':
            self.state = 'plansza6'
        if user_text == 'south':
            self.stage = 'plansza8'

    ''' PLANSZA GAME OVER'''

    def game_over(self):
        screen.fill((0, 0, 0))
        riddlefont = pygame.font.SysFont('Times New Roman', 80)

        textsurface = riddlefont.render("GAME OVER", False, (255, 255, 255))
        screen.blit(textsurface, (450, 400))

        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(4000)

        pygame.quit()

    '''CONGRATULATIONS'''
    def congratulations(self):
        screen.fill((0, 0, 0))
        riddlefont = pygame.font.SysFont('Times New Roman', 80)

        textsurface = riddlefont.render("CONGRATULATIONS", False, (255, 255, 255))
        screen.blit(textsurface, (300, 400))

        pygame.display.update()
        pygame.event.pump()
        pygame.time.delay(4000)

        pygame.quit()
    ''' STATE MENAGER '''
    def state_menager(self):
        if self.state=='intro_menu':
            self.intro_menu()
        elif self.state=='plansza_awaria':
            self.plansza_awaria()
        elif self.state=='plansza_2':
            self.plansza_2()
        elif self.state=='plansza_2_2':
            self.plansza_2_2()
        elif self.state=='plansza_2_3':
            self.plansza_2_3()
        elif self.state=='plansza_2_again':
            self.plansza_2_again()
        elif self.state == 'plansza_1_1':
            self.plansza_1_1()
        elif self.state == 'plansza_1_2':
            self.plansza_1_2()
        elif self.state == 'plansza_1_again':
            self.plansza_1_again()
        elif self.state == 'move_from1':
            self.move_from1()
        elif self.state == 'plansza_5_1':
            self.plansza_5_1()
        elif self.state == 'plansza_5_2':
            self.plansza_5_2()
        elif self.state == 'move_from5':
            self.move_from5()
        elif self.state == 'plansza_4':
            self.plansza_4()
        elif self.state =='plansza_4_again':
            self.plansza_4_again()
        elif self.state == 'move_from4':
            self.move_from4()
        elif self.state == 'plansza_4_hide':
            self.plansza_4_hide()
        elif self.state == 'plansza_4_hi':
            self.plansza_4_hi()
        elif self.state == 'game_over':
            self.game_over()
        elif self.state== 'plansza_6':
            self.plansza_6()
        elif self.state =='plansza_6_risk':
            self.plansza_6_risk()
        elif self.state == 'plansza_6_leave':
            self.plansza_6_leave()
        elif self.state== 'plansza_6_again':
            self.plansza_6_again()
        elif self.state=='gra_most':
            self.gra_most()
        elif self.state=='plansza_7':
            self.plansza_7()
        elif self.state=='plansza_7_1':
            self.plansza_7_1()
        elif self.state=='plansza_7_kartka':
            self.plansza_7_kartka()
        elif self.state=='plansza_7_2':
            self.plansza_7_2()
        elif self.state=='plansza_7_again_m1':
            self.plansza_7_again_m1()
        elif self.state=='plansza_7_again_m2':
            self.plansza_7_again_m2()
        elif self.state=='plansza_8':
            self.plansza_8()
        elif self.state=='plansza_finish':
            self.plansza_finish()
        elif self.state=='plansza_startowanie':
            self.plansza_startowanie()
        elif self.state=='congratulations':
            self.congratulations()

#inicjalizacja pygame
pygame.init()
clock=pygame.time.Clock()
game_state=GameState()
music = pygame.mixer.music.load('night in the desert.mp3')


#Tworzenie okna głównego
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
screen=pygame.display.set_mode((1400,900))
    #Tytuł i ikonka
pygame.display.set_caption("Lost in space")#Tu wpisać nazwę gry
icon=pygame.image.load('project.png')#nazwa pliku ikonki png, najlepiej z przezroczystym tłem. Jeżeli jest w innym folderze, dodać ścieżkę
pygame.display.set_icon(icon)


#Intro menu
user_text = ''
#Tło ekranu startowego
background=pygame.image.load('tlo.png')
background_resized=pygame.transform.scale(background, (SCREEN_WIDTH,SCREEN_HEIGHT))

#Intro menu
emergency_txt=pygame.image.load('emergency.png')
red_button=pygame.image.load("rec.png")
background_menu=pygame.image.load('Kokpit.PNG')
background_menu_resized=pygame.transform.scale(background_menu, (SCREEN_WIDTH,SCREEN_HEIGHT))
statek=pygame.image.load('ship.png')
statek_rotated=pygame.transform.rotate(statek,-90)
statek_rotated2=pygame.transform.rotate(statek,90)
danger=pygame.image.load('caution.png')

#plansza_6
tlo_zwykle=pygame.image.load('tło.png')
tlo_zwykle_resize=pygame.transform.scale(tlo_zwykle,(SCREEN_WIDTH,SCREEN_HEIGHT))

#GRA BUDOWANIE MOSTU
gra_most_tlo=pygame.image.load('most_tlo.png')
gra_most_tlo_resized=pygame.transform.scale(gra_most_tlo,(1400,900))
lina1=pygame.image.load('lina_prosta.png')
tlo_z_mostem=pygame.image.load('most.PNG')
tlo_z_mostem_resize=pygame.transform.scale(tlo_z_mostem,(1400,900))
lina2=pygame.image.load('lina_skret.png')
#plansza 2
background_plansza2=pygame.image.load('rakieta.PNG')
background_plansza2_resize = pygame.transform.scale(background_plansza2, (SCREEN_WIDTH,SCREEN_HEIGHT))
kartka=pygame.image.load('kartka_z_pamietnika_pierwsza.png')
kartka_resize = pygame.transform.scale(kartka,(SCREEN_WIDTH,SCREEN_HEIGHT))
cross=pygame.image.load('X.png')
#plansza 1- zagadka, hint 4
plansza_zwykla = pygame.image.load('tło.png')
plansza_zwykla_resize = pygame.transform.scale(plansza_zwykla, (SCREEN_WIDTH,SCREEN_HEIGHT))
#plansza 4 / 9
plansza_kosmita = pygame.image.load('kosmita.png')
plansza_kosmita_resize = pygame.transform.scale(plansza_kosmita, (SCREEN_WIDTH,SCREEN_HEIGHT))
#MAIN GAME LOOP


running=True
while running:

    game_state.state_menager()
    clock.tick(60)
    for event in pygame.event.get(): #zamiast wstawiania do każdej planszy osobno powinno zadziałać tutaj
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN: #daje możliwośc pisania w odpowienich polach użytkownikowi ale trzaba wcisnąć enter żeby tekst sie wyzerował na następny input
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                user_text = ''
            else:
                user_text += event.unicode
                user_text = (user_text.lower())
