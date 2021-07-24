'''Base module for YTScraper'''
from commander import Commander

if __name__ == '__main__':
    keyboard_input = input('Please input a full YouTube video/playlist link:\n')
    commander_obj = Commander()

    if 'playlist' in keyboard_input:
        commander_settings = {'set_dataprocessor': 'playlist',
                              'set_scraper': 'requests'}
        commander_obj.execute(commander_settings)

        playlist_settings = {'link': keyboard_input,
                             'parse': True,
                             #'save': True,
                             'display': False}
        commander_obj.execute(playlist_settings)
        playlist_data = commander_obj.dataprocessor.current_data

        commander_settings = {'set_dataprocessor': 'video',
                              'set_scraper': 'requests',
                              'set_recommender': 'simple'}
        commander_obj.execute(commander_settings)

        video_settings = {'link': '',
                          'parse': True,
                          #'save': True,
                          'display': False,
                          'recommend': True}
        for video in playlist_data:
            video_settings['link'] = video
            commander_obj.execute(video_settings)

        commander_obj.recommend()

    elif 'watch' in keyboard_input:
        commander_settings = {'set_dataprocessor': 'video',
                              'set_scraper': 'requests'}
        commander_obj.execute(commander_settings)

        video_settings = {'link': keyboard_input,
                          'parse': True,
                          'save': True,
                          'display': True}
        commander_obj.execute(video_settings)
