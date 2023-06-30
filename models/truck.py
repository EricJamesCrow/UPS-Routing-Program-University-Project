class Truck(object):
    '''
    Simple truck object which has a variable for storing the packages it needs to deliver.

    '''
    def __init__(self):
        self.packages = []

    def add(self, package: list) -> None:
        '''
        Appends a package to self.packages.

        Parameters:
        package (list): Takes a list which contains the package data
        
        '''
        self.packages.append(package)
