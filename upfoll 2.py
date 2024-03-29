import requests
import string
import json
import concurrent.futures
from bs4 import BeautifulSoup
import random
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
from datetime import datetime
import re


print("ZEPETRASH PANEL")
print("Auto Followers by ipowfu")




код_zепето = input("\n• Username: ")

количество_подписчиков = int(input("• Followers: "))


url = f"https://gw-napi.zepeto.io/profiles/{код_zепето}"
headers = {"Host": "gw-napi.zepeto.io","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"}
response = requests.get(url, headers=headers)
url = response.json()["profilePic"]
match = re.search(r'/users/([^/]+)/', url)
user_id = match.group(1)

идентификатор_пользователя = match.group(1)

def работник(итерация):
    def генерировать_идентификатор_устройства():
        значение = ''.join(random.choices(string.hexdigits.upper(), k=32))
        отформатированное_значение = '-'.join([значение[i:i+8] for i in range(0, len(значение), 8)])
        return отформатированное_значение

    идентификатор_устрйства = генерировать_идентификатор_устройства()

    сейчас = datetime.now()
    дата = сейчас.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    ответ = requests.post("https://gw-napi.zepeto.io/DeviceAuthenticationRequest", headers={ "X-Zepeto-Duid": идентификатор_устрйства, "User-Agent": "ios.zepeto_global/3.29.000 (ios; U; iOS 16.3.1; ph-PH; occ-PH; iPhone 11);ZEPETO", "X-Timezone": "Asia/Bangkok", "Content-Type": "application/json", "Connection": "keep-alive" }, json={"deviceId": идентификатор_устрйства})
    данные_ответа = ответ.json()
    ключ = данные_ответа["authToken"]   
    заголовки = {"Authorization": f"Bearer {ключ}", "X-Zepeto-Duid": идентификатор_устрйства, "Accept-Language": "ph-PH;q=1.0, ph-PH;q=0.9", "User-Agent": "ios.zepeto_global/3.29.000 (ios; U; iOS 16.3.1; ph-PH; occ-PH; iPhone 11);ZEPETO"}
    данные = {"country": "ID", "birth": ""}
    ответ = requests.post("https://gw-napi.zepeto.io/SaveUserDataPolicyRequest", headers=заголовки, json=данные)
    данные = {"key": "agreeTermsDate", "value": дата}
    ответ = requests.post("https://gw-napi.zepeto.io/PutUserAppProperty", headers=заголовки, json=данные)
    url = "https://gw-napi.zepeto.io/SaveCharacterRequest"
    данные_персонажа = {
        "IsMale": True,
        "Deformations": [],
        "Properties": [],
        "characterId": ""
    }
    запрос_персонажа = {
        "characterRequest": (
            "characterRequest.json",
            json.dumps(данные_персонажа),
            "application/json"
        )
    }
    мультиданные = MultipartEncoder(fields=запрос_персонажа)
    заголовки["Content-Type"] = мультиданные.content_type
    ответ = requests.post(url, headers=заголовки, data=мультиданные.to_string())
    заголовки = {
    "X-Worldtree-Greeter": "false",
    "Accept": "*/*",
    "Authorization": f"Bearer {ключ}",
    "X-Timezone": "Asia/Jakarta",
    "X-Zepeto-Duid": идентификатор_устрйства,
    "Accept-Language": "ph-PH;q=1.0, ph-PH;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "User-Agent": "ios.zepeto_global/3.29.000 (ios; U; iOS 16.3.1; ph-PH; occ-PH; iPhone 11);ZEPETO",
    "X-Worldtree-Newbie": "true",
    "Connection": "keep-alive"
    }
    данные_профиля = {"job": "", "name": None, "nationality": "", "statusMessage": "Powfu Sayang Chaizu.", "zepetoId": None}
    ответ = requests.post("https://gw-napi.zepeto.io/SaveProfileRequest_v2", headers=заголовки, json=данные_профиля)
    данные_abtest = {"testId": "onboardingD1RetentionTfTest"}
    ответ = requests.post("https://gw-napi.zepeto.io/AbTestGroupRequest", headers=заголовки, json=данные_abtest)
    данные_аккаунта = {"timeZone": "Asia/Jakarta"}
    ответ = requests.post("https://gw-napi.zepeto.io/AccountUser_v5", headers=заголовки, json=данные_аккаунта)
    данные_подписки = {"followUserId": идентификатор_пользователя}
    ответ = requests.post("https://gw-napi.zepeto.io/FollowRequest_v2", headers=заголовки, json=данные_подписки)
    print("\nAdding Followers...\n")
    

if __name__ == "__main__":
    количество_итераций = количество_подписчиков
    количество_работников = 10
    with concurrent.futures.ThreadPoolExecutor(max_workers=количество_работников) as executor:
        executor.map(работник, range(количество_итераций))
