title = 'Links'

class Link:
    def __init__(self, section, url, name):
        self.section = section; self.url = url; self.name = name

links = [
Link('News', 'https://hackaday.com', 'Hackaday : viz, articles on crazy engineering projects'),
Link('News', 'https://news.ycombinator.com', 'Hacker News : a mostly-software-related news aggregator'),
Link('News', 'https://slashdot.org', 'Slashdot : "News for nerds, stuff that matters."'),
Link('News', 'https://www.nytimes.com', 'The New York Times : the canonical world news source'),
Link('References', 'https://en.wikipedia.org/wiki/Main_Page', 'Wikipedia : the nascent <em>Encyclopedia Galactica</em>'),
Link('References', 'https://oeis.org', 'The On-Line Encyclopedia of Integer Sequences (OEIS).'),
Link('Vendors', 'https://www.mcmaster.com/#', 'McMaster-Carr : <em>the</em> American hardware vendor'),
Link('Vendors', 'https://www.digikey.com', 'Digi-Key : McMaster-Carr for electronics'),
Link('Vendors', 'https://www.pololu.com', 'Pololu : small robot parts'),
Link('Vendors', 'https://www.dreamhost.com', 'Dreamhost : excellent web hosting'),
Link('Vendors', 'https://darksky.net', 'Dark Sky : sufficiently modern weather forecasting'),
Link('Journals', 'https://www.nature.com/nature/', 'Nature : the premier scientific journal'),
Link('Journals', 'https://www.nature.com/nnano/', 'Nature Nanotechnology : nanotechnology from the Nature publishing group'),
Link('Journals', 'https://onlinelibrary.wiley.com/journal/15214095', 'Advanced Materials : best of materials science'),
Link('Journals', 'https://onlinelibrary.wiley.com/journal/16163028', 'Advanced Functional Materials : more materials science'),
Link('Journals', 'https://pubs.acs.org/journal/ancac3', 'ACS Nano : nanoscience'),
Link('Libraries', 'https://www.gutenberg.org', 'Project Gutenberg : public domain e-books'),
Link('Libraries', 'https://pixabay.com', 'Pixabay : public domain images'),
Link('Libraries', 'http://magnatune.com', 'Magnatune : DRM-free music'),
]

content="""<header>
<h1>Links / Daniel Teal</h1>
<p>Herein lie portals to stupendously awesome websites I find useful.</p>
</header>"""

sections = []
for link in links:
    if not link.section in sections:
        sections.append(link.section)
        content += '<div class="section">' + link.section + '</div>\n'
    content += '<a href="' + link.url + '" class="link">' + link.name + '</a>\n'
