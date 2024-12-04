import unittest
from unittest.mock import patch
from source.janken_main import main

class TestJankenMain(unittest.TestCase):
    @patch('computer.computer_pon', return_value='チョキ')
    @patch('player.player_pon', return_value='グー')
    def test_play_round_player_win(self, mock_player, mock_computer):
        player_win, computer_win, round_complete = main()
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 0)
        self.assertTrue(round_complete)

    @patch('computer.computer_pon', return_value='グー')
    @patch('player.player_pon', return_value='グー')
    def test_play_round_draw(self, mock_player, mock_computer):
        player_win, computer_win, round_complete = main()
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 0)
        self.assertFalse(round_complete)

if __name__ == '__main__':
    unittest.main()
