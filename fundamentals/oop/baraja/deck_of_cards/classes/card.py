class Card:

    def __init__( self , pinta , point_val , string_val ):
        
        self.pinta = pinta
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.pinta} : {self.point_val} points")