from lib.information_selector import InformationSelector

class Player:
    """Player class. """
    name = 'N/A'
    age = 'N/A'
    country = 'N/A'
    line = 'N/A'
    tries = 'N/A'
    position = 'N/A'
    drop = 'N/A'
    conversion = 'N/A'
    second_position = 'N/A'
    yellow_cards = 'N/A'
    substitue = 'N/A'
    penalties = 'N/A'
    red_cards = 'N/A'
    matches_played = 'N/A'
    starter = 'N/A'
    minutes_played = 'N/A'
    points_scored = 'N/A'
   
    def __init__(self, infos: dict) -> None:
        # Should probably iterate over the keys of InformationSelector
        # but I'm not sure if it's safe to do so.
        self.name = infos[InformationSelector.NAME.name]
        self.age = infos[InformationSelector.AGE.name]
        self.country = infos[InformationSelector.COUNTRY.name]
        self.line = infos[InformationSelector.LINE.name]
        self.tries = infos[InformationSelector.TRIES.name]
        self.position = infos[InformationSelector.POSITION.name]
        self.drop = infos[InformationSelector.DROP.name]
        self.conversion = infos[InformationSelector.CONVERSION.name]
        self.second_position = infos[InformationSelector.SECOND_POSITION.name]
        self.yellow_cards = infos[InformationSelector.YELLOW_CARDS.name]
        self.substitute = infos[InformationSelector.SUBSTITUTE.name]
        self.penalties = infos[InformationSelector.PENALTIES.name]
        self.red_cards = infos[InformationSelector.RED_CARDS.name]
        self.matches_played = infos[InformationSelector.MATCHES_PLAYED.name]
        self.starter = infos[InformationSelector.STARTER.name]
        self.minutes_played = infos[InformationSelector.MINUTES_PLAYED.name]
        self.points_scored = infos[InformationSelector.POINTS_SCORED.name]
        