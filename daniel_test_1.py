batch = 3
items = ['gigi', 'duru', 'ionel', 'florescu', 'popovici', 'restaurant', 'ovidiu']


def _process_var_input(_items, _batch):
    items_as_batch, result = list(), list()
    for item in _items:
        if len(item) >= _batch:
            for i in range(0, len(item) + 1):
                if len(item[i:i+_batch]) == _batch:
                    items_as_batch.append(item[i:i+_batch])

    for item in items_as_batch:
        item_count = items_as_batch.count(item)
        if (item, item_count) not in result:
            result.append((item, item_count))

    return result


print(_process_var_input(items, batch))