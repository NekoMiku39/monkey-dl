"""
Important notes to developers:

Some of the websites are using Cloudflare to protect their webistes. To bypass
Cloudflare protection, Monkey-DL is using Cloudscraper (https://github.com/VeNoMouS/cloudscraper) library.

However, since Cloudflare frequently changing their challenges, Cloudscraper needs to be constantly updated with the
newest version. Still, it is not guaranteed to be worked for all the websites.

In such events, Monkey-DL is relying on the Chrome/Firefox browser cookies using browser_cookie3 (
https://github.com/borisbabic/browser_cookie3) library to bypass Cloudflare. Which means, In order for the scrapers
to work, you need to visit the provided links first in either Chrome or Firefox web browser and let the browser store
cookies from Cloudflare for each of those websites.

Because of that, for the sake of passing the test cases below, it is advised to visit all the given URLs from either
Chrome or Firefox browser first.
"""

import sys
import json
import cloudscraper

try:
    from scrapers.animeflix.animeflix_scraper import AnimeFlixScraper
    from scrapers.animefreak.animefreak_scraper import AnimeFreakScraper
    from scrapers.animepahe.animepahe_scraper import AnimePaheScraper
    from scrapers.animetake.animetake_scraper import AnimeTakeScraper
    from scrapers.animeultima.animeultima_scraper import AnimeUltimaScraper
    from scrapers.fouranime.fouranime_scraper import FourAnimeScraper
    from scrapers.gogoanime.gogoanime_scraper import GoGoAnimeScraper
    from scrapers.nineanime.nineanime_scraper import NineAnimeScraper
    from scrapers.twist.twist_scraper import TwistScraper

except ModuleNotFoundError:
    sys.path.append("monkey_dl")

    from scrapers.animeflix.animeflix_scraper import AnimeFlixScraper
    from scrapers.animefreak.animefreak_scraper import AnimeFreakScraper
    from scrapers.animepahe.animepahe_scraper import AnimePaheScraper
    from scrapers.animetake.animetake_scraper import AnimeTakeScraper
    from scrapers.animeultima.animeultima_scraper import AnimeUltimaScraper
    from scrapers.fouranime.fouranime_scraper import FourAnimeScraper
    from scrapers.gogoanime.gogoanime_scraper import GoGoAnimeScraper
    from scrapers.nineanime.nineanime_scraper import NineAnimeScraper
    from scrapers.twist.twist_scraper import TwistScraper


class TestScrapers:

    def test_animeflix_scraper(self):
        """Unit test for AnimeFlix."""
        session = cloudscraper.create_scraper()
        assert len(AnimeFlixScraper("https://animeflix.io/shows/one-piece", 1, 4, session).get_direct_links()) > 0

    def test_animefreak_scraper(self):
        """Unit test for AnimeFreak."""
        session = cloudscraper.create_scraper()
        assert len(AnimeFreakScraper("https://www.animefreak.tv/watch/one-piece", 1, 4, session).get_direct_links()) > 0

    def test_animepahe_scraper(self):
        """Unit test for AnimePahe. Does not work without 2captcha key"""
        try:
            with open("monkey_dl/settings.json", "r") as st:
                data = json.load(st)
                api_key = data["api_key"]
                print(api_key)
                if api_key != "" or api_key != "insert_2captcha_api_key":
                    session = cloudscraper.create_scraper(
                        recaptcha={
                            'provider': '2captcha',
                            'api_key': api_key
                        }
                    )
                else:
                    session = cloudscraper.create_scraper()

        except FileNotFoundError:
            raise FileNotFoundError("Settings not found at : {path}".format(path=sys.path))

        assert len(AnimePaheScraper("https://animepahe.com/anime/one-piece", 1, 4, session).get_direct_links()) > 0
    #
    def test_animetake_scraper(self):
        """Unit test for AnimeTake."""
        session = cloudscraper.create_scraper()
        assert len(AnimeTakeScraper("https://animetake.tv/anime/one-piece", 1, 4, session).get_direct_links()) > 0

    # def test_gogoanime_scraper(self):
    #     """Unit test for GoGoAnime."""
    #     session = cloudscraper.create_scraper()
    #     assert len(GoGoAnimeScraper("https://www.gogoanime.io/one-piece", 1, 4, session).get_direct_links()) > 0
    #
    def test_twist_scraper(self):
        """Unit test for Twist."""
        session = cloudscraper.create_scraper()
        assert len(TwistScraper("https://twist.moe/a/one-piece", 1, 4, session).get_direct_links()) > 0

    def test_fouranime_scraper(self):
        """Unit test for 4Anime."""
        session = cloudscraper.create_scraper()
        assert len(FourAnimeScraper("https://4anime.to/anime/one-piece", 1, 4, session).get_direct_links()) > 0