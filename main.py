from lichess_api import Lichess

uname = input("Enter player's username: ")
g_format = input("Input game format (blitz/rapid/classic): ")
L = Lichess(uname, g_format)

rating = L.get_rating()
print(f'{uname} is rated {rating} in {g_format}')
L.get_loss_open()
