# The script of the game goes in this file.

default persistent.ending = False

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters
define p = Character("[playername]", color="#5D77CE")
define pr = Character("Baş kahraman", color="#928E81")
define v = Character("Vel", color="#7F5BE1")
define v1 = Character("Ölüm Meleği?", color="#7F5BE1")
define que = Character("????", color="#7F5BE1")
define que2 = Character("????", color="#FFA7B2")
define n1 = Character("Ölüm Meleği", color="#FFA7B2")
define n = Character("Neu", color="#FFA7B2")

# Images

image s1a:
    block:
        "s1a_0001.jpg"
        0.105
        "s1a_0004.jpg"
        0.105
        "s1a_0007.jpg"
        0.105
        "s1a_0010.jpg"
        0.105
        "s1a_0013.jpg"
        0.105
        repeat 8
    block:
        "s1a_0001.jpg"
        0.105
        "s1ab_0004.jpg"
        0.105
        "s1ab_0007.jpg"
        0.105
        "s1a_0010.jpg"
        0.105
        "s1a_0013.jpg"
        0.105
    block:
        "s1a_0001.jpg"
        0.105
        "s1a_0004.jpg"
        0.105
        "s1a_0007.jpg"
        0.105
        "s1a_0010.jpg"
        0.105
        "s1a_0013.jpg"
        0.105
        repeat 5
    block:
        "s1a_0001.jpg"
        0.105
        "s1ab_0004.jpg"
        0.105
        "s1ab_0007.jpg"
        0.105
        "s1a_0010.jpg"
        0.105
        "s1a_0013.jpg"
        0.105
    repeat

image s1b:
    block:
        "s1b_0001.jpg"
        0.105
        "s1b_0004.jpg"
        0.105
        "s1b_0007.jpg"
        0.105
        "s1b_0010.jpg"
        0.105
        "s1b_0013.jpg"
        0.105
        repeat 8
    block:
        "s1b_0001.jpg"
        0.105
        "s1bb_0004.jpg"
        0.105
        "s1bb_0007.jpg"
        0.105
        "s1b_0010.jpg"
        0.105
        "s1b_0013.jpg"
        0.105
    block:
        "s1b_0001.jpg"
        0.105
        "s1b_0004.jpg"
        0.105
        "s1b_0007.jpg"
        0.105
        "s1b_0010.jpg"
        0.105
        "s1b_0013.jpg"
        0.105
        repeat 5
    block:
        "s1b_0001.jpg"
        0.105
        "s1bb_0004.jpg"
        0.105
        "s1bb_0007.jpg"
        0.105
        "s1b_0010.jpg"
        0.105
        "s1b_0013.jpg"
        0.105
    repeat

image s1c:
    block:
        "s1c_0001.jpg"
        0.105
        "s1c_0004.jpg"
        0.105
        "s1c_0007.jpg"
        0.105
        "s1c_0010.jpg"
        0.105
        "s1c_0013.jpg"
        0.105
        repeat 8
    block:
        "s1c_0001.jpg"
        0.105
        "s1cb_0004.jpg"
        0.105
        "s1cb_0007.jpg"
        0.105
        "s1c_0010.jpg"
        0.105
        "s1c_0013.jpg"
        0.105
    block:
        "s1c_0001.jpg"
        0.105
        "s1c_0004.jpg"
        0.105
        "s1c_0007.jpg"
        0.105
        "s1c_0010.jpg"
        0.105
        "s1c_0013.jpg"
        0.105
        repeat 5
    block:
        "s1c_0001.jpg"
        0.105
        "s1cb_0004.jpg"
        0.105
        "s1cb_0007.jpg"
        0.105
        "s1c_0010.jpg"
        0.105
        "s1c_0013.jpg"
        0.105
    repeat

image boob1:
    block:
        "boobs1_0001.jpg"
        0.2
        "boobs1_0002.jpg"
        0.2
        repeat 8
    block:
        "boobs1b_0001.jpg"
        0.105
        "boobs1b_0002.jpg"
        0.105
    block:
        "boobs1_0001.jpg"
        0.2
        "boobs1_0002.jpg"
        0.2
        repeat 5
    block:
        "boobs1b_0001.jpg"
        0.105
        "boobs1b_0002.jpg"
        0.105
    repeat

image boob2:
    block:
        "boobs2_0001.jpg"
        0.2
        "boobs2_0002.jpg"
        0.2
        repeat 8
    block:
        "boobs2b_0001.jpg"
        0.105
        "boobs2b_0002.jpg"
        0.105
    block:
        "boobs2_0001.jpg"
        0.2
        "boobs2_0002.jpg"
        0.2
        repeat 5
    block:
        "boobs2b_0001.jpg"
        0.105
        "boobs2b_0002.jpg"
        0.105
    repeat

image stare:
    "Stare_0001.jpg"
    0.105
    "Stare_0005.jpg"
    0.105
    repeat

image lookw:
    "LookW1.png"
    0.2
    "LookW2.png"
    0.2
    repeat

image looks:
    "LookS1.jpg"
    0.2
    "LookS2.jpg"
    0.2
    repeat

image lookss:
    "LookSS1.jpg"
    0.2
    "LookSS2.jpg"
    0.2
    repeat

image lookh:
    "LookH1.jpg"
    0.2
    "LookH2.jpg"
    0.2
    repeat

image lookl:
    "LookL1.jpg"
    0.2
    "LookL2.jpg"
    0.2
    repeat

image looka:
    "LookA1.jpg"
    0.2
    "LookA2.jpg"
    0.2
    repeat

image hug:
    block:
        "Hug1.jpg"
        0.2
        "Hug2.jpg"
        0.2
        repeat 8
    block:
        "Hug3.jpg"
        0.15
        "Hug4.jpg"
        0.1
    block:
        "Hug1.jpg"
        0.2
        "Hug2.jpg"
        0.2
        repeat 5
    block:
        "Hug3.jpg"
        0.15
        "Hug4.jpg"
        0.1
    repeat


image neuc:
    "NeuC.jpg"

image reaper:
    "Reaper1.png"
    0.2
    "Reaper2.png"
    0.2
    "Reaper3.png"
    0.2
    repeat

image reaperd:
    "ReaperD1.png"
    0.2
    "ReaperD2.png"
    0.2
    "ReaperD3.png"
    0.2
    repeat

image reaperb:
    "ReaperB1.png"
    0.2
    "ReaperB2.png"
    0.2
    "ReaperB3.png"
    0.2
    repeat

image reaperbd:
    "ReaperBD1.png"
    0.2
    "ReaperBD2.png"
    0.2
    "ReaperBD3.png"
    0.2
    repeat

image reaperv:
    block:
        "ReaperV_0001.png"
        0.2
        "ReaperV_0002.png"
        0.2
        repeat 8
    block:
        "ReaperVB_0001.png"
        0.15
        "ReaperVB_0002.png"
        0.1
    block:
        "ReaperV_0001.png"
        0.2
        "ReaperV_0002.png"
        0.2
        repeat 5
    block:
        "ReaperVB_0001.png"
        0.15
        "ReaperVB_0002.png"
        0.1
    repeat

image bed:
    block:
        "Bed_0001.png"
        0.2
        "Bed_0002.png"
        0.2
        repeat 8
    block:
        "Bed_0003.png"
        0.15
        "Bed_0004.png"
        0.1
    block:
        "Bed_0001.png"
        0.2
        "Bed_0002.png"
        0.2
        repeat 5
    block:
        "Bed_0003.png"
        0.15
        "Bed_0004.png"
        0.1
    repeat

image neus:
    "NeuScared_0001.jpg"
    0.2
    "NeuScared_0002.jpg"
    0.2
    repeat

image neuh:
    "NeuHappy_0001.jpg"
    0.2
    "NeuHappy_0002.jpg"
    0.2
    repeat

image neuw:
    "NeuWorried_0001.jpg"
    0.2
    "NeuWorried_0002.jpg"
    0.2
    repeat

image neucry:
    "NeuCry_0001.jpg"

image neusm:
    "NeuSmug_0001.jpg"
    0.2
    "NeuSmug_0002.jpg"
    0.2
    repeat





# Mini
image controls:
    "Controls_0001.jpg"
    0.2
    "Controls_0002.jpg"
    0.2
    repeat

image ename:
    "EName_0001.jpg"
    0.2
    "EName_0002.jpg"
    0.2
    repeat

image tobe:
    "Tobe_0001.jpg"
    0.2
    "Tobe_0002.jpg"
    0.2
    repeat

image cred:
    "Cred_0001.png"
    0.2
    "Cred_0002.png"
    0.2
    repeat

image nextday:
    "NextDay_0001.jpg"
    0.2
    "NextDay_0002.jpg"
    0.2
    repeat

image note:
    "Note1.jpg"
    0.2
    "Note2.jpg"
    0.2
    repeat

image 2weeks:
    "2Weeks_0001.jpg"
    0.2
    "2Weeks_0002.jpg"
    0.2
    repeat

image fewdays:
    "FewDays_0001.jpg"
    0.2
    "FewDays_0002.jpg"
    0.2
    repeat

image theend:
    "TheEnd_0001.png"
    0.2
    "TheEnd_0002.png"
    0.2
    repeat

image afterword:
    "After_0001.jpg"
    0.2
    "After_0002.jpg"
    0.2
    repeat



## VEL SPRITE ###################

image veltalk:
    "VelTalk.png"

image veltalkE:
    block:
        "VelTalkE2.png"
        0.105
        "VelTalkE3.png"
        0.105
    block:
        "VelTalkE.png"
        0.2
        "VelTalkE1.png"
        0.2
        repeat 10
    block:
        "VelTalkE2.png"
        0.105
        "VelTalkE3.png"
        0.105
    block:
        "VelTalkE.png"
        0.2
        "VelTalkE1.png"
        0.2
        repeat 4
    repeat

image veltalkL:
    block:
        "VelTalkE2.png"
        0.105
        "VelTalkL3.png"
        0.105
    block:
        "VelTalkL.png"
        0.2
        "VelTalkL1.png"
        0.2
        repeat 10
    block:
        "VelTalkE2.png"
        0.105
        "VelTalkL3.png"
        0.105
    block:
        "VelTalkL.png"
        0.2
        "VelTalkL1.png"
        0.2
        repeat 4

    repeat

layeredimage veltalkg:

    always:
        "veltalk"


    group face:

        attribute blink default:
            "veltalkE"

        attribute look:
            "veltalkL"

image boobt:
    block:
        "BoobsT1.png"
        0.2
        "BoobsT2.png"
        0.2
        repeat 8
    block:
        "BoobsTB1.png"
        0.105
        "BoobsTB2.png"
        0.105
    block:
        "BoobsT1.png"
        0.2
        "BoobsT2.png"
        0.2
        repeat 5
    block:
        "BoobsTB1.png"
        0.105
        "BoobsTB2.png"
        0.105
    repeat

## NEU SPRITE

image neutalk:
    "NeuTalk.png"

image neutalkhappy:
    block:
        "NeuTalkHappy.png"
        0.2
        "NeuTalkHappy1.png"
        0.2
        repeat 8
    block:
        "NeuTalkHappy2.png"
        0.105
        "NeuTalkHappy3.png"
        0.105
    block:
        "NeuTalkHappy.png"
        0.2
        "NeuTalkHappy1.png"
        0.2
        repeat 5
    block:
        "NeuTalkHappy2.png"
        0.105
        "NeuTalkHappy3.png"
        0.105
    repeat

image neutalkaway:
    block:
        "NeuTalkAway.png"
        0.2
        "NeuTalkAway1.png"
        0.2
        repeat 8
    block:
        "NeuTalkAway2.png"
        0.105
        "NeuTalkAway3.png"
        0.105
        "NeuTalkAway2.png"
        0.105
        "NeuTalkAway3.png"
        0.105
    block:
        "NeuTalkAway.png"
        0.2
        "NeuTalkAway1.png"
        0.2
        repeat 5
    block:
        "NeuTalkAway2.png"
        0.105
        "NeuTalkAway3.png"
        0.105
    repeat

image neutalkcry:
    "NeuTalkCry.png"

image neutalkworried:
    block:
        "NeuTalkWorried.png"
        0.2
        "NeuTalkWorried1.png"
        0.2
        repeat 8
    block:
        "NeuTalkWorried2.png"
        0.105
        "NeuTalkWorried3.png"
        0.105
    block:
        "NeuTalkWorried.png"
        0.2
        "NeuTalkWorried1.png"
        0.2
        repeat 5
    block:
        "NeuTalkWorried2.png"
        0.105
        "NeuTalkWorried3.png"
        0.105

    repeat

image neutalkhappyl:
    block:
        "NeuTalkHappyL.png"
        0.2
        "NeuTalkHappyL1.png"
        0.2
        repeat 8
    block:
        "NeuTalkHappy2.png"
        0.105
        "NeuTalkHappyL3.png"
        0.105
    block:
        "NeuTalkHappyL.png"
        0.2
        "NeuTalkHappyL1.png"
        0.2
        repeat 5
    block:
        "NeuTalkHappy2.png"
        0.105
        "NeuTalkHappyL3.png"
        0.105
    repeat

image neutalkhehe:
    "NeuTalkHehe.png"


layeredimage neutalkg:

    always:
        "neutalk"


    group face:

        attribute happy default:
            "neutalkhappy"

        attribute away:
            "neutalkaway"

        attribute cry:
            "neutalkcry"

        attribute wor:
            "neutalkworried"

        attribute happyl:
            "neutalkhappyl"

        attribute hehe:
            "neutalkhehe"


#### NEU SPRITE FRONT

image neuclose:
    "NeuClose.png"

image neucloseangry:
    block:
        "NeuCloseAngry1.png"
        0.2
        "NeuCloseAngry2.png"
        0.2
    repeat

image neucloseaway:
    block:
        "NeuCloseAway1.png"
        0.2
        "NeuCloseAway2.png"
        0.2
        repeat 8
    block:
        "NeuCloseAway3.png"
        0.105
        "NeuCloseAway4.png"
        0.105
        "NeuCloseAway3.png"
        0.105
        "NeuCloseAway4.png"
        0.105
    block:
        "NeuCloseAway1.png"
        0.2
        "NeuCloseAway2.png"
        0.2
        repeat 5
    block:
        "NeuCloseAway3.png"
        0.105
        "NeuCloseAway4.png"
        0.105
    repeat

image neuclosecon:
    block:
        "NeuCloseCon1.png"
        0.2
        "NeuCloseCon2.png"
        0.2
        repeat 8
    block:
        "NeuCloseCon3.png"
        0.105
        "NeuCloseCon4.png"
        0.105
        "NeuCloseCon3.png"
        0.105
        "NeuCloseCon4.png"
        0.105
    block:
        "NeuCloseCon1.png"
        0.2
        "NeuCloseCon2.png"
        0.2
        repeat 5
    block:
        "NeuCloseCon3.png"
        0.105
        "NeuCloseCon4.png"
        0.105
    repeat

image neuclosecry:
    "NeuCloseCry.png"

image neuclosedumb:
    "NeuCloseDumb.png"

image neuclosehappy:
    block:
        "NeuCloseHappy1.png"
        0.2
        "NeuCloseHappy2.png"
        0.2
        repeat 5
    block:
        "NeuCloseHappy3.png"
        0.105
        "NeuCloseHappy4.png"
        0.105
    block:
        "NeuCloseHappy1.png"
        0.2
        "NeuCloseHappy2.png"
        0.2
        repeat 8
    block:
        "NeuCloseHappy3.png"
        0.105
        "NeuCloseHappy4.png"
        0.105
    repeat

image neuclosepout:
    "NeuClosePout.png"

image neuclosesmug:
    block:
        "NeuCloseSmug1.png"
        0.2
        "NeuCloseSmug2.png"
        0.2
        repeat 5
    block:
        "NeuCloseSmug3.png"
        0.105
        "NeuCloseSmug4.png"
        0.105
    block:
        "NeuCloseSmug1.png"
        0.2
        "NeuCloseSmug2.png"
        0.2
        repeat 8
    block:
        "NeuCloseSmug3.png"
        0.105
        "NeuCloseSmug4.png"
        0.105
    repeat

image neuclosewor:
    block:
        "NeuCloseWorried1.png"
        0.2
        "NeuCloseWorried2.png"
        0.2
        repeat 5
    block:
        "NeuCloseWorried3.png"
        0.105
        "NeuCloseWorried4.png"
        0.105
    block:
        "NeuCloseWorried1.png"
        0.2
        "NeuCloseWorried2.png"
        0.2
        repeat 8
    block:
        "NeuCloseWorried3.png"
        0.105
        "NeuCloseWorried4.png"
        0.105
    repeat

image neuclosexd:
    "NeuCloseXD.png"

layeredimage neucloseg:

    always:
        "neuclose"


    group face:

        attribute angry:
            "neucloseangry"

        attribute away:
            "neucloseaway"

        attribute con:
            "neuclosecon"

        attribute cry:
            "neuclosecry"

        attribute dumb:
            "neuclosedumb"

        attribute happy default:
            "neuclosehappy"

        attribute pout:
            "neuclosepout"

        attribute smug:
            "neuclosesmug"

        attribute wor:
            "neuclosewor"

        attribute xd:
            "neuclosexd"



# Movies

image tfuck1  = Movie(play="tfuck1.webm")
image tfuck2  = Movie(play="tfuck2.webm")
image tfuck3  = Movie(play="tfuck3.webm")
image tfuckcum  = Movie(play="tfuckcum.webm")
image play2  = Movie(play="Play2.webm")
image play1  = Movie(play="Play1.webm")
#HJ
image hj1a  = Movie(play="HJ1A.webm")
image hj1b  = Movie(play="HJ1B.webm")
image hj1c  = Movie(play="HJ1C.webm")
image hj2a  = Movie(play="HJ2A.webm")
image hj2b  = Movie(play="HJ2B.webm")
image hj2b2  = Movie(play="HJ2B 2.webm")
image hj2c  = Movie(play="HJ2C.webm")
image hjcum  = Movie(play="HJCum.webm")
image hjend  = Movie(play="HJEnd.webm")
image hjstart  = Movie(play="HJStart.webm")
#TJ
image tjob1  = Movie(play="tjob1.webm")
image tjob2  = Movie(play="tjob2.webm")
image tjob1s1  = Movie(play="tjob1s1.webm")
image tjob1s2  = Movie(play="tjob1s2.webm")
image tjob2s  = Movie(play="tjob2s.webm")
image tjobcum  = Movie(play="tjobcum.webm")
image tjobend  = Movie(play="tjobend.webm")
# CowGirl
image cow1  = Movie(play="cow1.webm")
image cow2  = Movie(play="cow2.webm")
image cowbeg  = Movie(play="cowbeg.webm")
image cowend  = Movie(play="cowend.webm")
image cowstart  = Movie(play="cowstart.webm")
image cowxray  = Movie(play="cowxray.webm")
image cowxray1  = Movie(play="cowxray1.webm")
image cowxraycum  = Movie(play="cowxraycum.webm")
# Grope
image spoon = Movie(play="Spoon.webm")
image grope1  = Movie(play="Grope1.webm")
image grope2  = Movie(play="Grope2.webm")
image grope3  = Movie(play="Grope3.webm")
# Doggy
image dogc  = Movie(play="DogCloth.webm")
image dogc2  = Movie(play="DogCloth2.webm")
image dogn  = Movie(play="DogNude.webm")
image dogn2  = Movie(play="DogNude2.webm")
image dogs  = Movie(play="DogStart.webm")
image dogsn  = Movie(play="DogStartN.webm")
image dogx  = Movie(play="DogXray.webm")
image dogx2  = Movie(play="DogXray2.webm")
image dogxc  = Movie(play="DogXrayCum.webm")


# Transitions
define fadefast = Fade(0.2, 0.0, 0.2)
define fadefast2 = Fade(0.5, 0.0, 0.2)
define fadefast3 = Fade(0.5, 0.0, 0.)
define fadelast = Fade(0.0, 0.0, 0.4)
define fadelast1 = Fade(0.0, 0.0, 0.1)
define fadelastlong = Fade(0.0, 0.0, 1.0)
define fadelastlong1 = Fade(0.0, 0.5, 1.0)
define fadelong = Fade(1.0, 0.5, 1.0)
define fadelong1 = Fade(1.0, 0.3, 1.0)
define fadelong2 = Fade(0.5, 0.3, 1.0)
define dissolvefast = Dissolve (0.3 )
define dissolvefast1 = Dissolve (0.2 )
define dissolvelong = Dissolve (0.6 )
define dissolvelong1 = Dissolve (0.8 )

transform bounce1:
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    easein .175 yoffset -2
    easeout .175 yoffset 0
    yoffset 0


# The game starts here.

label start:

    scene controls with fadelong2

    "You can hide me anytime."

    $ renpy.music.set_volume(0.1, 0, channel='music')
    play music "PerituneMaterial_Spook_loop.ogg" loop

    scene door with fadelong2:
        zoom 1.5 xalign 0.5 yalign 0.5
        linear 4.0 zoom 1.0 xalign 0.5 yalign 0.5

    pause 2.2

    "One day, a mysterious door appeared out of nowhere in my house."

    "At first I thought I was still half awake and was only imagining things, so I went to take a shower."

    "But when I came back.. {w}it's still there!"

    "Now certain there's actually a door I've never seen in my house, I carefully examined every corner of it."

    "It looks like just a normal door except for its unusual and ominous design."

    "I have no idea how a door would suddenly just appear in the wall of my house."

    "I never heard of something like this happening to anyone at least."

    "There shouldn't even be a space behind this wall.."

    "Maybe it's just a door someone put against the wall?"

    "Then did someone sneak a whole door inside my house just to mess with me?!"

    "Not likely.."

    "I obviously couldn't just leave it alone, so I decided to enter and see what lies on the other side."

    "If there's even another side anyway."

    "I slowly inch my hand to the door handle."

    "As I was opening it, I quickly saw there's actually a room lying behind it."

    "And what was in the room that invaded my home was something I never expected to see."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound "Dooropen.ogg"

    stop music fadeout 2.0

    scene door:
        zoom 1.0 xalign 0.5 yalign 0.5
        linear 2.0 zoom 1.5 xalign 0.5 yalign 0.5

    pause 0.5

    show s1a with fadelong

    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Puppet_loop.ogg" loop

    "It's a girl.. playing with a handheld console."

    "She's so focused on her game that it doesn't look like she even noticed me entering the room."

    "Brimming with confusion, I looked around the room for anything that could help me assess the situation."

    "I glanced from one side to another, and quickly realized there's something unusual with this place."

    "The whole room is dark and hazy. I'm barely able to tell where the walls are as they appear blurry and swallowed by blackness."

    "It was as if my eyes couldn't focus on anything but her."

    "And due to that reason, my instincts led me to try and get her attention."

    pr "Ummm.. Hello?"

    show s1c with fade

    que "Hm?"

    "She quickly diverts her gaze to me, but she doesn't seem to stop playing her game."

    que "Human. Who are you?"

    "A cold and monotonous voice came out from the girl staring at me."

    "But despite the distant tone of her voice, it also somehow feels welcoming."

    pr "I should be the one asking you that.."

    que "Why is there a human in my room?"

    pr "Why is your room inside my house?"

    pr "Also why are you calling me human?"

    show s1b with dissolve

    "She fixates back to her console, and focuses on her game again."

    que "Because you're a human."

    pr "Well I know that.. but people normally won't call others \"human.\""

    que "Is that so?"

    "Her question is filled with genuine curiosity which made me confused."

    pr "Umm.. It is so."

    pr "Isn't that like.. common sense?"

    que "But I'm not a human like you, Human."

    pr "You're not..?"

    pr "Then what are you?"

    hide s1b with dissolve
    show s1c with dissolve

    "She gazes back at me once again, and looks me straight in the eye."

    v1 "I'm a Grim Reaper."

    pr "You're a grim reaper?"

    "How could such a cute girl like her be a grim reaper?"

    show s1b with dissolve

    "Aren't grim reapers supposed to be scary or something?"

    "I wouldn't know as I never met one.{w}.. well maybe I have now."

    "Big emphasis on the maybe."

    ". . ."

    "Maybe she's just cosplaying as one."

    pr "Are you trying to cosplay as a grim reaper or something?"

    v1 ". . ."

    v1 "Cosplay? What's that?"

    "Huh? She doesn't even know what cosplaying is?"

    pr "You know.. dressing up as characters you see in animes or games."

    v1 "Human. Do you not believe me when I say I'm a Grim Reaper?"

    pr "How could I believe a cute girl like you is an actual grim reaper?!"

    hide s1b with dissolve
    show s1c with dissolve

    v1 "I'm cute?"

    "She looks at me with curious eyes which just further proves my point."

    pr "You definitely are!"

    v1 ". . ."

    show s1b with dissolve

    v1 "You're weird, Human."

    pr "No- no. You're definitely the weird one here. Calling yourself a grim reaper."

    pr "How could you be an actual grim reaper?"

    v1 "Then how do you explain my room appearing in your house?"

    show s1b with vpunch:
        zoom 1.02 xalign 0.5 yalign 0.5

    pr "I'm here to ask you why that even happened!"

    "She paused for a moment before answering my question, as if she had to collect her thoughts first."

    v1 "When someone is about to die, we get sent near them to collect their soul."

    pr "Your room gets sent to their house..?"

    hide s1b with dissolve
    show s1c with dissolve

    v1 "Yes."

    pr "For real?"

    v1 "Mmh."

    "What's with that serious look on her face?"

    "So she's actually a grim reaper?!"

    "How could that even be possible?"

    "But it's true that it shouldn't be physically possible for this room to exist in my house."

    "There's also the fact that this whole place feels so weird, as if it's telling me that I shouldn't be here."

    show s1b with dissolve

    "Maybe she really is a grim reaper."

    "Wait-"

    "If that's true, then that means.."

    pr "So umm.. Miss Grim Reaper?"

    v1 "Vel."

    pr "Huh?"

    v "You can call me Vel."

    pr "Oh.."

    pr "That's unexpectedly a really cute name for a grim reaper."

    pr "Or maybe it should be expected seeing how cute you actually are."

    hide s1b with dissolve
    show s1c with dissolve

    v ". . ."

    "The cute reaper looks at me weirdly as a response to my compliment."

    "She continues to stare right into my soul without meeking a word nor stopping her game."

    "I can't tell what exactly she's thinking as her expression hasn't changed since I started talking to her."

    show s1b with dissolve

    #"Plenty of awkward seconds later, she gazes back into the console in her hands as if nothing unusual happened."

    "A few awkward seconds passed as I tried to come up with what I should say next."

    pr "I guess.. I should introduce myself too."

    pr "My name is.."

    scene ename with fade

    $ playername = renpy.input("")
    $ playername = playername.strip() or "Human"

    scene s1b with fade

    p "[p]."

    p "My name is [p]."

    v "Hm."

    "She nods, but didn't seem too interested in my name."

    p "So Vel if what you say is true, that you're actually a grim reaper.."

    p "Are you here to collect my soul..?"

    v "That's what Grim Reapers do."

    p "Oh.. right."

    ". . ."

    "So I'm really gonna die?"

    "For some reason, I just find it hard to believe that this is all real."

    p "So. . are you gonna do it?"

    v "Later."

    p "Huh?"

    p "Later?"

    p "What do you mean later?"

    v "I'm still playing."

    p "Huh-?"

    v "I'll do it when I'm done playing."

    p ". . ."

    p "Isn't being a grim reaper like your job?"

    p "Is playing a game more important than that?!"

    show s1c with dissolve

    v "Yes."

    p ". . ."

    "Is this girl really the grim reaper..? "

    "She just seems like a cute normal girl who's clearly too addicted to playing games."

    "Well I wouldn't mind having more time to be alive. "

    v "Hey Human."

    "While in the middle of my thoughts, she called out to me."

    p "Y-Yes?"

    v "I've been wondering about it since you entered my room."

    p "Huh? What is it?"

    v "What's with that thing bulging in your pants."

    p "Huh?!"

    "She's staring directly at my crotch."

    "Is she talking about my dick?"

    hide s1c with dissolve
    show s1b with dissolve

    v "Is it like a joystick or something?"

    p "Huh?! No!"

    p "Are you seriously asking me that?"

    v "Mmh."

    p "Seriously..?"

    v ". . ."

    "How could she be seriously asking me that?"

    "Does she really have no idea what it is?"

    p "It's my dick.."

    p "How is it possible that you wouldn't even know about that?"

    v "Your dick..?"

    v "I think I heard about dicks before."

    v "But I can't remember."

    "What does that even mean?"

    p "You can't remember?"

    p "How could that even be the case?"

    v "I don't know."

    "Judging by her behavior, it really seems like she has no idea."

    "Are grim reapers just not aware of it?"

    "Does that mean she has never seen one before?"

    "Before I can interrogate her further, she asks me another question."

    v "Why is your dick sticking out like that?"

    p "Well..."

    show s1c with dissolve

    v "Hmm?"

    "She stares at me with curious and innocent eyes."

    "I feel guilty answering her when she stares at me like this, but she also looks like she really wants to know."

    p "It's because of you.."

    v "Because of me?"

    p "Yes! Or to be precise, it's because of your boobs."

    v "My boobs?"

    $ renpy.music.set_volume(1.5, 0, channel='sound')
    play sound ["<silence .4>","cloth1.ogg"]

    scene boob1 with fade

    "She seems to be intrigued by my claim, as she puts down her game and stops playing."

    v "What do you mean?"

    p "My dick couldn't help but stand when your boobs are being displayed like that."

    v "It's my boobs' fault?"

    v ". . ."

    v "Then should I hide them?"

    p "Huh?"

    v "My clothes can morph to whatever shape I want them to be."

    v "So I can cover my boobs if it's causing your dick to be like that."

    p "No- no! You don't have to do that!"

    v "I don't?"

    v "But isn't it a problem for you?"

    p "Of course not!"

    p "It's not a problem at all."

    p "Actually it would even be better if you're showing them more!"

    v "Really?"

    p "Yes!"

    scene boob2 with dissolve
    pause 1

    "Her clothes suddenly started tearing itself apart and uncovered more of her boobs."

    v "Then how's this? "

    p "Whoa-"

    "Her clothes really morphed!"

    "I guess she really is a grim reaper."

    "But more importantly, her boobs are so big!"

    v "Is this good, Human?"

    p "Yes! It's the best!"

    v ". . ."

    "She seems confused about my amusement."

    "But how could I not be when I'm presented with these two beauties?"

    p "Your boobs are so big!"

    v "Hm. They are."

    v "They're too big. They just get in the way when I'm playing."

    v "I could morph my clothes, but I can't make my own body smaller."

    p "No! Don't say that."

    p "They're not too big. Not at all!"

    p "They're beautiful!"

    v ". . ."

    v "Beautiful?"

    v "My boobs are beautiful?"

    p "Yes. They definitely are!"

    v "You really are weird, Human."

    p "Huh? How am I weird?"

    p "It's totally normal to think your big boobs are beautiful."

    v "Is that so?"

    p "Of course it is!"

    v "I just don't get you, Human."

    "What's with this cute clueless girl?"

    "It's still very hard to believe such a pure being like her could be a grim reaper."

    "Wait- if she's fine with showing her boobs like that.."

    "Maybe I could take it even further!"

    "If I'm gonna die anyway, I wanna go out with a bang!"

    p "Sooo.. Vel?"

    v "Hm?"

    p "Since I'm gonna die anyway.. May I request you for something..?"

    v "What is it?"

    p "Well.. can I use your boobs to relieve my hard dick?"

    v ". . ."

    "She stops, and seems to be surprised about what I said despite keeping a blank expression."

    "Was that really too far after all..?"

    v "What do you mean by that?"

    p "Huh?"

    "I was ready for her to turn me down, but she just looks confused."

    p "You didn't understand what I said?"

    v "No."

    "I guess I should have expected this when she had no idea what a dick is in the first place."

    "She didn't seem to mind talking about it, so maybe she wouldn't mind actually doing it too?"

    "If that's the case, maybe I really can do this!"

    p "Well what I mean is.. I want to stick my dick between your boobs."

    v "Between my boobs?"

    v "Why do you want to do that?"

    p "Because it would feel great!"

    v "Would it?"

    p "Yes! And it would get rid of my stiffness."

    v "Hmm."

    p "Please!"

    v ". . ."

    p "Please! This is all I ever wanted!"

    p "It's the only thing I can ask for before I say goodbye!"

    v "I don't really get it, but you seem so desperate right now."

    p "Then.. is that a yes?"

    v "Yes."

    v "Do what you want."

    p "Yes! Thank you!"

    v "You're so weird, Human."

    v "I don't understand why you're getting so excited."

    p "Anyone would get excited if they can get their hands on your breast."

    v "Is that so?"

    v "Well you can start whenever you want."

    p "Then don't mind if I do!"

    $ renpy.music.set_volume(0.8, 0, channel='sound')
    play sound ["<silence .4>","cloth4.ogg"]

    stop music fadeout 1.0

# Titfuck

    scene black with fade
    scene tfuck1 with fade
    show tfuck1s behind tfuck1
    pause 2

    "I told Vel to lay down on her bed, and I got up on top of her to wrap my dick with her breast."

    p "Aahhh- your boobs are so soft."

    p "It feels even better than I imagined."

    v "Do they?"

    p "Yes, they're incredible!"

    p "It feels so good being squished by them."

    v "Hmm."

    "I can't believe this is actually happening."

    "I get to fuck these huge breasts of such a cute girl."

    "A cute girl who's apparently the grim reaper."

    "Should the grim reaper really be this adorable?!"

    "I can't see her as anything but a cute innocent girl."

    show tfuck2 with dissolve
    hide tfuck1

    v "Mmm-"

    "She said that she had never even done this before."

    "I'm so lucky to be the first to feel her like this!"

    "Wait.. does that mean she would just let anyone else do this to her?"

    p "Say.. Vel."

    v "Hm?"

    p "You said this is your first time doing this.."

    p "Is it really fine that it's with me?"

    v "Why are you asking that?"

    p "Well you know.. your first time is supposed to be special or something."

    v "Supposed to be special?"

    v "I don't really get it, Human."

    v "Is there something special in what we're doing?"

    "Khu- that stings a bit."

    "I guess it's to be expected seeing how clueless she is."

    p "Well it is for me.."

    v "Is that so?"

    "*Sigh* I can't even get mad at her."

    "Regardless of what she feels, she's just so cute!"

    "And her boobs just feel too damn good!"

    "How can anyone expect me to be angry with someone as pure as her?"

    show tfuck3 with dissolve
    hide tfuck2

    p "Agh- You're just too cute, Vel!"

    p "I just can't control myself!"

    v "I told you to do whatever you want."

    p "But I don't want to end this so quickly!"

    p "I want to be between you as long as I can."

    v "Mmhh."

    "But I probably won't be able to keep this up for much longer."

    "Stroking my dick against her just feels so good."

    "The pressure of her boobs is too much!"

    v "Hmm-"

    v "You're going so fast, Human."

    p "Because it feels so good!"

    v "Mmmhh."

    v "I can feel your dick getting hotter and hotter."

    p "Ugh- I can't take this for much longer if you talk like that."

    v "Then should I not?"

    p "No- You should!"

    v "Hmm-"

    p "I'm gonna cum soon!"

    v "Come?"

    p "Ahh- Vel! Can I do it in your face?"

    v "I'm not sure what you mean, but you can do what you want."

    p "Then here I go!"

    show tfuckcum with dissolve
    hide tfuck3
    pause 5.2
    show tfuckcum1
    hide tfuckcum


    p "Ahhhh- *pant* That felt amazing."

    v ". . ."

    v "You got it all over my face."

    p "Sorry about that.. but I did ask for permission."

    p "And you look so lewd and cute right now!"

    v "Hmmm."

    v "Then are you done?"

    p "As much as I want to keep going, I really can't right now."

    p "I feel like you drained everything I have."

    v "Did I?"

    p "Yeah- You're just too much."

    v "Mmm."

    v "Then I'm gonna go back playing."

    p "Yeah.. You do that."

    p "I'm gonna go clean up."

    $ renpy.music.set_volume(0.7, 0, channel='sound')
    play sound ["<silence .0>","cloth2.ogg"]

    scene black with fade

    play music "PerituneMaterial_Puppet_loop.ogg" loop

    $ renpy.music.set_volume(0.1, 0, channel='sound')
    play sound ["<silence .0>","faucet.ogg"]

    "That seriously felt amazing."

    "They're the two best things I ever felt my entire life."

    "I could die with no regrets now that I got to play with such heavenly tits."

    "It's not like there's anything holding me in this world anyway."

    stop sound fadeout 1.0

    "I don't have anyone I'm dating and even if there was one, I doubt she would ever feel as great as Vel."

    "My life isn't gonna get any better than this so it's fine to let it all end."

    "Plus I get to die in the hands of such an adorable girl like her!"

    "How could this not be the best ending I could ever hope for?"

    "Well no point in idling."

    "I should go back to her, and get this over with."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound ["<silence .2>","Dooropen1.ogg"]

    scene s1b with fade

    "I went back to her room, and saw Vel is back to playing just like how I first saw her."

    "Does she even do anything else than that?"

    "I guess I'm actually interested to know more about her."

    "But it's too late for that now."

    "I'm only here to let her end me."

    p "Okay. Vel."

    p "My body is ready!"

    p "You can do me anytime!"

    v ". . ."

    show s1c with dissolvefast

    v "Human."

    p "No need for any last words. I'm fully ready for you!"

    v "There was a mistake."

    p "Huh?"

    p "A mistake?"

    p "What was a mistake?"

    v "I was sent to the wrong house."

    p ". . ."

    p "Huh?"

    p "What are you saying?"

    p "How could you be sent to the wrong house?!"

    hide s1c with dissolvefast
    show s1b with dissolvefast

    v ". . ."

    "She just goes back to playing, and avoids my question."

    p "Are you not even gonna answer that?"

    p "Seriously, how could that even happen?"

    p "So am I actually not gonna die?"

    v "If you really think about it, there's no signs of you dying anytime soon."

    v "Why were you so convinced you were actually gonna die?"

    p "Now that you mention it.. I guess you're right."

    p "It's not like I'm sick or anything."

    p "But it could have been an accident or something.."

    p "I don't have any plans to go out as it's the weekend though, so I don't know how an accident can happen."

    p "But wait- How was that my fault?!"

    p "Why didn't you tell me it wasn't me in the first place?!"

    show s1c with dissolve

    v "I didn't know."

    p "How could you not know?!"

    p "Doesn't your job require you to know?"

    v "I was still playing."

    p "You didn't even know anything before you were sent here?"

    v "Mmh."

    "There's not even any hint of shame from the way she answered."

    p "Could anyone please tell me how someone like you is a grim reaper.."

    hide s1c with dissolvefast
    show s1b with dissolvefast

    v ". . ."

    "I'm really having a hard time believing anything she says."

    "Believing she's actually a grim reaper is hard enough, but I can't tell what exactly is going through her mind."

    p "*Sigh*"

    p "I'm happy that I get to live longer though.."

    p "Then what's gonna happen now?"

    v "Hm?"

    p "About your room being in my house."

    p "Are you gonna leave soon?"

    v "Mmm- Yes."

    v "When I'm done playing."

    p "Oh.. of course."

    p "I should have expected that's what you were gonna say."

    p "Then I guess I won't get to see you again, huh?"

    show s1c with dissolve

    v ". . ."

    "Even though she's wearing her usual blank expression, I could tell there's a slight surprise from her eyes."

    v "Why would you want to see me again, Human?"

    p "How could I not want to when you're just so cute?"

    p "I'd die just to be with you forever!"

    v "You can't be with me if you're already dead."

    p "I know that.."

    v "Hmm."

    hide s1c with dissolve
    show s1b with dissolve

    v "I still don't understand you, Human."

    p "I don't really get you too."

    p "I still can't believe you're actually a grim reaper."

    p "All I see in front of me is a cute girl who likes playing games."

    v "I don't know why you keep calling me cute."

    p "Because you really are!"

    show s1c with dissolvefast

    v "Am I?"

    "I keep telling her that she is, but she still doesn't seem to be convinced."

    p "Definitely!"

    p "You're the cutest girl I ever met!"

    v ". . ."

    v "You're really just weird, Human."

    p "No, I'm not! This is completely normal."

    v "Then all humans are weird."

    p "In our point of view, you're probably the weird one."

    hide s1c with dissolvefast
    show s1b with dissolvefast

    p "Which makes me think.. are there actually more grim reapers like you?"

    v "There are."

    p "Oh. There are!"

    p "Are all of them just like you?"

    show s1c with dissolve

    v "Just like me?"

    p "A cute girl who likes playing games."

    v "No."

    p "So you really just like playing games? "

    v "Mmh."

    "So is there like some kind of society of grim reapers just like humans?"

    "Do they have the same things as we do like the game she's playing now?"

    p "How did you even start playing games?"

    v "Hmmm."

    "Vel blanks for a second, visibly thinking hard to answer my question."

    v "I can't remember."

    v "I don't know what I was doing before when I wasn't playing."

    p "Seriously?"

    p "How long has it been for you not to remember?"

    hide s1c with dissolvefast
    show s1b with dissolvefast

    v ". . ."

    v "I don't know."

    v "I don't remember how long I've been doing this."

    p "Really?"

    p "Is your memory that bad, or are you just too addicted to playing games?"

    v ". . ."

    v "I don't know."

    v "I can't think of why I don't remember."

    p "Huh.."

    "She doesn't seem to be lying."

    "She's clearly having a hard time trying to remember."

    p "Does that have something to do with you being a grim reaper?"

    v "Maybe."

    p "Then is that the case for all grim reapers?"

    v "Mmh."

    v "I think so."

    p "Hmmm.. interesting."

    show s1c with dissolve

    v "Is it?"

    p "Huh?"

    "Vel stares at me with curious eyes, as if she's expecting something from me."

    v "Is learning more about me interesting?"

    p "Yes! Knowing more about you is interesting!"

    p "I would like to understand you more."

    v "Hmm."

    hide s1c with dissolvefast
    show s1b with dissolvefast

    "She goes back to her screen, but her expression seems somehow satisfied."

    p "Wait.. Speaking of other reapers again."

    p "Does that mean I could have met a different reaper?"

    p "Were you just assigned randomly to me?"

    "Plenty of seconds passed before she answered me."

    "It seemed like she had to really think what she's going to tell me."

    show s1c with dissolve

    v "Yes."

    p "Then I'm so lucky that it's you!"

    hide s1c with dissolvefast
    show s1b with dissolvefast

    v ". . ."

    v "You're getting so excited again, Human."

    p "Of course I am!"

    p "I'm unbelievably lucky to have met you!"

    v "Are you?"

    p "Yes! I bet you're the cutest of all the reapers."

    p "I can't imagine how someone else could even be cuter than you!"

    v ". . ."

    p "Maybe the biggest and softest too!"

    show s1c with dissolve

    v ". . ."

    v "Hey Human."

    p "Y-yeah?"

    v "Your dick is sticking out again."

    p "Huh? How is it up already?!"

    p "I really felt like I had no energy left when we finished a while ago."

    v "Is it because of my boobs again?"

    p "Yes! That's gotta be it."

    p "Talking about it got me excited down here too!"

    p "Your boobs are just too lewd!"

    v "Then I really should hide them after all."

    p "No-! You really don't need to!"

    v "I don't?"

    p "I told you it's better if you're showing them more!"

    v "Hmm."

    v "You did."

    p "How about... {w}just let me use your boobs again?"

    hide s1c with dissolvefast
    show s1b with dissolvefast

    v ". . ."

    p "If you're gonna leave soon, I'd at least want to do it once again.."

    v ". . ."

    v "Do you really like them that much?"

    p "Of course I do!"

    p "Your boobs are the best things I ever felt my entire life!"

    p "I'll do anything to feel them again!"

    v ". . ."

    v "You're really just weird after all, Human."

    p "Then is that a no..?"

    v "Hmm."

    show s1c with dissolve

    v "When I reach a checkpoint."

    p "Really?!"

    v "Mmh."

    stop music fadeout 2.5

    scene black with fade

    scene nextday with fade
    $ renpy.pause(delay = 2.0, hard = True)
    #pause 2

    ## DAY 2 ###########

    scene black with fade

    "I woke up brooding over how I could possibly forget about Vel and how good she feels, but.."

    play music "PerituneMaterial_Spook4_loop.ogg" loop

    scene door with fade

    "The ominous door is still here."

    "Does that mean Vel is still here too?"

    "She said she would leave when she's done playing."

    "Does that mean she has just been playing, and hasn't stopped even now?"

    "I wouldn't even be surprised if that's the case.."

    "Well only one way to find out."

    "I reached out for the door, and entered the reaper's room once again."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound "Dooropen.ogg"

    stop music fadeout 2.0

    scene door:
        zoom 1.0 xalign 0.5 yalign 0.5
        linear 2.0 zoom 1.5 xalign 0.5 yalign 0.5

    pause 0.5



    scene play2 with fadelong

    play music "PerituneMaterial_Puppet_loop.ogg" loop
    pause 2

    "Just like how I first entered her room, my eyes quickly focused on the girl playing on her bed."

    "She's even more enticing this time as she's pointing out her butt to me."

    "I could even see her pussy.."

    "Does she not wear underwear at all?"

    "Not like I would prefer her to be wearing them though."

    "I thank all the Grim Repears for giving me this blessing."

    "Shit! Even this sight alone is enough to make me hard again."

    "I wonder if she'll let me do things with her again today."

    v "Hey Human."

    "I was startled by her monotonous voice breaking the silence."

    "I wasn't expecting her to start talking to me."

    "The first time I entered here, it was as if she wasn't even aware of my existence."

    p "Umm.. morning Vel."

    p "I thought you said you were gonna leave when you're done playing."

    p "So I was preparing myself for you to be gone by today."

    p "I'm happy that I still get to see you though.."

    p "Have you just been playing all this time?"

    v ". . ."

    v "Yes."

    p "Right."

    "Vel paused for a while before answering me."

    "Did she really need to think that long just to answer yes?"

    "Maybe her memory is really just that bad."

    "Was she really just playing all this time though?"

    p "Do you not even sleep at all?"

    v "Grim Reapers don't feel tired."

    p "So you never actually sleep?"

    v "I do.{w}. sometimes."

    p "I guess that's really convenient for you, so you can just keep on playing."

    p "Then how about food?"

    p "Do grim reapers not need them too?"

    v "Mhm."

    p "But surely you still do it, right?"

    v "No."

    p "Seriously? Is it because grim reapers can still get fat?"

    p "You know I wouldn't mind even if you gain a little."

    v ". . ."

    v "What are you talking about, Human?"

    v "Our bodies never change shape."

    p "Is that right?"

    p "Then why don't you do it?"

    p "You could be eating a lot of delicious food without it affecting your body's shape!"

    p "You know a lot of girls want to be able to do that."

    v "Do they?"

    "I'm getting used to talking with Vel now that I've been able to converse with her since yesterday."

    "I can kind of tell how she's feeling despite the lack of emotions with her face and words."

    "At least I like to think I can.."

    "And even though she doesn't seem to like talking a lot, I can tell she's not completely uninterested about what I tell her too."

    "I still have no idea what's really her deal though.."

    "She did just let me use her boobs twice yesterday, and she didn't seem to mind it."

    "More than anything, it sounds more like she doesn't see what we did the same way as I do."

    "But I guess I can't really expect her to."

    "Even if she looks just like a completely normal cute girl, she's still a grim reaper."

    "Maybe grim reapers are just not interested in sex like how humans are."

    "Not that big of a deal for me if I'm still able to do it with her though!"

    "I've been lost in my thoughts for a while, and Vel hasn't said anything."

    "She's just fully engrossed in her game as usual."

    "I was hoping she would just notice my dick sticking out again.."

    "But she's not even looking at me right now."

    "I still don't fully know her, and can't predict what she'll do, so I probably shouldn't just jump into her and poke her with my dick."

    "She's still a grim reaper after all."

    "I might still get in danger if I do something to make her mad."

    "With nothing in mind to tell her, I tried to look around her room once again."

    "Oddly enough I could actually see more this time, though everything still looks black and hazy."

    "Is it because it's not the first time I've been here?"

    "I glanced around the room, and one thing quickly catches my attention."

    "It's a shelf with a plethora of different games and even a couple of game consoles."

    $ renpy.music.set_volume(0.4, 0, channel='sound')
    play sound ["<silence .0>","foot.ogg"]

    "I walked up to it to examine the collection."

    "It's filled with various genres, from shooters to RPGs and rhythm games."

    "There's even older looking titles that I haven't heard of till now."

    p "This is an impressive amount of games you have here. Have you played all of them?"

    v ". . ."

    "Just like last time, she takes time before answering my question."

    v "I can't remember."

    p "Ah.. right."

    p "I guess I should have expected that when you have a hard time recalling things."

    "The room falls into silence for a moment until Vel speaks again."

    v "I think I have."

    p "Huh? Did you actually remember something?"

    v "No."

    v "But I have a feeling I already played all of them."

    p "A feeling..?"

    p "What do you mean exactly?"

    v "I'm not sure.."

    v "I have a feeling I already played this game I'm playing now."

    v "But I don't remember playing it."

    p "A feeling of already playing it.."

    p "Like you know what's gonna happen next?"

    v "Yes."

    p "Then is that why you're able to play it even without looking at the screen?"

    v "Mmh."

    v "I think so."

    p "Interesting.."

    v ". . ."

    "She feels like she already played her game, but don't remember actually doing it.."

    "Maybe she actually already played it before, but she just can't recall it for some reason."

    "Even if her mind forgets, her body still remembers."

    "Is that really possible though?"

    "How many times has she played the same game to be able to play it without even looking?"

    "Well that might not actually be the case."

    "We might never know for sure, as she can't answer more of my questions."

    "And though she sounds confused, it doesn't look like it really bothers her anyway."

    "She's still just enjoying playing her game like usual."

    "I decided not to linger on the thought anymore, and looked back at the selection of games."

    "Peering through the cases, I see there's local multiplayer games too."

    "Maybe Vel would be up to play something with me."

    p "Hey Vel."

    v "Hm?"

    p "Do you wanna play a game togethe-?{p=0.4}{nw}"

    v "Yes."

    "I wasn't even done with my question, but Vel already answered."

    "I guess she doesn't really have anyone to play with, so it's normal for her to be excited."

    p "Then what should we play?"

    v "You decide."

    p "Then how about a fighting game? That should be fun."

    v "Sure."

    $ renpy.music.set_volume(1.0, 0, channel='sound')
    play sound ["<silence .4>","cloth2.ogg"]

    scene black with fade

    "Vel gets up from her bed, and we set up a console to play with."

    scene play1 with fade

    pause 1.5
    $ renpy.start_predict("images/HJStart.webm")

    p "Have you played this before?"

    v "I can't remember."

    p "Oh.. right. I shouldn't have even asked."

    "Even though that's what she said, I could tell she definitely has, as she immediately picked a character."

    "I took some time deciding on mine, thinking of what's a good match up."

    "It's fun to be able to do this with her, but I'm not gonna take it easy and let her win!"

    "I locked on my fighter, and the match started."

    ". . ."

    p "Vel..."

    v "Hm?"

    p "Aren't you, like, really good at this..?"

    v "Am I?"

    p "Yes you are. I haven't even damaged you once yet!"

    v "I'm just playing normally."

    p "That's exactly what I mean that you're really good!"

    "She doesn't say anything more, and just focuses on the match we're having."

    "But I don't think I could even call it a match.. She's just whooping my ass!"

    "I try to find an opening to hit her, but I'm the only who's being left defenseless doing so."

    "And just like that, it's over."

    "She defeated me in a flash each round, and secured victory."

    v "I won."

    p "You definitely did.."

    p "Looks like I didn't even stand a chance."

    p "But at least you seem to be having fun."

    v "Do I?"

    "Vel looks at me with curious eyes."

    "It's her usual expression, but somehow I could sense that she's happy."

    p "But that's just the first match. I'm sure I can at least defeat you once!"

    v "Hmm.."

    "We kept on playing again and again, match after match."

    "I tried changing my character hoping for a better result."

    "I thought there was actually hope when I managed to hit her once, but that only made her more serious."

    "After that I wasn't able to hit her again, and I continued to lose each and every round."

    p "This is impossible! You're just too good at this."

    v ". . ."

    v "Then do you want to stop?"

    "We've been playing for a while, but Vel still looks like she wants to play more."

    "Of course I'm not gonna stop when her eyes are asking for more!"

    p "No.. I can still keep going!"

    p "But maybe you should at least have a handicap, so I would actually have a chance to win.."

    v "A handicap?"

    p "Yes! I think it's only fair when you're dominating me so hard."

    v ". . ."

    v "If you say so."

    "But what should her handicap be..?"

    ". . ."

    "Vel just stares at me as I'm lost in thought."

    "What could possibly give me a fighting chance when she's this good?"

    "She can play games without looking at them, so maybe that could work."

    "But that probably won't be fun for her anymore.."

    ". . ."

    "After some deliberation with myself, I thought of one."

    p "I got it!"

    v "Hm?"

    p "I thought of a fitting handicap for you!"

    v "What is it?"

    $ renpy.music.set_volume(1.2, 0, channel='sound')
    play sound ["<silence .45>","cloth4.ogg"]

    scene black with fade
    stop music fadeout 1.0
    scene hjstart with fade
    pause 2

    v ". . ."

    v "Hey Human."

    v "Why did you let your dick out?"

    v "And you're so hard again."

    p "This is your handicap!"

    v "Huh?"

    "Vel just stares at my dick in confusion."

    p "You're gonna be jerking me off while we're playing!"

    v "Jerking you off?"

    p "Yes. Play with it just like a joystick!"

    v ". . ."

    v "Would it feel good if I do that?"

    p "Yes it will!"

    p "And you'll only be playing against me with one hand, that should actually give me a chance."

    p "I hope.."

    v ". . ."

    v "If you say so."

    p "Then just grab my dick, and start fiddling with it."

# Handjob #########################

    scene black with fade
    scene hj2a with fade
    pause 2.5

    v "Is this good, Human?"

    p "Yes! Your hand feels so good!"

    p "They feel so soft just like your boobs."

    v "Do I need to continue moving like this as we play?"

    p "Yes, please!"

    p "It shouldn't be a problem for you, right?"

    v "No."

    v "I should still be able to play with my other hand."

    p "Great! As expected of you."

    v "Then let's go back to playing."

    scene black with fadefast2
    scene hj1a with fade
    pause 2

    "Just like before, we pick our characters and begin our match."

    "I was actually hoping this would give me more of a fighting chance.."

    "But it doesn't feel like there's any difference at all!"

    "She's still playing as skillfully as before."

    "She's not even losing focus on her other hand too."

    "She hasn't stopped jerking me off even for a second."

    "If even this is too easy for her then maybe.."

    p "Hey Vel."

    v "Hm?"

    p "Could you try moving your hand more?"

    v "Move my hand more?"

    p "Yes. Please press on my dick harder!"

    v ". . ."

    show hj1b with dissolvefast1
    hide hj1a
    pause 1

    v "Like this?"

    p "Ahh- Yes. That feels really good!"

    v "Does it?"

    p "Yes! Please continue moving just like that."

    v "Mmhh."

    "Her hand really does feel incredible!"

    "She's putting so much pressure on my cock."

    "I told her to do this so she would lose focus on our game, but that doesn't seem to be happening."

    "She's still just playing like usual."

    "If anything, this might be worse for me!"

    "I can't focus on playing when she's making me feel this good."

    show hj1c with dissolvefast1
    hide hj1b

    "Agh- Her hand is feeling even better now."

    "Is she getting the hang of this?"

    "How could she keep touching me like this while also playing a game?!"

    "This is impossible.."

    "I can't possibly keep playing while receiving this much pleasure!"

    v "Hey Human."

    p "Huh?"

    v "You've just been trying to run away from me for a while now."

    v "You can't win if that's all you do."

    p "Sorry, Vel.."

    p "Your hand just feels too good!"

    v "Is that a problem?"

    v "You're the one who told me to do this."

    p "I did.."

    p "I thought it would help me win, but it didn't even make a difference."

    p "Or rather, it just made me lose my focus."

    v "Then should I stop?"

    p "No! Of course not."

    p "I want you to keep stroking me!"

    v ". . ."

    v "Then we should stop playing."

    p "Huh?"

    p "Stop playing?"

    p "Did you really say that?!"

    p "Isn't playing all you want to do?!"

    v ". . ."

    v "We can't keep playing if you're like this."

    p "Well that's true.."

    p "But is that really fine with you?"

    v "Mmh."

    p "But you're still gonna continue rubbing me?"

    v "Yes."

    p "You're really just the best, Vel!"

    v ". . ."

    scene black with fadefast2
    scene hj2b with fade
    pause 2

    v "Hmm.."

    v "Aren't you even harder than before, Human?"

    p "That's because you're gripping me even harder!"

    p "And the way you look at my dick is just too lewd!"

    v "Is it?"

    "The way she's stroking me is even more incredible now that she's solely focusing on my dick."

    "I'm so happy that she's willing to stop playing just to caress me like this."

    "But now that we're not playing, there's nothing that's distracting me from her hand."

    "She just feels so good that I feel like I can cum if I'm not careful."

    "But I want her to keep stroking me like this."

    "I got to hold out for as long as I can!"

    show hj2c with dissolvefast1
    hide hj2b

    v "Does this really feel good, Human?"

    p "Huh? Why are you even asking that?"

    p "Of course it does!"

    p "Your hand just feels amazing!"

    p "Especially with the way you're gripping on me."

    v "First you asked me to let you use my boobs, now you're having me use my hand."

    v "I don't really get it."

    p "You really don't need to think too much about it."

    p "Having you play on my cock in any way feels good!"

    v "Is that so?"

    p "Of course!"

    p "I'm sure every part of Vel would feel great!"

    v ". . ."

    v "Then are you gonna come again like last time?"

    p "Yes.. actually I'm trying really hard not to right now."

    p "But it's so hard to resist with how you're stroking me."

    v "Why are you trying to resist it?"

    p "Because I want you to keep doing this even longer!"

    v "But wouldn't you feel good if you come?"

    p "Yes, cumming from your hand would feel great!"

    show hj2b2 with dissolvefast1
    hide hj2c
    pause 1

    v "Then you should just do it."

    p "Ahh- Vel, you're being really rough."

    v "Is this wrong?"

    v "Does it not feel good?"

    p "No.. It feels really great!"

    p "Keep stroking me just like that!"

    v "Mmh."

    v "I can feel your dick getting hotter."

    v "Are you gonna come?"

    p "Yes!"

    v "Then do it anytime."

    p "Ahhh- I'm cumming, Vel!"

    show hjcum
    pause 0.5
    hide hj2b2
    pause 6.5
    show hjend with dissolve
    hide hjcum

    p "*pant* That was incredible, Vel."

    v "Was it?"

    p "Yes! It felt really good."

    v "You let out so much."

    p "That just shows how good it felt."

    v ". . ."

    v "It feels really hot."

    p "Ugh- if you say things like that, you're gonna turn me on even more!"

    v "Is that bad?"

    p "Well that depends if you want to go back playing or not.."

    v "What do you mean?"

    p "Even though you already wringed a lot from me, it seems like my dick can still go for another."

    v "Even though you just came?"

    p "Yes! My dick can still keep going because of how lewd Vel is."

    v ". . ."

    v "Then what do you want to do next?"

    p "Huh? Is it really fine?!"

    v "Yes."

    p "I'm really just so lucky to have you, Vel!"

    v "You're getting so excited again, Human."

    scene stare with fade

    v "Then what are we gonna do next?"

    p "Hmmmm..."

    v ". . ."

    "What should I do next with her?"

    "There's so many things I could think of."

    v "Human?"

    v "Do you want to use my boobs again?"

    p "Huh?"

    "I was caught off guard when she offered a suggestion."

    "Is she starting to feel something with what we have been doing?"

    p "Well your boobs really feel great.."

    p "But I wanna try something new this time."

    v "Something new?"

    v "Then what do you want to do?"

    p "Well.."

    p "Could you come here, and sit on my lap?"

    v "On your lap?"

    v ". . ."

    "Vel ponders for a moment with her face filled with confusion."

    v "What do you plan to do, Human?"

    p "You'll see once you get on top of me."

    v "Hmm.."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound ["<silence .8>","cloth5.ogg"]

    scene black with fade

    "Her eyes are still brimming with confusion, but she slowly sets her body down on mine."

    "And I gently guided her to my desired position."

    scene tjob2s with fade
    pause 1

    v "Huh?"

    v "What are you doing, Human?"

    v "You're so close."

    p "Just set your legs right here.."

    p "And let me slip my dick in here.."

    scene tjob1s1 with fade
    pause 1

    v "Between my thighs?"

    p "Indeed! This time I want to cum from your thighs!"

    v ". . ."

    v "Do humans really do this?"

    p "Of course!"

    p "I wanna feel the plumpness of your thighs!"

    p "It would feel great rubbing my dick on them."

    p "Even just being between them already feels good!"

    v ". . ."

    v "Is that so?"

    v "Then what do you want me to do?"

    p "You can just relax, but could you please squeeze your thighs together?"

    show tjob1s2 with dissolve
    hide tjob1s1

    v "Like this?"

    "Vel tightens her legs together, and squishes my dick between her."

    p "Ahh- Yes! That feels really good."

    p "Then just stay like that, and I'll do the moving."

    v "Mmh."

# Thighjob ##############

    show tjob1 with dissolve
    pause 0.5
    hide tjob1s2

    p "This really feels amazing like I imagined!"

    p "Penetrating your thighs like this and feeling your softness."

    v "Does it?"

    p "Yes! I love feeling the friction between them."

    v ". . ."

    v "This feels kind of weird."

    p "Oh.."

    p "Then do you not like it?"

    v ". . ."

    v "I don't know."

    p "We could stop if you want to."

    p "I don't want to make you feel uncomfortable."

    v ". . ."

    v "It's fine."

    p "Are you sure?"

    v "You seem really happy right now."

    v "So it's fine."

    p "Of course I am, especially if you say something like that!"

    p "I'm just falling in love with you even more!"

    p "And I get to feel all of your softness like this."

    p "How could I not be happy?"

    scene tjob2 with fade

    v "Really?"

    p "Yes! I really just want to be with you forever!"

    v ". . ."

    p "And just as I thought, everything about you just feels really good!"

    v "Hmm.."

    p "Especially your boobs. They're just so soft!"

    p "I can never get tired of feeling them like this."

    v "Is that true?"

    p "Definitely! I got to feel them so much yesterday, but I can't get enough of them."

    p "And having your body so close to mine.."

    p "Feeling your warmth like this.."

    p "I never want to let you go."

    v ". . ."

    v "You're weird, Human."

    p "How am I so?"

    p "I'm just expressing how much I love you."

    v "Are you forgetting that I'm a Grim Reaper?"

    p "Of course not."

    p "But that doesn't matter!"

    p "You still just look like a really cute girl to me."

    p "It's still even hard to believe that you're an actual grim reaper."

    v ". . ."

    v "If you say so."

    scene tjob1 with fade

    "We both fell into silence, as I continue to grind my dick between her."

    "The whole time, Vel is just staring at me with her usual blank expression."

    "But despite her dull face, she still looks really lewd right now."

    p "You're really just too much, Vel!"

    v "Hm?"

    p "Rubbing my dick between your thighs just feels so good."

    p "And the way you're looking at me just makes it even better!"

    v "Does it?"

    v "I'm just looking at you the same as usual."

    p "Maybe.. but I feel like it's different somehow."

    p "I just feel really intimate right now.."

    v "Intimate.."

    v "Is that good?"

    p "Yes! It's making everything feel even better."

    v ". . ."

    v "Then are you gonna come again?"

    p "Yes. I'm getting close!"

    p "I can't stop myself when you just feel this good!"

    v "Then should I squeeze you even harder?"

    p "Please do!"

    "Vel presses her thighs together even harder, making me reach my limit."

    p "Ugh- Yes! This feels amazing!"

    p "I'm gonna cum, Vel!"

    v "Mmh."

    show tjobcum with dissolve
    pause 0.5
    hide tjob1
    pause 4
    show tjobend with dissolve
    hide tjobcum

    p "*pant* *pant*"

    p "That felt even better than last time."

    v "Did it?"

    p "Yes! Your thighs are amazing!"

    v "Hmm.."

    v "Your fluid feels so hot, Human."

    v "It's all over my thighs."

    p "Yeah *pant* I think I let out all I have in the tank."

    p "I feel so exhausted right now."

    "Maybe going for another round right away wasn't the best idea."

    "But I have no regrets when it felt that great."

    "I'm really feeling much more exhausted though."

    "I've never felt something like this before."

    scene blur1 with fade

    $ renpy.music.set_volume(0.2, 0, channel='music')

    play music "Abyss.ogg" loop

    v "Hey Human."

    "Huh?"

    "I heard Vel calling out to me, but it sounded so distant."

    "How could that be when she's so close to me?"

    v "Human?"

    scene blur2 with dissolve

    $ renpy.music.set_volume(0.4, 0.5, channel='music')

    $ renpy.music.set_volume(0.3, 0, channel='sound')
    play sound ["<silence .0>","flash3.ogg"]

    "Ugh! My head is starting to spin."

    "What's happening to me?"

    "Somehow my body feels really weak."

    "My vision is starting to get blurry."

    p "Vel.."

    "Just saying her name took a lot out of me."

    "At least it looks like she actually heard me."

    v "Is there a problem?"

    p "Did you.. always feel this heavy?"

    v ". . ."

    v "What do you mean by that?"

    "I tried to answer her, but no words came out."

    scene blur3 with dissolve

    $ renpy.music.set_volume(0.6, 0.5, channel='music')

    "No good.."

    "My body is falling apart."

    "I can't keep my eyes open."

    v "Hey Human."

    "Vel is just staring at me so intently."

    v ". . ."

    "Is she getting worried about me?"

    "I can't tell as my vision is too hazy now."

    "But I bet it's still just her usual blank expression."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound ["<silence .6>","cloth5.ogg"]

    scene black with fade

    "I feel her arms tug on me even harder."

    v "Human?"

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound ["<silence .0>","cloth6.ogg"]

    "She shakes her hand on my body, trying to get a response."

    "That was the last thing I felt before I fell into total darkness."

    stop music fadeout 2.0
    $ renpy.music.set_volume(0.0, 1, channel='music')

    pause 2.5


    "What happened?"

    "The last thing I remember I was in the warm clutches of Vel's thighs."

    "Then my body started feeling heavy."

    "Did I faint?"

    "Just from cumming twice..?"

    "Am I really that pathetic?"

    "Or is Vel really just too much?"

    que2 "Hey."

    "As my mind and body starts regaining consciousness, I hear a hazy voice calling out."

    que2 "Hey human!"

    "Human?"

    "Is that Vel?"

    que2 "Wake up!"

    "No..{w} That's not Vel."

    "It sounds too energetic to be her."

    "Vel would never shout like that."

    "But then who is it?"

    scene figure with fadelastlong

    pause 0.6


    "I was finally able to open my eyes, but everything still looks cloudy."

    "I can make out a figure of a girl looking down at me."

    "A figure I'm unfamiliar with."

    "That's not Vel.."

    scene black with fade

    que2 "Hey! Wake up already!"

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound "punch.ogg"

    "Ugh-!"

    "I suddenly felt something bludgeoning my stomach, and I finally regained all of my consciousness."

    scene lookw with fadelastlong1:
        zoom 2 xalign 0.45 yalign 1.0

    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Puppet_loop.ogg" loop

    pause 1

    "What greeted me is a commendable pair of breasts looking down at me."

    "The only thing stopping me from thinking they're great is my experience of Vel's perfect tits."

    que2 "Hey. Up here."


    scene lookw with dissolve:

    pause 0.8

    "Looking at where the voice is actually coming from, I found a girl I've never seen before."

    "But despite not knowing her, I can sense a familiar aura radiating from her."

    "It's an aura I've only come to know recently."

    que2 "Are you okay?"

    "A worried but cheerful-sounding voice came out from the girl staring at me."

    p "How are you gonna ask me that when you just slammed my gut?!"

    scene looka with dissolve:

    que2 "You wouldn't wake up so I had to do it."

    que2 "There was no other way."

    p "You didn't have to do it so hard."

    scene lookt with dissolve:

    que2 "Sorry about that. Sometimes I misjudge my strength."

    scene lookw with dissolve:

    que2 "But more importantly, who are you, and why are you here?"

    que2 "Where is Velvel?"

    p "Velvel?"

    p "Are you talking about Vel?"

    p "How do you know her?"

    p "How did you even get here in the first place?"

    que2 "I'm the one asking you that."

    que2 "Humans like you shouldn't be here."

    p "Humans?"

    "That's right. She was calling me Human when she was trying to wake me up."

    "I've only met one other girl that called me like that so far."

    "Then does that mean..?"

    p "Are you a grim reaper too?"

    scene looks with dissolve:

    n1 "Of course I am!"

    n1 "What else would I be?"

    "This cheery girl's claim of being a reaper is even far less believable than Vel."

    "She's way too bright and upbeat compared to the reaper I previously met."

    p "Well I wasn't expecting grim reapers to look like cute girls."

    scene lookx with dissolve:

    n1 "Cute?! You don't need to flatter me like that, Human!"

    n1 "You're so naughty!"

    p "I was pertaining more to Vel."

    scene lookc with dissolve:

    n1 "Eh?"

    n1 ". . ."

    n1 "But I'm cute too, right?"

    scene lookh with dissolve:

    n1 "Though I can't argue. Velvel is really cute."

    n1 "Velvel is the cutest of them all!"

    n1 "{size=-10}But Decadeca is also really cute...{/size}"

    p "What was that? I couldn't really hear you."

    scene looka with dissolve:

    n1 "Huh? It's nothing you should be concerned about!"

    n1 "You'd probably never meet her anyway."

    p "Her?"

    p "Well nevermind about that."

    p "I want to know how you're related to Vel, besides being another reaper."

    scene lookx with dissolve:

    n1 "Oh my! Are you interested in me, Human?"

    p "I was asking about Vel."

    scene lookc with dissolve:

    n1 "Oh.. {w}right."

    scene lookh with dissolve:

    n1 "Of course I'm close to Velvel."

    n1 "In fact, I'm her one and only best friend!"

    p "Her best friend?"

    "I couldn't even imagine Vel having a friend, but then again I've only known her for two days now."

    n1 "That's right! I've been with Velvel longer than anyone else."

    n1 "I know everything about her!"

    p "Then where is she right now?"

    scene lookc with dissolve:

    n1 "I don't know.."

    n1 "I've been searching for her, and just now finally found her room."

    n1 "But she wasn't here, and all I found is a human lying on her couch."

    n1 "Who are you, and why were you sleeping in her room?"

    n1 "What did you do to my Velvel?!"

    p "I live in this house, and her room just suddenly appeared here yesterday."

    scene lookw with dissolve:

    n1 "Oh. Is that so?"

    n1 "Then, on behalf of Vel, I'm sorry for intruding on your house."

    "The reaper suddenly spoke in an honest and polite tone which caught me off guard."

    p "Huh?"

    p "No, it's fine."

    p "Actually I'm happy that she appeared before me."

    n1 "Happy? Why is that?"

    p "Well.. I don't think I should actually talk about the reason."

    n1 "Eh? Why can't you?"

    n1 "Why would a human be happy to meet someone like Velvel.."

    n1 "Aside from her being really cute of course.."

    n1 "All she does is play games all day."

    n1 "Surely you weren't happy just by playing with her, right?"

    n1 "Unless it was a different type of playing..?"

    scene looksh with vpunch:
        zoom 1.02 xalign 0.5 yalign 0.5

    n1 "Human!"

    p "Y-yes?"

    n1 "D-d-did you-?!"

    n1 "Did you do lewd things with Velvel?!"

    p "Well..."

    p "Is it bad that I did?"

    scene looksh2 with vpunch:
        zoom 1.03 xalign 0.5 yalign 0.5

    n1 "*Gasp*"

    "Lost in total shock, she pauses for a few seconds."

    n1 "H-how could that even be possible?"

    n1 "How did Velvel do lewd things before me?!"

    p "That's what you're concerned about?"

    scene lookc with dissolve:

    n1 "Am I just not cute like her after all?"

    p "I don't think that's the reason at all."

    p "I probably would have done the same if you were the first reaper who presented themselves to me."

    scene lookx with dissolve:

    n1 "Really?"

    n1 "You don't need to say things like that!"

    n1 "You're so lewd, Human!"

    scene looks with dissolve:

    n1 "Speaking of lewd.."

    scene lookss with dissolve:

    "She averts her eyes, and a mischievous smile emerges on her face."

    "I turned to look at the direction she's gazing, and quickly realized she's looking straight at my dick."

    scene lookx with dissolve:

    n1 "Just look at you, Human!"

    n1 "If you were that happy to see me, you should have just said so!"

    p "Huh? No- that wasn't what I'm thinking."

    scene lookss with dissolve:

    n1 "You don't need to be shy."

    n1 "I understand why you would get hard seeing me."

    "Her crazed eyes are totally locked on my dick."

    p "Hey! What are you doing?"

    "She slowly inches herself closer to me, moving her hand to reach for my rod."

    $ renpy.music.set_volume(0.6, 0, channel='sound')
    play sound "Dooropen2.ogg"

    "But before she was able to grab onto me, we heard the door suddenly open."

    v "Human, are you awake?"

    scene lookl with dissolve:

    "It's Vel! She came back just in time."

    v ". . ."

    v "What are you doing?"

    v "That's my Human."

    "Seeing and hearing Vel made the frenzied reaper latch onto her rather than my cock."

    ##Talk################## ###########################################################

    scene black with fade

    show talkbg behind black

    show veltalkg behind black:
        zoom 1.01 xalign 0.15 yalign -0.5

    show neutalkg behind black:
        zoom 1.01 xalign 0.8 yalign -0.5

    hide black with dissolve

    pause 0.3

    show neutalkg at bounce1:
        zoom 1.01 xalign 0.8 yalign -0.5


    n1 "Velvel there you are!"

    n1 "I've been searching for you for so long."

    v "What were you doing just now?"

    show neutalkg away:
        zoom 1.01 xalign 0.8 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.85 yalign -0.5

    n1 "Well you know.. I just thought I'd help the human right there with the problem in his pants."

    v "You don't need to do that."

    v "I'm all he needs to fix that."

    show neutalkg happy at bounce1:
        zoom 1.01 xalign 0.85 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.8 yalign -0.5

    n1 "Oh don't be like that Velvel!"

    n1 "We can share him. It would be more fun with both of us!"

    v "No."

    show neutalkg cry:
        zoom 1.01 xalign 0.8 yalign -0.5
        ease 0.4 zoom 1.01 xalign 0.75 yalign -0.5

    n1 "Why?"

    n1 "Don't you want to have fun with me?"

    v "I don't want to share him with you."

    show neutalkg happy:
        zoom 1.01 xalign 0.75 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.8 yalign -0.5

    n1 "Oh my! Velvel."

    n1 "I never expected you to say something like that."

    n1 "When did you get so lewd?"

    v "What are you talking about?"

    v "Why are you even here in the first place?"

    n1 "Do you really need me to answer that?"

    show neutalkg happy at bounce1:
        zoom 1.01 xalign 0.8 yalign -0.5

    n1 "I'm here cause I'm worried about my best friend!"

    v "Why are you really here?"

    show neutalkg cry:
        zoom 1.01 xalign 0.8 yalign -0.5
        ease 0.4 zoom 1.01 xalign 0.75 yalign -0.5

    n1 "Why don't you believe me?"

    n1 "I was sent here by Suisui."

    show neutalkg wor:
        zoom 1.01 xalign 0.75 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.8 yalign -0.5

    n1 "You've been missing for a couple of weeks now, and you haven't been doing your job!"

    n1 "She tasked me to track you down, and get you to do what you need to do."

    n1 "I've been searching for so long, and only found where you are now."

    show neutalkg cry:
        zoom 1.01 xalign 0.8 yalign -0.5

    n1 "Why would you hide from your best friend too?"

    n1 "You could have told me where you were, and I would have kept it a secret!"

    v "No, you won't."

    show neutalkg happy at bounce1:
        zoom 1.01 xalign 0.8 yalign -0.5

    n1 "You're right!"

    n1 "I wouldn't be able to keep it, especially from Suisui."

    show neutalkg cry:
        zoom 1.01 xalign 0.8 yalign -0.5
        ease 0.4 zoom 1.01 xalign 0.85 yalign -0.5

    n1 "She was starting to get mad, and I didn't want her to punish me again."

    n1 "She's too scary when she's mad!"

    n1 "Even scarier than you."

    v "I'm not scary."

    show neutalkg happy at bounce1:
        zoom 1.01 xalign 0.85 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.8 yalign -0.5

    n1 "Definitely not right now!"

    n1 "You're really cute when you're in this form."

    "The two reapers have been talking for a while, and seem to have forgotten about me."

    p "Ummm... Hey Vel."

    p "Do you actually know this other reaper?"

    show neutalkg happyl:
        zoom 1.01 xalign 0.8 yalign -0.5
        ease 0.3 zoom 1.01 xalign 0.82 yalign -0.5

    show veltalkg look:
        zoom 1.01 xalign 0.15 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.13 yalign -0.5


    n1 "Oh right. The human!"

    n1 "I almost forgot about you when I saw Velvel."

    n1 "I guess I still haven't properly introduced myself."

    n "My name is Neu."

    scene note with fade

    "Neu is pronounced as \"New or Nyu\""

    scene black with fade

    show talkbg behind black

    show veltalkg look behind black:
        zoom 1.01 xalign 0.13 yalign -0.5

    show neutalkg happyl behind black:
        zoom 1.01 xalign 0.82 yalign -0.5

    hide black with dissolve

    pause 0.3

    n "I'm a Grim Reaper just like Velvel, but you already know that."

    show neutalkg happyl at bounce1:
        zoom 1.01 xalign 0.82 yalign -0.5

    n "And like I told you before I'm Velvel's best friend!"

    show veltalkg blink:
        zoom 1.01 xalign 0.13 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.15 yalign -0.5

    v "No, you're not."

    show neutalkg happy:
        zoom 1.01 xalign 0.82 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.75 yalign -0.5

    n "You don't need to be shy Velvel!"

    n "You know how long we've been together."

    v "I don't remember."

    show neutalkg cry at bounce1:
        zoom 1.01 xalign 0.75 yalign -0.5

    n "How could you not remember?!"

    show neutalkg hehe:
        zoom 1.01 xalign 0.75 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.8 yalign -0.5

    n "Actually I don't remember exactly too."

    n "It's been so many years."

    p "So you two are actually friends?"

    show neutalkg happyl at bounce1:
        zoom 1.01 xalign 0.8 yalign -0.5

    show veltalkg look:
        zoom 1.01 xalign 0.15 yalign -0.5

    n "Isn't that obvious?"

    v "I guess so."

    p "I didn't think that you'd be friends with someone as energetic as her."

    show neutalkg happyl:
        zoom 1.01 xalign 0.8 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.83 yalign -0.5

    n "Velvel doesn't really have any other friends beside me!"

    n "Most of them don't know how cute she is."

    show veltalkg blink:
        zoom 1.01 xalign 0.15 yalign -0.5

    v "I don't need friends."

    show neutalkg happy:
        zoom 1.01 xalign 0.83 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.75 yalign -0.5

    n "Right. All you need is video games."

    p "So all Vel does is really just play games all day?"

    show neutalkg happyl at bounce1:
        zoom 1.01 xalign 0.75 yalign -0.5

    n "Yeah! She doesn't even do her job properly anymore."

    show veltalkg blink:
        zoom 1.01 xalign 0.15 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.18 yalign -0.5

    v "I still do them."

    show neutalkg wor:
        zoom 1.01 xalign 0.75 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.8 yalign -0.5

    n "Hmmm.. I guess you still do."

    n "This is a new record for how long you haven't done them though."

    v "Is it?"

    n "Yes! Do you not even realize how long you've been gone?"

    show neutalkg wor at bounce1:
        zoom 1.01 xalign 0.8 yalign -0.5

    n "Actually I'm still shocked by the reason you were even gone in the first place!"

    n "I never expected you to be with a human."

    n "You never showed any interest in them before."

    show veltalkg look:
        zoom 1.01 xalign 0.18 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.15 yalign -0.5

    v ". . ."

    v "It was the human who talked to me first."

    show neutalkg happy:
        zoom 1.01 xalign 0.8 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.75 yalign -0.5

    n "Eh really? Was that really the case?"

    n "But he wouldn't have talked to you if you didn't come here in the first place."

    show veltalkg blink:
        zoom 1.01 xalign 0.15 yalign -0.5

    v ". . ."

    show neutalkg happy at bounce1:
        zoom 1.01 xalign 0.75 yalign -0.5

    n "You don't need to be shy Velvel!"

    n "I'm interested in them too!"

    n "It's totally normal you're also interested."

    n "You even did lewd things with him!"

    show veltalkg look:
        zoom 1.01 xalign 0.15 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.12 yalign -0.5

    v "It was his idea."

    show neutalkg happyl:
        zoom 1.01 xalign 0.75 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.8 yalign -0.5

    n "Is that true?"

    p "Well.. I did ask her if I can do it with her."

    n "But Velvel did give you her consent."

    show neutalkg happy:
        zoom 1.01 xalign 0.8 yalign -0.5

    n "You wouldn't have said the same to anyone else, right Velvel?"

    show veltalkg blink:
        zoom 1.01 xalign 0.12 yalign -0.5

    v ". . ."

    v "I don't know."

    show neutalkg happy at bounce1:
        zoom 1.01 xalign 0.8 yalign -0.5

    n "You're really just so cute!"

    n "I've known you for so long now, so it's fine if that's the case."

    n "I'm sure you'll understand it better soon."

    show veltalkg blink:
        zoom 1.01 xalign 0.12 yalign -0.5
        ease 0.5 zoom 1.01 xalign 0.15 yalign -0.5

    v "Will I?"

    n "Yes! This human would help you with it."

    show neutalkg happyl:
        zoom 1.01 xalign 0.8 yalign -0.5
        ease 0.3 zoom 1.01 xalign 0.83 yalign -0.5

    n "Isn't that right, human?"

    show veltalkg look:
        zoom 1.01 xalign 0.15 yalign -0.5

    p "Huh? What do you mean exactly?"

    show neutalkg happyl at bounce1:
        zoom 1.01 xalign 0.83 yalign -0.5

    n "Oh come on! You should know what I'm saying."

    $ renpy.music.set_volume(0.025, 1, channel='music')

    menu:
        "I don't.":
            jump idkchoice

        "Does Vel like me?":
            jump likeme

    label idkchoice:
    p "No, I really don't have an idea."

    show neutalkg happyl at bounce1:
        zoom 1.01 xalign 0.83 yalign -0.5

    n "Huh?! Don't start acting dense now!"

    n "I'm talking about Vel liking you!"

    p "Huh? What are you saying?"

    p "Vel likes me?"
    stop music fadeout 1.0
    jump afterchoice

    label likeme:
    p "Well I do know what you're getting at, but it's pretty hard to take it all in."

    p "Does.. Vel actually like me?"
    stop music fadeout 1.0
    jump afterchoice


    label afterchoice:

    scene boobt with fade

    $ renpy.music.set_volume(0.05, 1, channel='music')
    play music "PerituneMaterial_Wish5_HarpOnly_loop.ogg" loop

    v ". . ."

    v "Like you?"

    n "Isn't that obvious already?!"

    v "Is it?"

    v "I don't really get it."

    "Vel actually likes me?"

    "I do feel like she's been softening up to me since I met her yesterday."

    "But I thought she wasn't even capable of abstract emotions like that."

    n "You don't have to get it Velvel."

    n "But you can talk to your best friend anytime if you need to!"

    scene black with fade
    stop music fadeout 1.0

    show talkbg behind black

    show veltalkg blink behind black:
        zoom 1.01 xalign 0.13 yalign -0.5

    show neutalkg happy behind black:
        zoom 1.01 xalign 0.8 yalign -0.5

    hide black with dissolve
    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Puppet_loop.ogg" loop

    pause 0.3

    v "I won't."

    show neutalkg cry at bounce1:
        zoom 1.01 xalign 0.8 yalign -0.5

    n "At least say you would consider it!"

    scene tblur1 with dissolve
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.4, 0, channel='music')

    play music "Abyss.ogg" loop

    $ renpy.music.set_volume(0.2, 0, channel='sound')
    play sound ["<silence .0>","flash1.ogg"]

    "Ugh! Suddenly a sharp pain pierces my head."

    "My vision starts getting blurry. It was just like what happened before I passed out a while ago."

    scene tblur2 with dissolve

    "The two reapers quickly notice that I'm visibly in pain."

    v "Human?"

    n "Hey! Are you okay?"

    n "What's happening to you?"

    p "My head.. hurts."

    n "Your head hurts? What do you mean exactly?"

    v "It was just like what happened a while ago."

    n "What do you mean?"

    v "Human passed out a while ago when I was on top of him."

    n "Huh? He passed out?!"

    n "How long has he been here in your room?!"

    v "He stayed here the whole time last night."

    n "Then it's only to be expected his body would start feeling wrong!"

    n "Humans are not supposed to stay in our world! Do you not remember that?"

    scene tblur3 with dissolve

    v ". . ."

    v "I forgot."

    n "*Sigh* You shouldn't forget about the important things, Velvel."

    v "What do we do?"

    n "We just need to get him out of your room, and he should be fine."

    n "Come on. Let's hurry!"

    v "Human can you walk?"

    p "Y-yeah.."

    scene black with fade

    "Vel grabbed me by the arm, and guided me out of her room."

    $ renpy.music.set_volume(0.3, 0, channel='sound')
    play sound ["<silence .3>","foot.ogg"]

    "My head is aching too much and I'm about to pass out again, but I forced myself to walk as Vel leads me."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound "Dooropen.ogg"

    "I hear another door opening, and feel Vel gently guiding me to lay down."

    "I could hear her talking to Neu, but I can't make out any of the words they say."

    "The pain was too much for me to bear, and I passed out again."

    scene black with fade
    stop music fadeout 1.0

    "However it only felt a single moment."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound ["<silence .0>","cloth2.ogg"]

    "I was able to regain consciousness, as I feel something heavy being put on top of me."

# Pre Cow #########################

    show cowbeg with fade
    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Wish5_HarpOnly_loop.ogg" loop
    pause .5

    "I opened my eyes, and was greeted by Vel sitting on top of me."

    v "Human are you okay?"

    p "Yeah, now that I get to see how beautiful you are on top of me."

    p "All the pain I was feeling is now completely healed by this sight alone."

    p "Not that I'm complaining, but why are you riding me?"

    v "Neu told me I should do this."

    v "She said it's what lovers would do."

    p "Lovers.."

    p "Do you even understand what that means?"

    v "No."

    p "I figured.."

    v "What does it mean, Human?"

    "Vel stares at me intensely, waiting for my answer."

    p "Well.. I'm not really sure how I should explain it."

    p "It's someone you want to be with, and you do sexual things with them. I guess?"

    v ". . ."

    v "You've done sexual things to me. Does that make us lovers?"

    "Hearing her say that made my heart skip a beat."

    p "Well I want us to be."

    p "Do you want to be with me, Vel?"

    v ". . ."

    v "I don't know."

    "The mood felt really good, and I thought she was just gonna go with the flow."

    "I guess I really shouldn't have expected her to say yes."

    v "But I feel different when I'm close to you."

    p "Different?"

    p "What do you mean?"

    v "I never felt something like it before."

    v "My body feels hot, and I don't know what to think."

    p "Vel! Is that really how you feel?"

    p "I think that must be what love is!"

    v "Is it?"

    p "Well I wouldn't know what else to call it so it must be."

    v "Love?"

    v "I love Human?"

    p "I love Vel too!"

    "She said it as a question, but I couldn't help myself from saying it back. "

    v ". . ."

    v "I still don't get it."

    p "It's fine if you don't understand yet, as long as I know what you're feeling."

    p "You should just tell me what you're thinking, and I would help you understand."

    v "Would you?"

    p "Of course! I'll always be there for you."

    v "Then there's something else I'm feeling."

    p "What is it?"

    "Vel pauses for a second."

    "I could tell that she wasn't sure how she should say the words she's about to."

    v "Ever since you were rubbing your dick against my thighs, my body has been feeling really hot at a certain spot."

    p "Do you mean your pussy?"

    v "Mmh."

    v "It still feels hot even now."

    v "I don't know why it feels like that."

    p "I'm sorry for leaving you out like that Vel!"

    v "Hm? Why are you apologizing?"

    p "It's my fault for using your thighs, and not following through."

    v "It's not your fault you passed out."

    v "I forgot that you're not supposed to stay in my room."

    v ". . ."

    "I could feel the sadness behind Vel's words despite her face not showing it."

    p "It's fine. That wasn't your fault."

    p "I'm alright now, so you don't have to worry about it."

    v "Really?"

    p "Yes! Actually you're the one with the problem right now."

    p "I would help you fix that immediately."

    v "How do you plan to do that?"

    stop music fadeout 1.0
    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Puppet_loop.ogg" loop

    p "With my dick, of course!"

    p "He has been raging since I saw you on top of me."

    v "I can feel it too."

    p "You're just making me even harder by saying things like that!"

    v "Is that good?"

    p "Definitely!"

    v "Then what do you want me to do?"

    p "You can just stay there, and let me put my dick inside of you."

    p "I would do the moving, so you don't have to worry about anything."

    v "Okay."

    p "Oh! One more thing."

    v "Hm?"

    p "It would be much better if you take off your clothes."

    p "I want to see how beautiful you are in all of your glory!"

    v ". . ."

    v "You're still weird, Human."

    v "But if you say so."

    show cowstart
    pause 2.4
    hide cowbeg
    show cowend
    pause 0.5
    hide cowstart

    p "Whoa! That was the first time I saw your clothes fully morph like that."

    p "Your boobs are as beautiful as ever."

    p "You're just way too sexy Vel!"

    v "Am I?"

    p "Yes! You're too enticing."

    p "My dick can't wait to be inside you anymore."

    v "You can do it anytime."

    stop music fadeout 1.0

    scene black with fade
    show cow1 with dissolve
    pause 1.5
    hide cowend

    p "Ahh- Vel. You feel incredible."

    v "Do I?"

    p "Yes! Your insides are so tight."

    p "It's gripping my dick as if it doesn't want to let go."

    p "You feel so hot and slippery too!"

    v "Mmmh-"

    v "Your dick feels really hot too."

    v "My body is feeling even hotter than before."

    p "Yeah. I can feel your warmth directly."

    p "Your pussy is really sopping wet too."

    p "Must be because you've been waiting for me all this time."

    p "I really should have penetrated you sooner."

    v "Ah- Human."
    scene black with fade
    hide cow1
    scene cowxray with dissolvefast
    pause 1.5


    v "Your dick.."

    v "It's thrusting so deep inside."

    v "It's hitting me."

    p "Yeah- I can feel your womb."

    p "My dick keeps kissing its crevice."

    p "Does this feel good for you Vel?"

    v ". . ."

    v "I don't know."

    v "Maybe."

    v "I don't know how I'm feeling."

    scene black with fade
    hide cowxray
    scene cow1 with dissolvefast
    pause 1.5


    p "That just means you're feeling good!"

    v "Does it?"

    scene cow2 with dissolvefast
    pause 1.5

    v "Mmhh-"

    v "You're going even faster, Human."

    p "I can't control myself."

    p "You just feel too good Vel!"

    p "I just want to stay like this forever."

    v "Mmmhh."

    v "I can't stay like this forever."

    v "My body wouldn't be able to take it."

    p "You don't have to worry about that."

    p "Your pussy won't even let me."

    p "You just feel too good. I'm getting close to my limit."

    scene black with fade
    hide cow2
    scene cowxray1 with dissolvefast
    pause 1.5


    v "Ah, ahhh. Human, wait-"

    v "You're being so rough."

    v "It's stirring my insides."

    p "Just bear with it Vel!"

    p "It won't be long till I reach my limit."

    v "Mnnn-"

    p "Ah- Vel I'm almost there!"

    p "Is it fine to cum inside you?"

    v "Ahh-"

    n "Reapers don't get pregnant, so feel free to let it out inside her."

    p "Then I'm gonna do just that."

    p "Here I cum Vel!"

    show cowxraycum
    pause 0.1
    hide cowxray1
    pause 4.0

    scene cowxraycumend with dissolvefast
    hide cowxraycum
    pause 2.0

    scene cowend with fade
    pause 0.5
    hide cowxraycumend


    p "*pant* *pant*"

    v "Ahh-"

    p "That felt incredible."

    v "Did it?"

    p "Yeah. I couldn't imagine it's possible to feel that much pleasure."

    p "Your pussy is out of this world."

    p "I wish I could prove it by letting out even more, but my body still feels tired from all we've done earlier."

    v "It's fine."

    v "I think you let out enough."

    v "It feels really hot inside me."

    p "I'm glad you seem satisfied."

    v "Do I?"

    p "Yeah! You look really cute right now."

    p "The cutest you've ever been."

    v "Stop being weird, Human."

    v "Is that even possible?"

    p "Everything's possible if it's you."

    $ renpy.music.set_volume(0.0, 0, channel='music')
    $ renpy.music.set_volume(0.05, 3, channel='music')
    play music "PerituneMaterial_Wish5_HarpOnly_loop.ogg" loop

    ". . ."

    "I let myself rest as Vel stays on top of me."

    "She hasn't stopped staring at me, and I haven't broken it off either."

    "This moment in time feels so slow."

    "I feel connected to Vel, and it's not just because my dick is still inside her."

    "I want to treasure this time forever, and admire her for who she is."

    "She really does look the cutest right now."

    ". . ."

    p "Wait.. I think there was something odd that happened when I was about to cum inside you."

    p "I didn't really think about it in the heat of the moment, but.."

    stop music fadeout 1.0

    scene black with fade
    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Puppet_loop.ogg" loop

    show neuchibbg behind black

    show neuchib behind black:
        zoom 1.02 xalign -0.3  yalign 0.1

    hide black with dissolve


    pause 1.0

    n "Hello."

    p "Since when were you here?!"

    n "Since Velvel got on top of you."

    p "That was from the very beginning!"

    show neuchib at bounce1:
        zoom 1.02 xalign -0.3 yalign 0.1

    n "That's right! I never left."

    n "There's no way I'm gonna miss my best friend's first time!"

    n "You two look so lovely right now!"

    show neuchib at bounce1:
        zoom 1.02 xalign -0.3 yalign 0.1

    n "There's no way you two aren't in love!"

    n "This is the first time I'm seeing Velvel like this too."

    n "I got to see a new side of Velvel. How exciting!"

    p "I can't even believe this is actually happening."

    p "Were you aware of this too Vel?"

    v "Yes."

    p "Wh-Why would you not tell her to go away?"

    v "Was I supposed to?"

    p "Well... *Sigh*"

    p "I don't know."

    v "Human.."

    v "Did I do something wrong?"

    p "No.. Well I can't really fault you for it."

    p "This normally won't happen with most people."

    show neuchib at bounce1:
        zoom 1.02 xalign -0.3 yalign 0.1

    n "But we're Grim Reapers!"

    p "Even you reapers should show some decency!"

    p "Why are you even still here?"

    n "As much as I support Velvel with what she wants to do, I can't just forget about why I came here."

    n "Velvel still needs to do her job properly."

    n "I won't be coming back empty handed, or else I'll be punished!"

    n "So I'll be taking Velvel back with me."

    p "Does it really have to be now?"

    show neuchib at bounce1:
        zoom 1.02 xalign -0.3 yalign 0.1

    n "Yes! She's been gone for far too long."

    scene cowend with fade

    n "That's the situation, so you should get off him now Velvel."

    v "Hmm."

    v "Do I really need to?"

    n "Yes! How long do you even plan to stay like that?"

    v ". . ."

    v "How long do you want to, Human?"

    n "Velvel! That's not the issue here."

    n "He's most likely really tired by now, so you should give him time to rest."

    v "Is that true?"

    p "Huh? Well I'd be lying if I say that I'm not."

    p "Passing out twice and cumming thrice is really taking a toll on me."

    v ". . ."

    v "Will you be fine Human?"

    p "Yeah, you don't need to worry about me."

    p "I just need some rest, and I'll be ready to go again."

    p "Though I am gonna miss you."

    v "I'll be back soon."

    stop music fadeout 2.0

    scene black with fade

    scene 2weeks with fade

    $ renpy.pause(delay = 2.0, hard = True)
    #pause 2

    #### DAY 3 ###########################################

    scene black  with fade

    $ renpy.music.set_volume(0.02, 0, channel='sound')
    play sound ["<silence .0>","ac.ogg"] loop fadein 1.0

    scene roombg1  with fade

    "It's already been two weeks since Vel left along with Neu."

    "She said she would be back soon, so I thought it was just going to be a few days."

    "I wasn't expecting her to be gone for this long."

    "I've been eagerly checking if her door has appeared again, but there's been nothing so far."

    "I've only been with her for two days, but I already miss her so much."

    "*Sigh* I guess I should do something to distract myself from this loneliness."

    stop sound fadeout 1.0

    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Spook4_loop.ogg" loop

    scene roombg2  with dissolve

    "Just as I was deciding on what I should do, I suddenly felt my room getting dark."

    "The air circulating turns cold, and I see black mist forming before me."

    "The mist revolves to form what looks like a portal, and a girl emerges from the nothingness."

    "Longing to be with Vel again, I got my hopes up thinking she's finally home."

    "But I quickly realized who has appeared in front of me."

    stop music fadeout 1.0

    scene room with dissolve

    show neucloseg with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.7

    #hide black with dissolve

    pause 1

    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Puppet_loop.ogg" loop fadein 0.5

    "It's just Neu."

    show neucloseg angry at bounce1:
        zoom 1.0 xalign 0.5 yalign 0.7

    n "Huh? What's with that expression?"

    n "You got the look like \"It's just Neu\" on your face."

    n "Are you that unhappy to me see me, human?"

    show neucloseg cry at bounce1:
        zoom 1.0 xalign 0.5 yalign 0.7
        easein 0.5 zoom 1.0 xalign 0.52 yalign 0.7

    n "Am I just not cute after all?!"

    p "Huh? No.. I was just.."

    p "I really thought Vel has come back."

    show neucloseg pout:
        zoom 1.0 xalign 0.52 yalign 0.7
        easein 0.7 zoom 1.0 xalign 0.45 yalign 0.7

    n "Well sorry that I'm not Velvel."

    p "No. That's not what I'm trying to say."

    p "I'm happy to see you again too."

    show neucloseg xd at bounce1:
        zoom 1.0 xalign 0.45 yalign 0.7
        easein 0.5 zoom 1.0 xalign 0.5 yalign 0.7

    n "Oh my! Are you hitting on me, human?"

    n "You shouldn't do that just because Velvel isn't here!"

    p "No, I'm not. I'll only do that to Vel."

    show neucloseg cry with dissolvefast:
        zoom 1.0 xalign 0.5 yalign 0.7

    n "Oh.."

    n "You can hit on me too."

    show neucloseg cry:
        zoom 1.0 xalign 0.5 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.52 yalign 0.7

    n "I'm cute, right?"

    n "You hit on cute girls, right?"

    p "Do you even realize you just contradicted yourself?"

    "I really hoped it was Vel who's in front of me now, but this is better than nothing."

    "I could at least ask Neu how Vel is doing."

    p "So why did you come back here alone?"

    p "Do you know when Vel is coming back?"

    show neucloseg happy at bounce1:
        zoom 1.0 xalign 0.52 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.5 yalign 0.7

    n "Ah right!"

    n "Things are getting busy back in our world, and I have plenty of things I need to do."

    show neucloseg wor:
        zoom 1.0 xalign 0.5 yalign 0.7
        easein 0.8 zoom 1.0 xalign 0.53 yalign 0.7

    n "But then I felt like I'm forgetting something,"

    show neucloseg wor:
        zoom 1.0 xalign 0.53 yalign 0.7
        easein 0.5 zoom 1.0 xalign 0.55 yalign 0.7

    n "I kept thinking and thinking.."

    n "Then I finally remembered the reason why Velvel was even gone in the first place."

    show neucloseg happy at bounce1:
        zoom 1.0 xalign 0.55 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.53 yalign 0.7

    n "It was you!"

    "Neu wears a wide smile as if she just made the greatest discovery of her life."

    p "Well.. yeah?"

    p "Wasn't that obvious?"

    show neucloseg wor:
        zoom 1.0 xalign 0.53 yalign 0.7
        ease 0.6 zoom 1.0 xalign 0.5 yalign 0.7

    n "I already forgot what you even looked like, and I didn't want to completely forget."

    n "Especially when Velvel cares so much about you."

    show neucloseg happy at bounce1:
        zoom 1.0 xalign 0.5 yalign 0.7

    n "So here I am!"

    n "I'm visiting you so I don't forget about you."

    show neucloseg dumb:
        zoom 1.0 xalign 0.5 yalign 0.7

    n "Aren't you happy I didn't completely forget?"

    p "Forget about me?"

    p "It's only been two weeks since you left with Vel here."

    show neucloseg con:
        zoom 1.0 xalign 0.5 yalign 0.7
        easein 0.7 zoom 1.0 xalign 0.48 yalign 0.7

    n "Has it been two weeks?"

    "Neu's face gets filled with puzzlement."

    n "I can't remember days like that."

    p "Huh? You can't remember?"

    "Didn't Vel act the same way before?"

    "She always had a problem remembering things."

    "I remember her saying she thinks it's the same for all the reapers."

    p "Actually that's one interesting thing I discovered about Vel when she was here before."

    p "She seems to have a really bad memory."

    p "Is it the same case for you?"

    show neucloseg con:
        zoom 1.0 xalign 0.48 yalign 0.7
        easein 0.7 zoom 1.0 xalign 0.46 yalign 0.7

    n "Hmmmm.."

    "Neu pauses, and thinks for a few moments before answering."

    show neucloseg pout with dissolvefast:
        zoom 1.0 xalign 0.46 yalign 0.7

    n "It seems like it."

    n "It seems to be the same for all the Reapers."

    n "I feel like I heard of the reason why, but I can't remember it!"

    p "Well that makes sense if you forget things easily."

    "So all reapers could easily forget about things.."

    "It's already been two weeks since Vel was here."

    "Has she forgotten about me?"

    "Is that the reason she hasn't come back?"

    "Neu almost forgot about me. Who's to say it won't be the same for Vel?"

    show neucloseg con :
        zoom 1.0 xalign 0.46 yalign 0.7
        ease 0.5 zoom 1.05 xalign 0.46 yalign 0.6

    "As I'm lost in thought, Neu stares at me intently."

    n "Hmmm?"

    p "Huh? What is it?"

    show neucloseg wor with dissolvefast :
        zoom 1.05 xalign 0.46 yalign 0.6

    n "Why are you making that face?"

    n "You got the look like \"Velvel has forgotten about me\" all over you."

    "How could she even tell that?"

    "I'm honestly not sure if she's supposed to be dumb or some kind of genius."

    show neucloseg dumb:
        zoom 1.05 xalign 0.46 yalign 0.6

    n "Was I right?"

    "Definitely dumb."

    p "Well.. yeah..."

    p "She's been gone for some time now, and I can't do anything else than just wait for her."

    show neucloseg happy at bounce1:
        zoom 1.05 xalign 0.46 yalign 0.6

    n "There's nothing for you to worry, human."

    n "Velvel hasn't forgotten about you!"

    "Neu raises her energy as she tries to cheer me up."

    p "How do you know that?"

    show neucloseg happy:
        zoom 1.05 xalign 0.46 yalign 0.6
        ease 0.5 zoom 1.0 xalign 0.46 yalign 0.7

    n "It's not like we forget about everything."

    n "We can remember things that we really care about."

    n "That's why I remember a lot of things about Velvel!"

    show neucloseg happy:
        zoom 1.0 xalign 0.46 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.48 yalign 0.7

    n "I really care about her. I'm her best friend after all!"

    p "Vel can remember things she cares about?"

    show neucloseg happy at bounce1:
        zoom 1.0 xalign 0.48 yalign 0.7

    n "That's right!"

    n "Velvel seems to really care about you, so you don't have anything to worry about."

    n "She won't forget about you!"

    "I can't help but believe in her when she's brimming with so much optimism."

    "She does seem to really care about Vel, so maybe she's right on this one."

    p "I hope so."

    p "I don't want her to forget."

    show neucloseg happy:
        zoom 1.0 xalign 0.48 yalign 0.7
        ease 0.4 zoom 1.05 xalign 0.48 yalign 0.6

    n "Come on! Don't be such a downer."

    n "She won't! You can trust me, human!"

    p "Well if you say so."

    show neucloseg happy at bounce1:
        zoom 1.05 xalign 0.48 yalign 0.6

    n "Mhmm! I can't be wrong about Velvel."

    "Neu gets filled with satisfaction as I agree with her."

    "Wait..."

    "I took a few seconds to sort my thoughts, and then it clicked."

    p "You said you came here to remember me.."

    p "So you don't care about me enough that you started forgetting?"

    show neucloseg pout at bounce1:
        zoom 1.05 xalign 0.48 yalign 0.6
        ease 0.6 zoom 1.0 xalign 0.48 yalign 0.7

    n "What do you expect from me?"

    n "It's not like I'm in love with you like Velvel."

    p "Well.. I guess that's true."

    show neucloseg pout:
        zoom 1.0 xalign 0.48 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.5 yalign 0.7

    n "It's not like you care about me like you care about Velvel."

    #p "Yeah.. Vel is special after all."

    show neucloseg pout:
        zoom 1.0 xalign 0.5 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.52 yalign 0.7

    n "It's not like you do lewd things to me like you do with Velvel!"

    p "Do you seriously want me to..?"

    show neucloseg pout:
        zoom 1.0 xalign 0.52 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.54 yalign 0.7

    n "Plus there's a lot of things I think about back in our world."

    show neucloseg angry at bounce1:
        zoom 1.0 xalign 0.54 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.52 yalign 0.7

    n "Just be glad I didn't completely forget!"

    p "Right.. I am grateful for that."

    p "So do you know when Vel is coming back?"

    p "You said things are getting busy back in your world, does that have to do with Vel?"

    show neucloseg wor:
        zoom 1.0 xalign 0.52 yalign 0.7
        easein 0.5 zoom 1.0 xalign 0.5 yalign 0.7

    n "Nope. I haven't seen her since we came back."

    n "Velvel was bombarded with all of her overdue work plus plenty more in advance."

    show neucloseg away:
        zoom 1.0 xalign 0.5 yalign 0.7
        easein 0.6 zoom 1.0 xalign 0.53 yalign 0.7

    n "Because we both know full well that this is just going to happen again."

    p "So Vel has just been working all this time?"

    p "Are you sure she's alright?"

    show neucloseg dumb:
        zoom 1.0 xalign 0.53 yalign 0.7

    n "You really care about Velvel, huh?"

    p "Well.. of course I do."

    show neucloseg dumb:
        zoom 1.0 xalign 0.53 yalign 0.7
        ease 0.4 zoom 1.05 xalign 0.53 yalign 0.6

    n "Aren't you so sweet, human?"

    p ". . ."

    p "I think I'm just normal."

    show neucloseg happy at bounce1:
        zoom 1.05 xalign 0.53 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "You don't need to worry! She does this all the time."

    n "She just crams all the work she needs to do, and collects a ton of souls one after another."

    show neucloseg away :
        zoom 1.05 xalign 0.5 yalign 0.6
        easein 0.6 zoom 1.05 xalign 0.55 yalign 0.6

    n "She can be quite scary when she's working like that."

    n "I don't even really want to meet her until she's finally done."

    "That's really odd to hear coming from her, as she's always going on about being Vel's best friend."

    p "Scary? How can Vel be scary?"

    p "She's really cute, so I can't imagine her being the least bit scary."

    show neucloseg away at bounce1:
        zoom 1.05 xalign 0.55 yalign 0.6

    n "And I hope you never see her like that!"

    n "She's really cute on her normal form, so I don't understand why she can be so scary too."

    show neucloseg away:
        zoom 1.05 xalign 0.55 yalign 0.6
        ease 0.5 zoom 1.05 xalign 0.57 yalign 0.6

    n "But she's still not scarier than Suisui when she's mad."

    n "I hope I never see her like that too!"

    "I still can't imagine Vel being scary though."

    "I feel like I would always find her cute no matter what she does."

    "Neu is really acting odd, so I wanted to move on from the subject."

    p "Hey Neu.. there's actually something I've been wondering about since you came here."

    show neucloseg wor:
        zoom 1.05 xalign 0.57 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.53 yalign 0.6

    n "What is it?"

    show neucloseg smug:
        zoom 1.05 xalign 0.53 yalign 0.6
        easein 0.4 zoom 1.1 xalign 0.53 yalign 0.55

    n "Are you gonna hit on me now?"

    n "Maybe I'll remember you if you do it!"

    p "I already told you I won't do that."

    show neucloseg pout at bounce1:
        zoom 1.1 xalign 0.53 yalign 0.55
        easein 0.5 zoom 1.0 xalign 0.53 yalign 0.7

    n "Boo!"

    n "Then what's the boring thing you're thinking about?"

    p "Well it's about how you came here."

    p "How did you come here without a door to your room appearing on the wall?"

    show neucloseg wor:
        zoom 1.0 xalign 0.53 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.5 yalign 0.7

    n "Huh? What are you talking about?"

    p "Vel said that a reaper's room gets sent to people's houses when they're sent over to collect souls."

    show neucloseg dumb:
        zoom 1.0 xalign 0.5 yalign 0.7

    n "Huh..?"

    n "Did Velvel really say that?"

    p "Yeah.. she did."

    show neucloseg dumb at bounce1:
        zoom 1.0 xalign 0.5 yalign 0.7

    n "I never thought I'd ever hear something stupid coming from Velvel."

    p "Stupid? What do you mean?"

    show neucloseg dumb:
        zoom 1.0 xalign 0.5 yalign 0.7
        easein 0.5 zoom 1.0 xalign 0.48 yalign 0.7

    n "Ah? That's a total lie."

    n "Did you really believe such a ridiculous thing like that?"

    show neucloseg smug:
        zoom 1.0 xalign 0.48 yalign 0.7

    n "Are you perhaps dumb too, human?"

    "Neu looks down at me as she wears an annoying smile."

    p "How do you expect me to know how you reapers work?!"

    p "Vel even said that she was sent here by mistake."

    show neucloseg dumb:
        zoom 1.0 xalign 0.48 yalign 0.7
        ease 0.5 zoom 1.0 xalign 0.5 yalign 0.7

    n "Heh."

    n "That's also another dumb lie."

    n "There's no way that could ever happen."

    n "This is actually funny. Did Velvel say any more dumb things that you believed in?"

    "She seems to be enjoying herself hearing about what Vel told me."

    "But why would Vel even lie about something like that?"

    "Did she lie about something else too?"

    "Though it's hard for me to doubt her when she looks at me so innocently."

    show neucloseg angry at bounce1:
        zoom 1.0 xalign 0.5 yalign 0.7
        easein 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "To start with, most reapers aren't even capable of transporting a full room to another world!"

    "As I was focused on my thoughts, Neu suddenly blurted out."

    p "Huh? Not capable?"

    p "What do you mean?"

    show neucloseg wor:
        zoom 1.05 xalign 0.5 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.48 yalign 0.6

    n "A reaper would need a lot of power to be able to take a space from the reaper world to other worlds."

    n "I can't do something like that!"

    p "You can't?"

    show neucloseg wor at bounce1:
        zoom 1.05 xalign 0.48 yalign 0.6

    n "Of course not!"

    n "Just summoning myself here is the most I can do."

    show neucloseg away:
        zoom 1.05 xalign 0.48 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "I'm nowhere near as powerful as Velvel."

    p "As powerful as Vel?"

    p "Doesn't that mean Vel is really strong?"

    show neucloseg angry at bounce1:
        zoom 1.05 xalign 0.5 yalign 0.6

    n "Of course she is!"

    n "Velvel is ridiculously strong!"

    p "Is she?"

    n "She may not look like it, but she ranks at the top of all the reapers."

    p "Huh? What are you talking about?"

    p "Are you saying Vel is the strongest reaper?!"

    show neucloseg angry at bounce1:
        zoom 1.05 xalign 0.5 yalign 0.6
        ease 0.5 zoom 1.1 xalign 0.5 yalign 0.55

    n "Yes. She is!"

    p ". . ."

    "Neu just dropped a huge detail about Vel, but for some reason I just can't bring myself to believe it."

    "I mean.. Vel being strong?"

    "The strongest even?"

    p "How could that even be possible?"

    p "Are you sure you're not confusing her for anyone else?"

    show neucloseg wor at bounce1:
        zoom 1.1 xalign 0.5 yalign 0.55
        ease 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "Of course not! I would never get anything wrong about Velvel."

    p "But her being the strongest reaper..?"

    p "She really doesn't look like it.."

    show neucloseg away :
        zoom 1.05 xalign 0.5 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.53 yalign 0.6

    n "I know right.."

    "Neu and I let out a heavy sigh in unison."

    n "How could the number one reaper be a cute girl who just plays games all day and avoids her work?"

    show neucloseg away :
        zoom 1.05 xalign 0.53 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.55 yalign 0.6

    n "Though I'm responsible for why Velvel turned like that.."

    p "You're the reason why Vel plays games all day?"

    show neucloseg happy at bounce1:
        zoom 1.05 xalign 0.55 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "That's right!"

    n "Which means I'm also the reason why you even met her in the first place!"

    show neucloseg happy at bounce1:
        zoom 1.05 xalign 0.5 yalign 0.6
        easein 0.5 zoom 1.1 xalign 0.5 yalign 0.55

    n "Aren't you thankful to me, human?"

    "Neu inches closer to me with her eyes shining, waiting for me to praise her."

    p "Is that how it really works?"

    n "Come on. Don't be shy!"

    n "You can show me your gratitude however you like."

    show neucloseg smug:
        zoom 1.1 xalign 0.5 yalign 0.55

    n "You can even touch me if that's how you want to show it!"

    p "How is that showing my gratitude?!"

    n "You know you want to."

    p "That's not the issue here.."

    p "But more importantly how exactly are you responsible?"

    p "What happened with the two of you?"

    show neucloseg cry at bounce1:
        zoom 1.1 xalign 0.5 yalign 0.55
        easein 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "You're more interested in that than my body?!"

    n "Do I just not have any sex appeal?!"

    show neucloseg cry :
        zoom 1.05 xalign 0.5 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.53 yalign 0.6

    n "Do I just not compare to Velvel at all?"

    p "That's not what I'm saying.."

    p "You still look cute and sexy."

    show neucloseg xd at bounce1 :
        zoom 1.05 xalign 0.53 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "Oh my, human! How lewd!"

    n "Are you hitting on me now?!"

    n "You're so naughty! Just because Velvel isn't here."

    p ". . ."

    "What's wrong with this grim reaper.."

    p "So are you gonna answer my question now?"

    show neucloseg wor with dissolvefast :
        zoom 1.05 xalign 0.5 yalign 0.6

    n "Hmmm.. I guess I could tell you."

    n "But it's kind of a long story."

    $ renpy.music.set_volume(0.35, 0, channel='sound')
    play sound ["<silence .0>","phone.ogg"]

    show neucloseg con at bounce1 :
        zoom 1.05 xalign 0.5 yalign 0.6

    n "Ah-"

    "Before Neu could continue, some sort of alarm started buzzing from her skirt."

    p "Where's that coming from?"

    show neucloseg wor :
        zoom 1.05 xalign 0.5 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.48 yalign 0.6

    n "From my smartphone."

    p "You have a smartphone..?"

    n "Of course I do!"

    n "How else do you expect me to remember things if I don't set reminders?"

    p "Right.."

    "I guess I shouldn't be surprised when Vel was playing with a game console."

    n "What's the matter, human?"

    show neucloseg smug :
        zoom 1.05 xalign 0.48 yalign 0.6
        easein 0.5 zoom 1.1 xalign 0.48 yalign 0.55

    n "Do you wanna get my contact, and flirt behind Velvel's back?"

    p "Why would I even do that?"

    show neucloseg smug :
        zoom 1.1 xalign 0.48 yalign 0.55
        easein 0.4 zoom 1.13 xalign 0.48 yalign 0.52

    n "You just said a while ago that I'm cute and sexy!"

    n "Don't you want to flirt with a cute girl?"

    p "I don't need to do that when I already have Vel."

    show neucloseg happy at bounce1 :
        zoom 1.13 xalign 0.48 yalign 0.52
        easein 0.5 zoom 1.05 xalign 0.48 yalign 0.6

    n "You really love Velvel, huh?"

    n "You're so sweet, human!"

    p "As I said, I'm just normal."

    p "And would my texts even go through if you're in another world?"

    show neucloseg dumb :
        zoom 1.05 xalign 0.48 yalign 0.6

    n "I don't know."

    n "I never tried it before."

    show neucloseg happy:
        zoom 1.05 xalign 0.48 yalign 0.6

    n "Anyway I have to get going."

    p "Huh? But what about my question."

    show neucloseg wor:
        zoom 1.05 xalign 0.48 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "I can tell you some other day, but I don't have the time for it now."

    n "I only came here so I don't forget about you."

    n "I never meant to stay for long."

    p "Then are you going back to your world?"

    n "Mhmm. I have plenty of things I need to do."

    show neucloseg happy at bounce1:
        zoom 1.05 xalign 0.5 yalign 0.6

    n "And something really interesting is actually happening there right now!"

    #"I had a question at the back of my mind, and I knew how it's most likely going to be answered."

    #"But regardless I just had to ask it."

    p "Would it be possible for me to come with you?"

    #p "I really can't wait to see Vel."

    show neucloseg wor:
        zoom 1.05 xalign 0.5 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.48 yalign 0.6

    n "Huh? What are you talking about?"

    n "Humans like you aren't allowed in our world."

    "Just as I thought.."

    n "Didn't you have problems when you stayed in Velvel's room before?"

    p "Yeah.. I felt nauseous, and passed out."

    show neucloseg wor at bounce1:
        zoom 1.05 xalign 0.48 yalign 0.6

    n "Then you should have figured it out by now!"

    n "There's no way you'll be able to stay in our world."

    show neucloseg con:
        zoom 1.05 xalign 0.48 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.46 yalign 0.6

    n "Although the interesting thing I mentioned is someone who looks human is able to roam our world."

    p "Someone who looks like a human?"

    p "Then does that mean there's a chance for me too?"

    show neucloseg dumb:
        zoom 1.05 xalign 0.46 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.48 yalign 0.6

    n "Nope. Don't count on it."

    n "I'm fairly sure he is no longer human, and he'll be passing away soon."

    show neucloseg wor:
        zoom 1.05 xalign 0.48 yalign 0.6
        easein 0.5 zoom 1.05 xalign 0.5 yalign 0.6

    n "Just sit patiently until Velvel comes back."

    n "She should be back soon."

    p "Well.. I hope so."

    show neucloseg happy at bounce1:
        zoom 1.05 xalign 0.5 yalign 0.6

    n "I'll tell Velvel you're really missing her if I see her!"

    n "Then with that, I really should get going now."

    scene roombg2 with dissolvefast

    "The air turns cold once again, and a dark portal appears in thin air."

    "Neu waves me one last goodbye before entering and turning into nothingness."

    scene roombg1 with dissolve

    "The portal disperses, and the room's temperature comes back to normal."

    "Once again I'm left all alone as I sat in silence."

    "With nothing I can do, but wait patiently I went back to my normal daily routine."

    stop music fadeout 1.5

    scene black with fadefast

    scene fewdays with fade
    $ renpy.pause(delay = 2.0, hard = True)
    #pause 2

    scene black with fade

    "A few days passed since Neu visited me."

    "I just got home from work, and was preparing myself for another night of missing Vel."

    "But as soon as I stepped in my house, I was surprised by what greeted me."

    $ renpy.music.set_volume(0.1, 0, channel='music')
    play music "PerituneMaterial_Spook_loop.ogg" loop

    scene door with fade

    "It's the same ominous door that led me to meeting Vel."

    "Is Vel finally back?!"

    "My body gets filled with excitement, and I rushed through the door to finally see Vel again."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound "Dooropen.ogg"

    scene door:
        zoom 1.0 xalign 0.5 yalign 0.5
        linear 2.0 zoom 1.5 xalign 0.5 yalign 0.5

    pause 0.5

    scene black with fade

    "I was expecting to see the same cute and soft girl waiting for me behind the door."

    "But what met me on the other side was something I never expected to see."

    stop music fadeout 0.5

    scene reaperb with fade

    $ renpy.music.set_volume(0.5, 0, channel='music')
    play music "Abyss.ogg" loop

    pause 2

    "Standing at the center of the room is a black hooded figure belching an aura that invokes dismal fear."

    "My body quickly comes to a halt, surprised by what my eyes have met."

    "I feel like something is enveloping my whole body as shivers run down my spine."

    $ renpy.music.set_volume(0.3, 0, channel='sound')
    play sound ["<silence .15>","flash1.ogg"]

    scene reaperbd with dissolve

    "My eyes start to get blurry, and it gets harder to breath."

    "It's like something is gripping me, trying to squeeze me through."

    "I focused on my breathing to try and calm myself."

    "A few moments passed before I could feel myself being stable again."

    "Through the haziness of my eyes, I tried to focus on the figure standing in front of me."

    scene reaper with dissolve

    "Upon closer inspection, the figure looks like Vel, but she feels like an entirely different person"

    "She stares at me with cold listless eyes without emitting any emotion."

    "Is that really Vel?"

    "Is this what Neu meant that Vel can be scary?"

    "This goes beyond just being scary, she's radiating a terrifying aura."

    "It feels like I can die at any moment just from standing near her."

    "But despite all that, I mustered up all my courage to confront her."

    p "Vel..?"

    p "Is that you?"

    p "What.. happened to you?"

    "I tried calling out to her, but she didn't seem to pay me any mind."

    "Her eyes continue to pierce through me, not showing any hint of affection."

    p "We met here before.. don't you remember?"

    p "We've even done intimate things together."

    "I called out to her again, but it didn't make any difference."

    "She just continues to stare at me with uninterested eyes."

    "It's almost like she's not even acknowledging my existence."

    p "You're the same Vel who I met before, right?"

    p "We met here in this very same room."

    p "You were silently playing on your bed, and I started talking to you."

    p "I felt so lucky when you let me touch you, and even more so when I saw you're still here the next day."

    p "We even played a game together."

    p "Even though we were just together for such a short time, I really felt like we formed a connection."

    p "I still remember the sensation of holding you in my arms."

    p "And I've been wanting to hold you again."

    p ". . ."

    p "Please tell me you remember."

    "But even with all the words that left my mouth, none of them seemed to reach her."

    "I tried getting closer to her, thinking that touching her again would garner me her attention."

    "But as soon as I stepped forward, she tightened her grip on her scythe."

    "My body freezes as I sensed a dreaded aura coming from her."

    "It felt like she's ready to swing and cut me in half with her scythe any second now."

    "Just like my body coming to a halt, no more words would come out too."

    "Did she really forget about me?"

    "I did consider the possibility, but I didn't think it would actually happen."

    "And even if she did, I thought I could just help her remember."

    "But I can't even do anything when she's like this."

    "She hasn't even said anything since I entered  the room."

    "And there's no trace of the Vel I know of from the girl that's now standing in front of me."

    "What happened to her?"

    $ renpy.music.set_volume(0.3, 0, channel='sound')
    play sound ["<silence .15>","flash3.ogg"]

    scene reaperd with dissolve

    "My head started spinning, not knowing what I should do."

    #"I got myself so excited to be with her again, and I didn't prepare for something like this happening."

    "How could I even think something like this would happen?"

    "What am I supposed to do now?"

    scene black with fade

    "Just when I was about to lose hope, I suddenly heard soft words calling to me."

    stop music fadeout 1.0

    v "Hey Human."

    "Vel?"

    scene reaperv with fade

    "I open my eyes, and look forward once again."

    "I finally see the figure of the girl I've been wanting to see."

    #"My eyes focused on hers as indulge in her beauty."

    "My emotions come rushing through, and I feel my eyes starting to water."

    "My chest tightens as I take a quick deep breath, attempting to stop myself from crying."

    "I couldn't contain myself anymore, and I ran to hold her."

    $ renpy.music.set_volume(0.7, 0, channel='sound')
    play sound ["<silence .3>","cloth7.ogg"]

    ##### BACK #################



    scene hug with fade
    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Wish5_HarpOnly_loop.ogg" loop fadein 0.5
    pause 1

    p "Vel!"

    "I wrapped my arms around her, and held her close to me."

    p "It's really you!"

    v "Human.."

    v "I'm back."

    p "Yeah.. welcome back."

    p "I've been really missing you."

    v "Have you?"

    p "Of course! I couldn't wait to see you again."

    "Hearing Vel and feeling her warmth fills me with happiness, and I embraced her even tighter."

    "I stayed silent for a while, and confusion emerged from her eyes."

    v ". . ."

    v "Human, what's wrong with you?"

    v "You're holding me so tight."

    p "I'm just really happy right now."

    p "I really thought that you've forgotten about me."

    v ". . ."

    #"Vel looks at me with baffled eyes."

    v "What are you talking about?"

    v "I won't forget about you."

    p "Vel! You don't know how happy I am to hear those words."

    v "I can tell from how hard you're holding me."

    "The both of us paused for a few moments as we looked at each other."

    "I can sense the worry coming from Vel's eyes."

    "She must really be confused by my behavior."

    p "I really missed holding you like this."

    p "You're even softer than what I remembered."

    p "Especially on your chest area."

    p "I love feeling your boobs as they're pressed into me."

    v ". . ."

    v "You're being weird again, Human."

    #"We fell into silence as I continue to hold Vel dear to me."

    #"Time ticks in as we enjoy each other's warmth."

    #"The whole time Vel just stares at me with the usual look in her face."

    #"We continued to what felt like an eternity before I spoke again."

    p "No, I'm not."

    p "It's only normal for me to love your boobs."

    v ". . ."

    p "But what happened to you back then?"

    v "What happened to me?"

    p "You looked like a completely different person."

    p "You cloak was almost covering you fully, and you had a scythe in your hand."

    scene hug5 with dissolve

    v "Hmm.."

    "Vel closes her eyes, and thinks for a moment."

    "She seems to be struggling recollecting her thoughts."

    scene hug with dissolve

    v "I don't really remember."

    p "Huh? You don't?"

    p "You do have a bad memory, but that was just a minute ago."

    v "A minute ago?"

    v ". . ."

    v "Whenever I have to do my work, I always don't remember what happens."

    v "I just know that I'm done with them now."

    p "You don't remember anything?"

    p "Like there's a blank in your memory?"

    p "Then is the last thing you remember when you went back to your world?"

    v "Mmh."

    v "I think so."

    "Vel answered me with clear confusion in her eyes."

    "It really looks like she has no idea of what just happened."

    v "Did something happen?"

    "I was lost in my thoughts when Vel suddenly asked me worryingly."

    p "Well.. I just tried talking to you when you looked like that, but you didn't answer me."

    p "It really looked like you didn't know who I am."

    p "You held your scythe as if you were ready to attack me."

    p "I've always seen you as just a completely normal cute girl, but that really changed my mind."

    p "That was the first time I actually thought you really are a grim reaper."

    p "It was quite scary.. I guess it's only normal it would be."

    v "I was scary?"

    v ". . ."

    v "Did that really happen?"

    v "I really don't remember."

    p "Yeah... I could tell you have no recollection of it."

    v ". . ."

    v "Are you fine, Human?"

    "Vel's eyes show me a hint of sadness as she stares right at me."

    p "Well I'm fine now that I got to see your cute face."

    v ". . ."

    "I didn't want to see her like this, so I tried joking about it."

    "But she didn't seem impressed.."

    v "I'm asking seriously."

    p "I'm alright."

    v "Really?"

    p "Yeah.. you can't do anything about it now if you don't remember."

    v "Hmmm.."

    $ renpy.music.set_volume(0.6, 0, channel='sound')
    play sound ["<silence .22>","cloth5.ogg"]

    scene hugb1 with dissolve
    pause 1

    "I feel Vel bury her face in my chest."

    v "Are you sure?"

    p "Well.. I'd be lying if I say it doesn't bother me."

    p "Even now I'm still trying to figure out what exactly happened."

    p "The whole thing just felt so overwhelming."

    v "I really don't remember anything."

    "Vel speaks slowly, and I feel the sadness from her words."

    "She gently rubs her face on my chest as she broods over her words."

    v ". . ."

    p "I believe you.."

    v "I didn't want to scare you."

    p "Yeah.. I know Vel."

    p "You don't need to worry about it now."

    p "I'm sure we'll figure it out if it happens again."

    v "Will we?"

    p "Yeah. I'm sure we will."

    p "I won't run away from you no matter what happens."

    v "You should if you're about to be attacked."

    p "Well.. yes.."

    p "But that's not what I'm trying to say.."

    v "Mmh."

    p "But all that doesn't really matter now."

    p "What's important is you're here right now, and you know who I am."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound ["<silence .1>","cloth7.ogg"]

    scene hug with dissolve
    pause 0.4

    v "Mmh."

    v "I'm here now, Human."

    p "Yeah.. you are."

    #p "So very close to me."

    v "I won't forget about you."

    p "I believe you Vel."

    "Silence envelopes us once again as I slowly caress her head."

    "All the while, Vel just kept on staring right at me."

    "A few moments passed before I broke the silence."

    p "So what do you want to do now that you're finally back?"

    p "It's been so long since we were together."

    stop music fadeout 1.0

    v "I'm going to play."

    p ". . ."

    p "Huh?"

    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Puppet_loop.ogg" loop fadein 1.0

    v "I haven't played any games all this time, so I'm going to play."

    p ". . ."

    p "Right.."

    v "Am I not allowed to, Human?"

    p "Well.. no, of course you are."

    p "I can't force you to do anything."

    p "I guess I can't expect you to just break your old habits."

    v "Are you coming with me, Human?"

    p "Huh?"

    v "Are you not?"

    p "Oh.. of course I am!"

    p "I want to be with you as much as possible."

    v "Then I'm going to play in your room."

    p "Huh? Really?"

    p "I'm happy to hear that, but why in my room?"

    v "Because you can't stay on mine."

    p "Oh.. right."

    p "I wouldn't want to pass out again."

    v "Mmh."

    scene black with fade

    "Vel grabbed her game console, and we headed to my room."


######## SPOON #############################

    $ renpy.music.set_volume(0.7, 0, channel='sound')
    play sound ["<silence .0>","cloth8.ogg"]

    scene spoon with fade
    pause 1

    "Vel lays down on my bed, and starts playing as I cuddle from behind her back."

    "It didn't take long for her to get engrossed in her game. It's just like when I first met her."

    $ renpy.music.set_volume(1.2, 0, channel='sound')
    play sound ["<silence .0>","cloth5.ogg"]

    "I tug on her even harder, and feel her body press on mine."

    p "You're really just so cute, Vel."

    v "Am I?"

    p "Yeah! I would always find you cute no matter what you do."

    v "You just said I was scary."

    p "Well.. that was a different thing."

    v "Is it?"

    v "How so?"

    p "You know.."

    v "Hm?"

    p ". . ."

    #"Silence befalls us, and I tried to think of what we could talk about."

    p "Oh. That's right!"

    p "Neu came here a few days before."

    v "Did she?"

    v "Why did she come here?"

    p "Well she said it was because she started forgetting about me."

    p "She came just to remember me."

    v "Is that so?"

    v "Did she do anything else?"

    p "Huh? No.. we just talked for a little while."

    v "Really?"

    "Though subtle, I could feel concern coming from Vel's words."

    "Is she actually feeling jealous?"

    "That's something I never thought I would see from her."

    p "Yeah that's really all that happened."

    #v "If you say so."

    p "Are you concerned something else happened?"

    v ". . ."

    v "No."

    p "Really?"

    p "Are you truly not?"

    p "You can be honest with me, Vel."

    v ". . ."

    "I inched closer to Vel's ear, and talked to her softly."

    p "You should tell me how you feel, Vel."

    p "Did you think something happened between us?"

    v ". . ."

    v "Why are you being weird, Human?"

    p "Sorry. You just looked really cute, and I wanted to tease you."

    v ". . ."

    "She just went silent, and focused on her game as a response."

    "It doesn't seem like she's amused of what I did."

    "I didn't want to continue messing with her, and actually wanted to reassure her."

    p "You don't need to worry."

    p "I won't do the things I do to you with other girls."

    p "You can trust in me."

    v ". . ."

    v "If you say so."

    p "Plus you'll always be the cutest of them all!"

    p "I would never want to settle for less."

    v "What are you talking about?"

    v "You're weird, Human."

    #$ renpy.music.set_volume(1.0, 0, channel='sound')
    #play sound ["<silence .3>","cloth7.ogg"]

    "Despite her words, I feel Vel press herself onto me as she leans her head to mine."

    p "Neu did say something interesting to me though."

    p "Well I guess it was me who brought up the subject."

    p "It was about when you first came here."

    v ". . ."

    p "She said that you lied about being sent here by mistake. Is that true?"

    v ". . ."

    p "Vel..?"

    v "I don't want to talk about it."

    p "Huh? Why not?"

    p "It's not like I would get mad at you for lying."

    p "I just want to to know the reason why you did it."

    v ". . ."

    v "No."

    "I got confused by Vel's sudden change in behavior."

    "This is the first time I'm seeing her act like this."

    "All this time, she has responded positively to everything I said or did to her."

    "I let my curiosity get the better of me, and continued to prod on the subject."

    p "Could you please tell me Vel?"

    v ". . ."

    p "Please?"

    v ". . ."

    "I kept nudging on her to answer me, but she just stayed quiet the whole time."

    $ renpy.music.set_volume(0.7, 0, channel='sound')
    play sound ["<silence .6>","headbutt.ogg"]

    "She seemingly reached her limit as she suddenly knocked me with her head."

    "I was at a loss for words as I tried to think of what just happened."

    #"I'll take that as her telling me to stop."

    "That was the first time Vel stopped me from doing something."

    "It really must be a touchy subject when she's acting like this."

    p "I'm sorry.."

    p "It's fine if you don't want to talk about it."

    p "I don't want to make you feel uncomfortable."

    v ". . ."

    "Seems like she didn't have words to respond."

    "I didn't know what else to say too, and we both got swallowed by silence."

    "The air between us started feeling awkward, so I tried pulling away from her."

    "But before I could do so, Vel quickly grabs my hand to stop me."

    "She pulls my arm, and wraps it around her body again."

    p "Vel.."

    v "Human."

    v "Why did you pull away?"

    p "Well.. I thought I made you angry."

    v "I'm not."

    p "Still.. I'm sorry."

    v "Mmh."

    v "It's fine."

    "Vel inches herself into me once again, and I feel the warmth of her body."

    p "Vel.."

    p "I really can't win against you."

    v "Are you talking about in games?"

    p "Huh? No.. that's now what I'm saying."

    v "It's not?"

    p "I mean I can't bring myself to hate you."

    p "I love you, Vel."

    v ". . ."

    v "Love.."

    v "I still don't get it."

    p "Yeah.. that's what I thought you'd say."

    "Vel pauses, not knowing what to say."

    p "Do you remember what I told you before?"

    #v "Mmh."

    p "I told you it's fine if you don't understand. I would always be here to help you."

    p "You just need to tell me how you feel."

    v "How I feel?"

    v ". . ."

    "Vel gets lost in her thoughts for a few moments."

    "She seems to be really thinking hard on what she should say."

    v "Human.."

    p "Yes, Vel?"

    v "I want to play games while I'm with you."

    p ". . ."

    p "Do you want me to hold you like this too while you play?"

    v "Mmh."

    v "I guess so."

    v "You seem really happy whenever you do it."

    p ". . ."

    p "That's a really roundabout way of saying you love me back.."

    v "Is it?"

    v "Does that really mean the same?"

    p "Yeah. It's the same as how I feel about you."

    p "I just want to spend all my time with you, even if we're just doing this."

    p "If it's the same, then what you're feeling could only be love."

    v "Love.."

    v "Is that what it is?"

    p "Well.. I can't really explain it fully."

    p "There's a lot of ways you can define it."

    p "But we don't need to make it complicated like that."

    p "Maybe next time you can just say you love me too."

    v "Should I?"

    p "Of course. It's how people normally say it."

    v "Hmm.. if you say so."

    "She still sounds unsure about everything, but at least I heard from her directly how she feels."

    "This is already a big difference compared to when I first met her."

    "And even though she said it in an unconventional way, it still makes me really happy."

    "My happiness overfilled me, and led me to embracing Vel even harder."

    v ". . ."

    v "Does that make us lovers?"

    "I was caught off guard by her question as I was occupied indulging on her soft body."

    p "Umm.. I guess it does."

    p "Do you want us to be?"

    v "I guess so."

    p "Then starting today we're officially lovers!"

    v "Mmh."

    v "Does that change anything?"

    p "Well.. not really."

    p "We were already acting like one even before, so we can just continue what we're doing."

    v "Is that so?"

    p "Yeah, but it's still nice to say it."

    p "And we can celebrate the day for the coming years."

    v "Celebrate?"

    p "Yeah! It's normal for humans to celebrate that date."

    v ". . ."

    v "I can't remember days."

    p "Yeah. I know, but you have nothing to worry about."

    p "I won't forget about it, and I would always remind you."

    v "Will you?"

    p "Of course. Even if I have to do it everyday."

    v "I will try to remember."

    #p "Yeah, thank you."

    #p "I really love you, Vel."

    #v "Mmh."

    "Vel pushes her whole body on mine, and I embraced her really tightly."

    "A few moments passed as we lay in silence."

    "We've been huddled together for quite some time now, and something has been building up in me at a certain spot."

    "My lower half have become fully erect, and I can't help myself but push it against her plump butt."

    "Her soft body is so close to mine, making me want to caress her all over."

    "I couldn't contain myself anymore, and slid my hand to reach for her boobs. "

    stop music fadeout 1.0

    $ renpy.music.set_volume(0.7, 0, channel='sound')
    play sound ["<silence .0>","cloth9.ogg"]

    scene black with fadefast3
    scene grope2 with fadefast
    pause 1

    v "Ah-"

    "I feel the suppleness of her breast as I squish her with my hand."

    "She's really just so soft around here."

    "I started moving my hand, gently rolling over her boobs."

    v "Human.."

    p "Vel.. I just can't stop myself."

    p "I've missed feeling your body like this for so long."

    v ". . ."

    v "You always go for my boobs."

    p "Yeah, I really love them."

    p "They just feel so soft."

    p "I can never get enough of them."

    v "Is that so?"

    p "Yeah, I want to keep fondling you like this forever."

    p "Do you want me to stop?"

    v "No, it's fine."

    v "You're really happy when you're touching them, so it's fine."

    p "Vel.. you're just so lovely."

    p "I'm so lucky to have you."

    v "Are you?"

    "I kept on caressing Vel's supple boobs to my heart's content."

    "All the while, she kept her focus on her game."

    p "Hey Vel."

    v "Hm?"

    p "Could you make your cloak morph to let out your boobs?"

    p "I want to feel you directly."

    v ". . ."

    v "If you say so."

    scene black with fadefast3
    scene grope1 with fade
    pause 1

    "Vel's cloak started tearing itself, and her boobs are left fully exposed."

    "I continued to squeeze on her, going even harder this time."

    "She feels even better now that there's nothing separating us."

    p "Ahh- Vel. Your boobs really are just amazing."

    v "Are they?"

    p "Yeah, nothing beats fondling them directly."

    p "I love feeling your skin and the sensation of your nipple as I brush through it."

    p "Do you like it when I touch you here too, Vel?"

    v ". . ."

    v "I don't know."

    "Even if she said she doesn't know, I can tell the actual answer from her body."

    "She seems to start feeling it too, as I feel her nipples getting harder."

    "My finger flicks on it lightly a few times, and it became fully erect."

    p "Vel.. your body is so lewd."

    p "Especially this cute nipple of yours."

    scene grope3 with fade
    pause 1

    "I gently squeezed her boobs, and focused my finger on her erect nipple."

    "I slowly rolled my finger around, feeling the shape of it."

    "It produces a lovely sensation as it kisses my fingertip."

    p "Your nipples are totally standing straight."

    p "They feel so good to play around."

    v ". . ."

    v "You're being weird again, Human."

    p "No, I'm not."

    p "This is completely normal."

    p "It just means you're getting turned on too."

    v "Turned on?"

    p "It means you want me to keep having my way with you."

    v "Does it?"

    p "Yeah, I just want to touch your body all over."

    v ". . ."

    v "Hey Human."

    p "Yes, Vel?"

    v "You have been poking my butt for a while now."

    p "Yeah.. my dick couldn't help but stand because of Vel's lewd body."

    p "Even the plumpness of your ass feels great."

    p "I just can't contain myself when you feel this good."

    p "I want to stick it in you now, Vel."

    v "But I'm still playing."

    v "I haven't played all this time."

    p "Then you can just keep playing while I let myself inside you."

    v "Can I do that?"

    p "Of course. I don't want to stop you from doing what you want."

    v "Then what do you want me to do?"

    p "You just need to lie on your stomach, and I'll get behind you."

    #$ renpy.music.set_volume(0.7, 0, channel='sound')
    #play sound ["<silence .4>","cloth8.ogg"]

    scene black with fadefast3
    pause 0.7

    scene dogs with fadefast

    v "Like this?"

    p "Yeah, that's perfect."

    p "The sight of your plump ass is really turning me on."

    p "My dick can't wait anymore to penetrate you."

    v "Should I take off my clothes again?"

    menu:
        "You should.":
            jump dognude

        "You don't need to":
            jump dogcloth

    label dognude:
    $ dogcloak = 0
    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound ["<silence .3>","cloth8.ogg"]
    scene black with fadefast

    scene dogsn with fade

    "Vel's cloak morphs into nothingness, and her bare body is exposed."

    p "Your smooth skin looks so beautiful."

    v "Does it?"

    p "Yeah. I feel like I could cum just rubbing myself anywhere in your body."

    v ". . ."

    v "Stop being weird, Human."

    p "Sorry. My dick is just raging and taking over me."

    v "There's nothing stopping you."

    p "Then I'm going to pound you now."

    jump doggysex

    label dogcloth:
    $ dogcloak = 1
    scene dogs

    p "You don't really need to."

    v "I don't?"

    p "Yeah. You look cute even if you're not naked."

    p "I want to pound you while you're looking like that."

    v ". . ."

    v "I don't understand what you're saying, Human."

    v "But if you say so."

    p "Then I'm going to slip in you now."

    p "You can just keep playing like that."

    v "Mmh."

    jump doggysex

    label doggysex:
    if dogcloak >= 1:
        scene black with fadefast3
        scene dogc with fadefast
    else:
        scene black with fadefast3
        scene dogn with fadefast


    p "Vel.. your pussy just feels so amazing."

    v "Does it?"

    p "Yeah. It feels just as great when I was inside you before."

    p "I really missed feeling your tightness like this."

    p "If you didn't have to go, I would have done you like this everyday."

    v "Will you?"

    p "Of course! Who wouldn't want to keep grinding you like this."

    v "You can do it too tomorrow."

    p "Really?"

    v "Mmh."

    p "Ah- you're really just so lovely, Vel!"

    p "You're making me want to pound you even more."

    scene dogx with fade

    v "Ahh- Human."

    v "You hitting me so deep inside."

    p "Yeah.. your pussy just keeps sucking me in."

    p "I love hitting the entrance to your womb."

    v "Mmhh-"

    p "You're just so wet and slippery too."

    p "I guess playing with your boobs really turned you on, huh?"

    v ". . ."

    v "I don't know."

    v "I don't get what you're saying."

    p "You'll understand it soon enough as we keep doing this."

    if dogcloak >= 1:
        scene dogc with fade
    else:
        scene dogn with fade

    p "Are you able to play just fine, Vel?"

    p "Am I not disturbing you?"

    v "You're not."

    v "I can keep playing."

    if dogcloak >= 1:
        scene dogc2 with dissolve
    else:
        scene dogn2 with dissolve

    p "Then how about if I pound you even faster?"

    v "Ahhh- Human."

    v "You're going so fast."

    p "I can't stop myself when you feel this good."

    p "Squishing your ass just makes it even lewder too."

    p "I don't think I can hold out for much longer."

    v "Are you going to cum inside me again, Human?"

    p "Do you want me to?"

    v ". . ."

    v "You can do what you want."

    scene dogx2 with fade

    p "Of course I would love to let it out inside you!"

    v "Then are you getting close?"

    p "Yeah. I'll move even faster now."

    v "Mmmhhh-"

    v "You're hitting me so hard, Human."

    v "Your dick feels really hot."

    p "Ahh- Did you always speak lewdly like that?"

    p "You're making my dick twitch even more with your words."

    v "Am I?"

    p "Vel.. I'm almost there!"

    p "Ugh- you're tightening up even more."

    v "Don't you want me to?"

    p "Yeah. I love it when you do."

    p "Ah- I can't take it anymore, Vel."

    p "I'm going to fill you up!"

    show dogxc with dissolve
    pause 0.1
    hide dogx2
    $ renpy.pause(delay = 5.0, hard = True)
    #pause 5

    scene bed with fade
    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Wish5_HarpOnly_loop.ogg" loop fadein 0.5
    pause 1

    p "That felt amazing."

    v "Did it?"

    p "Yeah. I almost let out everything I've saved up since you were gone."

    v "Mmh. I can feel it all inside me."

    v "It's full of your hot liquid."

    p "Saying things like that just makes me want to do you more."

    v "Do you want to, Human?"

    p "Of course I do!"

    p "I've missed you so much this past two weeks."

    p "I gotta make up for all that lost time."

    v ". . ."

    v "You can do whatever you want."

    p "Really?"

    p "Will you be fine with whatever I want to do?"

    v "Mmh."

    v "Probably."

    p "I'm really just so lucky to have you, Vel!"

    p "Being with you just feels like a dream."

    v "Does it?"

    p "Yeah. I'm just really happy that you're here with me."

    v "I can tell."

    "The two of us stayed silent as we let time pass by."

    "I stared at Vel, appreciating the beauty I was bestowed upon."

    "I can never get enough of her cuteness."

    "I really wish I could stay like this with her forever."

    p "Vel.."

    p "What's gonna happen now?"

    v "Hm?"

    p "Are you gonna be staying here with me?"

    v "Mmh."

    v "I'm not going anywhere."

    p "Vel! I'm so happy to hear that."

    p "What did I ever do to deserve someone like you?"

    v "Why are you getting so excited, Human?"

    p "How could I not be?"

    p "I can't think of anything else that would make me happier than being with you."

    v ". . ."

    v "Really?"

    p "Of course."

    p "But what about your work?"

    p "Will Neu come back here again?"

    v "Mmh. Most likely."

    v "I still need to do my job."

    p "Yeah, I figured."

    v "I would always come back, Human."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound ["<silence .0>","cloth6.ogg"]

    "Vel leans herself closer to me as she answers."

    p "Yeah.. I know you will."

    p "And I would always be here waiting for you."

    v "What if it happens again?"

    p "Huh? What thing?"

    p "Do you mean when I said you looked like a different person?"

    v "Mmh."

    p "You don't have anything to worry about!"

    p "I would always call out to you no matter what happens."

    p "And I know you won't forget about me."

    v "I won't."

    v "I will always remember you, Human."

    "There's still a lot of things I don't know about Vel."

    "What exactly happened to her back then?"

    "Would I actually meet here like that again?"

    "She's apparently the strongest reaper, but what does that even really mean?"

    "And it seems like she doesn't know a lot about our world too."

    "I have a lot of things I want her to know about."

    "A lot of things I want to experience with her."

    "And I can't wait to do all those things with her."

    p "Hey Vel."

    v "Hm?"

    p "You're really just so cute."

    v ". . ."

    v "You keep on saying that."

    p "Only because it's true."

    v "You're weird, Human."

    p "No, I'm not."

    p "This is completely normal."

    p "Falling in love with a grim reaper is completely normal."

    p "I love you, Vel."

    v ". . ."

    v "I love you too, Human."

    scene white with dissolvelong1
    pause 1.5
    scene white2 with dissolve

    "My heart skipped a beat as those soft words left Vel's mouth."

    "I pulled her closer to me into a tight embrace."

    "We stayed silent, enjoying each other's warmth for a while."

    "But it didn't take long for her to tell me that something is poking her again."

    "Feeling her body made me fully erect once again, and she asked if we're going to do it again."

    "Of course there's only one answer to that."

    "I let myself inside her, and fucked her."

    "And we kept doing it until I passed out of exhaustion."

    "I landed on Vel's soft boobs, and she kept on nudging me to move."

    "But I didn't have the energy to abide by her, so she just gave up and started playing."

    "After a while I felt her gently laying down her hand on my head, and I completely dozed off."

    stop music fadeout 1.5

    scene black with fade
    pause 0.5

    "By the time I woke up, I'm still nestled in Vel's supple bosom while she's also fast asleep."



    pause 0.5



# THE END

    scene theend with fadelastlong
    pause 2

    "Thank you for playing!"

    "You can now read the afterword or go back to main menu."

    menu:

        "Read afterword":
            jump afterword

        "Go to main menu":
            jump ending


label afterword:
    scene black with fadefast3
    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "PerituneMaterial_Puppet_loop.ogg" loop fadein 1.0
    scene afterword with fade

    pause 1

    "Hello! This is Kamuo."

    "Thank you very much for playing this visual novel."

    "This is the very first vn I've finished."

    "The initial plan was always to keep it simple so I could finish it in a reasonable time."

    "But it still took a full year including pre-production, as I improved everything each update."

    "I think this vn is a good way to show my improvement as it's also been a year since I started doing lewd animations."

    "I started on the very last day of May 2019."

    "If you liked Vel (Why wouldn't you?) and Neu, then you have nothing to worry about."

    "This isn't the actual end for these characters. In fact it's only the beginning!"

    "I love Vel as my character, and I have a lot of things I wanna do with her."

    "I'm ending this vn here because I think it's a nice note to end on, and this is how I envisioned the vn from the start."

    "And also I wanted to be able to look back at the vn to know what I should improve on for the next one."

    "Even though there's been changes throughout this vn, I still loosely followed the style I set from the start."

    "Doing the next part as a separate vn means I can do things differently and make it better overall."

    "Once again, thank you for playing and supporting."

    "Thank you to all my patrons for making it possible for me to keep working on Vel."

    "I hope you keep supporting, so I can make even more of her!"


label ending:
    $ persistent.ending = True
    stop music fadeout 1.0
    scene black with fade











    # This ends the game.

    return
