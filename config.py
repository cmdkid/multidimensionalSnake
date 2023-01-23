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
    'field': [100, 100, 100, 100],  # field dimensions
    'snake': {
        'length': 3  # snake length at the beginning
    },
    'settings': {
        'speed': 0.1  # game speed in sec
    }
}