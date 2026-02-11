import uuid


def CreateUniqueKeyForMap(map):
    if map is None:
        print("while generating Unique key for map, map parameter wasn't passed")
        print(map)
        return
    key = uuid.uuid4()
    while key in map:
        key = uuid.uuid4()

    return key
