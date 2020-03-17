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
        global player_name
        global shirt_number
        global player_role
        while self.team_size > 0:
            try:
                player_name = input("Name: ")
                shirt_number = int(input("Shirt Number: "))
                player_role = input("Player Role: ")
            # append all to a list in form of dict
            except ValueError:
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


class MoreAboutFootball(FootballTeam):
    def __init__(self, founded, city):
        super().__init__(founded, city)
        self.tactics = None
        self.formations = None
        self.requirements = None
        self.tactics_info = []

    def __schedule__tactics(self):
        try:
            self.tactics = input("Style of Play: ")
            if self.tactics == "long ball game":
                self.formations = "4-1-4-1"
                self.requirements = ["defensive midfield shield defence",
                                     "wingers to attack",
                                     "striker must be strong"]
                print(self.get_the_tactics())

            elif self.tactics == "counter attack" or "high press":
                self.formations = "4-2-3-1"
                self.requirements = ["defence remain solid or compact",
                                     "spring attacking moves",
                                     "wingers exploit spaces"]
                print(self.get_the_tactics())

            elif self.tactics == "park the bus":
                self.formations = "4-3-2-1"
                self.requirements = ["defence tuck into central areas",
                                     "sole attacker is isolated"]
                print(self.get_the_tactics())

            elif self.tactics == "tikitaka":
                self.formations = "4-1-2-3"
                self.requirements = ["sweeper gk",
                                     "good on the ball",
                                     "passing and movement"]
                print(self.get_the_tactics())
            else:
                print("Wrong Input")

        except Exception as err:
            print(err.args)

    def get_the_tactics(self):
        # access the private method

        self.tactics_info.append(dict(tactics=self.tactics, formation=self.formations,
                                      requirements=self.requirements))
        return self.tactics_info

    def call_the_tactics(self):
        # call the private method here,
        self.__schedule__tactics()


club1 = MoreAboutFootball(1917, "Madrid")
club1.set_president_revenue()
print(club1.get_president_revenue())
club1.diff_sports_type()
print(club1.get_team_info())
club1.get_players()
club1.call_the_tactics()
