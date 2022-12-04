from app.main import firebase
from gcloud.storage.blob import Blob


class FirebaseConnection:
    def __init__(self):
        self.__database = firebase.database()
        self.__storage = firebase.storage()

    async def get_content_page(self, name: str) -> dict | None:
        page_data = self.__database.child(name).get()
        if page_data.each():
            page_data = [_.val() for _ in page_data.each()]
            return page_data[0]
        return None

    async def get_all_images(self):
        images = self.__database.child("images").get()
        images = [_.val() for _ in images.each()]
        return images

    async def find_image_by_uuid(self, uuid: str) -> dict | None:
        images = await self.get_all_images()
        img = [img for img in images if img["uuid"] == uuid]
        if len(img) > 0:
            return img[0]
        return None

    async def find_image_object_by_path(self, path: str) -> Blob | None:
        list_files = self.__storage.child(path).list_files()
        for file in list_files:
            if path in file.name:
                return file
        return None

    async def find_image_by_folder_path(self, id: int, folder: str):
        images = await self.get_all_images()
        imgs = [img for img in images if f"{folder}/{id}" in img["imgPath"]]
        return imgs
