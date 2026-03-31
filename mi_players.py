class Player:
    def __init__(self, jersey_no, name, runs, wickets, team_name):
        self.jersey_no = jersey_no
        self.name = name
        self.runs = runs
        self.wickets = wickets
        self.team_name = team_name

    def display(self):
        print(f"Jersey No: {self.jersey_no}")
        print(f"Name: {self.name}")
        print(f"Runs: {self.runs}")
        print(f"Wickets: {self.wickets}")
        print(f"Team: {self.team_name}")
        print("-" * 20)

# Create MI players
player1 = Player(45, "Rohit", 7878, 23, "MI")
player2 = Player(33, "Jasprit", 2323, 100, "MI")
player3 = Player(30, "Suryakumar", 4545, 120, "MI")
player4 = Player(4, "Hardik", 5656, 130, "MI")
player5 = Player(5, "Ishan", 6767, 135, "MI")
player6 = Player(10, "Kieron", 7575, 140, "MI")
player7 = Player(6, "Krunal", 5454, 135, "MI")
player8 = Player(12, "Rahul", 1313, 145, "MI")
player9 = Player(15, "Tim", 1515, 136, "MI")
player10 = Player(28, "Tilak", 1212, 50, "MI")
player11 = Player(20, "Samuels", 2424, 60, "MI")

# Created team list and append players
mi_team = []
mi_team.append(player1)
mi_team.append(player2)
mi_team.append(player3)
mi_team.append(player4)
mi_team.append(player5)
mi_team.append(player6)
mi_team.append(player7)
mi_team.append(player8)
mi_team.append(player9)
mi_team.append(player10)
mi_team.append(player11)

# Display all players in team
for player in mi_team:
    player.display()