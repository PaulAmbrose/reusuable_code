    # Magic method called when you compare
    # two Rectangle  objects with the == operator
    def __eq__(self, oOtherRectangle):
        if not isinstance(oOtherRectangle, Rectangle):
            raise TypeError('Second object was not a Rectangle')
        if self.area == oOtherRectangle.area:
            return True
        else:
            return False
