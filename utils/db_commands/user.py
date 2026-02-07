from core.model import users
from core.database_settings import database


async def add_user(data: dict) -> dict | None:
    try:
        # Age ni int ga o'tkazish, agar xato bo'lsa None qaytaradi
        age = data.get("age")
        if age is not None:
            try:
                age = int(age)
            except (ValueError, TypeError):
                print(f"Error: Invalid age value: {age}")
                return None
        
        query = users.insert().values(
            full_name=data.get("full_name"),
            phone_number=data.get("phone_number"),
            chat_id=data.get("chat_id"),
            language=data.get("language"),
            created_at=data.get("created_at"),
            age=age,
            updated_at=None
        )
        new_user = await database.execute(query=query)
        return new_user
    except Exception as e:
        error_text = f"Error appeared when adding user: {e}"
        print(error_text)
        return None