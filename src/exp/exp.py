from datetime import date

from pylatex.base_classes import Arguments, CommandBase, Environment
from pylatex.package import Package
from pylatex.utils import NoEscape

from .job import Job


class EnumItem(Environment):
    _latex_name = "itemize"
    packages = [
        Package("enumitem"),
    ]


class Item(CommandBase):
    _latex_name = "item"
    packages = [
        Package("enumitem"),
    ]



anzu = Job(
    date(2017, 11, 1),
    None,
    "Fullstack developer(JS, Python)",
    "\href{https://anzujewelry.com/}{\\textbf{Anzu Jewelry}}",
    "Contract",
    "Develop and maintenance simple system for accounting production in jewelry workshop. "
    "In project used systemd, GitLab CI, docker-compose, postgresql. "
    "For asynchron integration with digital registration system of precious metals used celery and mongodb. "
    # "Highlight of this project - advanced nomenclature of products and subproducts."
    # "Also it was integrated with digital registration system of precious metals."
    # EnumItem(
    #     arguments=[
    #         Item("System for accounting production in jewelry workshop"),
    #         Item("Integration with digital registration system of precious metals"),
    #     ]
    # ),
)

reviewcode = Job(
    date(2022, 3, 1),
    None,
    "Github Administrator",
    "\href{https://yourcodereview.com/}{\\textbf{YourCodeReview}}",
    "Part-time",
    EnumItem(
        arguments=[
            Item("Preparation and publication projects for code review."),
        ]
    ),
)
anzu_first = Job(
    date(2017, 11, 1),
    date(2019, 10, 1),
    "Fullstack developer(JS, Python) ",
    "\href{https://anzujewelry.com/}{\\textbf{Anzu Jewelry}}",
    "Contract",
    EnumItem(
        arguments=[
            Item("System for accounting production in jewelry workshop"),
        ]
    ),
)

itsm_main = Job(
    date(2013, 6, 1),
    None,
    "IT Support",
    NoEscape("\\textbf{Alexsupport}"),
    "Fulltime",
    NoEscape(
        "\\begin{itemize}"
        "{\\item{Deploying and maintenance restaurant-specific products(iiko, r-keeper, sh4)}}"
        "{\\item{Deploying and maintenance popular products(IIS, MSSQL, MS Exchange, Postgresql, "
        "Active Directory, etc.)}}"
        "{\\item{Integration client's systems with outsource-projects}}"
        "{\\item{System and network administration(locals, vpn for internal services, public wifi's)}}"
        "\\end{itemize}"
    )
    # EnumItem(
    #     arguments=[
    #         Item("System and network administration"),
    #         Item("Workflow organization"),
    #         Item("Contact with clients"),
    #     ]
    # ),
)

itsm_tbbot = Job(
    date(2019, 12, 1),
    date(2020, 2, 1),
    "Python Developer",
    "\\textbf{Alexsupport}",
    "Part-time",
    "Develop telegram bot for reserving tables in restaurant, using only mongodb."
    # EnumItem(
    #     arguments=[
    #         Item("Telegram bot for reserving tables in restaurant"),
    #     ]
    # ),
)

itsm_resendbot = Job(
    date(2018, 9, 1),
    date(2019, 3, 1),
    "Python Developer",
    "\\textbf{Alexsupport}",
    "Part-time",
    "Develop and maintenance telegram bot for it-support restaurants. It's deployed on lxc, "
    "using postgresql, mongodb, django, celery"
    # EnumItem(
    #     arguments=[
    #         Item(
    #             "Employers had to ask clients to send photos of incidents via telegram to private messengers"
    #         ),
    #         Item("Develop telegram bot for contacting with clients"),
    #         Item(
    #             "Our bot resending messages from chat associated with site(usually - restaurant) to our backend chat."
    #         ),
    #         Item(
    #             "Such organization allowed us to contact, with manager on shift. Managers able to send"
    #             "photos to describe incidents shortly. When the duty manager changes, they easy get information about"
    #             "current incidents."
    #         ),
    #     ]
    # ),
)

itsm_pycards = Job(
    date(2018, 1, 1),
    date(2018, 12, 1),
    "Developer(Python, C++) ",
    "\\textbf{Alexsupport}",
    "Part-time",
    "Develop and maintenance personal discount system for restaurant management company. "
    "Cliend-side deployed on windows, server-side on vps.",
    # EnumItem(
    #     arguments=[
    #         Item(
    #           "Develop and maintenance personal discount system for restaurant management company."
    #         ),
    #     ]
    # ),
)
itsm_sync_tickets = Job(
    date(2014, 1, 1),
    date(2014, 12, 1),
    "System Developer(Python)",
    "\\textbf{Alexsupport}",
    "Part-time",
    EnumItem(
        arguments=[
            Item("Clients prefered use their own ticket system"),
            Item("We wanted to make possible to work with them all from one point"),
            Item(
                "Develop django application for syncronization tickets from clients ticket-systems to one we was using"
            ),
            Item("Later some clients agreed to use the same system."),
        ]
    ),
    hide=True,
)
itsm_pbx = Job(
    date(2011, 3, 1),
    date(2014, 2, 1),
    "System Developer(Python) ",
    "\\textbf{Alexsupport}",
    "Part-time",
    "Develop and maintenance PBX for it-support. It's based on asterisk, as endpoints devices used mobile phones. "
    "For PBX management used AMI and django-based app. It's also integrated with telegram for convenience. "
    "For asyncron tasks used celery. "
    "It's deployed on proxmox via lxc with postgresql and mongodb. "
    # EnumItem(
    #     arguments=[
    #         Item("Users contact with specialists directly by phones."),
    #         Item(
    #             "We wanted to deploy pbx with possibility to receive calls outside the office"
    #         ),
    #         Item(
    #             "I have deployed asterisk and develop tool to manage calls."
    #             "It was first time managed by usual dialplan with sql,"
    #             "lua-dialpan via AMI and bash script, and finally Django app via AGI."
    #         ),
    #         Item("A functioning PBX with mobile employees and management via telegram"),
    #     ]
    # ),
)
mallina_sysadmin = Job(
    date(2011, 3, 1),
    date(2013, 6, 1),
    "System administrator",
    "\\textbf{Mallina LTD}",
    "",
    EnumItem(
        arguments=[
            Item("System and network administration"),
            Item("Resolving IT-like problems"),
            Item("Support users"),
        ]
    ),
)
mallina_ittech = Job(
    date(2011, 3, 1),
    date(2013, 6, 1),
    "It Support ",
    "\\textbf{Mallina LTD}",
    "",
    EnumItem(
        arguments=[
            Item("Resolving IT-like problems"),
            Item("Contact with users"),
        ]
    ),
)
bmstu = Job(
    date(2008, 1, 1),
    date(2011, 5, 1),
    "It Technician",
    "\href{https://www.bmstu.ru/}{\\textbf{BMSTU}}",
    "",
    EnumItem(
        arguments=[
            Item("Administration, maintenance and upgrade of computer class"),
        ]
    ),
)
