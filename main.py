import os
import logging
import papermill

#TODO: Run all notebooks and export HTML reports into notebook/pages

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')

    # List notebooks in /notebooks
    # Loop through notebooks:
    #   Try: run and export HTML to notebook/page
    #   Except: log warning
