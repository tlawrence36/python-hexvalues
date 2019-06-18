#! /usr/in/env python3
from tkinter import *
from tkinter import ttk

class RGBtoHex:
    '''
    Creates a RGB -> Hex widget that displays the hex value for any RGB color values.
    Values defined hrough the use of sliders and/or manually entering a value between 1-255 for each color.
    '''
    def __init__(self, *args, **kwargs):
        ''' Constructor function that creates and renders GUI '''
        # frame to hold widget
        self.frame = ttk.Frame(borderwidth=3, padding=10)

        # labels
        self.s1Label = ttk.Label(self.frame, text="R")
        self.s1Label.grid(column=0,row=0, sticky="e", padx=5)
        self.s2Label = ttk.Label(self.frame, text="G")
        self.s2Label.grid(column=0,row=1, sticky="e", padx=5)
        self.s3Label = ttk.Label(self.frame, text="B")
        self.s3Label.grid(column=0,row=2, sticky="e", padx=5)

        # variables to bind sliders and text fields
        self.slide1val = IntVar(name='slide1val')
        self.slide1val.set('1')
        self.slide2val = IntVar(name='slide2val')
        self.slide2val.set('1')
        self.slide3val = IntVar(name='slide3val')
        self.slide3val.set('1')
        self.colorCode = StringVar()

        # register validation function
        validator = self.frame.register(self.validateRange)

        # text fields
        self.entry1 = ttk.Entry(self.frame, width=3, textvariable=self.slide1val, validate="key", validatecommand = (validator, "%P"))
        self.entry1.bind('<FocusOut>', lambda _:self.validateField(self.slide1val))
        self.entry1.grid(column=4, row=0, padx=5)

        self.entry2 = ttk.Entry(self.frame, width=3, textvariable=self.slide2val, validate="key", validatecommand = (validator, "%P"))
        self.entry2.bind('<FocusOut>', lambda _:self.validateField(self.slide2val))
        self.entry2.grid(column=4, row=1, padx=5)

        self.entry3 = ttk.Entry(self.frame, width=3, textvariable=self.slide3val, validate="key", validatecommand = (validator, "%P"))
        self.entry3.bind('<FocusOut>', lambda _:self.validateField(self.slide3val))
        self.entry3.grid(column=4, row=2, padx=5)

        # read-only text field that holds resulting Hex value
        self.hexColorVal = ttk.Entry(self.frame, width=7, textvariable=self.colorCode, state='readonly', foreground='#777')
        self.hexColorVal.grid(column=5, row=4, padx=5, pady=3)

        # sliders
        self.slide1 = ttk.Scale(self.frame, from_=1, to=255, orient=HORIZONTAL, length=300, variable=self.slide1val, command=lambda s:self.slide1val.set('%d' % float(s)))
        self.slide1.grid(column=1, row=0, columnspan=3)
        self.slide2 = ttk.Scale(self.frame, from_=1, to=255, orient=HORIZONTAL, length=300, variable=self.slide2val, command=lambda s:self.slide2val.set('%d' % float(s)))
        self.slide2.grid(column=1, row=1, columnspan=3)
        self.slide3 = ttk.Scale(self.frame, from_=1, to=255, orient=HORIZONTAL, length=300, variable=self.slide3val, command=lambda s:self.slide3val.set('%d' % float(s)))
        self.slide3.grid(column=1, row=2, columnspan=3)

        # color swatch
        self.swatch = Canvas(self.frame, bg='#ffffff', height=100, width=100)
        self.swatch.grid(column=5,row=0, rowspan=3)

        # render gui
        self.frame.grid()

        # update color when values change, whether from slider or text entry
        self.slide1val.trace_add("write", self.updateColor)
        self.slide2val.trace_add("write", self.updateColor)
        self.slide3val.trace_add("write", self.updateColor)


    def updateColor(self, *args):
        ''' updates color swatch with new color based on current values '''
        try:
            vals=[int(float(self.slide1val.get())),
                 int(float(self.slide2val.get())),
                 int(float(self.slide3val.get()))]
            newColor = "#%02x%02x%02x" % (vals[0], vals[1], vals[2])
            self.swatch.configure(background = newColor)
            self.colorCode.set(newColor)
        except:
            # individual digit validation is being handled by the widget as user types,
            # overall value is validated when entry box loses focus,
            # so we don't need to raise any exceptions if a value doesn't exist
            pass


    def validateRange(self, val):
        ''' Validate range (1-255) when manually entering a value '''
        if val.isdigit():
            if int(val) >= 1 and int(val) <= 255:
                return True
        elif val is '': # allow 'temporary' empty field
            return True
        return False


    def validateField(self, *args):
        ''' Validate field value on blur to ensure a value is present '''
        triggerText = args[0] # entry box that triggered validation
        try:
            triggerText.get()
        except:
            # entry box empty, so keep focus until value entered
            if(str(triggerText) == 'slide1val'):
                self.entry1.focus()
            elif(str(triggerText) == 'slide2val'):
                self.entry2.focus()
            else:
                self.entry3.focus()



def main():
    root = Tk()
    root.title('Hex Color Conversion')
    root.geometry('505x160')
    root.resizable(False, False)
    # Create  widget
    widget = RGBtoHex(root)
    # Start event loop
    widget.frame.mainloop()

if __name__ == '__main__': main()
