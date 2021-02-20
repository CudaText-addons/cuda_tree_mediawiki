
def get_head(s):
    if not s.startswith('='):
        return
    if not s.endswith('='):
        return

    r = 0
    while (r<len(s)) and (s[r]=='='):
        r += 1

    r2 = 0
    i = len(s)-1
    while (i>0) and (s[i]=='='):
        i -= 1
        r2 += 1

    if r2>=r:
        return r

def get_headers(filename, lines):
    '''
    Generates headers in format:
    line_index, header_level, header_text
    '''
    res = []
    for i, s in enumerate(lines):
        r = get_head(s)
        if r:
            res.append( ((0, i, 0, i+1), r, s.strip(' ='), -1) )

    return res
