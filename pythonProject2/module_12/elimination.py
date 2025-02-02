import networkx as nx

class PlayoffElimination:
    def __init__(self, filename): # initialize and define the data
        self.teams = []
        self.wins = {}
        self.remaining = {}
        self.games = {}
        self.load_data(filename)

    def load_data(self, filename):
        with open(filename, 'r') as file:
            n = int(file.readline().strip()) # the first line the the number of teams
            for _ in range(n):
                line = file.readline().strip().split()
                team = line[0]
                self.teams.append(team)
                self.wins[team] = int(line[1])
                self.remaining[team] = int(line[3])

                # Initialize inner dictionary for the games between teams
                self.games[team] = {}

                # Populate games with remaining game data
                opponents = self.teams[:len(line) - 4]
                for opp, games in zip(opponents, map(int, line[4:])):
                    self.games[team][opp] = games

    def is_trivially_eliminated(self, team):
        max_wins_team = self.wins[team] + self.remaining[team] # maximum winning num
        for other_team in self.teams:
            if other_team != team and self.wins[other_team] > max_wins_team:
                return other_team
        return None

    def build_flow_graph(self, team):
        G = nx.DiGraph() # build a directed graph
        source = 's'
        sink = 't'
        game_nodes = []
        max_possible_wins = self.wins[team] + self.remaining[team] # maximum winning num

        # Add game nodes and edges from source to game nodes
        for i in range(len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                team1, team2 = self.teams[i], self.teams[j]
                if team1 != team and team2 != team:
                    game_node = f'{team1}-{team2}'
                    game_nodes.append(game_node)
                    if team1 in self.games and team2 in self.games[team1]:
                        G.add_edge(source, game_node, capacity=self.games[team1][team2])
                    elif team2 in self.games and team1 in self.games[team2]:
                        G.add_edge(source, game_node, capacity=self.games[team2][team1])
                    else:
                        raise KeyError(f"No remaining games between {team1} and {team2}")

                    G.add_edge(game_node, team1, capacity=float('inf'))
                    G.add_edge(game_node, team2, capacity=float('inf'))

        # Add edges from team nodes to sink
        for other_team in self.teams:
            if other_team != team:
                capacity = max_possible_wins - self.wins[other_team]
                G.add_edge(other_team, sink, capacity=capacity)

        return G, game_nodes

    def is_non_trivially_eliminated(self, team):
        G, game_nodes = self.build_flow_graph(team)
        flow_value, _ = nx.maximum_flow(G, 's', 't')
        total_game_capacity = sum(G['s'][game_node]['capacity'] for game_node in game_nodes)
        return flow_value < total_game_capacity

    def check_elimination(self): # check each team and output the result
        for team in self.teams:
            trivially_eliminated_by = self.is_trivially_eliminated(team)
            if trivially_eliminated_by:
                print(f"{team} has been trivially eliminated by {trivially_eliminated_by}.")
            elif self.is_non_trivially_eliminated(team):
                print(f"{team} is eliminated.")
            else:
                print(f"{team} is not eliminated.")

if __name__ == '__main__':
    playoff = PlayoffElimination('mlb.txt')
    playoff.check_elimination()