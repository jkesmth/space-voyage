import pygame

    
class EventManager:
    """handles posting events to listeners"""
    
    def __init__(self):
        self.listeners = {}
               
    def register_listener(self, listener):
        self.listeners[listener] = 1

    def unregister_listener(self, listener):
        if listener in self.listeners:
            del self.listeners[listener]

    def post(self, events):
        for listener in self.listeners.keys():
            listener.notify(events)


class GameView:

    def __init__(self):
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((500, 500))



        
        pygame.display.update()

    def notify(self, event):
        
        #once we have sprites we will draw them here

        pygame.display.update()

        if event.type == pygameQUIT: 
            pygame.display.quit()
    
class GameLoop:

    def __init__(self):

        self.running = False
        self.manager = EventManager()
        self.manager.register_listener(self)

        self.display = GameView()
        self.manager.register_listener(self.display)
        
        self.run()

    def run(self):

        self.running = True
        while self.running:
            
            for event in pygame.event.get():          
                self.manager.post(events)
             
    def notify(self, event):
        
        if event.type == pygame.QUIT:
            self.running = False
            

def main():
    main_loop = GameLoop()
    main_loop.run()


main()
