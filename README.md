# PySimpleGUI metadata example

#### What it is:

This is an example of how to display a portion of data in a PySimpleGUI Listbox while effecting changes to a larger portion of data, and also an example of how to use the metadata parameter. 

#### How it works:

The enumerated namedtuple class list (indexed_list) approximates a data type that one might compose in retrieving rows from a database. The enumeration (e.g., a database row id) and product SKUs are not displayed in the Listbox gui. When a selection is made in the 'Shelf' Listbox, the metadata is updated with the indexes of the highlighted items. The final output is copied from the indexed_list by retrieving the items that are at the indexes corresponding to those values collected in the metadata parameter.

#### Why do it this way:

The Listbox returns an ordinary Python list class. It is possible to compare the displayed items to larger pieces of data that contain the displayed items, but this can lead to false matches if the displayed data is not unique enough. For example, the organic banana at the end of the list has the same name and price as the non-organic banana. If we search the indexed_list for the item that matches the name and price, Python will stop at the first match, which would be the non-organic banana. 
