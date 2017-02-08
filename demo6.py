class ClassWithProperty(object):

    def __SetTheProperty(self, value):
        print("Setting the property")
        self.__m_the_property = value

    def __GetTheProperty(self):
        print("Getting the property")
        return self.__m_the_property

    def __DelTheProperty(self):
        print("Deleting the property")
        del self.__m_the_property

    TheProperty = property(fget=__GetTheProperty,
                           fset=__SetTheProperty,
                           fdel=__DelTheProperty,
                           doc="The property description.")

    def __GetReadOnlyProperty(self):
        return "This is a calculated value."

    ReadOnlyProperty = property(fget=__GetReadOnlyProperty)
