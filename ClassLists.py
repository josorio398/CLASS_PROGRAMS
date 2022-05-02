class list_upload:

    def __init__(self,url):
        self.url = url
        global URL
        URL =self.url

    @property
    def show(self):
        df = pd.read_csv(URL)
        return df
    
    @property
    def welcome(self):
        df = self.show
        col = df["nombres"]
        for nombre in col:
            print("BIENVENIDO AL CURSO"+" "+ nombre.upper())

    @property
    def winner(self):
        df = self.show
        col = df["nombres"]
        ganador = random.choice(col)
        return ganador
