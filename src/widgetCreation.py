from tkinter import *

## @file widgetCreation.py
#  @author The Trifecta
#  @brief This module implements methods to make tkinter labels and buttons.
#  @date Apr.06,2020

class makeLabels:

	## @brief initializes a tkinter label.
    #  @param1 frame to which label is be added.
    #  @param2 tkinter grid row.
    #  @param3 tkinter grid column.
    #  @param4 string with label text.
    def __init__(self, frame, row, column, text):
        self.frame = frame
        self.row = row
        self.column = column
        self.text = text

        self.label = Label(self.frame, text = self.text)
        self.label.grid(row = self.row, column = self.column)

class makeButtons:
		
		## @brief initializes a button component.
    	#  @param1 frame to which button is be added.
		#  @param2 colour of the button component to be made.
    	#  @param3 tkinter grid row.
    	#  @param4 tkinter grid column.
    	#  @param5 string with label text.
        def __init__(self, frame, colour, row, column, text):
            self.frame = frame
            self.colour = colour
            self.row = row
            self.column = column
            self.text = text

            if colour == "":
                self.button = Button(self.frame, height = 2, width = 6, state = DISABLED, text=self.text)
            else:
                self.button = Button(self.frame, height = 2, width = 6, state = DISABLED, bg = self.colour, text=self.text)
            self.button.grid(row = self.row, column = self.column)
			
		## @brief configures a buttons attribute.
    	#  @param1 attribute to be modifed.
		#  @param2 text to modify component with.
        def configure(self, attribute, text):
            self.button[attribute] = text
