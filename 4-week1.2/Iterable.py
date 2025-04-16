from collections.abc import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))
print(isinstance((x for x in range(10)),Iterable))