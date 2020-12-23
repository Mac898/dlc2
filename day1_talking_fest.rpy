#---- People ----
define t = Character("Tomas", color="#6e34eb")
define i = Character("Izzy", color="#ffff00")
define m = Character("Mac", color="#ffbe00")
define n = Character("Nico", color="#ff00ff")
define w = Character("Will", color="#000000")
define o = Character("Osho", color="#ff0000")
define b = Character("Bob", color="#00ff00")
define e = Character("Eric", color="#0000ff")
#---- Narrator / (Tomas)Thoughts ----
define n = Character("")
define a = Character("Tomas")
#setup
$ day1_complete = []
$ day1_talk_bob = False
$ day1_talk_eric = False
$ day1_talk_luke = False
$ day1_talk_mac = False
$ day1_talk_nico = False
$ day1_talk_osho = False
$ day1_talk_will = False
$ day1_talk_izzy = False

#script
label day1_talkingfest:
    n "Tomas walks over to a tent."
    #menu
    default talkingFestOneSet:
    menu:
        "BOB" if not day1_talk_bob:
            $ day1_complete.remove("BOB")
            $ day1_talk_bob = True
            jump day1_bob
        "ERIC" if not day1_talk_eric:
            $ day1_complete.remove("ERIC")
            $ day1_talk_eric = True
            jump day1_eric
        "LUKE" if not day1_talk_luke:
            $ day1_complete.remove("LUKE")
            $ day1_talk_luke = True
            jump day1_luke
        "MAC" if not day1_talk_mac:
            $ day1_complete.remove("MAC")
            $ day1_talk_mac = True
            jump day1_mac
        "NICO" if not day1_talk_nico:
            $ day1_complete.remove("NICO")
            $ day1_talk_nico = True
            jump day1_nico
        "WILL" if not day1_talk_will:
            $ day1_complete.remove("WILL")
            $ day1_talk_will = True
            jump day1_will
        "IZZY" if not day1_talk_izzy:
            $ day1_complete.remove("IZZY")
            $ day1_talk_izzy = True
            n "Izzy's tent is empty"
            jump day1_talkingfest
