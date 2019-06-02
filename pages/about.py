title = 'About'

content="""<header>
<h1>About / Daniel Teal</h1>
<p>Hello, world.</p>
<p>I'm Daniel Teal, a mechanical engineer and mathematician. I'm a graduate student at Berkeley, where I design and build tiny robots. I appreciate freedom, morality, and a good day's work. I look forward to nanotechnology, spaceflight, and globalization.</p>
<p>I am interested in nanomanufacturing, self-assembly, and computation.</p>
<p>Please contact me at <b>daniel at teals dot org</b>.</p>
<p>My key is <a href="resources/dteal.asc"><b>D127 41E4 9070 D3D0 F9E7  CDD8 F785 AAF2 07BD F883</b></a>.</p>
<p>You may be interested in my <a href="research.html"><b>research</b></a> or <a href="projects.html"><b>projects</b></a>, but can also find me at:</p>
<table class="references">
<tr>
<td><a href="https://www.linkedin.com/in/dteal/" class="link">LinkedIn</a></td>
<td><a href="https://github.com/dteal" class="link">GitHub</a></td>
<td><a href="https://orcid.org/0000-0002-4006-3204" class="link">ORCID</a></td>
</tr>
</table>
<p>Below is my CV. You can download it in PDF form <a href="resources/cv-dteal.pdf"><b>here</b></a>.</p>
</header>
<table class="cv">
<tr><td colspan=2 class="table-section">Education</td></tr>
<tr><td class="left">2015-2019</div>
<td class="right"><b>University of Texas at Austin</b>,<br><em>Mechanical Engineering &amp; Mathematics, 3.88/4.00</em>.<p>nanopatterning, nanoenergy, materials science, dynamic systems, thermodynamics, organic chemistry, heat transfer, numerical analysis</p></td></tr>
<tr><td class="left">2011-2015</div>
<td class="right"><b>Liberal Arts and Science Academy High School</b>.</td></tr>
"""

content += '<tr><td colspan=2 class="table-section">Experience</td></tr>'

class Experience:
    def __init__(self, date, location, position, description):
        self.date=date; self.location=location; self.position=position; self.description=description
experiences = [
Experience('8/17-now', 'Fan Nanomaterial Innovation Lab', 'research assistant', 'Automating nanowire assembly. Implemented computer vision-based detection of nanowires at ≈ 500 Hz and a custom FPGA-based programmable 4-channel arbitrary function generator for vastly improved electric tweezers control.'),
Experience('5/18-8/18', 'NNCI iREU : Nano Functionality Integration Group', 'research intern', 'Studied neuromorphic computation in random PVP@Ag nanowire networks via computer simulations and physical experiment. Learned international research culture in Tusukuba, Japan.'),
Experience('6/17-8/17', 'REU : Cornell NanoScale Facility', 'research intern', 'Created low power voltage rectifiers in the CNF fab. Performed mask design, photolithography, evaporation, graphene application, automated 200 MHz electrical tests, and UHF vibrometry.'),
Experience('9/15-now', 'UT Longhorn Maker Studios', 'student assistant', 'Trained students for and maintained laser cutters and 3D printers. Attained proficiency in rapid prototyping equipment. Proposed and ran large student hardware hackathon in collaboration with ME Undergraduate Advisory Board.'),
Experience('9/15-now', 'UT IEEE Robotics & Automation Society', 'Robotathon & webmaster', 'Organized the annual RAS introductory student robotics competition, Robotathon, while rewriting and maintaining the club website. Also built assorted small robots and large robotic couch.'),
Experience('8/17-now', 'UT ME Undergraduate Advisory Board', 'member', 'Proposed, designed, and ran the first UT engineering Createathon hardware hackathon with ≈ 50 students and multiple corporate sponsors in collaboration with the UT makerspace.'),
Experience('11/16-5/17', 'Zheng Research Group', 'research assistant', 'Reviewed plasmonic nanostructures.'),
Experience('11/15-11/16', 'UT Advanced Manufacturing Center', 'research assistant', 'Designed and fabricated head impact metrology equipment for future research. Mounted 30 psi baseball air cannon to steel frame and SLS nylon dummy head. Automated measurements and tested high-speed camera.'),
Experience('6/15-8/15', 'UT Applied Research Laboratories', 'intern', 'Acoustically detected unmanned aerial vehicles. Used digital signal processing to estimate range of common Phantom 3 pro quadcopter from analysis of its ultrasonic altitude finder and propeller noise under laboratory conditions.'),
Experience('9/11-6/15', 'FIRST Tech Challenge Robotics Team', 'design & build lead', 'Lead team to become 2014-2015 world competition finalists. Designed in CAD and fabricated most of unorthodox leafblower-based wooden structure.'),
Experience('6/11-8/15', 'DIY 3D Printer Design & Construction', 'hobbyist', 'Self-taught mechatronics by evolving generations of FDM machines.'),
]
for experience in experiences:
    content += '<tr><td class="left">' + experience.date + '</td>\n'
    content += '<td class="right"><b>' + experience.location + '</b>, <em>' + experience.position + '</em>.<p>' + experience.description + '</p></td></tr>\n'
    

content += '<tr><td colspan=2 class="table-section">Honors &amp; Affiliations</td></tr>\n'

experiences = [
Experience('3/16-5/17', 'UT Longhorn Maker Studios Club', 'president', ''),
Experience('9/15-5/16', '512 Hyperloop', 'member', ''),
Experience('2015', 'ASME', 'student member', ''),
Experience('2017', 'IEEE', 'student member', ''),
Experience('2016', 'Tau Beta Pi', 'engineering honor society member', ''),
Experience('2016', 'Pi Tau Sigma', 'mechanical engineering honor society member', ''),
Experience('2015', 'National Merit Finalist', 'recipient', ''),
Experience('2013', 'National Honor Society', 'member', '')
]

for experience in experiences:
    content += '<tr><td class="left">' + experience.date + '</td>\n'
    content += '<td class="right"><b>' + experience.location + '</b>, <em>' + experience.position + '</em>.</td></tr>\n'

content += '<tr><td colspan=2 class="table-section">Skills</td></tr>'

class Skill:
    def __init__(self, domain, tools):
        self.domain = domain; self.tools = tools
skills=[
Skill('Tooling', 'Laser cutter, FDM 3D printer, cleanroom (var.), measurement (var.).'),
Skill('Domains', 'Mechanics, electronics, computation.'),
Skill('CAD', 'SolidWorks, Fusion 360, OpenSCAD.'),
Skill('Languages', 'Python; some C/C++, LabVIEW, Verilog, Java, HTML/CSS, TI-BASIC.'),
Skill('Software', 'Linux, Windows, Excel, MATLAB, Word, LaTeX.')
]
for skill in skills:
    content += '<tr><td class="left">' + skill.domain + '</td>\n'
    content += '<td class="right">' + skill.tools + '</td></tr>\n'

content += '</table>\n'
