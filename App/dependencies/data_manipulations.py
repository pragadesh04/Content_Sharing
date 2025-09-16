def serialiser(doc):
    doc["_id"] = str(doc["_id"])
    print(doc)
    return doc