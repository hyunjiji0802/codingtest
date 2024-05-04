# Python3 샘플 코드 #

import requests

url = 'http://apis.data.go.kr/9760000/VoteXmntckInfoInqireService2/getVoteSttusInfoInqire'
params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'sgId' : '20231011', 'sgTypecode' : '4', 'sdName' : '서울특별시', 'wiwName' : '강서구' }



response = requests.get(url, params=params)
print(response.content)