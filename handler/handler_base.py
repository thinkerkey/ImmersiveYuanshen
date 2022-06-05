from pyjoycon import JoyCon, get_R_id, get_L_id

joycon_id = get_R_id()
print(joycon_id)
joycon = JoyCon(*joycon_id)

print(joycon.get_status())