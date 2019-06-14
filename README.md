# python-hexvalues
Summary: 
A simple GUI (tkinter) that allows the user to define a hex color value by using RGB slides or manually enter values for each.

I'm just starting out with the Python language, so I thought this would be an ideal first project to get my feet wet. 
I'm using a class (RGBtoHex) to define the GUI and define the validation functions.  

There are two validations that occur on the text (Entry) fields:

validateField() - validates the overall field value when the field loses focus to ensure a value exists. If there is no value in the field, the field keeps focus until the user enters a value or uses the respective slider.
validateRange() - validates the field values as they are updated to ensure only digits between 1-255 are being entered.

Possible future enhancements:
 - Add a copy button to save the hex value to the clipboard
 - A toggle to set RGB or HSL values
 - Add a field/label to display color names when specific values are entered (ie 'aliceblue' = 240, 248, 255)
 - Allow users to enter a color name and update RGB and hex values accordingly.
 - Initial beginnings of my own module?
 
 
