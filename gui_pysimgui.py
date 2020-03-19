import PySimpleGUI as sg

def layout_gui():
    sg.ChangeLookAndFeel('GreenTan')

    layout = [
        [sg.Text('Concatenator2', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('')],
        [sg.Text('Files: '), sg.Input(), sg.FilesBrowse()],

        [sg.Text('_' * 80)],
        [sg.Text('Que tipo de ficheiro quer no seu output?')],
        [sg.Radio('Fasta     ', "RADIO1"), sg.Radio('Nexus    ', "RADIO1"),
         sg.Radio('Phylip     ', "RADIO1"), sg.Radio('Clustal / ALN    ', "RADIO1")],

        [sg.Text('_' * 80)],
        [sg.Text('Deseja concatenar?')],
        [sg.Radio('Sim!     ', "RADIO2", default=True), sg.Radio('Não!', "RADIO2")],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Everything bagel', default_element_size=(40, 1)).Layout(layout)
    button, values = window.Read()
    return values