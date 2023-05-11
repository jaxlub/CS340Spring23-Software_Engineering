# a module of nice things

class NiceThing:
    # constructor
    def __init__(self, num_pub_cookies):
        # use self to access instance data and methods
        self.num_pub_cookies = num_pub_cookies

    def calories(self):
        return self.num_pub_cookies * 756
    