import re
import pprint
import requests
import lichess.api
from collections import Counter
from pgn_parser import Parser

class Lichess():
    def __init__(self, username, g_format, g_num):
        self.username = username
        self.g_format = g_format
        self.user = lichess.api.user(self.username)
        self.p_num = g_num
        self.pgn_url = f'https://lichess.org/api/games/user/{username}'
        self.pgn_dict = self.parse()

    def get_rating(self):
        '''
        get user rating
        '''
        rt = self.user['perfs'][self.g_format]['rating']
        return rt

    def get_pgn(self):
        '''
        get user games in pgn file and read it
        '''
        pgn = requests.get(self.pgn_url, \
                           params={'max':self.p_num,  \
                                   'opening':'true', \
                                   'perfType': self.g_format})
        #self.dwn_pgn(pgn)
        return pgn.content.decode('utf-8')

    def dwn_pgn(self, pgn):
        '''
        download the pgn file
        '''
        file = open(f'{self.username}_games.pgn', 'wb')
        file.write(pgn.content)
        file.close()

    def parse(self):
        '''
        user pgn_parser to parse the pgn output
        '''
        pgn = self.get_pgn()
        return Parser(pgn).parse()

    def get_side(self, game):
        '''
        check which side the player is playing on
        '''
        game_dict = self.pgn_dict[f'game{game}']
        white = game_dict['White']
        black = game_dict['Black']
        
        if black == self.username:
            side = 'black'
        elif white == self.username:
            side = 'white'

        return side

    def get_result(self, game):
        '''
        check the result of the game: won, lost or draw
        '''
        game_dict = self.pgn_dict[f'game{game}']
        result = game_dict['Result']
        side = self.get_side(game)

        if side == 'white':
            if result == '1-0': side_result = 'won'
            elif result == '0-1': side_result = 'lost'
            else: side_result = 'draw'
        elif side == 'black':
            if result == '1-0': side_result = 'lost'
            elif result == '0-1': side_result = 'won'
            else: side_result = 'draw'
        else:
            print('what side ARE you on!?')
        
        return side_result


    def get_loss_open(self):
        '''
        get and print out game statistics
        '''
        before_colon = r'([^\:]+)'
        w_openings = []
        b_openings = []
        for game in range(1, self.p_num+1):
            if self.get_result(game) == 'lost' and self.get_side(game)=='white':
                opening = self.pgn_dict[f'game{game}']['Opening']
                w_openings.append(re.findall(before_colon, opening)[0])
            elif self.get_result(game) == 'lost' and self.get_side(game)=='black':
                opening = self.pgn_dict[f'game{game}']['Opening']
                b_openings.append(re.findall(before_colon, opening)[0])
        
        wco = Counter(w_openings)
        bco = Counter(b_openings)
        print("\n[some statistics on lost games as white]")
        [print(i, wco[i]) for i in wco]
        print("\n[some statistics on lost games as black]")
        [print(i, bco[i]) for i in bco]
        print("\n")


if __name__ == '__main__':
    uname = 'LabBrat'
    g_format = 'blitz'
    g_num = 2
    L = Lichess(uname, g_format, g_num)

