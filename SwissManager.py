from tkinter import *
from math import log


class Application:
    def __init__(self):
        self.root = Tk()
        self.root.title("Swiss Manager")
        self.root.geometry("660x394")
        self.root.resizable(0, 0)
        self.root.configure(bg="Lavender")
        self.frame = Frame(self.root, bg="Lavender")
        self.frame.grid()
        self.hraci = []
        self.hraciKteriSpoluHrali = []
        self.nazevTournamentu = "tournament.txt"
        self.counterID = 1000
        self.homeScreen()
        self.root.mainloop()

# home screen
    def homeScreen(self):
        self.root.title("Swiss Manager")
        self.root.geometry("660x394")
        self.root.resizable(0, 0)
        self.nazevTournamentu = "tournament.txt"
        self.menuHome()
        for widget in self.frame.winfo_children():
            widget.destroy()
        _ = Label(
            self.frame,
            text="Welcome to Manager",
            fg="Black",
            bg="Lavender",
            font=("Arial Bold", 50)
        ).grid(row=0, column=0, ipadx=65, ipady=20)
        _ = Button(
            self.frame,
            text="New Tournament",
            bg="Lavender",
            fg="Deep sky blue",
            font=("Arial Bold", 30),
            command=self.newTournamentPreparation
        ).grid(row=1, column=0, ipadx=30, ipady=15)
        _ = Label(self.frame, bg="Lavender").grid(row=2, column=0)
        _ = Button(
            self.frame,
            text="Load Tournament",
            bg="Lavender",
            fg="Deep sky blue",
            font=("Arial Bold", 30),
            command=self.loadPreparation
        ).grid(row=3, column=0, ipadx=25, ipady=15)
        _ = Label(self.frame, bg="Lavender").grid(row=4, column=0)
        _ = Button(
            self.frame,
            text="Quit",
            bg="Lavender",
            fg="Red",
            font=("Arial Bold", 30),
            command=self.end
        ).grid(row=5, column=0, ipadx=20, ipady=15)

# tournament
    def newTournamentPreparation(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        _ = Label(
            self.frame,
            text="Enter Name of the Tournament: ",
            fg="Deep sky blue",
            bg="Lavender",
            font=("Arial Bold", 30)
        ).grid(row=0, column=0, ipadx=90, ipady=30)
        entry = Entry(self.frame, font=("Arial Bold", 20))
        entry.grid(row=1, column=0, ipadx=0, ipady=10)
        _ = Label(self.frame, bg="Lavender").grid(row=3, column=0)
        _ = Button(
            self.frame,
            text="Confirm",
            fg="Red",
            font=("Arial Bold", 30),
            command=lambda: self.newTournamentPreparation2(entry.get())
        ).grid(row=4, column=0, ipadx=20, ipady=10)

    def newTournamentPreparation2(self, name):
        file = open(name, "w+")
        file.close()
        self.counterID = 1000
        self.hraci = []
        self.hraciKteriSpoluHrali = []
        self.nazevTournamentu = name
        self.tournament()

    def tournament(self):
        self.root.geometry("660x394")
        self.root.title(self.nazevTournamentu)
        self.root.resizable(0, 0)
        self.menuTournament()
        for widget in self.frame.winfo_children():
            widget.destroy()
        _ = Label(self.frame, bg="Lavender").grid(row=0, column=0, rowspan=20, ipadx=15)
        scrollbar = Scrollbar(self.frame)
        scrollbar.grid(row=0, column=1, rowspan=20)
        self.list = Listbox(self.frame, yscrollcommand=scrollbar.set, width=25, height=23)
        self.list.grid(row=0, column=1, rowspan=20)
        for hrac in self.hraci:
            self.list.insert(END, " "+str(hrac.score)+" - "+str(hrac.jmeno)+"   ("+str(hrac.idHrace)+")")
        _ = Label(self.frame, bg="Lavender").grid(row=0, column=2, rowspan=20, ipadx=30)
        _ = Button(
            self.frame,
            text="Next Round",
            bg="Lavender",
            fg="Deep sky blue",
            font=("Arial Bold", 20),
            command=self.nextRound
        ).grid(row=0, column=3, ipadx=50, ipady=10, columnspan=2)
        _ = Button(
            self.frame,
            text="Add Players",
            bg="Lavender",
            fg="Deep sky blue",
            font=("Arial Bold", 17),
            command=self.pridatHracu
        ).grid(row=1, column=3, ipadx=15, ipady=10)
        _ = Button(
            self.frame,
            text="Delete Player",
            bg="Lavender",
            fg="Red",
            font=("Arial Bold", 17),
            command=self.deletePlayer
        ).grid(row=1, column=4, ipadx=15, ipady=10)
        _ = Button(
            self.frame,
            text="End Rounds",
            bg="Lavender",
            fg="Green",
            font=("Arial Bold", 17),
            command=self.endRounds
        ).grid(row=2, column=3, ipadx=10, ipady=10, columnspan=2)
        _ = Button(
            self.frame,
            text="Save & Quit",
            bg="Lavender",
            fg="Red",
            font=("Arial Bold", 17),
            command=lambda: self.saveTournament(True)
        ).grid(row=3, column=3, ipadx=10, ipady=10, columnspan=2)

# data manage methods
    def loadPreparation(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        _ = Label(
            self.frame,
            text="Enter Name of the Tournament: ",
            fg="Deep sky blue",
            bg="Lavender",
            font=("Arial Bold", 30)
        ).grid(row=0, column=0, ipadx=90, ipady=30)
        entry = Entry(self.frame, font=("Arial Bold", 20))
        entry.grid(row=1, column=0, ipadx=0, ipady=10)
        _ = Label(self.frame, bg="Lavender").grid(row=3, column=0)
        _ = Button(
            self.frame,
            text="Confirm",
            fg="Red",
            font=("Arial Bold", 30),
            command=lambda: self.loadTournament(entry.get())
        ).grid(row=4, column=0, ipadx=20, ipady=10)

    def loadTournament(self, name):
        self.nazevTournamentu = name
        self.hraci = []
        self.hraciKteriSpoluHrali = []
        file = open(self.nazevTournamentu, "r")
        oddeleni = 0
        if file.readline(10) == "":
            self.counterID = 1000
        for line in file:
            if "-----" in line:
                oddeleni += 1
            else:
                if oddeleni == 1:
                    self.counterID = int(line)
                elif oddeleni == 2:
                    indexID = line.index(";")
                    indexScore = line.index("&")
                    jmeno = line[:indexID]
                    idHrace = int(line[indexID + 1:indexScore])
                    score = int(line[indexScore + 1:])
                    hrac = self.Hrac(jmeno, idHrace, score)
                    self.hraci.append(hrac)
                elif oddeleni == 3:
                    '''indexJmena = line.index("#")
                    indexID1 = line.index(";")
                    indexID2 = line.index("@")
                    indexScore1 = line.index("&")
                    indexScore2 = line.index("*")
                    hrac1Jmeno = line[:indexID1]
                    hrac1ID = int(line[indexID1+1:indexScore1])
                    hrac1Score = int(line[indexScore1+1:indexJmena])
                    hrac2Jmeno = line[indexJmena+1:indexScore2]
                    hrac2ID = int(line[indexID2 + 1:indexScore2])
                    hrac2Score = int(line[indexScore2+1:])
                    self.hraciKteriSpoluHrali.append([self.Hrac(hrac1Jmeno, hrac1ID, hrac1Score), self.Hrac(hrac2Jmeno, hrac2ID, hrac2Score)])'''
        file.close()
        self.tournament()

    def saveTournament(self, konec):
        file = open(self.nazevTournamentu, "w+")
        file.write("")
        file.close()
        file = open(self.nazevTournamentu, "a")
        file.write("\n" + "-----")
        file.write("\n" + str(self.counterID))
        file.write("\n" + "-----")
        for hrac in self.hraci:
            radek = hrac.jmeno + ";" + str(hrac.idHrace) + "&" + str(hrac.score)
            file.write("\n" + radek)
        file.write("\n" + "-----")
        '''for dvojice in self.hraciKteriSpoluHrali:
            radek = dvojice[0].jmeno + ";" +str(dvojice[0].idHrace) + "&" + str(dvojice[0].score) + "#" + dvojice[1].jmeno + "@"  + str(dvojice[1].idHrace) + "*" + str(dvojice[1].score)
            file.write("\n" + radek)'''
        file.close()
        if konec:
            self.end()

# add and delete players
    def pridatHracu(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        _ = Button(
            self.frame,
            text="Add player: ",
            fg="Deep sky blue",
            font=("Arial Bold", 15),
            command=self.pridaniVstupuProHrace
        ).grid(row=0, column=0, ipadx=5, ipady=5)
        _ = Button(
            self.frame,
            text="Confirm",
            fg="Red",
            font=("Arial Bold", 15),
            command=self.vytvoreniHracuZeJmen
        ).grid(row=1, column=0, ipadx=5, ipady=5)
        self.rowProVstup = 0
        self.columnProVstup = 1
        self.pocetHracu = 1

    def pridaniVstupuProHrace(self):
        if self.pocetHracu < 21:
            _ = Label(
                self.frame,
                text="Player #" + str(self.pocetHracu),
                fg="Blue",
                bg="Lavender",
                font=("Arial Bold", 15)
            ).grid(row=self.rowProVstup, column=self.columnProVstup, ipadx=0, ipady=5)
            _ = Entry(
                self.frame
            ).grid(row=self.rowProVstup, column=self.columnProVstup+1, ipadx=0, ipady=5)

        self.rowProVstup += 1
        if self.pocetHracu == 10:
            self.columnProVstup += 2
            self.rowProVstup = 0
        self.pocetHracu += 1

    def vytvoreniHracuZeJmen(self):
        for widget in self.frame.winfo_children():
            if widget.winfo_class() == "Entry":
                jmeno = widget.get()
                if jmeno != "":
                    hrac = self.Hrac(jmeno, self.counterID, 0)
                    self.hraci.append(hrac)
                    self.counterID += 1
            widget.destroy()
        self.tournament()

    def deletePlayer(self):
        if len(self.hraci) > 0 and self.list.curselection() != ():
            selectedLine = self.list.curselection()
            allIdes = []
            for line in self.list.get(0, len(self.hraci)):
                allIdes.append(line[-5:-1])
            for hrac in self.hraci:
                if hrac.idHrace == int(allIdes[selectedLine[0]]):
                    self.hraci.remove(hrac)
            self.tournament()

# rounds
    def nextRound(self):
        self.pripravitHraceNaKolo()
        if len(self.hraci) % 2 == 0 and len(self.hraci) != 0:
            for widget in self.frame.winfo_children():
                widget.destroy()
            self.root.resizable(300, 0)
            _ = Button(
                self.frame,
                text="Confirm Results",
                fg="Deep sky blue",
                font=("Arial Bold", 15),
                command=self.calculteRound
            ).grid(row=0, column=0, ipadx=5, ipady=2)
            for i in range(int(len(self.hraci) / 2)):
                prvni = self.hraci[i * 2].jmeno
                druhy = self.hraci[i * 2 + 1].jmeno
                boolJestliDvojice = False
                if self.hraciKteriSpoluHrali != []:
                    for j in self.hraciKteriSpoluHrali:
                        if j == [self.hraci[i * 2], self.hraci[i * 2 + 1]]:
                            boolJestliDvojice = True
                if boolJestliDvojice == False:
                    self.hraciKteriSpoluHrali.append([self.hraci[i * 2], self.hraci[i * 2 + 1]])
                _ = Label(
                    self.frame,
                    text=prvni + " / vs / " + druhy,
                    fg="Blue",
                    bg="Lavender",
                    font=("Arial Bold", 15),
                ).grid(row=i, column=1)
                _ = Entry(self.frame).grid(row=i, column=2)
                #print(self.hraciKteriSpoluHrali)

    def calculteRound(self):
        bodyKPridani = []
        for widget in self.frame.winfo_children():
            if widget.winfo_class() == 'Entry':
                zapsaneScore = widget.get()
                if zapsaneScore != "":
                    body = zapsaneScore[0]
                    bodyKPridani.append(int(body))
                    body = zapsaneScore[2]
                    bodyKPridani.append(int(body))
            widget.destroy()
        if len(bodyKPridani) > 0:
            counterProPridaniBodu = 0
            for hrac in self.hraci:
                hrac.score += bodyKPridani[counterProPridaniBodu]
                counterProPridaniBodu += 1
        self.seraditHracePodleScore()
        self.tournament()

# ending tournament
    def endRounds(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        _ = Label(
            self.frame,
            text="Enter number, where n=2^k : ",
            fg="Deep sky blue",
            bg="Lavender",
            font=("Arial Bold", 20)
        ).grid(row=0, column=0, ipadx=200, ipady=30)
        entry = Entry(self.frame, font=("Arial Bold", 20))
        entry.grid(row=1, column=0, ipadx=0, ipady=10)
        _ = Label(self.frame, bg="Lavender").grid(row=3, column=0)
        _ = Button(
            self.frame,
            text="Confirm",
            fg="Red",
            font=("Arial Bold", 30),
            command=lambda: self.pavouk(int(entry.get()))
        ).grid(row=4, column=0, ipadx=20, ipady=10)

    def pavouk(self, pocetDoFinale):
        self.root.resizable(100000, 100000)
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.hraciVeFinale = []
        for i in range(pocetDoFinale):
            self.hraciVeFinale.append(self.hraci[i])
        pocetDvojic = int(pocetDoFinale / 2)
        pocetKol = log(pocetDoFinale, 2) + 1
        for i in range(int(pocetKol)):
            posuvnik = int(2 ** i - 1)
            if i == 0:
                for j in range(pocetDvojic):
                    label1 = Label(self.frame, text=self.hraciVeFinale[j].jmeno).grid(row=posuvnik, column=0)
                    label2 = Label(self.frame, text=self.hraciVeFinale[(j + 1) * -1].jmeno).grid(row=posuvnik + 2,column=0)
                    labelX = Label(self.frame, text="x", fg="Red", bg="Lavender").grid(row=posuvnik + 1, column=0)
                    posuvnik += 4
            elif i == int(pocetKol - 1):
                entry = Entry(self.frame)
                entry.grid(row=posuvnik, column=i)
            else:
                pocetDvojic = int(pocetDvojic / 2)
                for _ in range(int(pocetDvojic)):
                    entry1 = Entry(self.frame).grid(row=posuvnik, column=i)
                    entry2 = Entry(self.frame).grid(row=posuvnik + 2 ** (i + 1), column=i)
                    label = Label(self.frame, text="x", fg="Red", bg="Lavender").grid(
                        row=int(posuvnik + 2 ** (i + 1) / 2), column=i)
                    posuvnik += (2 ** (i + 1)) * 2

# sorting players methods
    def seraditHracePodleScore(self):
        self.hraci = sorted(self.hraci, key=lambda hrac: hrac.score, reverse=True)

    def pripravitHraceNaKolo(self):
        '''if self.hraciKteriSpoluHrali != []:
            for dvojice in self.hraciKteriSpoluHrali:
                counter = 0
                for _ in range(int(len(self.hraci) / 2)):
                    try:
                        if dvojice == [self.hraci[counter], self.hraci[counter+1]]:
                            index1 = self.hraci.index(self.hraci[counter + 1])
                            index2 = self.hraci.index(self.hraci[counter + 2])
                            self.hraci[index1], self.hraci[index2] = self.hraci[counter + 1], self.hraci[counter + 2]
                        counter += 2
                    except IndexError:
                        pass'''
        pass

# menus
    def menuHome(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenuManager = Menu(self.menu)
        self.menu.add_cascade(label="Manager", menu=self.submenuManager)
        self.submenuManager.add_command(label="Home", command=self.homeScreen)
        self.submenuManager.add_separator()
        self.submenuManager.add_command(label="Quit", command=self.end)

    def menuTournament(self):
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenuManager = Menu(self.menu)
        self.menu.add_cascade(label="Manager", menu=self.submenuManager)
        self.submenuManager.add_command(label="Home", command=self.homeScreen)
        self.submenuManager.add_separator()
        self.submenuManager.add_command(label="Quit", command=self.end)

        self.submenuFile = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.submenuFile)
        self.submenuFile.add_command(label="New Tournament", command=self.newTournamentPreparation)
        self.submenuFile.add_separator()
        self.submenuFile.add_command(label="Save", command=lambda: self.saveTournament(False))
        self.submenuFile.add_command(label="Load", command=self.loadPreparation)

# other
    def end(self):
        self.root.destroy()

    class Hrac:
        def __init__(self, jmeno, idHrace, score):
            self.jmeno = jmeno
            self.score = score
            self.idHrace = idHrace


if __name__ == "__main__":
    app = Application()
