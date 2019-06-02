title = 'Research'

class Link:
    def __init__(self, section, url, name):
        self.section = section; self.url = url; self.name = name

links = [
Link('2018', 'resources/research/automatic/poster.pdf', 'Automatic Electric Nanomanipulation Platform'),
Link('2018', 'resources/research/nims/poster.pdf', 'Modeling Random Memristive Nanowire Networks'),
Link('2017', 'resources/research/saw/poster.pdf', 'Piezoelectric RF-based SAW Energy Detectors'),
Link('2016', 'resources/research/hitr/hitr.jpg', 'Head Impact Test Rig'),
Link('2016', 'resources/research/fire/poster.pdf', 'Energy Storage Demo Rig'),
Link('2015', 'resources/research/uav/poster.pdf', 'Unmanned Aerial Vehicle Detection via Acoustic Feature Extraction')
]

content="""<header>
<h1>Research / Daniel Teal</h1>
<p>Some of what I do counts as science. Here it is, in chronological order. </p>
<p>You may also be interested in my <a href="projects.html">projects</a>.</p>
</header>"""

sections = []
for link in links:
    if not link.section in sections:
        sections.append(link.section)
        content += '<div class="section">' + link.section + '</div>\n'
    content += '<a href="' + link.url + '" class="link">' + link.name + '</a>\n'
