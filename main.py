from config import accounts, Account
from vkbottle import PhotoWallUploader, API
import os
from dataclasses import dataclass
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class UploadData:
    account: Account
    filepath: str
    group_id: int

def get_uploads_for_account(account: Account):
    dir = os.path.join('photos', account.id)
    filenames = os.listdir(dir)

    if len(filenames) == 0 or len(filenames) != len(account.groups):
        logger.info(f'wrong files count for account {account.id}')
        return

    data = [UploadData(account=account, filepath=os.path.join(dir, filename), group_id=group_id) for filename, group_id in zip(filenames, account.groups)]
    logger.info(data)
    return data

async def post(data: UploadData):
    try:
        api = API(token=data.account.token.value)
        photo_uploader = PhotoWallUploader(api=api)
        logger.info(f'uploading {data.filepath} to group {data.group_id}')
        attachment = await photo_uploader.upload(file_source=data.filepath, group_id=data.group_id)
        logger.info(f'uploaded successfully: {attachment} posting started')
        await api.wall.post(owner_id=data.group_id, attachment=[attachment], attachments_list='''[{"type":"action_button","action_button":{"type":"message_to_community","title":"Написать сообществу","description":"Открывает чат с сообществом"}}]''')
        logger.info('posted successfully')
    except Exception as e:
        logger.error('posting error', exc_info=True)

async def main():
    tasks = [post(data) for data in [upload_data for account in accounts for upload_data in get_uploads_for_account(account)]]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())