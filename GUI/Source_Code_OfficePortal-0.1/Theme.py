import PySimpleGUI as gui

def setTheme():
    return(
        gui.theme('Default1'),
        gui.theme_background_color(('#ebfdff')),
        gui.theme_element_background_color(('#ebfdff')),
        gui.theme_input_background_color(('white')),
        gui.theme_element_text_color(('#ebfdff')),
        gui.theme_button_color(('#ebfdff'))
    )
   