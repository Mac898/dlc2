#---- People ----
define n = Character("Nico", color="#f53a18")
define m = Character("Mac", color="#25f516")
define w = Character("Will", color="#1ba0f2")
define t = Character("Tomas", color="#fa1111")
define e = Character("Eric", color="#267a2c")
define i = Character("Izzy", color="#f2f538")
define b = Character("Ismail", color="#42f5e3")
define o = Character("Osho", color="#ff991c")
#---- Narrator / (Tomas)Thoughts ----
define n = Character("")
define a = Character("Tomas")
###########################################################
# The game starts here.
label start:
    jump prologue_scene


    n "Well that's it, game over!"
    return

label prologue_scene:
    #load background
    scene prologue bg
    with fade
    #load characters
    show tomas prologue
    show mac prologue at right
    with dissolve
    #begin script
    t "I didn\'t mean to kill her"
    m "Sure you didn\'t tomassi wassi uwu"
    n "Tomas shakes violently through the chains that hold him"
    m "You know what you did to Sayori!"
    n "Mac leans back in his chair, and takes a sip of his coke."
    m "I\'ll leave you to think about what you've done Tomas."
    hide mac prologue
    with dissolve
    n "Days pass and Tomas begins to degrade"
    scene prologue bg
    with fade
    scene prologue bg
    with fade
    t "Why? WHY HAS he done this to me."
    t "All I did was love Sayori, It wasn’t my fault she was depressed and was afraid of being cared for"
    n "A picture of Sayori hanging flashes upon the wall before Tomas"
    show prologue sayori_picture at left
    t "AHHH! My eyes!"
    hide tomas prologue
    show tomas prologue_crying
    with dissolve
    t "Mac you know I can’t"
    t "You son of a bitch"
    show mac prologue at right
    with dissolve
    m "Tomas, we have thought about what we should do with you."
    t "WHAT IS IT THAT YOU WANT FARJAD"
