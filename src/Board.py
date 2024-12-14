class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        
        self.gravity = "DOWN"
        self.score = 0
        self.set_gravity() # set gravity
        
    def set_gravity(self, gravity_direciton):
        self.gravity = gravity_direciton
    
    
        
    