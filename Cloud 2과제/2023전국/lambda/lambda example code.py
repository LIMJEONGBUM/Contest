슬라이싱
hello

스플릿
dir를 json으로 

import json
import base64
def lambda_handler(event, context):
    # Kinesis Firehose에서 전달된 이벤트 데이터
    records = event['records']
    transformed_records = []
    for record in records:
        # Firehose에서 전달된 데이터는 base64로 인코딩되어 있습니다.
        # 디코딩하여 원래 데이터를 얻습니다.
        payload = json.loads(base64.b64decode(record['data']))
        # 데이터 변환 및 개행 문자 추가
        transformed_data = transform_and_add_newline(payload)
        # 데이터를 다시 base64로 인코딩하여 Firehose로 전달합니다.
        transformed_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(transformed_data).encode('utf-8')).decode('utf-8') + '\n'
        }
        transformed_records.append(transformed_record)
    return {'records': transformed_records}
    ###############################################################
def transform_and_add_newline(event):                            #{
    born = (2023 + 1) - event["age"]                             #"name": "park",
                                                                 #"age": 20,                 -> 이 데이터를 밑에 데이터로 변환 하는 코드
    if born > 2004:                                              #"phone": "010-5681-1160",
        st = "bad"                                               #"year": "2023"
    elif born <= 2004:                       #예시 부분          #}
        st = "good"
                                                                #{
    data = {                                                    #"name": "park",
        "name": event["name"],                                  #"born_year": 20,  # 출생일자 출력       -> 이 데이터를 기반으로 만든 python 함수
        "born_year": born,                                      #"last_phone": "1160", # 전화번호 뒷자리
        "last_phone": event["phone"][9:13],                     #"status": "good or bad" # 2004년 생 이상일 경우 good, 이 이하일 경우 bad
        "status": st                                            #}
    }                                                           
    ################################################################

    # 데이터 변환 및 개행 문자 추가 로직을 작성합니다.
    # 예: 데이터 필드 변경, 포맷 변경, 개행 문자 추가 등
    # 여기에서는 단순히 데이터 뒤에 개행 문자를 추가하는 예시를 제공합니다.
    transformed_data = data + '\n'
    return transformed_data
