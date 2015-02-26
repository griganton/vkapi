__author__ = 'agrigoryev'
__author__ = 'agrigoryev'

import requests
import json


class VkApi:
    def __init__(self, token):
        self.token = token
        self.version = '5.28'

    def request(self, method, data={}):
        data['access_token'] = self.token
        data['v'] = self.version
        r = requests.post("https://api.vk.com/method/"+method, data)
        return json.loads(r.content.decode())

    def send_photo_album(self, group_id, album_id, image, caption):
        upload_server_info = self.request('photos.getUploadServer', {'album_id': album_id,
                                                                     'group_id': group_id})['response']
        send_file = requests.post(upload_server_info['upload_url'], files={"file1":("file1.jpg", image)})
        photo_save_info = json.loads(send_file.content.decode())
        photo_save_info['caption']= caption
        photo_save_info['album_id']=photo_save_info['aid']
        photo_save_info['group_id']=photo_save_info['gid']
        r = self.request('photos.save',photo_save_info)
        return r

