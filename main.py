import pygame, os, random

pygame.init()

#  Variables for Game
gameWidth = 800
gameHeight = 600
picSize = 64
gameColumns = 5
gameRows = 4
padding = 10
leftMargin = (gameWidth - ((picSize + padding) * gameColumns)) // 2
rightMargin = leftMargin
topMargin = (gameHeight - ((picSize + padding) * gameRows)) // 2
bottomMargin = topMargin
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128,0,128)
selection1 = None
selection2 = None

# Loading the pygame screen.
screen = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption('Memory Game')
gameIcon = pygame.image.load('images/2.jpg')
pygame.display.set_icon(gameIcon)

# Load the BackGround image into Python
bgImage = pygame.image.load('Background.jpg')
bgImage = pygame.transform.scale(bgImage, (gameWidth, gameHeight))
bgImageRect = bgImage.get_rect()
font = pygame.font.SysFont("Times new Roman", 72)  
# Render the text in new surface  
text = font.render("Hello, Pygame", True, (158, 16, 16))

# Create list of Memory Pictures
memoryPictures = []
for item in os.listdir('images/'):
    memoryPictures.append(item.split('.')[0])
memoryPicturesCopy = memoryPictures.copy()
memoryPictures.extend(memoryPicturesCopy)
memoryPicturesCopy.clear()
random.shuffle(memoryPictures)

# Load each of the images into the python memory
memPics = []
memPicsRect = []
hiddenImages = []
for item in memoryPictures:
    picture = pygame.image.load(f'images/{item}.jpg')
    picture = pygame.transform.scale(picture, (picSize, picSize))
    memPics.append(picture)
    pictureRect = picture.get_rect()
    memPicsRect.append(pictureRect)

for i in range(len(memPicsRect)):
    memPicsRect[i][0] = leftMargin + ((picSize + padding) * (i % gameColumns))
    memPicsRect[i][1] = topMargin + ((picSize + padding) * (i % gameRows))
    hiddenImages.append(False)


print(memoryPictures)
print(memPics)    

print(memPicsRect)
print(hiddenImages)
 
gameLoop = True
while gameLoop:
    # Load background image
    screen.blit(bgImage, bgImageRect)

    # Input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for item in memPicsRect:
                if item.collidepoint(event.pos):
                    if hiddenImages[memPicsRect.index(item)] != True:
                        if selection1 != None:
                            selection2 = memPicsRect.index(item)
                            hiddenImages[selection2] = True
                        else:
                            selection1 = memPicsRect.index(item)
                            hiddenImages[selection1] = True

    for i in range(len(memoryPictures)):
        if hiddenImages[i] == True:
            screen.blit(memPics[i], memPicsRect[i])
        else:
            pygame.draw.rect(screen, WHITE, (memPicsRect[i][0], memPicsRect[i][1], picSize, picSize))
    pygame.display.update()

    if selection1 != None and selection2 != None:
        if memoryPictures[selection1] == memoryPictures[selection2]:
            selection1, selection2 = None, None
        else:
            pygame.time.wait(1000)
            hiddenImages[selection1] = False
            hiddenImages[selection2] = False
            selection1, selection2 = None, None

    win = 1
    for number in range(len(hiddenImages)):
        win *= hiddenImages[number]

    if win == 1:
        gameLoop=False
             

    pygame.display.update()

pygame.quit()