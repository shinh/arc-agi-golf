from importlib.machinery import SourceFileLoader
m=SourceFileLoader('t','dsl/task240.py').load_module()
m.rot90=lambda p:tuple(zip(*p[::-1]))
p=m.p
