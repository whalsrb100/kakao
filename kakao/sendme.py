import requests
import json
class kakao:
    def __new__(self):
        return super().__new__(self)

    def __del__(self):
        pass

    def __init__(self):
        self.rest_api = 'b052a914d2157cbbfd00f0d04356a3a6'
        self.refresh_token = 'gI9IenLp3yOZNkUgls9vE0I6C2JemiDKuaCioAorDNMAAAF6h2vTBA'
        #self.access_token = '9-hDQZx60uE17cRonv7435L60Aen34lyaTe4jgopyNgAAAF6jSxM9A'
        fp = open("acctkn.data",'r')
        self.access_token = json.loads(fp.readline().replace("'",'"'))['access_token']
        fp.close()
        print(self.access_token)
        super().__init__()

    def SetAccessToken(self,token):
        self.access_token=token

    def GetAccessToken(self):
        return self.access_token

    def RefreshToken(self):
        url = "https://kauth.kakao.com/oauth/token"
        data = {
            "grant_type" : "refresh_token",
            "client_id": self.rest_api,
            "refresh_token" : self.refresh_token
        }
        response = requests.post(url, data=data)
        tokens = response.json()
        fp = open("acctkn.data",'w')
        fp.write(str(tokens))
        fp.close()

        return tokens
    
    def NewToken(self):
        url = "https://kauth.kakao.com/oauth/token"
        code='R9O5AbI43CxJrzw7b9_7tsCd_jgcTFY-Wk_8N9X5joRJx4TChT9mIA2tcRegZIHoMJOHpQopb1QAAAF6h2fyNQ'
        data = {
            "grant_type" : "authorization_code",
            "client_id": self.rest_api,
            "redirect_url" : "https://localhost.com",
            "code" : code
        }
        response = requests.post(url, data=data)
        tokens = response.json()
        return tokens

        #{
        # 'access_token': 'bl1JjVdwQCUiV-hJSaLckehZ2bYriOYMBNzeOwo9cusAAAF6h8mAig',
        # 'token_type': 'bearer',
        # 'refresh_token': 'gI9IenLp3yOZNkUgls9vE0I6C2JemiDKuaCioAorDNMAAAF6h2vTBA',
        # 'expires_in': 21599,
        # 'refresh_token_expires_in': 5183999
        # }

    def SendMSG(self,msg):
        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        # 사용자 토큰
        headers = {
            "Authorization": "Bearer " + self.access_token
        }
        data = {
            "template_object" : json.dumps({ "object_type" : "text",
                                             "text" : msg,
                                             "link" : {"web_url" : "www.naver.com"}
                                           })
        }
        response = requests.post(url, headers=headers, data=data)
        print(response.status_code)
        print(response.json())
        if response.json().get('result_code') == 0:
            print('메시지를 성공적으로 보냈습니다.')
        else:
            print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))

k = kakao()
k.RefreshToken()
k.SendMSG("카카오 나에게 보내기123")
#https://kauth.kakao.com/oauth/authorize?client_id={REST_API 앱키를 입력하세요}&response_type=code&redirect_uri=https://localhost.com
#https://kauth.kakao.com/oauth/authorize?client_id=b052a914d2157cbbfd00f0d04356a3a6&response_type=code&redirect_uri=https://localhost.com
get_accesstoken_url='https://kauth.kakao.com/oauth/authorize?client_id=' + k.rest_api + '&response_type=code&redirect_uri=https://localhost.com'