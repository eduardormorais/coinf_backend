import base64
import io
from app.modules.core.firebase_connection import FirebaseConnection
from starlette.responses import StreamingResponse
from app.modules.images import schema
from fastapi import HTTPException, status


class GetImageUseCase:
    def __init__(self, payload: schema.GetImageSchema):
        self.__payload = payload
        self.__firebase_connection = FirebaseConnection()

    async def execute(self):
        img = await self.__firebase_connection.find_image_by_uuid(self.__payload.uuid)
        if not img:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Image not found."
            )
        file = await self.__firebase_connection.find_image_object_by_path(
            img["imgPath"]
        )
        str_file = file.download_as_string()
        image_bytes_io = io.BytesIO(base64.b64decode(base64.b64encode(str_file)))
        return StreamingResponse(image_bytes_io, media_type="image/png")


class GetFolderImagesInfo:
    def __init__(self, payload: schema.GetFolderImageInfoSchema):
        self.__payload = payload
        self.__firebase_connection = FirebaseConnection()

    async def execute(self):
        images_info = await self.__firebase_connection.find_image_by_folder_path(
            self.__payload.id, self.__payload.folder
        )
        if len(images_info) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Images info not found for this folder.",
            )
        return images_info
