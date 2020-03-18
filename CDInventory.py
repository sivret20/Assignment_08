#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# ASivret, 2020-Mar-17, replaced pseudocode with functional program
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = cd_title
            self.__cd_artist = cd_artist
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))
    
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value
        
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be a string')
        
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be a string')
            
    def print_neat(self):
        return '{}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist)
 
    def print_file(self):
        return '{},{},{}'.format(self.cd_id, self.cd_title, self.cd_artist)
 
       
    def __str__(self):
        return '{}, {}, {}'.format(self.cd_id, self.cd_title, self.cd_artist)

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    @staticmethod
    def load_inventory(file_name):             
        """Function to load data from file to a list of CD Objects

        Reads the data from file identified by file_name into a 2D table

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            2D list: list of CD Objects
        """
        table = []
        with open(file_name, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                row = CD(data[0], data[1], data[2])
                table.append(row)
        return table
     
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        

        """Function to save CD inventory (list of CDObjects) to file

        Reads data from a 2D table (list of CD Objects) to file file_name

        Args:
            file_name (string): name of file used to append the data to
            table (list of dict): 2D data structure (list of CD Objects) that holds the data during runtime

        Returns:
            None.
        """
        
        objFile = open(file_name, 'w')
        for row in lst_Inventory:
            objFile.write(row.print_file() + '\n')
        objFile.close()


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handles IO within the program:

    properties:
        
    methods:
        print_menu(): -> None
        menu_choice(): -> A menu selection (string)
        show_inventory(table): -> None
        get_input(): -> strID (int), strTitle (string), strArtist (String)
    """
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[i] Display Current Inventory\n[a] Add CD\n[s] Save Inventory to file\n[l] load Inventory from file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['i', 'a', 's', 'l', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of CDObjects): 2D data structure (list of CDObjects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row.print_neat())
        print('======================================')
    
    @staticmethod
    def get_input():
        """Prompts user for new entry input.
            Throws an exception if ID input can't be converted to int.


        Args:
            None.

        Returns:
            ID, title, and artist (strings).

        """
        while True:
            try:
                strID = input('Enter ID: ').strip()
                intCheck = int(strID)
                break
            except ValueError as e:
                print('Please enter an integer for ID #.')
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist

class DataProcessor:
    """Manipulates memory stored within the program

    properties:
        
    methods:
        add_CD(CDInfo, table): -> None
    """
    
    @staticmethod        
    def add_CD(CDInfo, table):
        """Function to add a CD to memory based on previous user input.
        
        Args:
            CDInfo (tuple): Holds info about the CD
            table (list of CDObjects): 2D data structure that holds the tuples
        Returns:
            None.
        """
        
        cdID, title, artist = CDInfo
        try:
            cdID = int(cdID)
        except ValueError as e:
            print('ID is not an integer!')
            print(e.__doc__)
        row = CD(cdID, title, artist)
        table.append(row)
        

# -- Main Body of Script -- #

lstOfCDObjects = FileIO.load_inventory(strFileName)
while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    # let user exit program
    if strChoice == 'x':
        break
    # let user add data to the inventory
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist
        tplCDInfo = IO.get_input()
        # Add item to the table
        DataProcessor.add_CD(tplCDInfo,lstOfCDObjects)
        # show user current inventory
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user load inventory from file
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # let user save inventory to file
    elif strChoice == 's':
        #  Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process choice
        if strYesNo == 'y':
            # save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
        # catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')

 