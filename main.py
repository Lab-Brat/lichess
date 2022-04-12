from lichess_api import Lichess

uname = input("Enter player's username: ")
g_format = input("Input game format (blitz/rapid/classic): ")
g_num = input("How many games to search: ")
L = Lichess(uname, g_format, int(g_num))

rating = L.get_rating()
print(f'{uname} is rated {rating} in {g_format}')
L.get_stat()

