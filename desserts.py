"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    

    def __init__(self, name, flavor, price):
        self.cache = {}
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[self.name] = self
    
    def add_stock(self, amount):
        self.qty += amount
    
    def sell(self, amount):
        if self.qty == 0 or amount > self.qty:
            print("Sorry, these cupcakes are sold out.")
        else:
            self.qty -= amount


    def __repr__(self):
        """Human-readable printout for debugging."""
        return f'<Cupcake name="{self.name}" qty={self.qty}>'


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
