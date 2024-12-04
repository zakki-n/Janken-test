import unittest
from unittest.mock import patch
from source.janken_judge import judge


class TestJankenGame(unittest.TestCase):

    @patch('player.player_pon', return_value='グー')  
    @patch('computer.computer_pon', return_value='チョキ')  
    def test_judge_player_win(self, mock_computer, mock_player):
    
        result = judge('チョキ', 'グー')  
        self.assertEqual(result, 'player_win')

    @patch('player.player_pon', return_value='グー')
    @patch('computer.computer_pon', return_value='グー')
    def test_judge_draw(self, mock_computer, mock_player):

        result = judge('グー', 'グー')  
        self.assertEqual(result, 'draw')

    @patch('player.player_pon', return_value='パー')
    @patch('computer.computer_pon', return_value='グー')
    def test_judge_computer_win(self, mock_computer, mock_player):
        
        result = judge('グー', 'パー')  
        self.assertEqual(result, 'computer_win')

    @patch('builtins.print')  
    def test_display_result(self, mock_print):
        
        result = judge('グー', 'チョキ')
        self.assertEqual(result, 'player_win')
        mock_print.assert_any_call("あなたの勝ち！")

if __name__ == '__main__':
    unittest.main()
