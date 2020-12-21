from web_scraper.scraper import get_citations_needed_report, get_citations_needed_count
from web_scraper import __version__

def test_version():
    assert __version__ == '0.1.0'

url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def test_get_number_of_citation_needed():
    actual = 5
    expected = get_citations_needed_count(url)
    assert actual == expected

def test_get_report_of_citation_needed():
    get_citations_needed_report(url)
    assert "The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][7] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.\n" 

