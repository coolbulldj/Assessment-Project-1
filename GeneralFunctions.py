import uuid


def CreateUniqueKeyForMap(map):
    key = uuid.uuid4()
    while map[key]:
        key = uuid.uuid4()

    return key
