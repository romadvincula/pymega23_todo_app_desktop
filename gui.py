import functions
import PySimpleGUI as sg
import time
import os

TIME_FORMAT = "%b %d, %Y %H:%M:%S"
THEME = "DarkGreen1"

if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH, "w") as f:
        pass

sg.theme(THEME)
clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter to-do', key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='current_todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', + 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime(TIME_FORMAT))
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['current_todos'].update(values=todos)

    elif event == "current_todos":
        if not values['current_todos']:
            continue
        else:
            window['todo'].update(value=values['current_todos'][0])

    elif event == "Edit":
        try:
            todo_to_edit = values['current_todos'][0]
            new_todo = values['todo'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.write_todos(todos)
            window['current_todos'].update(values=todos)
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))

    elif event == "Complete":
        try:
            todo_to_complete = values['current_todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['current_todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item first.", font=("Helvetica", 20))

    elif event == sg.WIN_CLOSED or event == "Exit":
        break

window.close()
