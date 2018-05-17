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
    for i, s in enumerate(lines):
        if not s.strip():
            continue
        r = is_line_head(s)
        if r:
            yield i, r, s.strip(' =')
