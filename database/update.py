from update_tables import update_heroes_table, update_items_table, update_matches_tables

def update():
    print('UPDATING TABLES')
    update_heroes_table()
    update_matches_tables()
    update_items_table()
    print('DONE UPDATING TABLES')

update()