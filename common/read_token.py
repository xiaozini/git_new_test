#coding=utf-8
import os,yaml
cur = os.path.dirname(os.path.realpath(__file__))

def get_token(yamlName='token.yaml'):
    p = os.path.join(cur,yamlName)
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    return t['token']

# if __name__ == '__main__':
#     print(get_token())