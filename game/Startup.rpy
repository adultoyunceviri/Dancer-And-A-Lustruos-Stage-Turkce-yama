label main_menu :
    scene black
    pause 1
    play music "Music/Main_Menu.mp3" fadein 5.0
    pause 3
    scene splash_01 with dissolve
    pause 2
    show splash_02 with dissolve
    pause 2
    scene black with dissolve
    pause 3
    scene splash_03 with dissolve
    pause 5
    scene main_menu_bg with dissolve
    call screen main_menu

label main_menu_load :
    jump load_screen

label main_menu_prefs :
    jump preferences_screen

label main_menu_gallery :
    jump gallery

label main_menu_quit :
    $renpy.quit()

label gallery :
    call screen Gallery_Screen01

label gallery_Img01 :
    scene S02_Bar_03
    pause
    call screen Gallery_Screen01

label gallery_Img02 :
    scene S02_Bar_02
    pause
    call screen Gallery_Screen01

label gallery_Img03 :
    scene S02_Bar_04
    pause
    call screen Gallery_Screen01

label gallery_Img04 :
    scene S04_Alley_11
    pause
    call screen Gallery_Screen01

label gallery_Img05 :
    scene S06_Bedroom_08
    pause
    call screen Gallery_Screen01

label gallery_Img06 :
    scene S08_Bedroom_06
    pause
    call screen Gallery_Screen01

label Gallery_Next :
    call screen Gallery_Screen02

label gallery2_Img01 :
    scene S07_Bathroom_02
    pause
    call screen Gallery_Screen02

label gallery2_Img02 :
    scene S08_Bedroom_07
    pause
    call screen Gallery_Screen02

label gallery2_Img03 :
    scene S08_Bedroom_02
    pause
    call screen Gallery_Screen02

label gallery2_Img04 :
    scene S09_Gina_01
    pause
    call screen Gallery_Screen02

label gallery2_Secret :
    scene black with LT
    $ renpy.pause (3.0, hard=True)
    $ Gal_Input = renpy.input("??? ?????? ??????")

    if Gal_Input == "Sis" :
        show Gina_Gal_01 with LT:
            xalign 0.5 yalign 0
            pause 3.0
            linear 10.0 yalign 1.0
            pause 3.0
            linear 10.0 yalign 0.0
            pause 3.0
            repeat
        pause
        call screen Gallery_Screen02

    if Gal_Input == "Violet" :
        show Violet_Gal_01 with LT:
            xalign 0.5 yalign 0
            pause 3.0
            linear 10.0 yalign 1.0
            pause 3.0
            linear 10.0 yalign 0.0
            pause 3.0
            repeat
        pause
        call screen Gallery_Screen02

    if Gal_Input == "Sentry" :
        show Clara_Gal_01 with LT:
            xalign 0.5 yalign 0
            pause 3.0
            linear 10.0 yalign 1.0
            pause 3.0
            linear 10.0 yalign 0.0
            pause 3.0
            repeat
        pause
        call screen Gallery_Screen02

label gallery_Exit :
    call screen main_menu_screen

label gallery2_Back :
    call screen Gallery_Screen01
