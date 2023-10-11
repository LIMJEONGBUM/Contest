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
def transform_and_add_newline(data):
    # 데이터 변환 및 개행 문자 추가 로직을 작성합니다.
    # 예: 데이터 필드 변경, 포맷 변경, 개행 문자 추가 등
    # 여기에서는 단순히 데이터 뒤에 개행 문자를 추가하는 예시를 제공합니다.
    transformed_data = data + '\n'
    return transformed_data
