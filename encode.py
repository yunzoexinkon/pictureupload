import base64
import gc
import json
import urequests as requests

def encode() :
    # 打開影像檔並讀取內容
    with open('image.jpg', 'rb') as image:
        # 初始化空的位元組流
        image_64_encode = b''
        # 每次讀取的大小
        chunk_size = 1024
        while True:
            # 從文件中讀取塊
            chunk = image.read(chunk_size)
            if not chunk:
                break  # 檔讀取完成，退出迴圈
            # 將塊編碼為Base64，並添加到結果中
            image_64_encode += base64.b64encode(chunk)

    data = { "key" : image_64_encode }
    json_data = json.dumps(data)
    headers = {"Content-Type": "application/json"}
    gc.collect()
    requests.post( 'https://1qququi6u6.execute-api.us-east-1.amazonaws.com/default/pictureupdate', data=json_data,headers=headers)


