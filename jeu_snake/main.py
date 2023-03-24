import sys
import random
import pygame

class Jeu:
    def __init__(self):
        # permet de definir la taille de ma fenetre de jeu 
        self.ecran = pygame.display.set_mode((800,600))
        # permet de créer un titre à la fenetre
        pygame.display.set_caption('Jeu du Snake')
        # permet que le jeu finisse seulement si je perd
        self.jeu_encours = True

        # on définit les variables de position et de direction initiale du serpent
        self.serpent_position_x = 300
        self.serpent_position_y = 300
        self.serpent_direction_x = 0
        self.serpent_direction_y = 0
        # on définit la grosseur de notre serpent
        self.serpent_corps = 10
        # taille initiale du serpent
        self.taille_serpent = 1

        # on définit la position initiale de la pomme
        self.pomme_position_x = random.randrange(110,690,10)
        self.pomme_position_y = random.randrange(110,590,10)
        # on définit la grosseur de la pomme
        self.pomme = 10

        # fixer les fps
        self.clock = pygame.time.Clock()

        # on créer une liste qui recence toutes les positions du serpent
        self.position_serpent = []

        self.ecran_debut = True

        self.score = 0 



    def fonction_principale(self):

        # Avant que le jeu démarre 
        while self.ecran_debut:
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.ecran_debut = False
                self.ecran.fill((0,0,0))
                self.message('grande','Jeu du Snake',(250,160,100,50),(255,255,255))
                self.message('petite',"Le but du jeu est d'avoir le serpent le plus grand",(250,200,200,5),(240,240,240))
                self.message('petite',"Pour grandir mange autant de pommes que possible",(250,220,200,5),(240,240,240))
                self.message('petite',"Mais attention de ne pas te manger toi meme !",(250,240,200,5),(240,240,240))
                self.message('moyenne',"Appuyez sur Enter pour commencer la partie !",(180,300,200,5),(240,240,240))
                pygame.display.flip()

        # Quand on a lancé le jeu 
        while self.jeu_encours:
            # ici looper sur pygame.event.get() permet de recenser tous les event fait par le joueur. Exemple bouger la souris, appuyer sur une touche, relacher cette touche...
            for evenement in pygame.event.get():
                # le pygame.QUIT represente la croix pour fermer la fenetre de jeu
                if evenement.type == pygame.QUIT:
                    # sys.exit() c'est pour quitter la fenetre, sans ca meme en appuyant sur la croix la fenetre ne se ferme pas
                    sys.exit()

                # Créer les evenement pour bouger le serpent 
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RIGHT:
                        self.serpent_direction_x = 10
                        self.serpent_direction_y = 0                       
                    elif evenement.key == pygame.K_LEFT:
                        self.serpent_direction_x = -10
                        self.serpent_direction_y = 0                      
                    elif evenement.key == pygame.K_DOWN:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = 10
                    elif evenement.key == pygame.K_UP:
                        self.serpent_direction_x = 0
                        self.serpent_direction_y = -10


            self.serpent_mouvement()

            # faire bouger le serpent seulement si il est dans les limites du terrain 
            if self.serpent_position_x <= 100 or self.serpent_position_x >= 690 or self.serpent_position_y <= 100 or self.serpent_position_y >= 590:
                sys.exit()
            
            # Condition si le serpent mange la pomme
            if self.pomme_position_y == self.serpent_position_y and self.pomme_position_x == self.serpent_position_x:
                self.pomme_position_x = random.randrange(110,690,10)
                self.pomme_position_y = random.randrange(110,590,10)
                self.taille_serpent += 1
                self.score += 1


            tete_serpent = []
            tete_serpent.append(self.serpent_position_x)
            tete_serpent.append(self.serpent_position_y)
            
            self.position_serpent.append(tete_serpent)

            if len(self.position_serpent) > self.taille_serpent:
                self.position_serpent.pop(0)
                
            self.afficher_elements()
            self.se_mordre(tete_serpent)
            # si le serpent se mord la queue on perd
            for partie_seprent in self.position_serpent[:-1]:
                if tete_serpent == partie_seprent:
                    sys.exit()

            # afficher le score 
            self.message('grande','score : {}'.format(str(self.score)),(340,50,50,50),(255,255,255))

            # afficher les limites 
            self.limites()
            self.clock.tick(30)

            # permet de mettre a jour l'écran en continue
            pygame.display.flip()


    def limites(self):
        pygame.draw.rect(self.ecran,(255,255,255),(100,100,600,500),3)
    
    def serpent_mouvement(self):
        self.serpent_position_x += self.serpent_direction_x
        self.serpent_position_y += self.serpent_direction_y

    def afficher_elements(self):
        # ici on attribue une couleur 
        self.ecran.fill((22,41,85))
        # Afficher le Serpent 
        pygame.draw.rect(self.ecran, (0,255,0),(self.serpent_position_x,self.serpent_position_y, self.serpent_corps, self.serpent_corps))
        # Afficher la pomme
        pygame.draw.rect(self.ecran,(255,0,0),(self.pomme_position_x,self.pomme_position_y,self.pomme, self.pomme))

        self.afficher_serpent()
    
    def afficher_serpent(self):
        # afficher les autre partie du serpent 
        for partie_serpent in self.position_serpent:
            pygame.draw.rect(self.ecran,(0,255,0),(partie_serpent[0],partie_serpent[1],self.serpent_corps,self.serpent_corps))
    
    def se_mordre(self,tete_serpent):
        # si le serpent se mord la queue on perd
        for partie_seprent in self.position_serpent[:-1]:
            if tete_serpent == partie_seprent:
                sys.exit()
    
    def message(self,font,message,message_rectangle,couleur):
        if font == 'petite':
            font = pygame.font.SysFont('Lato',20,False)
        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato',30,False)
        elif font == 'grande':
            font = pygame.font.SysFont('Lato',40,True)
        message = font.render(message,True,couleur)
        self.ecran.blit(message,message_rectangle)


if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
        