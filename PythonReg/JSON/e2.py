import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sampleJson)
print(data['key2'])
