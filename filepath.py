path = __file__.rsplit('/', 1)[0]

def rel_path(inpath):
    if inpath[0] == '/':
        return path + inpath
    else:
        return path + '/' + inpath
