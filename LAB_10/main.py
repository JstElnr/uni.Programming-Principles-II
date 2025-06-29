from snake_db import get_or_create_user, get_last_level, save_game_state, close_connection
username = input("name: ")
user_id = get_or_create_user(username)
last_level = get_last_level(user_id)
print(f"begin with level {last_level}")
save_game_state(
    user_id=user_id,
    level=last_level,
    score=150,
    snake_pos=[(5,5), (5,6), (5,7)],
    food_pos=(10,10),
    direction="RIGHT"
)
close_connection()
