import json


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True


InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
isValid = validateJSON(InvalidJsonData)

print("Given JSON string is Valid", isValid)
