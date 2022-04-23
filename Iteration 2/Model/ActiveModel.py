from Anmodninger import Anmodninger

class ActiveModel(object):
    list_anmodninger: list = []
    current_anmodning: Anmodninger = None

    @classmethod
    def add_anmodning(cls,anmodning):
        cls.list_anmodninger.append(anmodning)
