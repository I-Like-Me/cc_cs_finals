import cutscene_database as CSDB
import char_select_menu as CSM

print(CSDB.intro_cutscene)
input()
print(CSDB.screen_wipe)
character_selection = CSM.select_char()
print(character_selection)