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
            mocked_print.assert_called_once_with("""
            ------
               |    |
               |
               |
               |
               |
            ---------
            """)
    
    def test_jouer(self):
        # Mocking the input to test the jouer() method
        with patch('builtins.input', side_effect=['a', 'b', 'c', 'd', 'e', 'f', 'g']), patch('builtins.print') as mocked_print:
            jouer()  # Appelle la méthode jouer()
            
            # Test if afficher_pendu was called the correct number of times
            self.assertEqual(mocked_print.call_count, 8)  # 7 appels à afficher_pendu() pour chaque tour, plus 1 pour la fin
            
            # Test the final print messages to ensure correct game outcome
            expected_calls = [
                "Bienvenue dans le jeu du pendu !",
                "Vous avez 6 chances pour deviner le mot.",
                "Mot à deviner : _ _ _ _ _ _ _ _ _ _",
                "Lettres tentées : a",
                "Raté ! La lettre 'a' n'est pas dans le mot.",
                "Mot à deviner : _ _ _ _ _ _ _ _ _ _",
                "Lettres tentées : a, b",
                "Raté ! La lettre 'b' n'est pas dans le mot.",
                # Vous devez ajouter les autres appels à mocked_print pour chaque lettre entré
                "Dommage ! Vous avez perdu. Le mot était : ..."  # Remplace ... par le mot choisi aléatoirement
            ]
            actual_calls = [call[0][0] for call in mocked_print.call_args_list]
            for call in expected_calls:
                self.assertIn(call, actual_calls)

if __name__ == '__main__':
    unittest.main()
