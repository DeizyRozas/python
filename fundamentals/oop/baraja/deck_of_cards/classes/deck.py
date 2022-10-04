from . import card

class Baraja:


    def __init__( self ):
        pinta = [ "pica" , "corazon" , "trebol" , "diamante" ]
        self.cards = []

        for s in pinta:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "As"
                elif i == 11:
                    str_val = "Jota"
                elif i == 12:
                    str_val = "Quina"
                elif i == 13:
                    str_val = "Kayser"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

