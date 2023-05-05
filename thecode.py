##### 0 = bedroom, 1 = livingroom, 2 = frontdoor, 3 = backyard, 6 = kitchen.
app.setMaxShapeCount(100000)
#####scene switch
app.sceneswitch = 0


#TextBox
Rect(0, 340, 400, 60, fill = 'snow')
Rect(0, 340, 400, 2)

direction = Oval(30, 30, 10, 5 , fill = "pink")
app.armSwingFront = True
app.legSwingFront = True
app.legTwoSwingFront = True
app.counter = 0
armRight = Line(28, 43, 28, 50, lineWidth = 3, fill = 'darkSalmon')
armRight2 = Line(28, 43, 28, 50, lineWidth = 3, fill = 'darkSalmon')
armRight.toFront()
legRight = Line(28, 50, 28, 60, lineWidth = 4, fill = 'darkSalmon')
legRight2 = Line(28, 50, 28, 60, lineWidth = 4, fill = 'darkSalmon')
fixeddirection = Oval(30, 30, 10, 5 , fill = "pink")
pinkHairRight = Polygon(25, 30, 25, 37, 23, 43, 21, 46, 17, 52, 19, 48, 17, 50, 17, 42, 19, 35, 21, 30, 25, 27, 32, 27, fill = "pink")
pinkHairLeft = Polygon(20, 32, 24, 27, 27, 26, 34, 28, 38, 36, 44, 45, 47, 50, 46, 55, 42, 52, 40, 50, 39, 47, 35, 38, 33, 31, fill = "pink")
pinkHairRight.centerX = direction.centerX - 5
pinkHairLeft.centerX = direction.centerX - 5
pinkHairRight.centerY = direction.centerY + 10
pinkHairLeft.centerY = direction.centerY + 11


###livingroom loops
Floor = Group()
Stairs = Group()


###doortolivingroom (from bedroom)
toLivingRoom = Rect(0, 260, 5, 80, fill = 'peru')

###door to bedroom(from livingroom)
toBedroom = Rect(225, 140, 5, 50, fill = "maroon")

#door to backyard(from livingroom)
toBackyard = Rect(155, 0, 50, 5, fill = "maroon")

#door to frontdoor(from livingroom)
toFrontDoor = Rect(0, 210, 10, 130, fill = 'maroon')

#door to kitchen(from livingroom)
toKitchen = Rect(225, 50, 5, 50, fill = "maroon")

# back to living room(from outside)
toLivingRoom2 = Line(240, 220, 300, 220, lineWidth = 0.05)

###Kitchen
toLivingRoom3 = Rect(0, 240, 5, 50, fill = "maroon")

###backyard
ToLivingRoom4 = Line(80, 157, 110, 157, lineWidth = 0.05)

###bedroom
#bed
bedside = Line(85, 40, 85, 145, lineWidth = 0.05)
bedbottom = Line(0, 145, 85, 145, lineWidth = 0.05)
#cabinet
cableft = Line(200, 50, 200, 100, lineWidth = 0.05)
cabbottom = Line(205, 95, 245, 95, lineWidth = 0.05)
cabright = Line(250, 50, 250, 100, lineWidth =0.05)
#wardrobe
wardleft = Line(350, 35, 350, 130, lineWidth = 0.05)
wardbottom = Line(350, 130, 400, 130, lineWidth = 0.05)
#shelf
shelfbottom = Line(255, 70, 340, 70, lineWidth = 0.05)

###livingroom
#table 
tableup = Line(22, 50, 128, 50, lineWidth = 0.05)
tableright = Line(128, 50, 128, 170, lineWidth = 0.05)
tablebottom = Line(22, 160, 128, 160, lineWidth = 0.05)
tableleft = Line(22, 50, 22, 170, lineWidth = 0.05)

#Chair1
Chair1right = Line(90, 35, 90, 50, lineWidth = 0.05)
Chair1up = Line(50, 15, 93, 15, lineWidth = 0.05)
Chair1left = Line(53, 35, 53, 50, lineWidth = 0.05)

#Chair2
Chair2right = Line(92, 170, 92, 210, lineWidth = 0.05)
Chair2up = Line(52, 185, 91, 185, lineWidth = 0.05)
Chair2left = Line(52, 170, 52, 210, lineWidth = 0.05)

#didn't build
right = Line(316, 250, 316, 400, lineWidth = 0.05)
top = Line(230, 250, 400, 250, lineWidth = 0.05)
#####outside
houseLeft = Line(60, 95, 60, 245, lineWidth = 0.05)
houseBottom = Line(60, 212, 340, 212, lineWidth = 0.05)
houseRight = Line(340, 95, 340, 245, lineWidth = 0.05)

#####backyard
###Tree
Treeleft = Line(305, 148, 294, 225, lineWidth = 0.05)
Treebottom = Line(294, 225, 400, 220, lineWidth = 0.05)
###house
Housebottom2 = Line(35, 154, 285, 154, lineWidth = 0.005)
HouseLeft2 = Line(35, 185, 35, 85, lineWidth = 0.05)

#when pink girl walking 
pinkHairGirl = Group(
    armRight2,
    ###Skirt
    #fourth layer
    Circle(24.5, 49, 3, fill = "white", border = "pink", borderWidth = 1),
    Circle(27, 49, 3, fill = "white", border = "pink", borderWidth = 1),
    Circle(29.5, 49, 3, fill = "white", border = "pink", borderWidth = 1),
    Circle(32.5, 49, 3, fill = "white", border = "pink", borderWidth = 1),
    
    #third layer
    Circle(25, 46, 3, fill = "white", border = "pink", borderWidth = 1),
    Circle(28, 46, 3, fill = "white", border = "pink", borderWidth = 1),
    Circle(32, 46, 3, fill = "white", border = "pink", borderWidth = 1),
    
    #second layer
    Circle(30.5, 43, 3, fill = "white", border = "pink", borderWidth = 1),
    Circle(26.5, 43, 3, fill = "white", border = "pink", borderWidth = 1),
    
    #first layer
    Circle(28.5, 40, 3, fill = "white", border = "pink", borderWidth = 1),
    
    #body
    Circle(28, 35, 5, fill = 'lightSalmon'),
    

    #arm and leg
    legRight, 
    legRight2, 
    armRight, 
    pinkHairRight, 
    pinkHairLeft,
    direction,
    )
#direction changing
pinkHairLeft.visible = False

##### bedroom
bed = Group(
    Rect(0, 40, 85, 100, fill = 'whiteSmoke'),
    Rect(0, 140, 85, 20, fill = 'lavender'),
    Rect(20, 45, 40, 15, fill = 'silver'),
    Rect(0, 65, 85, 80, fill = 'pink'),
    Rect(0, 65, 85, 15, fill = 'azure'),
    Rect(48, 63, 10, 15, fill = 'darkRed'),
    bedside, 
    bedbottom,
    )

wardrobe = Group(
    Rect(350, 35, 50, 30, fill = 'burlyWood'),
    Rect(350, 65, 50, 100, fill = 'darkGoldenrod'),
    )
    
cabinet = Group(
    Rect(200, 50, 50, 20, fill = 'oliveDrab'),
    Rect(200, 70, 50, 50, fill = 'olive'),
    Rect(205, 75, 40, 20, fill = 'greenYellow'),
    Rect(205, 100, 40, 15, fill = 'greenYellow'),
    Rect(210, 52, 5, 7, fill = 'crimson'),
    cableft,
    cabbottom,
    cabright,
    )
    
window = Group(    
    Rect(115, 15, 60, 40, fill = 'lightCyan'),
    Rect(110, 10, 70, 50, fill = None, border = 'mintCream', borderWidth = 5),
    Line(145, 15, 145, 55, fill = 'mintCream'),
    )
shelf = Group(
    Rect(255, 0, 85, 100, fill = 'saddleBrown'),
    Rect(260, 35, 75, 5, fill = 'peru'),
    Rect(260, 65, 75, 5, fill = "peru"),
    )    
    
for i in range(5, 80, 5):
    #first layer
    whatColor = randrange(0, 5)
    if whatColor == 0:
        bookColor = "red"

    elif whatColor == 1:
        bookColor = "green"

    elif whatColor == 2:
        bookColor = "orange"
    
    elif whatColor == 3:
        bookColor = "blue"

    elif whatColor == 4:
        bookColor = "purple"
    books = Rect(260, 20, 80-i, 15, fill = bookColor)
    shelf.add(books)
    
    #second layer
    whatColor2 = randrange(0, 5)
    if whatColor2 == 0:
        bookColor2 = "red"

    elif whatColor2 == 1:
        bookColor2 = "green"

    elif whatColor2 == 2:
        bookColor2 = "orange"
    
    elif whatColor2 == 3:
        bookColor2 = "blue"

    elif whatColor2 == 4:
        bookColor2 = "purple"
    books2 = Rect(260, 50, 80-i, 15, fill = bookColor2)
    
    shelf.add(books2)
    
    #third layer
    whatColor3 = randrange(0, 5)
    if whatColor3 == 0:
        bookColor3 = "red"

    elif whatColor3 == 1:
        bookColor3 = "green"

    elif whatColor3 == 2:
        bookColor3 = "orange"
    
    elif whatColor3 == 3:
        bookColor3 = "blue"

    elif whatColor3 == 4:
        bookColor3 = "purple"
    books3 = Rect(260, 80, 80-i, 15, fill = bookColor3)
    
    shelf.add(books3)


##### entire bedroom
Bedroom = Group(
    Rect(0, 0, 400, 400, fill = 'lemonChiffon'),
    Rect(0, 0, 400, 85, fill = "skyBlue", opacity = 75),
    bed,
    wardrobe,
    cabinet,
    window,
    toLivingRoom,
    shelf,
    Rect(0, 340, 400, 60, fill = 'snow'),
    Rect(0, 340, 400, 2),

    )

###livingroom

#for y in range(0, 211, 15):
#    for x in range(0, 240, 10):
##        bricks = Rect(x, y, 7, 13, fill = 'peru')
 #       Floor.add(bricks)
        
for x in range(0, 170, 5):
    if x % 10 == 0:
        even = Rect(x+240, 250, 5, 90, fill = 'saddleBrown')
        Stairs.add(even)
    else:
        odd = Rect(x+240, 250, 5, 90, opacity = 50)
        odd2 = Rect(x+240, 250, 5, 90, fill = 'burlyWood')
        Stairs.add(odd, odd2)
    
    
DiningTable = Group(
    Rect(22, 50, 106, 120, fill = 'sienna'),
    Line(25, 170, 25, 190, lineWidth = 5),
    Line(125, 170, 125, 190, lineWidth = 5),
    Line(25, 170, 25, 190, lineWidth = 5, fill = 'sienna', opacity = 50),
    Line(125, 170, 125, 190, lineWidth = 5, fill = 'sienna', opacity = 50),
    ###vase
    Line(73, 100, 73, 70, fill = 'yellowGreen'),
    Star(70, 72, 10, 6, fill = 'lightGreen'),
    Circle(70, 72, 3, fill = 'lightGoldenrodYellow'),
    Oval(73, 100, 10, 20, fill = 'aliceBlue'),
    )

Chair1 = Group(
    Rect(53, 15, 40, 35, fill = 'chocolate'),
    )
        
Chair2 = Group(
    Rect(53, 135, 40, 60, fill = 'chocolate'),
    Rect(53, 195, 5, 20, fill = 'brown'),
    Rect(88, 195, 5, 20, fill = "brown"),
    )
    
    
##### entire livingroom
LivingRoom = Group(
    Rect(0, 0, 400, 400, fill = 'beige'),
    Floor,
    Chair1,
    DiningTable,
    Chair2,
    Rect(230, 0, 170, 250),
    Stairs,
    toBedroom,
    toBackyard,
    Rect(0, 70, 3, 70, fill = 'mistyRose'),
    Polygon(0, 80, 230, -20, 243, 342, 0, 125, fill = 'yellow', opacity = 10),
    Rect(0, 0, 400, 400, fill = 'ivory', opacity = 40),
    Rect(128, 50, 20, 120, opacity = 20),
    Polygon(128, 50, 148, 55, 148, 185, 128, 190, opacity = 20),
    Line(55, 215, 71, 205, opacity = 20, lineWidth = 5),
    Line(91, 215, 105, 205, opacity = 20, lineWidth = 5),
    Polygon(88, 205, 69, 205, 69, 195, 88, 195, opacity = 20),
    Polygon(93, 148, 105, 134, 128, 134, 128, 170, 105, 205, 93, 215, opacity = 20),
    Polygon(93, 33, 107, 22, 128, 50, 93, 50, opacity = 20),
    toFrontDoor,
    toKitchen,
    right,
    top,
    Rect(0, 340, 400, 60, fill = 'snow'),
    Rect(0, 340, 400, 2),
    )
### flowers
Flowers = Group()
quantity = randrange(5, 20)
for i in range(quantity):
    FlowersX = randrange(0, 400)
    FlowersY = randrange(250, 340)
    whatColorFlower = randrange(0, 5)
    if whatColorFlower == 0:
        ColorFlower = 'lavenderBlush'

    elif whatColorFlower == 1:
        ColorFlower = 'lightGoldenrodYellow'

    elif whatColorFlower == 2:
        ColorFlower = 'cornSilk'
    
    elif whatColorFlower == 3:
        ColorFlower = 'lightCyan'

    elif whatColorFlower == 4:
        ColorFlower = 'gainsboro'
    
    Flower1 = Star(FlowersX, FlowersY, 8, 6, roundness = 80, fill = ColorFlower)
    
    whatColorFlowerCenter = randrange(0, 5)
    if whatColorFlowerCenter == 0:
        ColorFlowerCenter = "red"

    elif whatColorFlowerCenter == 1:
        ColorFlowerCenter = "green"

    elif whatColorFlowerCenter == 2:
        ColorFlowerCenter = "orange"
    
    elif whatColorFlowerCenter == 3:
        ColorFlowerCenter = "blue"

    elif whatColorFlowerCenter == 4:
        ColorFlowerCenter = "purple"
    Flower2 = Circle(FlowersX, FlowersY, 4, fill = ColorFlowerCenter)
    Flowers.add(Flower1, Flower2)
    
##### entire outdoor

outdoor = Group(
    Rect(0, 0, 400, 120, fill = "skyBlue"),
    Circle(350, 50, 150, fill = "yellow", opacity = 10),
    Rect(0, 120, 400, 280, fill = 'lightGreen'),
    Star(350, 50, 35, 400, fill=gradient('orange', 'yellow', 'orangeRed')),
    Rect(60, 95, 280, 150, fill = 'lavenderBlush'),
    Rect(110, 130, 70, 40, fill = 'azure'),
    Rect(105, 125, 80, 50, fill = None, border = 'white', borderWidth = 5),
    Line(110, 150, 180, 150, fill = "white", lineWidth = 5),
    Line(145, 130, 145, 170, fill = "white", lineWidth = 5),
    Polygon(200, 0, 360, 95, 45, 95, fill = 'azure', ),
    Rect(240, 140, 60, 105, fill = 'gainsboro'),
    Circle(290, 192.5, 5, fill = 'dimGray'),
    Rect(175, 30, 50, 50, fill = 'lightSkyBlue'),
    Rect(170, 25, 60, 60, fill = None, border = 'lavender', borderWidth = 5),
    Line(200, 30, 200, 80, fill = "lavender", lineWidth = 3),
    Line(140, 90, 260, 90, lineWidth = 5, fill = 'lightSteelBlue'),
    Line(142.5, 55, 142.5, 90, lineWidth = 5, fill = 'lightSteelBlue'),
    Line(257.5, 55, 257.5, 90, lineWidth = 5, fill = 'lightSteelBlue'),
    Line(142.5, 57.5, 257.5, 57.5, lineWidth = 5, fill = 'lightSteelBlue'),
    Line(165.5, 55, 165.5, 90, lineWidth = 5, fill = 'lightSteelBlue'),
    Line(188.5, 55, 188.5, 90, lineWidth = 5, fill = 'lightSteelBlue'),
    Line(211.5, 55, 211.5, 90, lineWidth = 5, fill = 'lightSteelBlue'),
    Line(234.5, 55, 234.5, 90, lineWidth = 5, fill = 'lightSteelBlue'),
    Line(257.5, 55, 257.5, 90, lineWidth = 5, fill = 'lightSteelBlue'),
    Flowers,
    Rect(0, 340, 400, 60, fill = 'snow'),
    Rect(0, 340, 400, 2),
    )



###kitchen
#Floor2 = Group()
#for y in range(190, 400, 16):
#    for x in range(0, 400, 10):
#        bricks2 = Rect(x, y, 7, 13, fill = 'ghostWhite')
#        Floor2.add(bricks2)

#sink
Sink = Group(
    Rect(190, 150, 90, 50, fill = 'burlyWood', border = "black"),
    Line(235, 150, 235, 200),
    Rect(225, 170, 5, 10),
    Rect(240, 170, 5, 10),
    )



##### entire kitchen

Kitchen = Group(
    Rect(0, 0, 400, 400, fill = 'blanchedAlmond'),
#    Floor2,
    Rect(0, 0, 400, 200, fill = 'lightSteelBlue'),
    Rect(290, 60, 110, 5, fill = "white"),
    Polygon(290, 60, 320, 30, 320, 0, 370, 0, 370, 30, 400, 60, fill = gradient("silver", 'gray', start = "bottom")),
    Rect(0, 50, 80, 150, fill = 'snow'),
    Line(0, 55, 75, 55, lineWidth = 0.5),
    Line(75, 55, 75, 120, lineWidth = 0.5),
    Line(0, 120, 75, 120, lineWidth = 0.5),
    Line(5, 135, 75, 135, lineWidth = 0.5),
    Line(5, 135, 5, 195, lineWidth = 0.5),
    Line(75, 135, 75, 195, lineWidth = 0.5),
    Line(5, 195, 75, 195, lineWidth = 0.5),
    Rect(60, 70, 6, 40, opacity = 20),
    Rect(15, 145, 50, 6, opacity = 20),
    
    #cooktop
    Rect(80, 125, 320, 80, fill = 'lightBlue'),
    Rect(290, 145, 110, 10, fill = "mintCream"),
    Line(80, 145, 400, 145, lineWidth = 0.5),
    Rect(290, 125, 110, 20, fill = 'mintCream'),
    Circle(316.5, 150, 3, fill = 'silver'),
    Circle(376.5, 150, 3, fill = 'silver'),
    
    Polygon(313, 130, 307, 132, 307, 135, 313, 134),
    Polygon(320, 130, 326, 132, 326, 135, 320, 134),
    
    Polygon(373, 130, 367, 132, 367, 135, 373, 134),
    Polygon(380, 130, 386, 132, 386, 135, 380, 134),
    
    #sink
    Rect(200, 127, 70, 15, fill = 'gainsboro'),
    Rect(232.5, 105, 5, 22, fill = 'darkGray'),
    Rect(232.5, 105, 5, 10, fill = 'dimGray'),
    toLivingRoom3, Sink,
    Rect(0, 340, 400, 60, fill = 'snow'),
    Rect(0, 340, 400, 2),
    )



###backyard stuff
Flowers2 = Group()
quantity2 = randrange(5, 20)
for i in range(quantity2):
    FlowersX2 = randrange(0, 400)
    FlowersY2 = randrange(195, 400)
    whatColorFlower2 = randrange(0, 5)
    if whatColorFlower2 == 0:
        ColorFlower2 = 'lavenderBlush'

    elif whatColorFlower2 == 1:
        ColorFlower2 = 'lightGoldenrodYellow'

    elif whatColorFlower2 == 2:
        ColorFlower2 = 'cornSilk'
    
    elif whatColorFlower2 == 3:
        ColorFlower2 = 'lightCyan'

    elif whatColorFlower2 == 4:
        ColorFlower2 = 'gainsboro'
    
    Flower1x = Star(FlowersX2, FlowersY2, 10, 6, roundness = 60, fill = ColorFlower2)
    
    whatColorFlowerCenter2 = randrange(0, 5)
    
    if whatColorFlowerCenter2 == 0:
        ColorFlowerCenter2 = "red"

    elif whatColorFlowerCenter2 == 1:
        ColorFlowerCenter2 = "green"

    elif whatColorFlowerCenter2 == 2:
        ColorFlowerCenter2 = "orange"
    
    elif whatColorFlowerCenter2 == 3:
        ColorFlowerCenter2 = "blue"

    elif whatColorFlowerCenter2 == 4:
        ColorFlowerCenter2 = "purple"
    Flower2x = Circle(FlowersX2, FlowersY2, 4, fill = ColorFlowerCenter2)
    Flowers2.add(Flower1x, Flower2x)


backyardFine = Group(
    Rect(0, 0, 400, 150, fill = gradient("skyBlue", 'lightYellow', start = "right"), opacity = 50),
    Rect(0, 0, 400, 150, fill = "skyBlue", opacity = 50),
    Rect(0, 150, 400, 250, fill = gradient('lightGreen', 'lightGreen', "lightYellow", start = "right-bottom")),
    Rect(0, 150, 400, 250, fill = 'lightGreen', opacity = 50),
    
    Flowers2,

    Rect(35, 85, 250, 100, fill ="lavenderBlush"),
    Polygon(160, 0, 15, 85, 300, 85, fill = "azure"),
    
    #window
    Rect(205, 115, 50, 50, fill = "azure", border = "white", borderWidth = 5),
    Line(230, 115, 230, 165, lineWidth = 3, fill = "white"),
    
    #tree
    Polygon(330, 234, 287, 247, 301, 188, 305, 148,  309, 85, 311, 44, 328, 62, 341, 47, 352, 80, 350, 129, 352, 168, 370, 220, 378, 244, fill = 'saddleBrown'),
    Polygon(308, 128, 233, 109, 217, 122, 225, 105, 243, 105, 309, 106, fill = "saddleBrown"),
    Circle(326, 33, 25, fill = "chartreuse"),
    Circle(280, 16, 20, fill = 'chartreuse'),
    Circle(300, 2, 20, fill = 'chartreuse'),
    Circle(286, 2, 20, fill = 'chartreuse'),
    Circle(293, 44, 20, fill = 'chartreuse'),
    Circle(353, 33, 20, fill = "chartreuse"),
    Circle(316, 14, 20, fill = "chartreuse"),
    Circle(314, 57, 20, fill = "chartreuse"),
    Circle(306, 60, 20, fill = "chartreuse"),
    Circle(330, 65, 20, fill = "chartreuse"),
    Circle(263, 40, 20, fill = "chartreuse"),
    Circle(286, 51, 20, fill = "chartreuse"),
    Circle(266, 9, 20, fill = "chartreuse"),
    Circle(378, 47, 20, fill = "chartreuse"),
    Circle(355, 64, 20, fill = "chartreuse"),
    Circle(339, 4, 20, fill = "chartreuse"),
    Circle(382, 16, 20, fill = "chartreuse"),
    Circle(362, 7, 20, fill = "chartreuse"),
    
    Rect(81, 120, 30, 60, fill = "gainsboro"),
    Rect(75, 180, 42, 5, fill = 'antiqueWhite'),
    Circle(107, 150, 3, fill = "dimGrey"),
    ToLivingRoom4,Treeleft,Treebottom,Housebottom2,HouseLeft2,
    Rect(0, 340, 400, 60, fill = 'snow'),
    Rect(0, 340, 400, 2),
    )
    
    
    

#####switching scenes, scenes must be drawn above this line
LivingRoom.visible = False





outdoor.visible = False

Kitchen.visible = False

backyardFine.visible = False

pinkHairGirl.toFront()



# All the labels in bedroom
lab1 = Label("Sunny day!", 200, 370, size = 10, visible = False)
lab2 = Label("My paintings", 200, 370, size = 10, visible = False)
lab3 = Label("nothing here", 200, 370, size = 10, visible = False)
lab4 = Label("photo of me and my mom", 200, 370, size = 10, visible = False)
lab5 = Label("My bed and my notebook", 200, 370, size = 10, visible = False)
lab6 = Label("a cabinet, with left over coffee on top of it", 200, 370, size = 10, visible = False)
lab7 = Label("a wardrobe, stores my clothes", 200, 370, size = 10, visible = False)
lab8 = Label("a weird bookshelf, everytime you rerun the game the book change colors", 200, 370, size = 10, visible = False)

# All the labels in living room
lr1 = Label("Mon said it's dangerous upstairs", 200, 370, size = 10, visible = False)
lr2 = Label("where me and my mom sit and eat lunch", 200, 370, size = 10, visible = False)
lr3 = Label("you can't fit through between the gap", 200, 370, size = 10, visible = False)
lr4 = Label("where me and my mom sit and eat lunch", 200, 370, size = 10, visible = False)
lr5 = Label("My chair", 200, 370, size = 10, visible = False)
lr6 = Label("Mom's chair", 200, 370, size = 10, visible = False)

# All the labels in outside
o1 = Label("Mom said it's dangerous outside", 200, 370, size = 10, visible = False)
o2 = Label("this neighborgh is playing with her dog", 200, 370, size = 10, visible = False)
o3 = Label("Blocked by the tree", 200, 370, size = 10, visible = False)
o4 = Label("nothing here", 200, 370, size = 10, visible = False)
o5 = Label("Front door", 200, 370, size = 10, visible = False)
o6 = Label("used to be my favorite place", 200, 370, size = 10, visible = False)
o7 = Label("A tree my grand-grandfather planted", 200, 370, size = 10, visible = False)
o8 = Label("Nope, you can't fit through this one too", 200, 370, size = 10, visible = False)
o9 = Label("the window to kitchen!", 200, 370, size = 10, visible = False)
o10 = Label("this neighborgh is working on his garden", 200, 370, size = 10, visible = False)
o11 = Label("Water pipes and garden stuff", 200, 370, size = 10, visible = False)

# All the labels in kitchen
k1 = Label("nothing here", 200, 370, size = 10, visible = False)
k2 = Label("bunch of photos samuel was too lazy to draw", 200, 370, size = 8, visible = False)
k3 = Label("all the kitchen stuff", 200, 370, size = 10, visible = False)


def onKeyHold(keys):
    if app.sceneswitch == 0:
        LivingRoom.visible = False
        Bedroom.visible = True
        outdoor.visible = False
        Kitchen.visible = False
        backyardFine.visible = False
        pinkHairGirl.toFront()
        
    elif app.sceneswitch == 1:
        LivingRoom.visible = True
        Bedroom.visible = False
        outdoor.visible = False
        Kitchen.visible = False
        backyardFine.visible = False
        pinkHairGirl.toFront()
        
    elif app.sceneswitch == 2:
        LivingRoom.visible = False
        Bedroom.visible = False
        outdoor.visible = True
        Kitchen.visible = False
        backyardFine.visible = False
        pinkHairGirl.toFront()
        
    elif app.sceneswitch == 3:
        LivingRoom.visible = False
        Bedroom.visible = False
        outdoor.visible = False
        Kitchen.visible = False
        backyardFine.visible = True
        pinkHairGirl.toFront()
        
    elif app.sceneswitch == 6:
        LivingRoom.visible = False
        Bedroom.visible = False
        outdoor.visible = False
        Kitchen.visible = True
        backyardFine.visible = False
        pinkHairGirl.toFront()
        
    app.counter += 1
    if "up" in keys or "w" in keys: 
        pinkHairGirl.centerY -= 4
        #every 5 steps arm and leg move
        if app.counter % 3 == 0:
            if app.armSwingFront == True:
                armRight.x2 = armRight.x2 + 8
                armRight.y2 = armRight.y2 + 2
                armRight2.x2 = armRight2.x2 - 8
                armRight2.y2 = armRight2.y2 - 2
                app.armSwingFront = False
            else:
                armRight.x2 = armRight.x2 - 8
                armRight.y2 = armRight.y2 - 2
                armRight2.x2 = armRight2.x2 + 8
                armRight2.y2 = armRight2.y2 + 2
                app.armSwingFront = True
            #first foot
            if app.legSwingFront == True:
                legRight.x2 = legRight.x2 - 10
                legRight.y2 = legRight.y2 - 4
                legRight2.x2 = legRight2.x2 + 10
                legRight2.y2 = legRight2.y2 - 4
                app.legSwingFront = False
            else:
                legRight.x2 = legRight.x2 + 10
                legRight.y2 = legRight.y2 + 4
                legRight2.x2 = legRight2.x2 - 10
                legRight2.y2 = legRight2.y2 + 4
                app.legSwingFront = True
            
    elif "down" in keys or "s" in keys: 
        pinkHairGirl.centerY += 4
        #every 5 steps arm and leg move
        if app.counter % 3 == 0:
            if app.armSwingFront == True:
                armRight.x2 = armRight.x2 + 8
                armRight.y2 = armRight.y2 + 2
                armRight2.x2 = armRight2.x2 - 8
                armRight2.y2 = armRight2.y2 - 2
                app.armSwingFront = False
            else:
                armRight.x2 = armRight.x2 - 8
                armRight.y2 = armRight.y2 - 2
                armRight2.x2 = armRight2.x2 + 8
                armRight2.y2 = armRight2.y2 + 2
                app.armSwingFront = True
            if app.legSwingFront == True:
                legRight.x2 = legRight.x2 - 10
                legRight.y2 = legRight.y2 - 4
                legRight2.x2 = legRight2.x2 + 10
                legRight2.y2 = legRight2.y2 - 4
                app.legSwingFront = False
            else:
                legRight.x2 = legRight.x2 + 10
                legRight.y2 = legRight.y2 + 4
                legRight2.x2 = legRight2.x2 - 10
                legRight2.y2 = legRight2.y2 + 4
                app.legSwingFront = True
            
                
                
    elif "a" in keys or "left" in keys:
        pinkHairGirl.centerX -= 4
        pinkHairLeft.visible = True
        pinkHairRight.visible = False
        pinkHairRight.centerX = direction.centerX - 5
        pinkHairLeft.centerX = direction.centerX + 3
        pinkHairRight.centerY = direction.centerY + 10
        pinkHairLeft.centerY = direction.centerY + 11
        #every 5 steps arm and leg move
        if app.counter % 3 == 0:
            if app.armSwingFront == True:
                armRight.x2 = armRight.x2 + 8
                armRight.y2 = armRight.y2 + 2
                armRight2.x2 = armRight2.x2 - 8
                armRight2.y2 = armRight2.y2 - 2
                app.armSwingFront = False
            else:
                armRight.x2 = armRight.x2 - 8
                armRight.y2 = armRight.y2 - 2
                armRight2.x2 = armRight2.x2 + 8
                armRight2.y2 = armRight2.y2 + 2
                app.armSwingFront = True
            if app.legSwingFront == True:
                legRight.x2 = legRight.x2 - 10
                legRight.y2 = legRight.y2 - 4
                legRight2.x2 = legRight2.x2 + 10
                legRight2.y2 = legRight2.y2 - 4
                app.legSwingFront = False
            else:
                legRight.x2 = legRight.x2 + 10
                legRight.y2 = legRight.y2 + 4
                legRight2.x2 = legRight2.x2 - 10
                legRight2.y2 = legRight2.y2 + 4
                app.legSwingFront = True
            
    elif "d" in keys or "right" in keys:
        pinkHairGirl.centerX += 4
        pinkHairLeft.visible = False
        pinkHairRight.visible = True
        pinkHairRight.centerX = direction.centerX - 5
        pinkHairLeft.centerX = direction.centerX + 3
        pinkHairRight.centerY = direction.centerY + 10
        pinkHairLeft.centerY = direction.centerY + 11
        #every 5 steps arm and leg move
        if app.counter % 3 == 0:
            if app.armSwingFront == True:
                armRight.x2 = armRight.x2 + 8
                armRight.y2 = armRight.y2 + 2
                armRight2.x2 = armRight2.x2 - 8
                armRight2.y2 = armRight2.y2 - 2
                app.armSwingFront = False
            else:
                armRight.x2 = armRight.x2 - 8
                armRight.y2 = armRight.y2 - 2
                armRight2.x2 = armRight2.x2 + 8
                armRight2.y2 = armRight2.y2 + 2
                app.armSwingFront = True
            if app.legSwingFront == True:
                legRight.x2 = legRight.x2 - 10
                legRight.y2 = legRight.y2 - 4
                legRight2.x2 = legRight2.x2 + 10
                legRight2.y2 = legRight2.y2 - 4
                app.legSwingFront = False
            else:
                legRight.x2 = legRight.x2 + 10
                legRight.y2 = legRight.y2 + 4
                legRight2.x2 = legRight2.x2 - 10
                legRight2.y2 = legRight2.y2 + 4
                app.legSwingFront = True
    
    ##### bedroom walling restrict
    if app.sceneswitch == 0:
        lab1.visible = False 
        lab2.visible = False
        lab3.visible = False
        lab4.visible = False
        lab5.visible = False
        lab6.visible = False
        lab7.visible = False
        lab8.visible = False
        if pinkHairGirl.bottom > 340:
            pinkHairGirl.bottom = 340
            lab1.visible = True
            
        elif pinkHairGirl.right > 400:
            pinkHairGirl.right = 400
            lab2.visible = True
            
        elif pinkHairGirl.bottom < 85:
            pinkHairGirl.bottom = 85
            lab3.visible = True
            
        elif pinkHairGirl.left < 0:
            pinkHairGirl.left = 0
            lab4.visible = True
            
    #bed restrict
        elif pinkHairGirl.hitsShape(bedbottom) == True:
            pinkHairGirl.centerY += 4
            lab5.visible = True
            
        elif pinkHairGirl.hitsShape(bedside) == True:
            pinkHairGirl.centerX += 4
            lab5.visible = True
            
        #cabinet restrict
        elif pinkHairGirl.hitsShape(cableft) == True:
            pinkHairGirl.centerX -= 4
            lab6.visible = True
            
        elif pinkHairGirl.hitsShape(cabright) == True:
            pinkHairGirl.centerX += 4
            lab6.visible = True
            
        elif pinkHairGirl.hitsShape(cabbottom) == True:
            pinkHairGirl.centerY += 4
            lab6.visible = True
            
        elif pinkHairGirl.hitsShape(wardbottom) == True:
            pinkHairGirl.centerY += 4
            lab7.visible = True
            
        elif pinkHairGirl.hitsShape(wardleft) == True:
            pinkHairGirl.centerX -= 4
            lab7.visible = True
            
        elif pinkHairGirl.hitsShape(shelfbottom) == True:
            pinkHairGirl.centerY += 4
            lab8.visible = True
    #####livingroom
    lr1.visible = False 
    lr2.visible = False
    lr3.visible = False
    lr4.visible = False
    lr5.visible = False
    lr6.visible = False
    
    if app.sceneswitch == 1:
        if pinkHairGirl.bottom > 340:
            pinkHairGirl.bottom = 340
            
            
        elif pinkHairGirl.right > 400:
            pinkHairGirl.right = 400
                    
        elif pinkHairGirl.bottom < 0:
            pinkHairGirl.bottom = 0
                    
        elif pinkHairGirl.left < 0:
            pinkHairGirl.left = 0
    
        elif pinkHairGirl.hitsShape(right) == True:
            pinkHairGirl.centerX -= 4
            lr1.visible = True
        
        elif pinkHairGirl.hitsShape(top) == True:
            pinkHairGirl.centerY += 4
            lr1.visible = True
        
        elif pinkHairGirl.hitsShape(tableup) == True:
            pinkHairGirl.centerY -= 4
            lr2.visible = True
            
        elif pinkHairGirl.hitsShape(tableright) == True:
            pinkHairGirl.centerX += 4
            lr2.visible = True
            
        elif pinkHairGirl.hitsShape(tablebottom) == True:
            pinkHairGirl.centerY += 4
            lr3.visible = True
            
        elif pinkHairGirl.hitsShape(tableleft) == True:
            pinkHairGirl.centerX -= 4
            lr4.visible = True

        ###Chair1
        
        elif pinkHairGirl.hitsShape(Chair1right) == True:
            pinkHairGirl.centerX += 4
            lr5.visible = True
        
        elif pinkHairGirl.hitsShape(Chair1up) == True:
            pinkHairGirl.centerY -= 4
            lr5.visible = True
            
        elif pinkHairGirl.hitsShape(Chair1left) == True:
            pinkHairGirl.centerX -= 4
            lr5.visible = True
            
        ###Chair2
        
        elif pinkHairGirl.hitsShape(Chair2right) == True:
            pinkHairGirl.centerX += 4
            lr6.visible = True
            
        elif pinkHairGirl.hitsShape(Chair2up) == True:
            pinkHairGirl.centerY += 4
            lr6.visible = True
            
        elif pinkHairGirl.hitsShape(Chair2left) == True:
            pinkHairGirl.centerX -= 4
            lr6.visible = True
            
    #####outside
    o1.visible = False
    o2.visible = False
    o3.visible = False
    o4.visible = False
    o5.visible = False
    o6.visible = False 
    o7.visible = False
    o8.visible = False
    o9.visible = False
    o10.visible = False
    o11.visible = False
    if app.sceneswitch == 2:

        if pinkHairGirl.bottom > 340:
            pinkHairGirl.bottom = 340
            o1.visible = True
            
        elif pinkHairGirl.right > 400:
            pinkHairGirl.right = 400
            o2.visible = True

        elif pinkHairGirl.bottom < 120:
            pinkHairGirl.bottom = 120
            if pinkHairGirl.centerX > 200:
                app.sceneswitch = 3
                pinkHairGirl.centerX = 20
                pinkHairGirl.centerY = 165
            else:
                o3.visible = True
                
        elif pinkHairGirl.left < 0:
            pinkHairGirl.left = 0
            o2.visible = True
            
        elif pinkHairGirl.hitsShape(houseLeft) == True:
            pinkHairGirl.centerX -= 4
            o4.visible = True
        
        elif pinkHairGirl.hitsShape(houseBottom) == True:
            pinkHairGirl.centerY += 4
            o5.visible = True
            
        elif pinkHairGirl.hitsShape(houseRight) == True:
            pinkHairGirl.centerX += 4
            o6.visible = True
    
    #####backyard
    if app.sceneswitch == 3:
        if pinkHairGirl.hitsShape(Treeleft) == True:
            pinkHairGirl.centerX -= 4
            o7.visible = True
        
        elif pinkHairGirl.hitsShape(HouseLeft2) == True:
            pinkHairGirl.centerX -= 4
            o11.visible = True
            
        elif pinkHairGirl.hitsShape(Treebottom) == True:
            pinkHairGirl.centerY += 4
            o8.visible = True
            
        elif pinkHairGirl.hitsShape(Housebottom2) == True:
            pinkHairGirl.centerY += 4
            o9.visible = True
            
        elif pinkHairGirl.bottom > 340:
            pinkHairGirl.bottom = 340
            o10.visible = True
            
        elif pinkHairGirl.right > 400:
            pinkHairGirl.right = 400
            o2.visible = True
                    
        elif pinkHairGirl.bottom < 150:
            pinkHairGirl.bottom = 150
            app.sceneswitch = 2
            pinkHairGirl.centerX = 370
            pinkHairGirl.centerY = 152
           
        elif pinkHairGirl.left < 0:
            pinkHairGirl.left = 0
            o2.visible = True
            
    #####Kitchen 
    k1.visible = False
    k2.visible = False
    k3.visible = False
    if app.sceneswitch == 6:
        if pinkHairGirl.bottom > 340:
            pinkHairGirl.bottom = 340
            k1.visible = True
            
        elif pinkHairGirl.right > 400:
            pinkHairGirl.right = 400
            k2.visible = True
                    
        elif pinkHairGirl.bottom < 205:
            pinkHairGirl.bottom = 205
            k3.visible = True
            
        elif pinkHairGirl.left < 0:
            pinkHairGirl.left = 0
            k1.visible = True
    
    #####sceneswitching
    if pinkHairGirl.hitsShape(toLivingRoom) == True and app.sceneswitch == 0:
        pinkHairGirl.centerX = 200
        pinkHairGirl.centerY = 160
        app.sceneswitch = 1
    
    elif pinkHairGirl.hitsShape(toBedroom) == True  and app.sceneswitch == 1:
        pinkHairGirl.centerX = 25
        pinkHairGirl.centerY = 300
        app.sceneswitch = 0
        
    elif pinkHairGirl.hitsShape(toFrontDoor) == True and app.sceneswitch == 1:
        pinkHairGirl.centerX = 273
        pinkHairGirl.centerY = 273
        app.sceneswitch = 2
    
    elif pinkHairGirl.hitsShape(toLivingRoom2) == True and app.sceneswitch == 2:
        pinkHairGirl.centerX = 40
        pinkHairGirl.centerY = 275
        app.sceneswitch = 1
    
    elif pinkHairGirl.hitsShape(toKitchen) == True and app.sceneswitch == 1:
        pinkHairGirl.centerX = 25
        pinkHairGirl.centerY = 265
        app.sceneswitch = 6
        
    elif pinkHairGirl.hitsShape(toLivingRoom3) == True and app.sceneswitch == 6:
        pinkHairGirl.centerX = 210
        pinkHairGirl.centerY = 70
        app.sceneswitch = 1
     
    elif pinkHairGirl.hitsShape(toBackyard) == True and app.sceneswitch == 1:
        pinkHairGirl.centerX = 100
        pinkHairGirl.centerY = 195
        app.sceneswitch = 3
        
    elif pinkHairGirl.hitsShape(ToLivingRoom4) == True and app.sceneswitch == 3:
        pinkHairGirl.centerX = 180
        pinkHairGirl.centerY = 35
        app.sceneswitch = 1
