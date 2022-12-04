from fastapi_camelcase import CamelModel


class GetImageSchema(CamelModel):
    uuid: str


class GetFolderImageInfoSchema(CamelModel):
    id: int
    folder: str
