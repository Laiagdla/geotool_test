from geotool_test.lib import geotranslator, map_drawer

adress = 'an der filmfabrik'

def test_geotranslator():
    assert len(geotranslator(adress)) == 2

def test_map_drawer():
    assert type(map_drawer(geotranslator(adress))).__name__ == 'Map'
