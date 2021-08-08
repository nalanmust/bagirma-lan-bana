from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest


class TelethonBot():
    def __init__(self, api_id: int, api_hash: str) -> None:
        self.client = TelegramClient(
            r'hkeybot', api_id, api_hash
        )
        await self.client.connect()


    async def get_user_info(self, username: str) -> str:
        user = await self.client(GetFullUserRequest(username))
        info =  {
            "firstname": user.user.first_name,
            "pp_path": await self.client.download_profile_photo(username, file="static"),
            "bio": user.about
        }

        info['pp_path'] = info['pp_path'].replace("\\", "/")

        return info
