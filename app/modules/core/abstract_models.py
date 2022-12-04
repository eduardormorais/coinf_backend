from tortoise import Model, fields, models, timezone
from tortoise.exceptions import BaseORMException


class DateableModel(models.Model):
    created_at = fields.DatetimeField(auto_now_add=True, default=timezone.now())
    updated_at = fields.DatetimeField(auto_now=True, default=timezone.now())

    class Meta:
        abstract = True


class BaseRepository:
    def __init__(self):
        self.entity = Model

    async def create(self, payload: dict):
        return await self.entity.create(**payload)

    async def update(self, payload: dict, id: int) -> bool:
        try:
            await self.entity.filter(id=id).update(**payload)
            return True
        except BaseORMException:
            return False

    async def get_all(self) -> list:
        return await self.entity.all()

    async def get_by_id(self, id: int) -> [dict, None]:
        return await self.entity.get_or_none(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.entity.filter(id=id).delete()
            return True
        except BaseORMException:
            return False
