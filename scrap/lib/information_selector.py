from enum import Enum

class InformationSelector(Enum):
    """ Enum for the information selector."""
    NAME = '#page-title'
    AGE = 'body > div.page-bg > div > div.row.page-content > div > div:nth-child(3) > section.block.block-lnr-custom.block-lnr-custom-joueur-visu > div > div.col-infos.inverted-colors > div > div > div:nth-child(3) > ul > li:nth-child(1) > span.text'
    COUNTRY = 'body > div.page-bg > div > div.row.page-content > div > div:nth-child(3) > section.block.block-lnr-custom.block-lnr-custom-joueur-visu > div > div.col-infos.inverted-colors > div > div > div:nth-child(3) > ul > li:nth-child(2) > span.text'
    LINE = 'body > div.page-bg > div > div.row.page-content > div > div:nth-child(3) > section.block.block-lnr-custom.block-lnr-custom-joueur-visu > div > div.col-infos.inverted-colors > div > div > h2'
    TRIES = '#panel-more-main-stats > ul > li:nth-child(1) > span.text'
    POSITION = '#panel-more-main-stats > ul > li:nth-child(2) > span.text'
    DROP = '#panel-more-main-stats > ul > li:nth-child(3) > span.text'
    CONVERSION = '#panel-more-main-stats > ul > li:nth-child(4) > span.text'
    SECOND_POSITION = '#panel-more-main-stats > ul > li:nth-child(5) > span.text'
    YELLOW_CARDS = '#panel-more-main-stats > ul > li:nth-child(6) > span.text'
    SUBSTITUTE = '#panel-more-main-stats > ul > li:nth-child(7) > span.text'
    PENALTIES = '#panel-more-main-stats > ul > li:nth-child(8) > span.text'
    RED_CARDS = '#panel-more-main-stats > ul > li:nth-child(9) > span.text'
    MATCHES_PLAYED = 'body > div.page-bg > div > div.row.page-content > div > div:nth-child(3) > section.block.block-lnr-custom.block-lnr-custom-player-stats > div > div.main > div > ul.big-numbers.small-block-grid-5.hide-for-small > li:nth-child(1) > span.number'
    STARTER = 'body > div.page-bg > div > div.row.page-content > div > div:nth-child(3) > section.block.block-lnr-custom.block-lnr-custom-player-stats > div > div.main > div > ul.big-numbers.small-block-grid-5.hide-for-small > li:nth-child(2) > span.number'
    MINUTES_PLAYED = 'body > div.page-bg > div > div.row.page-content > div > div:nth-child(3) > section.block.block-lnr-custom.block-lnr-custom-player-stats > div > div.main > div > ul.big-numbers.small-block-grid-5.hide-for-small > li:nth-child(4) > span.number'
    POINTS_SCORED = 'body > div.page-bg > div > div.row.page-content > div > div:nth-child(3) > section.block.block-lnr-custom.block-lnr-custom-player-stats > div > div.main > div > ul.big-numbers.small-block-grid-5.hide-for-small > li:nth-child(5) > span.number'
    