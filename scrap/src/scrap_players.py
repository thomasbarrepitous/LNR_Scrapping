# Allows us to declare return annotations for types that are not yet invoked
from __future__ import annotations
from lib.information_selector import InformationSelector

# Progress bar
from tqdm import tqdm

# Import Pandas
import pandas as pd

# Scrapping libraries
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Detail Page Extraction Module
import lib.modules.details_page as dp

# Objects
from lib.player import Player

if __name__ == '__main__':
    print("You cannot run this file by itself.")

def run():
    """ Calls the main function. Probably needs to be changed for script varargs. """
    main('https://www.lnr.fr/rugby-pro-d2/joueurs')


def main(url: str) -> None:
    """ Main function. """
    print('Configuring selenium ...')    
    browser = selenium_configuration(url)
    print('Starting players scraping ...')
    scrap_players_lnr(browser)


def selenium_configuration(url: str, headless: bool = True) -> WebDriver:
    """ The selenium webdriver configuration. """
    # Download latest chromedriver and add it to path.
    chromedriver_autoinstaller.install()
    # Allow multiple file downloads
    options = webdriver.ChromeOptions()
    # Able / Disable GUI, doesnt work yet
    if headless:
        options.add_argument("headless")
        # Starting scrapping
        # Accepting cookies when in non headless browser
        #button_accept_all = browser.find_element_by_id('ez-accept-all').click()
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    browser.get(url)
    return browser


def scrap_players_lnr(browser: WebDriver) -> None:
    """ Main function. """
    browser.implicitly_wait(65)
    # df = pd.DataFrame(columns=InformationSelector._member_names_)
    df = pd.DataFrame()
    # Iterate over every page
    df = scrap_player_lnr(browser, df)
    # Save to csv
    df.to_csv('players.csv')
    browser.close()
    browser.quit()


def scrap_player_lnr(browser: WebDriver, df: DataFrame) -> DataFrame:
    """ Iterate over each players in the landing page. """
    page_main_block = browser.find_element_by_class_name('block-lnr-custom-players-list')
    players_list_area = page_main_block.find_element_by_tag_name('ul')
    players_list = players_list_area.find_elements_by_tag_name('li')

    # For each players' personal pages link
    for player in players_list:
        player_link = player.find_element_by_tag_name('a').get_attribute('href')
        # Extract player info
        df = df.append(get_player_info(browser, player_link).__dict__, ignore_index=True)
        return df


def get_player_info(browser: WebDriver, player_link: str) -> Player:
    """ Get an individual player's infos from his detail page. """
    cur_win = browser.current_window_handle # Save current/main window
    open_tab(browser, player_link)
    
    player_infos = Player(extract_info_detail_page(browser))
    
    browser.close() # close new window
    browser.switch_to.window(cur_win) # switch back to main window
    return player_infos


def extract_info_detail_page(browser: WebDriver) -> dict:
    """ Extract player info from personal page. """
    # A Mapper would be ideal but not worth the time in such a small project.
    return dp.extract_all_infos_from_page(browser)


def open_tab(browser: WebDriver, link: str) -> None:
    """ Open a new tab. """
    browser.execute_script('window.open("+ tab_url +","_blank");''')
    window_after = browser.window_handles[1]
    browser.switch_to.window(window_after)
    browser.get(link)


""" 
#############################################################################

    This part is not deprecated. Will be removed in the future.
    This scrapping does not include itsrugby.fr anymore.

#################################################################################

def scrap_players_itsrugby(ref: Reference, browser: WebDriver) -> None:
    #  This function has too much stuff in it, needs to be refactored. It gathers every scraping
    # event of the file. 
    # Number of tables that contain names
    tables = browser.find_elements_by_css_selector('div#slides.row > table')

    for table in tqdm(tables, desc='Tabs'): 
        cur_win = browser.current_window_handle # get current/main window

        # Each player is in a <tr> tag
        players = table.find_elements_by_tag_name('tr')
        links = []

        # Storing links in list to avoid DOM changes bugs
        for p in players:
            links.append(p.find_element_by_tag_name('a').get_attribute('href'))

        # For each players listed
        for link in tqdm(links, desc='Players'):
            # Opening a new window and switching to the players stats
            browser.execute_script('window.open("+ tab_url +","_blank");''')
            window_after = browser.window_handles[1]
            browser.switch_to.window(window_after)
            browser.get(link)

            # Table of
            table_player = browser.find_element_by_css_selector('div > table > tbody')
            seasons = table_player.find_elements_by_tag_name('tr')

            # Create a dict out of the basic informations we have 
            player_object = extract_info(browser)
            player_seasons = {}
            last_season = '2021'
            last_club = ''

            # Fetching data for each seasons
            for s in tqdm(seasons, desc='Seasons'):
                stats = {}
                if s != seasons[0]:
                    try:
                        season = s.find_element_by_css_selector('#bleu_bold').text 
                        seasons_tokens = season.split('/')
                        if len(seasons_tokens) > 1:
                           season = '20' + seasons_tokens[0] + '-20' + seasons_tokens[1]
                        else:
                            season = last_season
                    except NoSuchElementException: 
                        season = last_season

                    try:
                        club = s.find_element_by_class_name('bleu_moy').text
                    except:
                        club = last_club
                    # Gathering infos from compet
                    compet = s.find_elements_by_id('noir')[0].text.replace('-','0')
                    
                    if len(s.find_elements_by_id('noir')) > 1:
                        pts = s.find_elements_by_id('noir')[1].text.replace('-','0')
                        match_played = s.find_elements_by_id('noir')[2].text.replace('-','0')
                        starts = s.find_elements_by_id('noir')[3].text.replace('-','0')
                        tries = s.find_elements_by_id('noir')[4].text.replace('-','0')
                        drop = s.find_elements_by_id('noir')[5].text.replace('-','0')
                        conversion = s.find_elements_by_id('noir')[6].text.replace('-','0')
                        y_card = s.find_elements_by_id('noir')[7].text.replace('-','0')
                        r_card = s.find_elements_by_id('noir')[8].text.replace('-','0')
                    else:
                        club = 'NA'
                        pts = 'NA'
                        match_played = 'NA'
                        starts = 'NA'
                        tries = 'NA'
                        drop = 'NA'
                        conversion = 'NA'
                        y_card = 'NA'
                        r_card = 'NA'
                    try:
                        minutes_played = s.find_element_by_css_selector('td#bold_bleu > span').text
                    except NoSuchElementException:
                        minutes_played = '0'

                    stats_dict = {'Club': club, 'Points': pts, 'Matchs': match_played, 'Starts': starts, 'Tries': tries, 'Drops': drop, 'Conversions': conversion, 'Yellows': y_card, 'Reds': r_card, 'Minutes': minutes_played}

                    # If the season is not in the season dict, create it
                    if season not in player_seasons:
                        player_seasons[season] = {compet : stats_dict}
                    else:    
                        player_seasons[season][compet] = stats_dict
                    # Save for next iteration
                    last_season = season
                    last_club = club

            # Adding information to our player object       
            player_object['seasons'] = player_seasons

            browser.close() # close new window
            browser.switch_to.window(cur_win) # switch back to main window
            # Push player to db
            ref.push(player_object)


def extract_info(browser: WebdDiver) -> dict:
    # Extract the info in the top paragraph of the players page. 
    info_paragraph = browser.find_element_by_css_selector('div.row > div > p')
    info_paragraph_text = info_paragraph.text
    name = browser.find_element_by_css_selector('div > div > p > b').text    
    nationality = info_paragraph.find_element_by_tag_name('a').text
    age = find_in_regex(info_paragraph_text, 'agé de (.+?) ans')
    birthday = find_in_regex(info_paragraph_text, 'né le (.+?). Il')
    weight = find_in_regex(info_paragraph_text, 'pour (.+?) kg')
    height = find_in_regex(info_paragraph_text, 'mesure (.+?) pour')
    return {'name': name, 'nationality': nationality, 'age': age, 'birthday': birthday, 'weight': weight, 'height': height}


def find_in_regex(text: str, regex: str) -> str:
    # Return a string equal to the regex given. 
    try:
        token = re.search(regex, text).group(1)
    except AttributeError:
        # regex not found then
        token = 'NA' 
    return token
"""