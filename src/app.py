#!/usr/bin/env python

import flet

from ui.bar import *


from flet import (
    Page,
    colors,
    theme,
)
 
        
        

if __name__ == "__main__":
 
    def main(page: Page):
 
        page.title = "Flet Trello clone"
        page.padding = 0
        page.theme = theme.Theme(
            font_family="Verdana")
        page.theme.page_transitions.windows = "cupertino"
        page.fonts = {
            "Pacifico": "/Pacifico-Regular.ttf"
        }
        page.bgcolor = colors.BLUE_GREY_200
        page.update()
        
        app = ManaGoApp().build()
        page.add(app)
        page.update()
 
    flet.app(target=main)

