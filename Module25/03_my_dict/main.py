class MyDict(dict):

    def get(self, key, default=0):
        return super().get(key,default)



normal = dict()
normal['a']=1
normal['c']=7
print(normal)
print(normal.get('2'))

upgrade = MyDict()
upgrade['begin'] = 120
upgrade['end'] = '4df5'
print(upgrade)
print(upgrade.get('enf'))
