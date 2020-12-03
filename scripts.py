import numpy as np
import json
import cv2
import sys
sys.path.append('/Users/user/opt/anaconda3/lib/python3.8/site-packages')


# json으로 받기.
inputs = sys.stdin.read()
# 문자열로 받은 형태를 json형태로 반환해준다.(dict)
dat = json.loads(inputs)

# 그 중에서 array로 담겨져있던 binary코드를 가져온다.
binary_arry = dat['binary']['data']

# opencv는 바이너리코드를 인코딩하여
# python에서 컨트롤 가능한 비트맵으로 만들어 줄 수 있다.
# 각 np의 원소는 uint8이어야 한다. 1byte = 8bits
binary_np = np.array(binary_arry, dtype=np.uint8)

# data cv2 np convert
img_np = cv2.imdecode(binary_np, cv2.IMREAD_ANYCOLOR)

# 좌측 끝상단에 검은색 네모를 칠한다.
img_np[0:50, 0:50] = 0

# convert bytes
# 다시 byte형태를 담은 list로 바꾸어준다.
_, imen = cv2.imencode('.jpeg', img_np)
imenb = bytes(imen)
imnb = list(imenb)

# 보낼때 역시 json으로 보내준다.
result = json.dumps({'img': imnb})
print(result)
