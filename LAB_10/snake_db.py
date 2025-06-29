import psycopg2
import json
conn = psycopg2.connect(
    dbname="snake_game",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)
cur = conn.cursor()
def get_or_create_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        print(f"welcome {username}!")
        return user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"user {username} was created")
        return user_id
def get_last_level(user_id):
    cur.execute("""
        SELECT level FROM user_score
        WHERE user_id = %s
        ORDER BY timestamp DESC LIMIT 1
    """, (user_id,))
    row = cur.fetchone()
    return row[0] if row else 1
def save_game_state(user_id, level, score, snake_pos, food_pos, direction):
    cur.execute("""
        INSERT INTO user_score (user_id, level, score, snake_position, food_position, direction)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        user_id,
        level,
        score,
        json.dumps(snake_pos),
        json.dumps(food_pos),
        direction
    ))
    conn.commit()
    print("game saved")
def save_score(user_id, score, level):
    cur.execute(
        "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level)
    )
    conn.commit()
def close_connection():
    cur.close()
    conn.close()
