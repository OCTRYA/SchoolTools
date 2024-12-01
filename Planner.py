class Planner:

    def __init__(self):
        self.leerkrachten = []
        self.lessen = []
        self.roosterkolommen = 6
        self.roosterrijen = 10
        self.rooster = [[0]*self.roosterkolommen for _ in range(self.roosterrijen)]
        self.initRooster()


    def initRooster(self):
        self.rooster[0][0] = ""
        self.rooster[0][1] = "Maandag"
        self.rooster[0][2] = "Dinsdag"
        self.rooster[0][3] = "Woensdag"
        self.rooster[0][4] = "Donderdag"
        self.rooster[0][5] = "Vrijdag"
        self.rooster[1][0] = "1"
        self.rooster[2][0] = "2"
        self.rooster[3][0] = "3"
        self.rooster[4][0] = "4"
        self.rooster[5][0] = "5"
        self.rooster[6][0] = "6"
        self.rooster[7][0] = "7"
        self.rooster[8][0] = "8"
        self.rooster[9][0] = "9"
        self.rooster[1][1] = 0
        for i in range(10):
            for j in range(6):
                if i > 0 and j > 0:
                    self.rooster[i][j]=0


    def genereerRooster(self, leerkrachtenlijst):
        self.initRooster()
        #zoek alle lessen waar leerkrachtcode overeenkomt.
        for lesItem in self.lessen:
            for leerkrachtenlijstItem in leerkrachtenlijst:
                if(leerkrachtenlijstItem.code == lesItem.leerkrachtcode):
                    for m in lesItem.momenten:
                        self.rooster[m.uur][m.dag] = self.rooster[m.uur][m.dag]+1

        for i in range(10):
            print()
            for j in range(6):
                print(self.rooster[i][j], end ="")
        #
    #def checkBeschikbaarheid(self, datum, teachers):

        # maak lessenrooster van leerkrachten op gekozen datum
        # vergelijk lessenrooster van leerkrachten
