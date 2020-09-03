#!/usr/bin/python3
"""Create site."""

import os
import shutil

def create():
    """Create site."""

    # clean output directory
    shutil.rmtree('bin')
    os.mkdir('bin')

    # create pages
    pages = [f[:-3] for f in os.listdir('pages') if f[-3:] == '.py']
    for page in pages:
        data = {}
        with open('pages/{}.py'.format(page)) as source:
            exec(source.read(), {}, data)
        output = open('bin/{}.html'.format(page), 'w')
        output.write(head(data['title']))
        output.write(navbar())
        output.write(data['content'])
        output.write(footer())
        output.close()

    # copy resources
    shutil.copytree('resources', 'bin/resources')

    # copy other
    for item in os.listdir('special'):
        if os.path.isfile('special/{}'.format(item)):
            shutil.copy('special/{}'.format(item), 'bin/{}'.format(item))
        else:
            shutil.copytree('special/{}'.format(item), 'bin/{}'.format(item))

def head(title):
    """Create head string."""
    output = ''
    output += '<!doctype html>\n'
    output += '<html lang="en">\n'
    output += '<head>\n'
    output += '<title>' + title + ' - Daniel Teal</title>\n'
    output += '<meta charset="utf-8">\n'
    output += '<meta name="referrer" content="no-referrer">\n'
    output += '<link rel="stylesheet" type="text/css" href="resources/style.css">\n'
    output += '<link rel="icon" type="image/x-icon" href="resources/favicon.ico">\n'
    output += '</head>\n'
    output += '<body>\n'
    return output

def navbar():
    """Create navbar string."""
    pages = ['index', 'projects', 'research', 'links', 'about']
    output = ''
    output += '<nav>\n'
    for page in pages:
        output += '<a href="' + page + '.html">' + page.upper() + '</a>\n'
    output += '</nav>\n'
    return output

def footer():
    """Create footer string."""
    import datetime
    license_link = 'http://creativecommons.org/publicdomain/zero/1.0/'
    license_image = 'resources/cc-zero.svg'
    license_notice = 'To the extent possible under law, Daniel Teal has' \
                     ' waived all copyright and related or neighboring' \
                     ' rights to this website. This work is published' \
                     ' from the United States.'
    date = datetime.datetime.today().strftime('%d %B %Y')
    output = ''
    output += '<footer>\n'
    output += '<div class="license">\n'
    output += '<a rel="license" href="' + license_link + '">'
    output += '<img src="' + license_image + '" alt="CC0"/>'
    output += '</a>\n'
    output += '<p>' + license_notice + '</p>\n'
    output += '</div>\n'
    output += '<div class="update">\n'
    output += 'This site was last updated on {}.\n'.format(date)
    output += '</div>\n'
    output += '</footer>\n'
    output += '</body>\n'
    output += '</html>'
    return output

if __name__ == "__main__":
    create()
