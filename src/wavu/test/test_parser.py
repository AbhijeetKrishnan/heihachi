import unittest, json
from src.wavu import parser

class MyTestCase(unittest.TestCase):

    def test_convert_html_move_to_json(self):
        character_movelist = parser.get_character_movelist("Azucena")
        self.assertEqual(character_movelist[44].input,"BT.3")


    def test_get_move(self):
        character_movelist = parser.get_character_movelist("Azucena")
        move = parser.get_move("Azucena-df+1,4",character_movelist)
        self.assertEqual(move.id,"Azucena-df+1,4")

    def test_complete_parent_input(self):
        character_movelist = parser.get_character_movelist("Azucena")
        move = parser.get_move("Azucena-df+1,4,1",character_movelist)
        move2 = parser.get_move("Azucena-f+4,4~3",character_movelist)
        move3 = parser.get_move("Azucena-LIB.1,2",character_movelist)
        move4 = parser.get_move("Azucena-b+4,3,4,3",character_movelist)
        move5 = parser.get_move("Azucena-df+1,4,1~2",character_movelist)
        self.assertEqual(move.input,"df+1,4,1")
        self.assertEqual(move2.input,"f+4,4~3")
        self.assertEqual(move3.damage,"14,20")
        self.assertEqual(move4.damage,"10,10,16,23")
        self.assertEqual(move5.input,"df+1,4,1~2")


