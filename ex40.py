import mystuff
mystuff.apple()

print(mystuff.tangerine)


class ThisStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")


thing = ThisStuff()
thing.apple()
print(thing.tangerine)
