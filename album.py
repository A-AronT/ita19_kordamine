class Album:

    def __init__(self, pealkiri, aasta, laulja):
        self.pealkiri = pealkiri
        self.aasta = aasta
        self.laulja = laulja
        self.laulud = []
    def lisa_laul(self, laul):
        self.laulud.append(laul)