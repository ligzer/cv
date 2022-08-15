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
)

itsm_tbbot = Job(
    date(2019, 12, 1),
    date(2020, 2, 1),
    "Python Developer",
    "\\textbf{Alexsupport}",
    "Part-time",
    "Develop telegram bot for reserving tables in restaurant, using only mongodb."
)

itsm_resendbot = Job(
    date(2018, 9, 1),
    date(2019, 3, 1),
    "Python Developer",
    "\\textbf{Alexsupport}",
    "Part-time",
    "Develop and maintenance telegram bot for it-support restaurants. It's deployed on lxc, "
    "using postgresql, mongodb, django, celery"
)

itsm_pycards = Job(
    date(2018, 1, 1),
    date(2018, 12, 1),
    "Developer(Python, C++) ",
    "\\textbf{Alexsupport}",
    "Part-time",
    "Develop and maintenance personal discount system for restaurant management company. "
    "Cliend-side deployed on windows, server-side on vps.",
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
