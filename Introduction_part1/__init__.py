from otree.api import *
c = Currency


doc = """
This application provides an instruction for part 1.
"""


class Constants(BaseConstants):
    name_in_url = 'introduction_part1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class Introduction(Page):
    def is_displayed(self):
        return True


page_sequence = [Introduction]
