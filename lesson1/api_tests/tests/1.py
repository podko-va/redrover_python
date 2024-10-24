import json

my_dict = {'detail': [{'type': 'missing', 'loc': ['body', 'name'], 'msg': 'Field required', 'input': {}}, {'type': 'missing', 'loc': ['body', 'description'], 'msg': 'Field required', 'input': {}}, {'type': 'missing', 'loc': ['body', 'steps'], 'msg': 'Field required', 'input': {}}, {'type': 'missing', 'loc': ['body', 'expected_result'], 'msg': 'Field required', 'input': {}}, {'type': 'missing', 'loc': ['body', 'priority'], 'msg': 'Field required', 'input': {}}]}

md= '{'detail': [{'type': 'missing', 'loc': ['body', 'name'], 'msg': 'Field required', 'input': {}}, {'type': 'missing', 'loc': ['body', 'description'], 'msg': 'Field required', 'input': {}}, {'type': 'missing', 'loc': ['body', 'steps'], 'msg': 'Field required', 'input': {}}, {'type': 'missing', 'loc': ['body', 'expected_result'], 'msg': 'Field required', 'input': {}}, {'type': 'missing', 'loc': ['body', 'priority'], 'msg': 'Field required', 'input': {}}]}'
data = json.loads(md)
print(type(md))