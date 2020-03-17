# sample program using python class


class SportsClub:
    clubName = "Real Madrid"

    def __init__(self, founded, city):
        # instance variables
        self.city = city
        self.founded = founded
        self.__president = None
        self.__totalRevenue = None

    # set the value
    def set_president_revenue(self):
        self.__president = input("President: ")
        self.__totalRevenue = input("Revnue($): ")

    # get those value
    def get_president_revenue(self):
        return f"{SportsClub.clubName}'s president is" \
               f"{self.__president} and has revenue of {self.__totalRevenue}"

    def diff_sports_type(self):
        games = input("sports: ")
        games = games.split(" ")
        print(f"{SportsClub.clubName} has {len(games)} teams")
        for counter, game in enumerate(games):
            print(f"{counter}: {game}")


class FootballTeam(SportsClub):
    teamName = "Real Madrid CF"
    stadium = "santiago bernabue"

    def __init__(self, founded, city):
        super().__init__(founded, city)
        self.team_size = None
        self.team_manager = None
        self.players_list = []

    # define a private method -1
    def __add_team_info(self):
        self.team_size = int(input("squad size: "))
        self.team_manager = input("manager: ")

    # private method -2
    def __add_players(self):
        while self.team_size > 0:
            player_name = input("Name: ")
            shirt_number = int(input("Shirt Number: "))
            player_role = input("Player Role: ")
            # append all to a list in form dict
            self.players_list.append(dict(playerName=player_name, shirtNumber=shirt_number,
                                          playerRole=player_role))
            self.team_size -= 1

    # access the private method from public methods
    def get_team_info(self):
        # gets private method-1
        self.__add_team_info()
        return f"{self.team_size}, {self.team_manager}"

    def get_players(self):
        # access the private method __add_players
        self.__add_players()
        for each_player in self.players_list:
            for pl_key, pl_value in each_player.items():
                print("\n")
                print(f"{pl_key}: {pl_value}")
                # break


club1 = FootballTeam(1917, "Madrid")
club1.set_president_revenue()
print(club1.get_president_revenue())
club1.diff_sports_type()
print(club1.get_team_info())
club1.get_players()
