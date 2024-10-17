
--- 
title:  PaddleOCR Docker CPU版 一键部署运行 
tags: []
categories: [] 

---
**构建了一个镜像，直接部署运行即可使用**

```
docker run -dp 8866:8866  --name paddle_ocr nowindandmoon/paddle_ocr:latest
```

**测试代码**

```
import requests
import base64
import json


class InvoiceOcr:
    def __init__(self, url):
        self.api_url = url if url else "http://xxxxxx:8866/predict/ocr_system"

    def post(self, parameters):
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

        try:
            response = requests.post(self.api_url, data=json.dumps(parameters), headers=headers)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Error: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
            return None


def image_to_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


if __name__ == "__main__":
    api_url = "http://xxxxxx:8866/predict/ocr_system"
    ocr = InvoiceOcr(api_url)

    # 替换为你的图片路径
    base64_image = image_to_base64("./test.jpg")

    parameters = {
        "images": [base64_image]
    }

    result = ocr.post(parameters)

    print(result)
    result = json.loads(result)

    for item in result['results'][0]:
        print(item['text'])

```

**效果**

<img alt="" height="567" src="https://img-blog.csdnimg.cn/direct/6b63c27176454c35b7f50b50cc7f6d12.png" width="1200">
