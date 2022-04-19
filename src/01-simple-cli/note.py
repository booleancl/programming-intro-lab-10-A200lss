counter = 0
class Note:
    def __init__(self, content, *tags):
        self.content = content
        self.tags = [*tags]
        global counter
        counter += 1
        self.id = counter

    def match(self, check):
        if check in self.content:
            return True
        elif check in self.tags:
            return True
        else:
            return False



