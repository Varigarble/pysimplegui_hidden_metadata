from collections import namedtuple
import PySimpleGUI as sg

sg.theme('Dark Blue 3')

Produce = namedtuple('Produce', ['Name', 'SKU', 'Price'])

banana = Produce('Banana', 4419, 0.89)
organic_banana = Produce('Banana', 99419, 0.89)  # this is a copy of banana with a different SKU only
apple = Produce('Gala Apple', 4012, 0.69)
beans = Produce('Black Beans', 7559, 1.29)
soy_cake = Produce('Tofu', 88682, 4.25)

shelf = [banana, apple, beans, soy_cake, apple, apple, organic_banana]
# the "shelf" list index is hardcoded to the items so that we can see the exact items that are placed in the bag:
indexed_shelf = list(enumerate(shelf))
gui_shelf = [(item[0], item[2]) for item in shelf]  # a subset of data for a pretty display

bag = []  # empty bag to fill at checkout

layout = [[sg.T("Shelf", size=(37, 0), justification='left'), sg.T("Basket", size=(37, 0), justification='left')],
        [sg.Listbox(values=gui_shelf, size=(40, 10), select_mode='multiple', key='SELECTION', enable_events=True, \
            metadata=()),
        sg.Listbox(values=['Empty Basket'], size=(40, 10), key='BASKET')],
        [sg.B("View Metadata", key='-META-'), sg.B("Checkout", key='CHECKOUT')]
        ]

window = sg.Window(layout=layout, title='Go shopping!', element_padding=((10, 10), (5, 5)))

while True:
    event, value = window.read()
    
    if event is None:
        window.close()
        break

    if event == 'SELECTION':
        # replace existing metadata with a tuple of the indexes of highlighted items in the Listbox:
        window.Element('SELECTION').metadata=window.Element('SELECTION').GetIndexes()
        # copy the pretty display of items in a second Listbox:
        window.Element('BASKET').Update(value['SELECTION'])

    if event == '-META-':
        print("metadata: ", window.Element('SELECTION').metadata)

    if event == 'CHECKOUT':
        for item in indexed_shelf:
            if indexed_shelf.index(item) in window.Element('SELECTION').metadata:
                bag.append(item)
        print("metadata: ", window.Element('SELECTION').metadata)
        print("bag: ", bag)
        bag = []  # get a new empty bag
