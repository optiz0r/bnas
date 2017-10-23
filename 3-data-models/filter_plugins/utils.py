class FilterModule(object):

    def offset(self, value, base):
        """ Returns the value (or list of values) incremented by the base number

        e.g.
        1|offset(20) returns 21
        [12,34]|offset(5) returns [17, 39]

        :param value: Integer or list of integers to be incremented by the base
        :param base: Number to add to the values
        :return:
        """
        try:
            return list(map(lambda x: x + base, value))
        except TypeError:
            return value + base

    def filters(self):
        return {
            'offset': self.offset,
        }
