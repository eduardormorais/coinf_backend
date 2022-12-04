from fastapi_camelcase import CamelModel


class GetPageSchema(CamelModel):
    name: str
