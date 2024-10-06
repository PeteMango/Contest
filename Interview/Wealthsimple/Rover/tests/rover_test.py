from ..rover.rover import Rover

def test_rotate():
    r = Rover()
    assert r.facing == 'N'

    r.handle('R')
    assert r.facing == 'E'

    r.handle('R')
    assert r.facing == 'S'

    r.handle('R')
    assert r.facing == 'W'