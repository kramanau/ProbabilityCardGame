import pygame
import random
import time

pygame.init()

##DISPLAY##
display_width = 800
display_height = 600

##COLORS##
grey = (100,100,100)
red = (242,15,15)
green = (28,157,0)
white = (255,255,255)
black = (0,0,0)

##VARIABLES##
deck = [None] * 52

##CARDOBJECT##
class card(object):
    value = 0
    color = ""
    suit = ""
    picture = ""
    played = False

    def __init__(self, value, color, suit, picture):
        self.value = value
        self.color = color
        self.suit = suit
        self.picture = picture

for num in range(0,13):
    if(num == 10 or num == 11 or num == 12):
        deck[num] = card(10, "black", "club", pygame.image.load('club'+str(num)+'.png'))
    else:
        deck[num] = card(num + 1, "black", "club", pygame.image.load('club'+str(num)+'.png'))
for num in range(13,26):
    if(num == 23 or num == 24 or num == 25):
        deck[num] = card(10, "black", "spade" ,pygame.image.load('spade'+str(num)+'.png'))
    else:
        deck[num] = card(num - 12, "black", "spade" ,pygame.image.load('spade'+str(num)+'.png'))
for num in range(26,39):
    if(num == 36 or num == 37 or num == 38):
        deck[num] = card(10, "red", "heart", pygame.image.load('heart'+str(num)+'.png'))
    else:
        deck[num] = card(num - 25, "red", "heart", pygame.image.load('heart'+str(num)+'.png'))
for num in range(39,52):
    if(num == 49 or num == 50 or num == 51):
        deck[num] = card(10, "red", "diamond", pygame.image.load('diamond'+str(num)+'.png'))
    else:
        deck[num] = card(num - 38, "red", "diamond", pygame.image.load('diamond'+str(num)+'.png'))

##GAMEWINDOW+CLOCK##
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Cards")
clock = pygame.time.Clock()

##PICTURES##
title_image = pygame.image.load('cards.png')
felt = pygame.image.load('felt.jpg')
title_text = pygame.image.load('cardstitle.png')
carddeck = pygame.image.load('deckback.png')

##QUITTINGGAME##
def quitgame():
    pygame.quit()
    quit()

##TEXTOBJECTS##
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def textButton(text,xloc,yloc,width,height,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(gameDisplay, white,(xloc,yloc,width,height))
    displaytext = pygame.font.SysFont("comicsansms", 30)
    textSurf, textRect = text_objects(text, displaytext, black)
    textRect.center = ((xloc+(width/2),(yloc+(height/2))))
    gameDisplay.blit(textSurf, textRect)

    if xloc+width > mouse[0] > xloc and yloc+height > mouse[1] > yloc:
        if click[0] == 1 and action != None:
            action()

def colorBox(xloc,yloc,width,height,color):
    pygame.draw.rect(gameDisplay,color,(xloc,yloc,width,height))

def textBox(text,xloc,yloc,width,height,color, fcolor):
    pygame.draw.rect(gameDisplay, color, (xloc,yloc,width,height))
    displaytext = pygame.font.SysFont("comicsansms", 30)
    textSurf, textRect = text_objects(text, displaytext, fcolor)
    textRect.center = ((xloc+(width/2),(yloc+(height/2))))
    gameDisplay.blit(textSurf, textRect)

##CHOOSINGGAMEMODE##
def choosegame():
    choosen = False
    while not choosen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(felt,(0,0))
        textBox("Choose your game", display_width / 2 - 150, display_height / 2 - 250, 300, 50, white, black)
        textButton("Red / Black" , display_width/2 - 300, display_height/2 - 100, 200, 200, redOrBlack)
        textButton("21", display_width / 2, display_height / 2 - 100, 200, 200, twenty_one)
        textButton("Quit", display_width - 200, display_height - 100, 200, 100, quitgame)
        pygame.display.update()
        clock.tick(30)

##GUESSINGNUMBER##
def randomCard():
    rand = random.randint(0,51)
    return rand

##REDORBLACKGAME##
def redOrBlack():
    guess = 0
    gameLoop = True
    attempt = 0
    correct = 0
    selected = carddeck
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(felt,(0,0))
        selected = pygame.transform.scale(selected,(120,145))
        gameDisplay.blit(selected,(display_width/2 - 60 ,display_height/2 - 75))
        textBox(str(attempt),display_width/ 2 - 300, display_height / 2 - 250, 100, 100, white, black)
        textBox(str(correct),display_width/ 2 + 200, display_height / 2 - 250, 100, 100, green, white)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        textBox("Guess the next color", display_width/ 2 - 150, display_height / 2 - 250, 300, 50, white, black)
        textBox("Red", display_width / 2 - 250, display_height - 200, 125, 100, red, white)
        textBox("Black", display_width / 2 + 125, display_height - 200, 125, 100, black, white)
        textBox("Back", display_width /2 - 50, display_height - 100, 100, 100, grey, white)
        if guess == 1:
            textBox('Nice guess',display_width/ 2 - 75, display_height / 2 - 200, 150, 50, green, white)
        elif guess == 2:
            textBox('Nice try',display_width/ 2 - 75, display_height / 2 - 200, 150, 50, red, white)
        elif guess == 3:
            textBox('Nice guess',display_width/ 2 - 75, display_height / 2 - 200, 150, 50, green, white)
        elif guess == 4:
            textBox('Nice try',display_width/ 2 - 75, display_height / 2 - 200, 150, 50, red, white)
        ##RED GUESS##
        if (display_width / 2 - 250) + 125 > mouse[0] > (display_width / 2 - 250) and (display_height - 200 + 100) > mouse[1] > (display_height - 200):
            if click[0] == 1:
                attempt+=1
                selectedCard = deck[randomCard()]
                if(selectedCard.color == "red"):
                    selected = selectedCard.picture
                    guess = 1
                    correct+=1
                else:
                    selected = selectedCard.picture
                    guess = 2
                time.sleep(.15)
        ##BLACK GUESS##
        elif (display_width / 2 + 125) + 125 > mouse[0] > (display_width / 2 + 125) and (display_height - 200 + 100) > mouse[1] > (display_height - 200):
            if click[0] == 1:
                attempt+=1
                selectedCard = deck[randomCard()]
                if(selectedCard.color == "black"):
                    selected = selectedCard.picture
                    guess = 3
                    correct+=1
                else:
                    selected = selectedCard.picture
                    guess = 4
                time.sleep(.15)
        elif (((display_width / 2 - 50) + 100> mouse[0] > (display_width /2 - 50)) and ((display_height - 100) + 100 > mouse[1] > (display_height - 100))):
            if click[0] == 1:
                gameLoop = False
                gameDisplay.blit(felt,(0,0))

        pygame.display.update()
        clock.tick(30)
    return

##DEALING PROMPT
def dealing():
    dealing = True
    while dealing:
        textBox("Dealing . . .", display_width/2 - 137.5, display_height/2 - 75, 275, 75, black, white)
        pygame.display.update()
        clock.tick(30)
        dealing = False
        time.sleep(1)
    return

def updateScore(pScore,dScore):
    textBox("You: " + str(pScore),100,200,200,100,white,black)
    textBox("Dealer: " + str(dScore),500,200,200,100,white,black)

def updateDecks(playerDeck,dealerDeck,pdealtCards,ddealtCards):
    for num in range(0,pdealtCards):
        gameDisplay.blit(playerDeck[num].picture,(180 + (num * 20),360))
    for num in range(0,ddealtCards):
        gameDisplay.blit(dealerDeck[num].picture,(180 + (num * 20),60))

##TWENTY ONE GAME
def twenty_one():
    playerDeck = [card] * 21
    dealerDeck = [card] * 21
    pdealtCards = 0
    ddealtCards = 0
    playerScore = 0
    stood = False
    newGame = True
    dealerScore = 0
    running = True
    while running:
        gameDisplay.blit(felt,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        gameDisplay.blit(pygame.transform.scale(carddeck,(120,145)),(display_width/2 - 60, display_height/2 - 112))
        textBox("Back", display_width /2 - 50, display_height - 100, 100, 100, grey, white)
        if (((display_width / 2 - 50) + 100> mouse[0] > (display_width /2 - 50)) and ((display_height - 100) + 100 > mouse[1] > (display_height - 100))):
            if click[0] == 1:
                running = False
        colorBox(150,350,500,125,green)
        colorBox(150,50,500,125,red)
        textBox("Hit",175,485,125,100, white, black)
        textBox("Stand", display_width - 300, 485, 125, 100, white, black)
        if(newGame):
            stood = False
            playerDeck = [card] * 21
            dealerDeck = [card] * 21
            dealing()
            playerDeck[0] = deck[randomCard()]
            playerDeck[1] = deck[randomCard()]
            pdealtCards = 2
            dealerDeck[0] = deck[randomCard()]
            ddealtCards = 1
            playerScore = playerDeck[0].value + playerDeck[1].value
            dealerScore = dealerDeck[0].value + dealerDeck[1].value
            newGame = False

        updateScore(playerScore,dealerScore)
        updateDecks(playerDeck,dealerDeck,pdealtCards,ddealtCards)

        if((175 + 125 > mouse[0] > 175) and (485 + 100> mouse[1] > 485)):
            if click[0] == 1:
                playerDeck[pdealtCards] = deck[randomCard()]
                playerScore += playerDeck[pdealtCards].value
                pdealtCards += 1
                time.sleep(.5)

        if(playerScore > 21):
            updateDecks(playerDeck,dealerDeck,pdealtCards,ddealtCards)
            updateScore(playerScore,dealerScore)
            textBox("Dealer Wins", display_width/2 - 137.5, display_height/2 - 75, 275, 75, black, white)
            pygame.display.update()
            time.sleep(1)
            newGame = True

        if(playerScore == 21):
            updateDecks(playerDeck,dealerDeck,pdealtCards,ddealtCards)
            updateScore(playerScore,dealerScore)
            textBox("You Win!", display_width/2 - 137.5, display_height/2 - 75, 275, 75, black, white)
            pygame.display.update()
            time.sleep(1)
            newGame = True

        if((display_width - 300 + 125 > mouse[0] > display_width - 300) and (485 + 100> mouse[1] > 485)):
            if click[0] == 1:
                stood = True
                while(dealerScore < playerScore):
                    dealerDeck[ddealtCards] = deck[randomCard()]
                    dealerScore += dealerDeck[ddealtCards].value
                    ddealtCards += 1
                    updateDecks(playerDeck,dealerDeck,pdealtCards,ddealtCards)
                    updateScore(playerScore,dealerScore)
                    pygame.display.update()
                    time.sleep(.5)

        if(dealerScore > 21):
            textBox("You Win!", display_width/2 - 137.5, display_height/2 - 75, 275, 75, black, white)
            pygame.display.update()
            time.sleep(1)
            newGame = True
        elif(stood and dealerScore > playerScore):
            textBox("Dealer Wins", display_width/2 - 137.5, display_height/2 - 75, 275, 75, black, white)
            pygame.display.update()
            time.sleep(1)
            newGame = True
        elif(stood and dealerScore == playerScore):
            textBox("Push", display_width/2 - 137.5, display_height/2 - 75, 275, 75, black, white)
            pygame.display.update()
            time.sleep(1)
            newGame = True

        pygame.display.update()
        clock.tick(30)
    return

##MAINMENU##
def main_menu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(felt,(0,0))
        gameDisplay.blit(title_image,((display_width/2 - 120),(display_height/2) - 275))
        gameDisplay.blit(title_text, ((display_width/2- 170,display_height/2 - 100)))
        textButton("Quit",display_width - 200, display_height - 100, 200, 100, quitgame)
        textButton("Play",0, display_height - 100, 200,100, choosegame)
        pygame.display.update()
        clock.tick(30)

main_menu()

pygame.quit()
quit()