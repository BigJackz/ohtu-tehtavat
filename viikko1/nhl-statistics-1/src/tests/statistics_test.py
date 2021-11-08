import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Jones", "AAA", 4, 12),
            Player("Jonne", "GGE", 20, 21),
            Player("Disaster", "TSG", 1, 2),
            Player("Minister", "AAA", 121, 1),
            Player("Keke", "GGE", 56, 27)
            ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_finds_the_right_player(self):
        player = self.statistics.search("Minister")
        players_points = player.points

        self.assertEqual(players_points, 122)
    
    def test_search_returns_nothing_if_player_doesnt_exist(self):
        player = self.statistics.search("Homer")
        
        self.assertEqual(player, None)

    def test_team_returns_all_team_members(self):
        players = self.statistics.team("AAA")

        info = ""
        for player in players:
            info = info + str(player)
        
        self.assertEqual(info, "Jones AAA 4 + 12 = 16Minister AAA 121 + 1 = 122")

    def test_top_scorers_returns_top_scoring_players(self):
        players = self.statistics.top_scorers(2)

        info = ""
        for player in players:
            info = info + str(player)
        
        self.assertEqual(info, "Minister AAA 121 + 1 = 122Keke GGE 56 + 27 = 83Jonne GGE 20 + 21 = 41")
