import PySimpleGUI as sg
METER_PER_FEET = 0.3048
METER_PER_INCH = 0.0254

feet_label = sg.Text('Enter feet:')
feet_input = sg.InputText(key='feet')

inches_label = sg.Text('Enter inches:')
inches_input = sg.InputText(key='inches')

convert_button = sg.Button('Convert', key='convert')
output = sg.Text(key='output')

window = sg.Window('Converter',
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [convert_button, output]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    if event == "convert":
        try:
            feet = float(values['feet'])
            inches = float(values['inches'])

            meters = (feet * METER_PER_FEET) + (inches * METER_PER_INCH)

            output_message = f'{meters} m'

        except ValueError:
            output_message = 'Enter numerical values only, no string nor blanks accepted.'

        except Exception as e:
            print(e)
            output_message = e

        window['output'].update(value=output_message)

    elif event == sg.WIN_CLOSED:
        break

window.close()

