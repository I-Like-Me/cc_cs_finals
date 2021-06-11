import cutscene_database as CSDB
import char_select_menu as CSM
import difficulty_chooser_setter as DCS
import player_builder as PB
import npc_builder as NB
import character_dictionary_database as CDDB
import scene_director as SDIR
import pick_action as PA


print(CSDB.intro_cutscene)
input()

print(CSDB.screen_wipe)
p_char_sel = CSM.select_char()

print(CSDB.screen_wipe)
dif_sel = DCS.select_dif()

current_player = PB.Player(CDDB.characters[p_char_sel.lower()+"n"], CDDB.characters[p_char_sel.lower()+"j"], CDDB.characters[p_char_sel.lower()+"b"], CDDB.characters[p_char_sel.lower()+"m"], CDDB.characters[p_char_sel.lower()+"c"], dif_sel)

n_char_sel = SDIR.scenes[p_char_sel][current_player.win_count]

current_npc = NB.NPC(CDDB.characters[n_char_sel.lower()+"n"], CDDB.characters[n_char_sel.lower()+"j"], CDDB.characters[n_char_sel.lower()+"b"], CDDB.characters[n_char_sel.lower()+"m"], CDDB.characters[n_char_sel.lower()+"c"])

print(current_player)
print(current_player.p_name)
print(current_player.p_job)
print(current_player.p_body)
print(current_player.p_mind)
print(current_player.p_charm)
print(current_player.difficulty)
print("\n")
print(current_npc)
print(current_npc.n_name)
print(current_npc.n_job)
print(current_npc.n_body)
print(current_npc.n_mind)
print(current_npc.n_charm)


print(PA.take_action(current_player.p_body, current_player.p_mind, current_player.p_charm, current_npc.n_body, current_npc.n_mind, current_npc.n_charm))
# for npc in SDIR.scenes[p_char_sel]:
  # print(npc)
  # PA.take_action(current_player.difficulty, current_player.win_count, current_player.loss_count, current_player.p_body, current_player.p_mind, current_player.p_charm, current_npc.n_body, current_npc.n_mind, current_npc.n_charm)
