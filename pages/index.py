title = 'Portfolio'

class Card:
    def __init__(self, section, url, name, description, image):
        self.section = section; self.url = url;
        self.image = image; self.name = name; self.description = description

cards = [
#joule bonding paper
#microgripper papers
#cargo robot
#couch
#AWG papers
#Link('2018', 'resources/research/automatic/poster.pdf', 'Automatic Electric Nanomanipulation Platform'),
#Link('2018', 'resources/research/nims/poster.pdf', 'Modeling Random Memristive Nanowire Networks'),
#Link('2017', 'resources/research/saw/poster.pdf', 'Piezoelectric RF-based SAW Energy Detectors'),
#Link('2016', 'resources/research/hitr/hitr.jpg', 'Head Impact Test Rig'),
#Link('2016', 'resources/research/fire/poster.pdf', 'Energy Storage Demo Rig'),
#Link('2015', 'resources/research/uav/poster.pdf', 'Unmanned Aerial Vehicle Detection via Acoustic Feature Extraction')

Card('2024', 'resources/dissertation-dteal.pdf', 'PhD Thesis: Printing Silicon', '<p>Multimaterial Nanoscale Printing</p><p>via Charged Nanoparticle Deposition</p>', 'resources/projects/2024-multimaterial/octothorpe-thumb.jpg'),
Card('2024', 'resources/projects/2024-vacuum/vacuum.jpg', 'Vacuum Nanoparticle Deposition', '<p>custom vacuum+process equipment for research</p><p>(see PhD dissertation for detail)</p>', 'resources/projects/2024-vacuum/thumb.jpg'),
Card('2024', 'resources/projects/2024-wavegen/wavegen.jpg', 'HV Arbitrary Waveform Generator', '<p>modular ±100V 1MHz programmable outputs</p><p>(see PhD dissertation for detail)</p>', 'resources/projects/2024-wavegen/wavegen-thumb.jpg'),
Card('2023', 'resources/projects/2023-ee143/wafer.jpg', 'NMOS Transistors', 'from teaching Berkeley\'s EE143 microfabrication course', 'resources/projects/2023-ee143/thumb.jpg'),
Card('2022', 'resources/projects/2022-joule-bonding/joulebonding.pdf', 'Localized Joule Heating', 'playing with on-chip multipoint temperature control</p><p> https://doi.org/10.1109/MEMS51670.2022.9699553', 'resources/projects/2022-joule-bonding/thumb.jpg'),
Card('2021', 'resources/projects/2021-robust-inchworm-motors/robustinchworms.pdf', 'Better Robust MEMS Motors', 'including the world\'s longest MEMS electrostatic motor</p><p>https://doi.org/10.1109/Transducers50396.2021.9495446', 'resources/projects/2021-robust-inchworm-motors/thumb.jpg'),
Card('2020', 'resources/projects/2020-gripper/grippers.pdf', 'MEMS Microrobot Grippers', 'demonstrating macroscopic MEMS electrostatic motors</p><p> https://doi.org/10.1109/MEMS46641.2020.9056128', 'resources/projects/2020-gripper/thumb.jpg'),
Card('2019', 'resources/projects/couch.jpg', 'Robotic Couch', 'motorized all-terrain cushioned seating', 'resources/projects/couch-thumb.jpg'),
Card('2019', 'resources/projects/automatic/poster.pdf', 'Nanowire Manipulation Platform', 'electric tweezers system for nanowire control research', 'resources/projects/awg.png'),
Card('2018', 'resources/projects/alluvial_highres.jpg', 'Alluvial', 'three-day hexapod robot', 'resources/projects/alluvial.png'),
Card('2018', 'resources/projects/nims/poster.pdf', 'Nanowire Experiments', 'investigating nanowire network electrical behavior', 'resources/projects/nims/thumb.jpg'),
Card('2018', 'http://web.archive.org/web/20181108210059/http://ras.ece.utexas.edu/', 'UT IEEE RAS Website', 'rewritten in Bootstrap', 'resources/projects/ras.png'),
Card('2017', 'resources/projects/curmudgeon_highres.png', 'Curmudgeon', 'three-day jumping robot', 'resources/projects/curmudgeon.png'),
Card('2017', 'resources/projects/saw/poster.pdf', 'Microfabricated Piezo Sensors', 'surface acoustic wave energy harvesting devices', 'resources/projects/saw/device-thumb.jpg'),
Card('2016', 'resources/projects/liberty_highres.jpg', 'Freedom to Make', 'maker spirit statue', 'resources/projects/liberty.jpg'),
Card('2016', 'resources/projects/chess_highres.jpg', 'Lasered Chess', 'an exercise in rapid prototyping', 'resources/projects/chess.jpg'),
Card('2016', 'resources/projects/mesa_highres.jpg', 'Battletank Mesa', 'dual-monitor workstation', 'resources/projects/mesa.jpg'),
Card('2016', 'resources/projects/piano_highres.png', 'PIano', 'Raspberry Pi keyboard system', 'resources/projects/piano.png'),
Card('2016', 'resources/projects/markovi_highres.jpg', 'MARKOVI', 'balancing robot chassis', 'resources/projects/markovi.jpg'),
Card('2016', 'resources/projects/dckx_highres.png', 'DCKX', 'xkcd headline illustrator', 'resources/projects/dckx.png'),
Card('2016', 'resources/projects/hitr/hitr.jpg', 'Head Impact Test Rig', 'ballistic baseball research system', 'resources/projects/hitr.png'),
Card('2016', 'resources/projects/fire/poster.pdf', 'Energy Storage Demo Rig', 'pumped-storage hydroelectricity demonstration model', 'resources/projects/fire.jpg'),
Card('2015', 'resources/projects/ultron_highres.jpg', 'Ultron', 'wooden competition roomba', 'resources/projects/ultron.jpg'),
Card('2015', 'resources/projects/sgi_highres.jpg', 'Sensel Gesture Interface', 'swiping keyboard with relative positioning', 'resources/projects/sgi.png'),
Card('2015', 'resources/projects/uav/poster.pdf', 'UAV Audio Detection', 'detecting quadcopters via audio signal processing', 'resources/projects/uav/uav.png'),
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


content = """<h1>Portfolio / Daniel Teal</h1>
<p>Hello, world.</p>
<p>I'm Daniel Teal, an engineer. I've just finished my PhD at Berkeley where I studied microfabrication. I appreciate kindness, freedom, morality, and a good day's work. I look forward to nanotechnology, spaceflight, and a good future.</p>
<p>Download my resume in PDF format <a href="resources/resume-dteal.pdf"><b>(here)</b></a>.</p>
<p>I build things. Hardware, software, electronics. Sometimes from the atoms up. Here are some of them in chronological order. Some counts as research.</p>
"""

sections = []
for card in cards:
    if not card.section in sections:
        sections.append(card.section)
        content += '<h3 class="section">' + card.section + '</h3>\n'
    content += '<a class="card"' + (' href="' + card.url + '"' if card.url else '') + '>\n'
    content += '<div class="left"><img src="' + card.image + '" alt="' + card.name + '"></div>\n'
    content += '<div class="right"><h2>' + card.name + '</h2><p>' + card.description + '</p></div></a>\n'

