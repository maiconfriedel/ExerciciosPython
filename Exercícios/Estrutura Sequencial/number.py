#https://wiki.python.org.br/EstruturaSequencial
class Number:
    def isnumber(self, value):
        try:
            float(value)
        except ValueError:
            return False
        return True