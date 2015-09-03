class Main:
    ''' This Main class of Master server is intended for following tasks:
    - Functions for acting on messages received by the listener
    - Passing graph, config informations to slaves
    - Collecting results
    - Receiving heartbeats
    - Allocating initial tasks to slaves
    '''
    def __init__(self):
        pass

    def gotTest(self):
        return "WINTER IS COMING"
