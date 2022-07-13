from pylatex.utils import NoEscape
from pylatex.base_classes import CommandBase, Arguments, Environment
from pylatex.package import Package
from datetime import date


class EnumItem(Environment):
    _latex_name = 'itemize'
    packages = [Package('enumitem'), ]


class Item(CommandBase):
    _latex_name = 'item'
    packages = [Package('enumitem'), ]


class Job:
    def __init__(self, date_begin, date_end, title, company, format, description, hide=False):
        self.date_begin = date_begin
        self.date_end = date_end
        self.title = title
        self.company = company
        self.format = format
        self.description = description
        self.hide = hide

    def dates(self):
        begin = self.date_begin.strftime('%b %Y')
        if self.date_end:
            end = self.date_end.strftime('%b %Y')
        else:
            end = '...'
        return NoEscape(f'{begin} -\\\\{end}')


jobs = [
    Job(
        date(2013, 6, 1),
        None,
        'IT Support',
        NoEscape('\\textbf{Alexsupport}'),
        'Fulltime',
        EnumItem(arguments=[
            Item('System and network administration'),
            Item('Workflow organization'),
            Item('Contact with clients'),
        ]),
    ),
    Job(
        date(2017, 11, 1),
        None,
        'Fullstack developer(JS, Python)',
        '\href{https://anzujewelry.com/}{\\textbf{Anzu Jewelry}}',
        'Contract',
        EnumItem(arguments=[
            Item('System for accounting production in jewelry workshop'),
            Item('Integration with digital registration system of precious metals'),
        ]
        ),
    ),
    Job(
        date(2022, 3, 1),
        None,
        'Github Administrator',
        '\href{https://yourcodereview.com/}{\\textbf{YourCodeReview}}',
        'Part-time',
        EnumItem(arguments=[
            Item('Preparation and publication projects for code review.'),
        ]
        ),
        hide=True
    ),
    Job(
        date(2019, 12, 1),
        date(2020, 2, 1),
        'Python Developer',
        '\\textbf{Alexsupport}',
        'Part-time',
        EnumItem(arguments=[
            Item('Telegram bot for reserving tables in restaurant'),
        ]
        ),
    ),
    Job(
        date(2017, 11, 1),
        date(2019, 10, 1),
        'Fullstack developer(JS, Python) ',
        '\href{https://anzujewelry.com/}{\\textbf{Anzu Jewelry}}',
        'Contract',
        EnumItem(arguments=[
            Item('System for accounting production in jewelry workshop'),
        ]
        ),
        hide=True
    ),
    Job(
        date(2018, 9, 1),
        date(2019, 3, 1),
        'Python Developer',
        '\\textbf{Alexsupport}',
        'Part-time',
        EnumItem(arguments=[
            Item('Employers had to ask clients to send photos of incidents via telegram to private messengers'),
            Item('Develop telegram bot for contacting with clients'),
            Item(
                'Our bot resending messages from chat associated with site(usually - restaurant) to our backend chat.'),
            Item('Such organization allowed us to contact, with manager on shift. Managers able to send'
                 'photos to describe incidents shortly. When the duty manager changes, they easy get information about'
                 'current incidents.'),
        ]
        ),
    ),
    Job(
        date(2018, 1, 1),
        date(2018, 12, 1),
        'Developer(Python, C++) ',
        '\\textbf{Alexsupport}',
        'Part-time',
        EnumItem(arguments=[
            Item('Developing flexible personal discount system for restraunt management company.'),
        ]
        ),
    ),
    Job(
        date(2014, 1, 1),
        date(2014, 12, 1),
        'System Developer(Python)',
        '\\textbf{Alexsupport}',
        'Part-time',
        EnumItem(arguments=[
            Item('Clients prefered use their own ticket system'),
            Item('We wanted to make possible to work with them all from one point'),
            Item(
                'Develop django application for syncronization tickets from clients ticket-systems to one we was using'),
            Item('Later some clients agreed to use the same system.'),
        ]
        ),
        hide=True,
    ),
    Job(
        date(2011, 3, 1),
        date(2014, 2, 1),
        'System Developer(Python) ',
        '\\textbf{Alexsupport}',
        'Part-time',
        EnumItem(arguments=[
            Item('Users contact with specialists directly by phones.'),
            Item('We wanted to deploy pbx with possibility to receive calls outside the office'),
            Item('I have deployed asterisk and develop tool to manage calls.'
                 'It was first time managed by usual dialplan with sql,'
                 'lua-dialpan via AMI and bash script, and finally Django app via AGI.'),
            Item('A functioning PBX with mobile employees and management via telegram'),
        ]
        ),
    ),
    Job(
        date(2011, 6, 1),
        date(2013, 6, 1),
        'System and database administrator ',
        '\\textbf{Mallina LTD}',
        '',
        EnumItem(arguments=[
            Item('System and network administration'),
        ]
        ),
    ),
    Job(
        date(2011, 3, 1),
        date(2013, 6, 1),
        'It Support ',
        '\\textbf{Mallina LTD}',
        '',
        EnumItem(arguments=[
            Item('Resolving IT-like problems'),
            Item('Contact with users'),
        ]
        ),
    ),
    Job(
        date(2008, 1, 1),
        date(2011, 5, 1),
        'It Technician',
        '\href{https://www.bmstu.ru/}{\\textbf{BMSTU}}',
        '',
        EnumItem(arguments=[
            Item('Administration, maintenance and upgrade of computer class'),
        ])
    ),
]

educations = [
    Job(
        date(2021, 12, 1),
        date(2022, 8, 1),
        '',
        '\href{https://practicum.yandex.ru/promo/devops-course}{\\textbf{Yandex Practicum}}',
        '',
        'DevOps - for use and development. A course for experienced professionals'),
    Job(
        date(2017, 9, 1),
        date(2020, 6, 1),
        '',
        '\href{https://www.bmstu.ru/}{\\textbf{Bauman Moscow State Technical University}}',
        '',
        'Plasma engine\'s specialization - incomplete',
    ),
]
