def extract_names(json_string):
    import json
    try:
        data = json.loads(json_string)
        return [item['name'] for item in data]
    except (json.JSONDecodeError, KeyError, TypeError):
        return []