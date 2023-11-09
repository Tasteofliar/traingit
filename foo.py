def greeting(name):
    result = 'Hello, {name}'.format(name=name)
    return result

def rename(name,side,suffix):
    objname =  '{side}_{name}_{suffix}'.format(name=name
                                ,side=side
                                ,suffix=suffix)

    return objname