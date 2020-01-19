import sys
sys.path.insert(0, './libs')
# from helper import greeting
import helper as h

def render():
    print(h.greeting('Ryley', 'Arnold'))


render()