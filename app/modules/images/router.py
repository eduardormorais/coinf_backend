from fastapi import APIRouter, status
from app.config.settings import get_settings
from app.modules.images import schema, usecase

router = APIRouter()

setting = get_settings()


@router.get(
    "/{uuid}",
    description="Router to get image.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "content": {"image/png": {}},
        }
    },
)
async def get_content_image(uuid: str):
    streaming_response = await usecase.GetImageUseCase(
        schema.GetImageSchema(uuid=uuid)
    ).execute()
    return streaming_response


@router.get(
    "/info/{folder}/{id}",
    description="Router to get images info by folder.",
    status_code=status.HTTP_200_OK,
)
async def get_image_info_by_folder(folder: str, id: int):
    folder_images_info = await usecase.GetFolderImagesInfo(
        schema.GetFolderImageInfoSchema(id=id, folder=folder)
    ).execute()
    return folder_images_info
