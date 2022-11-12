import TestGUI

def main():

    #runs the test GUI
    my_gui = TestGUI.Monitor(-1000, -1000) #invalid coordinates for checking error messages
    my_gui.display()    

    my_gui = TestGUI.Monitor(1, 1) #valid coordinates for checking error messages
    my_gui.display()    


if __name__ == main():
    main()