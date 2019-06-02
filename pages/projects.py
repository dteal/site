title = 'Projects'

class Card:
    def __init__(self, section, url, name, description, image):
        self.section = section; self.url = url;
        self.image = image; self.name = name; self.description = description

cards = [
Card('2018', 'resources/projects/awg_highres.jpg', 'Automatic Nanomanipulation Platform', 'electric tweezers research system for nanowire control', 'resources/projects/awg.png'),
Card('2018', 'resources/projects/alluvial_highres.jpg', 'Alluvial', 'three-day hexapod robot', 'resources/projects/alluvial.png'),
Card('2018', 'https://ras.ece.utexas.edu', 'UT IEEE RAS Website', 'rewritten in Bootstrap', 'resources/projects/ras.png'),
Card('2017', 'resources/projects/curmudgeon_highres.png', 'Curmudgeon', 'three-day jumping robot', 'resources/projects/curmudgeon.png'),
Card('2016', 'resources/projects/liberty_highres.jpg', 'Freedom to Make', 'maker spirit statue', 'resources/projects/liberty.jpg'),
Card('2016', 'resources/projects/chess_highres.jpg', 'Lasered Chess', 'an exercise in rapid prototyping', 'resources/projects/chess.jpg'),
Card('2016', 'resources/projects/mesa_highres.jpg', 'Battletank Mesa', 'dual-monitor workstation', 'resources/projects/mesa.jpg'),
Card('2016', 'resources/projects/piano_highres.png', 'PIano', 'Raspberry Pi keyboard system', 'resources/projects/piano.png'),
Card('2016', 'resources/projects/markovi_highres.jpg', 'MARKOVI', 'balancing robot chassis', 'resources/projects/markovi.jpg'),
Card('2016', 'resources/projects/dckx_highres.png', 'DCKX', 'xkcd headline illustrator', 'resources/projects/dckx.png'),
Card('2016', 'resources/research/hitr/hitr.jpg', 'Head Impact Test Rig', 'ballistic baseball research system', 'resources/projects/hitr.png'),
Card('2016', 'resources/research/fire/poster.pdf', 'Energy Storage Demo Rig', 'pumped-storage hydroelectricity demonstration model', 'resources/projects/fire.jpg'),
Card('2015', 'resources/projects/ultron_highres.jpg', 'Ultron', 'wooden competition roomba', 'resources/projects/ultron.jpg'),
Card('2015', 'resources/projects/sgi_highres.jpg', 'Sensel Gesture Interface', 'Swype-style keyboard with relative positioning', 'resources/projects/sgi.png'),
Card('2015', 'resources/projects/giraphphe_highres.jpg', 'GiraPHPHe', 'FTC Team 4290 2014-2015 pneumatic powerhouse', 'resources/projects/giraphphe.png'),
Card('2014', 'resources/projects/fermi_highres.jpg', 'FERmi 14', 'symmetrical teleoperated sumobot', 'resources/projects/fermi.jpg'),
Card('2014', 'resources/projects/pov.gif', 'POV Globe', 'persistence-of-vision LEDs', 'resources/projects/pov.png'),
Card('2014', 'resources/projects/4290_2014_highres.png', 'FTC 4290 2013-2014', 'experiments in gearing', 'resources/projects/4290_2014.png'),
Card('2014', 'resources/projects/sinusoidesque_highres.png', 'Sinusoidesque', 'simple arbitrary "sinusoid" visualizer', 'resources/projects/sinusoidesque.png'),
Card('2013', 'resources/projects/4290_2013_highres.png', 'FTC 4290 2012-2013', 'holonomic drives are hard', 'resources/projects/4290_2013.png'),
Card('2012', 'resources/projects/creator_3d_highres.png', 'Creator 3D', '"stochastic" "constraint solving" CAD sketcher', 'resources/projects/creator_3d.png'),
Card('2012', 'resources/projects/phobia_highres.jpg', 'PHobia', 'FTC Team 4290 2011-2012 gateway competition robot', 'resources/projects/phobia.png'),
Card('2012', 'resources/projects/tetris_highres.png', 'Tetris', 'blocks in TI-89 TI-BASIC', 'resources/projects/tetris.png'),
Card('2012', 'resources/projects/mendelssohn_highres.png', 'Mendelssohn', '3D printing from scratch', 'resources/projects/mendelssohn.png'),
]

content="""<header>
<h1>Projects / Daniel Teal</h1>
<p>I build things. Hardware, software, electronics. Here are some of them in chronological order.</p>
<p>Some favorites are the Automatic Electric Nanomanipulation platform, the Head Impact Test Rig, Ultron, and GiraPHPHe.</p>
<p>You may also be interested in my <a href="research.html">research</a>.</p>
</header>"""

sections = []
for card in cards:
    if not card.section in sections:
        sections.append(card.section)
        content += '<div class="section">' + card.section + '</div>\n'
    content += '<a class="card"' + (' href="' + card.url + '"' if card.url else '') + '>\n'
    content += '<div class="left"><img src="' + card.image + '" alt="' + card.name + '"></div>\n'
    content += '<div class="right"><h2>' + card.name + '</h2><p>' + card.description + '</p></div></a>\n'

