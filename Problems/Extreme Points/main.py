import json

test_dict = json.loads(input())
print(f'min: {min(test_dict, key=test_dict.get)}')
print(f'max: {max(test_dict, key=test_dict.get)}')
