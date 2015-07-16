class System(object):
    ''' class representing system object '''
    
    def __init__(self):
        self.name = ''
        self.version = ''

class Cluster(object):
    ''' class representing cluster object '''
    
    def __init__(self):
        self.name = ''
        self.version = ''
                
    def cross_checks(self):
        ''' verify if entire cluster (all the systems) 
        is on the same software level '''
        pass

if __name__ == '__main__':
    print 'Sys utils simplex run'
    