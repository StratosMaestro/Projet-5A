import unittest
from pendu import choisir_mot, jouer, afficher_pendu
from unittest.mock import patch

class TestPendu(unittest.TestCase):

    def test_choisir_mot(self):
        mot = choisir_mot()
        assert isinstance(mot, str)
        assert len(mot) > 0
        
    def test_afficher_pendu(self):
        with patch('builtins.print') as mocked_print:
            afficher_pendu(0)
            mocked_print.assert_called_once_with("""\n           ------\n           |    |\n           |\n           |\n           |\n           |\n        ---------\n        """)
    
    def test_jouer(self):
    # Mocking the input to test the jouer() method
    with patch('builtins.input', side_effect=['a', 'e', 'i', 'o', 'u', 'x', 'z']), patch('builtins.print') as mocked_print:
        jouer()  # Appelle la méthode jouer()

        # Test if afficher_pendu was called the correct number of times
        self.assertEqual(mocked_print.call_count, 7)  # Adjusted count to match the expected number of loops

        # Check the final print messages to ensure correct game outcome
        expected_calls = [
            "Bienvenue dans le jeu du pendu !",
            "Vous avez 6 chances pour deviner le mot.",
            "Mot à deviner : _ _ _ _ _ _ _ _ _ _",
            "Lettres tentées : a",
            "Raté ! La lettre 'a' n'est pas dans le mot.",
            "Mot à deviner : _ _ _ _ _ _ _ _ _ _",
            "Lettres tentées : a, e",
            "Félicitations ! Vous avez deviné le mot : ...",  # Replace ... with the actual word chosen randomly
        ]
        actual_calls = [call[0][0] for call in mocked_print.call_args_list]
        for call in expected_calls:
            self.assertIn(call, actual_calls)


if __name__ == '__main__':
    unittest.main()
