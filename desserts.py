"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

    def __repr__(self, name, qty):
        """Human-readable printout for debugging."""
        super().__init__(name, qty)
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
