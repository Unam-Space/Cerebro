#!/usr/bin/env python3
import Panel_components

class Actions:

    def __init__ (self,windowm):
        self.window = windowm

    def KeyboardControl(self, event): 
        key = event.keysym
        if(key == "W" or key == "w" or key == "Up"):
            Panel_components.Char(self.window, 1350, 700, "W")
        elif(key == "A" or key == "a" or key == "Left"):
            Panel_components.Char(self.window, 1350, 700, "A")
        elif(key == "S" or key == "s" or key == "Right"):
            Panel_components.Char(self.window, 1350, 700, "S")
        elif(key == "D" or key == "d" or key == "Down"): 
            Panel_components.Char(self.window, 1350, 700, "D")