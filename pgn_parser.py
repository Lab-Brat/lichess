import re
import pprint

class Parser():
    def __init__(self, pgn):
        # get variable containing games in pgn format
        self.pgn = pgn

        # create an initial dictionary 
        self.pd = {'game1':{}}

        # regular expression patterns
        self.sqr = r'\[(.*?)\]'
        self.qwt = r'\"(.*?)\"'
        self.fsp = r'([^\s]+)'

    def parse(self):
        '''
        read self.pgn variable containing one or more chess games,
        store all the data in the format:

        {game<n>: {game info and moves}, game<n+1>: ...}

        '''
        rc = 0 # row count
        gc = 1 # game count 

        for row in (self.pgn.split('\n')):
            if row != '' and rc!=3:
                param = re.findall(self.sqr, row)
                if param != []:
                    feature = re.findall(self.fsp, param[0])[0]
                    info = re.findall(self.qwt, param[0])[0]
                elif param == []:
                    feature = 'moves'
                    info = row
            elif row == '':
                rc += 1
            elif rc == 3:
                gc += 1
                self.pd[f'game{gc}'] = {}
                rc = 0
            self.pd[f'game{gc}'][f'{feature}'] = info
        
        return self.pd


if __name__ == "__main__":
    pass

