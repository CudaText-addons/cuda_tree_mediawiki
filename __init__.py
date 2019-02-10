import itertools

def is_line_head(s):
    if not s.startswith('='):
        return
    r = len(list(itertools.takewhile(lambda c: '=' == c, s)))
    r2 = len(list(itertools.takewhile(lambda c: '=' == c, reversed(s))))
    if r2 >= r:
        return r


def get_headers(filename, lines):
    '''
    Generates headers in format:
    line_index, header_level, header_text
    '''
    res = []
    for i, s in enumerate(lines):
        if not s.strip():
            continue
        r = is_line_head(s)
        if r:
            res.append( ((0, i, 0, i+1), r, s.strip(' ='), -1) )

    return res
