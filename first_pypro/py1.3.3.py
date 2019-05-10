# -*- coding: utf-8 -*-
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(url='index.html',title='首页',content='首页')
print pickle.dumps(d)

f=open(r'd:\dump.txt','wb')
pickle.dump(d,f)
f.close()


f = open(r'd:\dump.txt', 'rb')
d=pickle.load(f)
print d