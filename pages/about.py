title = 'About'

content="""<h1>About / Daniel Teal</h1>
<p>Hello, world.</p>
<p>I'm Daniel Teal, an engineer. I'm finishing my PhD at Berkeley (update October 2024: dissertation talk is complete and I'm in the process of turning in my dissertation!) where I study microfabrication. I appreciate kindness, freedom, morality, and a good day's work. I look forward to nanotechnology, spaceflight, and a good future.</p>
<p>My main interest is semiconductor manufacturing equipment. I'm a mechanical engineer with additional experience in semiconductor microfabrication and processing, electronics, and software.</p>
<p>Please contact me at <b>dteal at dteal dot org</b>. I'm happy to talk!</p>
<p>My key is <a href="resources/dteal.asc"><b>903D 4542 C569 5735 232D  C027 C24D 4FF7 94B4 E724</b></a>.</p>
<p>(<a href="resources/dteal-old.asc">previous key</a>)</p>
<p>Download my resume in PDF format <a href="resources/resume-dteal.pdf"><b>here</b></a>.</p>
<p>You may be interested in my <a href="portfolio.html"><b>projects</b></a>, but can also find me at:</p>
<table class="references">
<tr>
<td><a href="https://www.linkedin.com/in/dteal/" class="link">LinkedIn</a></td>
<td><a href="https://github.com/dteal" class="link">GitHub</a></td>
<td><a href="https://scholar.google.com/citations?user=iCdq_ZsAAAAJ" class="link">Scholar</a></td>
</tr>
</table>
"""

content += '<div class="cvheading"><h2>Experience</h2><div class="cvline"></div></div>\n'
content += '<table class="cvtable">\n'

class Experience:
    def __init__(self, date, location, position, description):
        self.date=date; self.location=location; self.position=position; self.description=description
experiences = [
Experience('7/19-10/24', 'University of California, Berkeley', 'electrical engineering PhD student', 'Studied microfabrication. Developed direct-write nanoparticle deposition techniques. Built custom vacuum chambers, electronics, and process equipment. Also built world\'s longest MEMS electrostatic motor in Berkeley Marvell NanoLab research fab. Advised by Prof. Kristofer Pister.'),
Experience('8/22-5/24', 'Berkeley EE143 Microfabrication', 'lead teaching assistant', 'Taught hands-on lab course (Berkeley EE143) building NMOS transistors from scratch on silicon wafers, four semesters in a row. Instructed students, maintained equipment, troubleshot processes, and managed other TAs.'),
Experience('8/17-6/19', 'Fan Nanomaterial Innovation Lab', 'research assistant', 'Automated nanowire assembly. Implemented computer vision-based detection of nanowires at ≈ 500 Hz and a custom FPGA-based programmable 4-channel arbitrary function generator for vastly improved electric tweezers control.'),
Experience('5/18-8/18', 'NNCI iREU : Nano Functionality Integration Group', 'research intern', 'Studied neuromorphic computation in random PVP@Ag nanowire networks via computer simulations and physical experiment. Learned international research culture in Tusukuba, Japan.'),
Experience('6/17-8/17', 'REU : Cornell NanoScale Facility', 'research intern', 'Created low power voltage rectifiers in the CNF fab. Performed mask design, photolithography, evaporation, graphene application, automated 200 MHz electrical tests, and UHF vibrometry.'),
Experience('9/15-5/19', 'UT Longhorn Maker Studios', 'student assistant', 'Trained students for and maintained laser cutters and 3D printers. Attained proficiency in rapid prototyping equipment. Proposed and ran large student hardware hackathon in collaboration with ME Undergraduate Advisory Board.'),
Experience('9/15-5/19', 'UT IEEE Robotics & Automation Society', 'Robotathon & webmaster', 'Organized the annual RAS introductory student robotics competition, Robotathon, while rewriting and maintaining the club website. Also built assorted small robots and large robotic couch.'),
Experience('8/17-5/19', 'UT ME Undergraduate Advisory Board', 'member', 'Proposed, designed, and ran the first UT engineering Createathon hardware hackathon with ≈ 50 students and multiple corporate sponsors in collaboration with the UT makerspace. Organized the second a year later.'),
Experience('11/16-5/17', 'Zheng Research Group', 'research assistant', 'Reviewed plasmonic nanostructures.'),
Experience('11/15-11/16', 'UT Advanced Manufacturing Center', 'research assistant', 'Designed and fabricated head impact metrology equipment for future research. Mounted 30 psi baseball air cannon to steel frame and SLS nylon dummy head. Automated measurements and tested high-speed camera.'),
Experience('6/15-8/15', 'UT Applied Research Laboratories', 'intern', 'Acoustically detected unmanned aerial vehicles. Used digital signal processing to estimate range of common Phantom 3 pro quadcopter from analysis of its ultrasonic altitude finder and propeller noise under laboratory conditions.'),
Experience('9/11-6/15', 'FIRST Tech Challenge Robotics Team', 'design & build lead', 'Lead team to become 2014-2015 world competition finalists. Designed in CAD and fabricated most of unorthodox leafblower-based wooden structure.'),
Experience('6/11-8/15', 'DIY 3D Printer Design & Construction', 'hobbyist', 'Self-taught mechatronics by evolving generations of FDM machines.'),
]
for experience in experiences:
    content += '<tr><td class="left">' + experience.date + '</td>\n'
    content += '<td class="right"><b>' + experience.location + '</b><br><em>' + experience.position + '</em><p>' + experience.description + '</p></td></tr>\n'

content += '</table>\n' #experience

content += '<div class="cvheading"><h2>Education</h2><div class="cvline"></div></div>\n'
content += '<table class="cvtable">\n'
content += """
<tr><td class="left">2019-2024</div>
<td class="right"><b>University of California, Berkeley</b><br><em>PhD Electrical Engineering and Computer Science</em><p>microfabrication and process engineering, MEMS</p></td></tr>
<tr><td class="left">2015-2019</div>
<td class="right"><b>University of Texas at Austin</b><br><em>BS Mechanical Engineering, BS Mathematics</em><p>solids/dynamics, materials science, dynamic systems, thermodynamics, organic chemistry, heat transfer, numerical analysis</p></td></tr>
"""
content += '</table>\n' #education

content += '<div class="cvheading"><h2>Honors</h2><div class="cvline"></div></div>\n'
content += '<table class="cvtable">\n'
experiences = [
Experience('2020 and 2024', 'Fall BSAC Conference Best Presentation Award', '', ''),
Experience('2022-2023', 'Demetri Angelakos Memorial Achievement Award', '', ''),
Experience('2019', 'NSF GRFP Fellowship', '', ''),
]
for experience in experiences:
    content += '<tr><td class="left">' + experience.date + '</td>\n'
    #content += '<td class="right"><b>' + experience.location + '</b>, <em>' + experience.position + '</em></td></tr>\n'
    # no comma after award name
    content += '<td class="right"><b>' + experience.location + '</b> <em>' + experience.position + '</em></td></tr>\n'
content += '</table>\n' #honors

content += '<div class="cvheading"><h2>Skills</h2><div class="cvline"></div></div>\n'
content += '<table class="cvtable">\n'
class Skill:
    def __init__(self, domain, tools):
        self.domain = domain; self.tools = tools
skills=[
Skill('Microfabrication', 'MEMS, litho, deposition, etching, metrology, packaging'),
Skill('Hardware', 'part design/simulation/fab, thermal/vacuum systems'),
Skill('Prototyping', '3D printing, laser cutting, CNC'),
Skill('Electronics', 'KiCad PCB design, analog electronics, some embedded'),
Skill('CAD + FEA', 'SolidWorks, Fusion, SIMION, some ANSYS & COMSOL'),
Skill('Software', 'Python, C/C++, Rust, LaTeX, Linux, HTML/CSS'),
]
for skill in skills:
    content += '<tr><td class="left"><b>' + skill.domain + '</b></td>\n'
    content += '<td class="right">' + skill.tools + '</td></tr>\n'
content += '</table>\n' #skills

