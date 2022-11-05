#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def lineNotify(message,token):
    payload = {'message':message}
    return _lineNotify(payload,token)

def notifyFile(filename,token):
    file = {'imageFile':open(filename,'rb')}
    payload = {'message': 'test'}
    return _lineNotify(payload,token,file)

def notifyPicture(url,token):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload,token)

def notifySticker(stickerID,stickerPackageID,token):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload,token)

def _lineNotify(payload,token,file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization':'Bearer '+token}
    return requests.post(url, headers=headers , data = payload, files=file)
