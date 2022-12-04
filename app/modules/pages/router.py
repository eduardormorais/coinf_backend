from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page, paginate
from app.config.settings import get_settings
from app.modules.core.auth_bearer import JWTBearer
from app.modules.pages import schema, usecase

router = APIRouter()

setting = get_settings()


@router.get(
    "/{name}",
    description="Router to get page content json.",
    # response_model=Page[schema.GetPageSchema],
    status_code=status.HTTP_200_OK,
    # dependencies=[Depends(JWTBearer())],
)
async def get_page(name: str):
    page_content = await usecase.GetPageContentUseCase(
        schema.GetPageSchema(name=name)
    ).execute()
    return page_content
