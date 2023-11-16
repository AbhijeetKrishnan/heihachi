import os,sys

from src.module import character
from src.wavu import parser

sys.path.insert(1, (os.path.dirname(os.path.dirname(__file__))))
base_path = os.path.dirname(__file__)

def import_character(character_meta: dict) -> character.Character:
    name = character_meta["name"]
    wavu_page = character_meta["wavu_page"]
    portrait = character_meta["portrait"]

    move_list = parser.get_character_movelist(name)
    move_list_path = os.path.abspath(os.path.join(base_path,".." ,"json", name+".json"))

    cha = character.Character(name,wavu_page,portrait,move_list,move_list_path)
    return cha