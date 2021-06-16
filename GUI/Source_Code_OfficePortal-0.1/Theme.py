import PySimpleGUI as gui

def setTheme():
    return(
        gui.theme('Default1'),
        gui.theme_background_color('#ebfdff'),
        #gui.theme_border_width('#ebfdff'),
        gui.theme_button_color('#ffffff'),
        gui.theme_element_background_color('#ebfdff'),
        #gui.theme_element_text_color('#ebfdff'),
        gui.theme_input_background_color('white')
        #gui.theme_input_text_color('#ebfdff'),
        #gui.theme_progress_bar_border_width('#ebfdff'),
        #gui.theme_progress_bar_color('#ebfdff'),
        #gui.theme_slider_border_width('#ebfdff'),
        #gui.theme_slider_color('#ebfdff'),
        #gui.theme_text_color('#ebfdff') mouseover
    )
   