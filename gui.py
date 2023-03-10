import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter to-do', key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='current_todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica',+ 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window['current_todos'].update(values=todos)

    elif event == "current_todos":
       window['todo'].update(value=values['current_todos'][0])

    elif event == "Edit":
        todo_to_edit = values['current_todos'][0]
        new_todo = values['todo'] + '\n'

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo

        functions.write_todos(todos)
        window['current_todos'].update(values=todos)

    elif event == sg.WIN_CLOSED:
        break

window.close()

