from aiogram import Router, F
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from filters.admin import IsAdmin

router = Router()

@router.message(F.text == "⚙️ Settings", IsAdmin())# IsAdmin() bu filterlaydi
async def settings_handler(message: Message):
    text = "Setting is working"
    await message.answer(text=text)

class FileStates(StatesGroup):
    waiting_for_file = State()

@router.message(Command("file"))
async def get_file_id(message: Message, state: FSMContext):
    text = "Fileni kiriting"
    await message.answer(text)
    await state.set_state(FileStates.waiting_for_file)


@router.message(FileStates.waiting_for_file, F.content_type == ContentType.PHOTO)
async def sent_file_id(message: Message):
    text = message.photo[-1].file_id
    await message.answer(text)