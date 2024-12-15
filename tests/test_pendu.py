from pendu import choisir_mot

def test_choisir_mot():
    mot = choisir_mot()
    assert isinstance(mot, str)
    assert len(mot) > 0

