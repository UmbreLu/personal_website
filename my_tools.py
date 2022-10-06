from datetime import date, timedelta
from sqlite_ops import Operator

class Analytics:


    def __init__(self, db_file):
        self.unique_useragents = set()
        self.today = date.today()
        self.accesses = {
            'greeting': 0,
            'home': 0,
            'bio': 0,
            'contato': 0,
            'jobs': 0,
            'resume': 0
        }
        self.db = Operator(db_file)

    def analyse(self, request):
        if request.url_root != 'https://lucaspinto.dev.br/':
        #if request.url_root != 'http://localhost:5000/':
            #print(request.url_root)
            return
        #print('keeping analyse')
        today = date.today()
        if today != self.today:
            self.save_stats()
        self.accesses[request.endpoint] += 1
        self.unique_useragents.add(str(request.user_agent))

    def save_stats(self):
        try:
            #print('trying to save stats')
            self.db.exe(
                'INSERT INTO daily VALUES (?, ?, ?, ?, ?, ?, ?, ?);',
                str(self.today),
                len(self.unique_useragents),
                *self.accesses.values()
            )
        except exception as err:
            #print('exception block')
            with open('error_log.txt', 'w+') as log:
                log.write(str(err))
        finally:
            #print('finally block')
            self.today = date.today()
            self.unique_useragents = set()
            for key in self.accesses.keys():
                self.accesses[key] = 0

    def analytics(self):
        try:
            return self.db.query('SELECT rowid, * FROM daily', option='all')
        except exception as err:
            return err

    def current(self):
        return self.accesses

    def test(self, _date):
        self.today = date.fromisoformat(_date)
        print(self.db.query('SELECT rowid, * FROM daily;', option='all'))
        print(self.unique_useragents)
        print(self.accesses)
