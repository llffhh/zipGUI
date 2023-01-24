import PySimpleGUI as sg
import zipCreator

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key = "filename")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key = "folderpath")

compress_button = sg.Button("Compress")
output_label = sg.Text(key = 'output', text_color = "red")
exit_button = sg.Button("Exit")

col1 = sg.Column([[label1],[label2]])
col2 = sg.Column([[input1],[input2]])
col3 = sg.Column([[choose_button1],[choose_button2]])
window = sg.Window("File Compressor", layout = [[col1, col2, col3],
                                                [compress_button, exit_button, output_label]])

while True:
    event, values = window.read()
    print("event:", event)
    print("values: ", values)
    match event:
        case "Compress":
            filepaths = values['filename'].split(";")
            dest_dir = values['folderpath']
            zipCreator.zip(filepaths, dest_dir)
            window['output'].update(value = 'Compression completed')
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()