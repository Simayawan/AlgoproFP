import pygame

class Twowho():
    def __init__(self, player, x, y):
        self.player = player
        self.flip = False
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100



    def controls(self, w, h, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0 #dx and dy are just the change in coordinates

        #key presses
        key = pygame.key.get_pressed()

        #check if player is player 1
        if self.player == 1 and self.health > 0:
        #Movement
            if key[pygame.K_LEFT]:
                dx -= SPEED

            if key[pygame.K_RIGHT]:
                dx += SPEED
            #jumping
            if key[pygame.K_UP] and self.jump == False:
                self.vel_y = -30 #negative because in Y coordinate, negative moves up for some reason I don't understand
                self.jump == True

            #cannot move when attack
            if self.attacking == False:

                #Attacks
                if key[pygame.K_z] or key[pygame.K_x]:
                    self.attack(surface, target)

                    #determine which atack type was used
                    if key[pygame.K_z]:
                        self.attack_type = 1

                    if key[pygame.K_x]:
                        self.attack_type = 2

        if self.player == 2 and self.health > 0:
        #Movement
            if key[pygame.K_a]:
                dx -= SPEED

            if key[pygame.K_d]:
                dx += SPEED
            #jumping
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30 #negative because in Y coordinate, negative moves up for some reason I don't understand
                self.jump == True

            #cannot move when attack
            if self.attacking == False:

                #Attacks
                if key[pygame.K_m] or key[pygame.K_n]:
                    self.attack(surface, target)

                    #determine which atack type was used
                    if key[pygame.K_m]:
                        self.attack_type = 1

                    if key[pygame.K_n]:
                        self.attack_type = 2

        #gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #ensure players stay on screen
        if self.rect.left + dx <0:
            dx = 0 - self.rect.left

        if self.rect.right + dx > w:
            dx = w - self.rect.right

        if self.rect.bottom + dy > h - 110:
            self.vel_y = 0
            self.jump = False
            dy = h - 110 - self.rect.bottom

        #ensure players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False

        else:
            self.flip = True

        #update player position
        self.rect.x += dx
        self.rect.y += dy
            
    def attack(self, surface, target):
        self.attacking == True
        attacking_rect = pygame.Rect(self.rect.centerx - (2*self.rect.width*self.flip), self.rect.y, 2*self.rect.width, self.rect.height)

        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

#draw the hitbox (temp)
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

