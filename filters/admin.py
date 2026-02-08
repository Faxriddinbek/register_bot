from aiogram.filters import Filter
from aiogram.types import Message


ADMINS = [5799795856]

#admin ekanligini tekshiradi
class IsAdmin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in ADMINS
