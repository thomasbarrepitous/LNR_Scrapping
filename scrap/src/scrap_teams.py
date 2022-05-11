# Allows us to declare return annotations for types that are not yet invoked
from __future__ import annotations

import subprocess
import os
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
# Auth module
import lib.modules.firebase.auth as firebase


if __name__ == '__main__':
    print("You cannot run this file by itself.")


def run():
    """ Calls the main function. Probably needs to be changed for script varargs. """
    main('teams', 'https://www.lnr.fr/rugby-pro-d2/clubs-rugby-pro-d2')


def main(subbranch: str, url: str) -> None:
    """ Main function. """
    print('Authenticating to firebase ...')
    ref = firebase.fetchDB(subbranch)
    print('Configuring selenium ...')
    browser = selenium_configuration(url)
    print('Starting teams scraping ...')
    scrap_teams(ref, browser)


def selenium_configuration(url: str, headless: bool = True) -> WebDriver:
    """ The selenium webdriver configuration. """
    abs_path = os.path.abspath("selenium/chromedriver")
    # Allow multiple file downloads
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    # Trick needed for certains elements that only appears
    # at a certain size
    options.add_argument("window-size=3840, 2160")
    browser = webdriver.Chrome(abs_path, options=options)
    browser.implicitly_wait(10)
    browser.get(url)
    return browser

#######################################################################################################################
#                                                                                                                     # 
#        Deprecated, the whole code is wrong and unpractical. A rewrite is necessary to scrap the teams.              #
#                                                                                                                     #
#######################################################################################################################

# def scrap_teams(ref: Reference, browser: WebDriver) -> None:
#     """ """
#     tables = browser.find_element_by_css_selector('div > section > ul')
#     teams_area = tables.find_elements_by_tag_name('li > a')
#     links = [team.get_attribute('href') for team in teams_area]
#     # For each teams, we iterate over their links
#     for link in tqdm(links, desc='Teams'):
#         cur_win = browser.current_window_handle  # Save landing page
#         # Opens the link in a new window
#         browser.execute_script('window.open("+ tab_url +","_blank");''')
#         window_after = browser.window_handles[1]
#         browser.switch_to.window(window_after)
#         browser.implicitly_wait(10)
#         browser.get(link)
#         # Extract infos
#         team_object = extract_info(browser)
#         # Close the new window
#         browser.close()
#         browser.switch_to.window(cur_win)  # switch back to main window
#         # Push player to db
#         ref.push(team_object)


# def extract_info(browser: WebDriver) -> dict:
#     # Get team's name
#     name = browser.find_element_by_id('page-title').text
#     # Display stats
#     stats_button = browser.find_element_by_xpath('//a[@href="#panel-club-stats"]')
#     browser.execute_script("arguments[0].scrollIntoView(true)", stats_button)
#     browser.execute_script("arguments[0].click()", stats_button)

#     # Fetch stats
#     stats_area = browser.find_elements_by_css_selector(
#         '.team-stats > li > ul > li > span.text')
#     points_total = stats_area[0].text
#     bonus_points = stats_area[1].text
#     points_scored = stats_area[2].text
#     points_conceded = stats_area[3].text
#     points_differential = stats_area[4].text
#     matches_won = stats_area[6].text
#     matches_lost = stats_area[7].text
#     matches_drawn = stats_area[8].text
#     yellow_cards = stats_area[9].text
#     red_cards = stats_area[10].text
#     # If stadium's name exist
#     """
#     stadium = polling2.poll(lambda: browser.find_element_by_css_selector('ul.infos-list > li > span.text').text, step=0.5, timeout=20) # Waiting for it to appear to evaluate
#     stadium_exposed = browser.find_element_by_css_selector('ul.infos-list > li > span.title').text == 'Stade'
#     if stadium_exposed:
#         stadium = browser.find_element_by_css_selector('ul.infos-list > li > span.text').text
#     else: 
#         stadium = 'NA'
#     """
#     return {
#             'name': name, 
#             'current-season':
#                 {
#                 'points_total': points_total, 'bonus_points': bonus_points,
#                 'points_scored': points_scored, 'points_conceded': points_conceded,
#                 'points_differential': points_differential, 'matches_won': matches_won,
#                 'matches_lost': matches_lost, 'matches_drawn': matches_drawn, 
#                 'yellow_cards': yellow_cards, 'red_cards': red_cards,
#                 }
#             }
