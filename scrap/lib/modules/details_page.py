from selenium.common.exceptions import NoSuchElementException
from lib.information_selector import InformationSelector

""" Module for functions related to the details page. """

def extract_all_infos_from_page(driver) -> dict:
    """ Extract all informations where a selector has been specified in InformationSelector. """
    # Still thinking about how to do this in a more elegant way.
    # Like linking selectors with players attributes in order to extract infos
    # by iterating over the player attributes.
    # This would allows fewer changes when adding new infos to the Player Class.
    player_infos = {}
    # Iterate over every selector
    for info in InformationSelector:
        player_infos[info.name] = extract_info(info.value, driver)
    return player_infos


def extract_info(selector, driver) -> str:
    """ Return a specific element on the detail page. """
    if len(driver.find_elements_by_css_selector(selector)) > 0:
        try: 
            return driver.find_element_by_css_selector(selector).get_attribute("innerHTML")
        except NoSuchElementException as e:
            print("No Such Element Exception:", e)