import PySimpleGUI as sg
import re
from functions import to_binary, to_decimal

# Theme
sg.theme('LightGreen10')

# Window One - Convert decimal to binary
def decimal_to_binary():

    layout = [ 
        [sg.Text("", key='warning')],
        [sg.Text("Decimal Number:"), sg.InputText(key='decimalNum'), sg.Push()],
        [sg.Text("Binary Number: "), sg.Text("", key='result'), sg.Push()],
        [sg.Text("")],
        [sg.Button("Convert"), sg.Button("Clean"), sg.Button("Change Conversion")]
        ]

    return sg.Window('Decimal to Binary Conversor by Cesar Coppola Santos', layout, element_justification='c', finalize=True)

# Window Two - Convert binary to decimal
def binary_to_decimal():

    layout = [ 
        [sg.Text("", key='warning')],
        [sg.Text("Binary Number:"), sg.InputText(key='binaryNum'), sg.Push()],
        [sg.Text("Decimal Number: "), sg.Text("", key='result'), sg.Push()],
        [sg.Text("")],
        [sg.Button("Convert"), sg.Button("Clean"), sg.Button("Change Conversion")]
        ]

    return sg.Window('Binary to Decimal Conversor by Cesar Coppola Santos', layout, element_justification='c', finalize=True)

window1, window2 = decimal_to_binary(), None

# Loop Event
while True:

    window, event, values = sg.read_all_windows()
    
    # If user close window
    if (window == window1 or window == window2) and event == sg.WIN_CLOSED:
        break

    # If user press change conversion button
    if window == window1 and event == "Change Conversion":
        window1.close()
        window2 = binary_to_decimal()
    
    elif window == window2 and event == "Change Conversion":
        window2.close()
        window1 = decimal_to_binary()

    # If user press convert button
    if window == window1 and event == "Convert":
        # Verify if decimal number input have only numeric characters
        if values['decimalNum'].isdecimal():
            window['warning'].Update('')
            window['result'].Update(to_binary(values['decimalNum']))
            
        else:
            window['result'].Update('')
            window['warning'].Update('Please, enter a valid Decimal Number.')

    elif window == window2 and event == "Convert":
        # Verify if binary number have only 1 and 0
        if re.match("^[10]+$", values['binaryNum'] ) != None:
            window['warning'].Update('')
            window['result'].Update(to_decimal(values['binaryNum']))

        else:
            window['result'].Update('')
            window['warning'].Update('Please, enter a valid Binary Number.')
    
    # If user press clean button
    if window == window1 and event == "Clean":
        window['decimalNum'].Update('')
        window['warning'].Update('')
        window['result'].Update('')
        
    elif window == window2 and event == "Clean":
        window['binaryNum'].Update('')
        window['warning'].Update('')
        window['result'].Update('')

window.close()
