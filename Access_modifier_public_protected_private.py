class AccessModifier:
    public=("This is protected class variable")
    _protected=("This is protected class variable")
    __private="This is private class variable"

check=AccessModifier()
print(check.public)
print(check._protected)
print(check._AccessModifier__private)




class Example:
    a=5
    _b=7
    __c=9
e=Example()
print(e.a)
print(e._b)
print(e._Example__c)