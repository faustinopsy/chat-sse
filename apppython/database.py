import aiomysql
from config import DB_CONFIG

async def insert_message(message: str, user: str):
    async with aiomysql.connect(**DB_CONFIG) as conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO messages (message,user) VALUES (%s)", (message,user))
            await conn.commit()

async def get_new_messages(last_id: int):
    async with aiomysql.connect(**DB_CONFIG) as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute("SELECT id, message, user FROM messages WHERE id > %s ORDER BY id ASC", (last_id,))
            result = await cur.fetchall()
            return result
