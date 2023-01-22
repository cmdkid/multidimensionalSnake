def conf(*attr):
    tmp_item = False
    for val in attr:
        if tmp_item is False:
            tmp_item = conf_data.get(val, None)
        else:
            tmp_item = tmp_item.get(val, None)

        if tmp_item is None:
            return None
    return tmp_item


conf_data = {
    'field': [25, 80],  # field dimensions
    'snake': {
        'length': 3
    },
    'settings': {
        'speed': 1  # game speed in ms
    }
}