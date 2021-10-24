import json

items = json.loads('[{"id":1, "text": "item1"}, {"id":2, "text": "item2"}]')

for item in items:
    print(item['text'])
