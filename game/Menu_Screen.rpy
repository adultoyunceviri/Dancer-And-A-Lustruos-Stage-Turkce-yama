screen main_menu_screen :
     imagemap:
        ground "images/Main_Menu/main_menu.png"
        idle "images/Main_Menu/main_menu.png"
        hover "images/Main_Menu/main_menu_hover.png"
        selected_idle "images/Main_Menu/main_menu.png"
        selected_hover "images/Main_Menu/main_menu_hover.png"

        hotspot (73, 87, 265, 109) action [ui.jumps("start")]
        hotspot (70, 223, 266, 95) action [ui.jumps("main_menu_load")]
        hotspot (50, 340, 484, 103) action [ui.jumps("main_menu_prefs")]
        hotspot (95, 454, 282, 127) action [ui.jumps("main_menu_gallery")]
        hotspot (102, 587, 182, 107) action [ui.jumps("main_menu_quit")]

screen Gallery_Screen01 :
     imagemap:
        ground "images/Main_Menu/Gallery_01_Idle.png"
        idle "images/Main_Menu/Gallery_01_Idle.png"
        hover "images/Main_Menu/Gallery_01_Hover.png"
        selected_idle "images/Main_Menu/Gallery_01_Idle.png"
        selected_hover "images/Main_Menu/Gallery_01_Hover.png"

        hotspot (45, 106, 578, 325) action [ui.jumps("gallery_Img01")]
        hotspot (671, 106, 580, 327) action [ui.jumps("gallery_Img02")]
        hotspot (1297, 107, 580, 326) action [ui.jumps("gallery_Img03")]
        hotspot (45, 484, 578, 330) action [ui.jumps("gallery_Img04")]
        hotspot (671, 485, 577, 329) action [ui.jumps("gallery_Img05")]
        hotspot (1295, 484, 582, 329) action [ui.jumps("gallery_Img06")]
        hotspot (1537, 900, 196, 82) action [ui.jumps("Gallery_Next")]

screen Gallery_Screen02 :
     imagemap:
        ground "images/Main_Menu/Gallery_02_Idle.png"
        idle "images/Main_Menu/Gallery_02_Idle.png"
        hover "images/Main_Menu/Gallery_02_Hover.png"
        selected_idle "images/Main_Menu/Gallery_02_Idle.png"
        selected_hover "images/Main_Menu/Gallery_02_Hover.png"

        hotspot (45, 106, 578, 325) action [ui.jumps("gallery2_Img01")]
        hotspot (671, 106, 580, 327) action [ui.jumps("gallery2_Img02")]
        hotspot (1297, 107, 580, 326) action [ui.jumps("gallery2_Img03")]
        hotspot (45, 484, 578, 330) action [ui.jumps("gallery2_Img04")]
        hotspot (671, 485, 577, 329) action [ui.jumps("gallery2_Secret")]
        hotspot (282, 898, 186, 83) action [ui.jumps("gallery2_Back")]
        hotspot (1537, 900, 196, 82) action [ui.jumps("gallery_Exit")]
