from app.modules.pages import schema
from app.modules.core.firebase_connection import FirebaseConnection


class GetPageContentUseCase:
    def __init__(self, payload: schema.GetPageSchema):
        self.__payload = payload
        self.__firebase_connection = FirebaseConnection()

    async def execute(self):
        return await self.__firebase_connection.get_content_page(self.__payload.name)
