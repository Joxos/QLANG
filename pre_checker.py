def indent_checker(res):
    for i in res:
        if i[0] % 4 != 0:
            return [False, i[2]]
    return [True, 0]


def check_all(res):
    status = indent_checker(res)
    if not status[0]:
        return [False, 'indent', status[1]]
    return [True, '', 0]
