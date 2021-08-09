from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
import asyncio


class TelethonBot():
    async def baslat(self):
        
        await self.client.connect()
 
    def __init__(self, api_id: int, api_hash: str) -> None:
        self.client = TelegramClient(
            None, api_id, api_hash
        )
        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.baslat())

 
    async def get_user_info(self, username: str) -> str:
        user = await self.client(GetFullUserRequest(username))
        info =  {
            "firstname": user.user.first_name,
            "pp_path": await self.client.download_profile_photo(username, file="static"),
            "bio": user.about
        }

        info['pp_path'] = info['pp_path'].replace("\\", "/")

        return info
