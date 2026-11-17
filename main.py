import asyncio

from aiogram import Bot, Dispatcher
from handler import setup_message_routers

API_TOKEN = "8863818964:AAF_JtDJ2k3TiINhZbznf19N_4o3vRlyxVU"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def main():
    handler_router = setup_message_routers()
    dp.include_router(handler_router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
