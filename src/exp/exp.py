from datetime import date

from pylatex.base_classes import Arguments, CommandBase, Environment
from pylatex.package import Package
from pylatex.utils import NoEscape

import i18n

from .job import Job, company_url


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
    i18n.t("expierence.anzu.title"),
    company_url(i18n.t("expierence.anzu.url"), i18n.t("expierence.anzu.name")),
    i18n.t("expierence.contract"),
    i18n.t("expierence.anzu.describe")
)

reviewcode = Job(
    date(2022, 3, 1),
    None,
    i18n.t("expierence.yourcodereview.title"),  # + "Github Administrator",
    i18n.t("expierence.tmp") + "\href{https://yourcodereview.com/}{\\textbf{YourCodeReview}}",
    i18n.t("expierence.parttime"),
    EnumItem(
        arguments=[
            Item(i18n.t("expierence.tmp") + "Preparation and publication projects for code review."),
        ]
    ),
)
anzu_first = Job(
    date(2017, 11, 1),
    date(2019, 10, 1),
    i18n.t("expierence.anzu.title"),  # + "Fullstack developer(JS, Python) ",
    company_url(i18n.t("expierence.anzu.url"), i18n.t("expierence.anzu.name")),
    i18n.t("expierence.contract"),
    EnumItem(
        arguments=[
            Item(i18n.t("expierence.tmp") + "System for accounting production in jewelry workshop"),
        ]
    ),
)

itsm_main = Job(
    date(2013, 6, 1),
    None,
    i18n.t("expierence.alexsupport.it.title"),  # + "IT Support",
    NoEscape("\\textbf{"+i18n.t("expierence.alexsupport.name")+"}"),
    i18n.t("expierence.fulltime"),
    # NoEscape(i18n.t("expierence.alexsupport.it.describe"))
    EnumItem(
        arguments=[
            Item(i18n.t("expierence.alexsupport.it.d1")),
            Item(i18n.t("expierence.alexsupport.it.d2")),
            Item(i18n.t("expierence.alexsupport.it.d3")),
            Item(i18n.t("expierence.alexsupport.it.d4")),
        ]
    )
)

itsm_tbbot = Job(
    date(2019, 12, 1),
    date(2020, 2, 1),
    i18n.t("expierence.alexsupport.reserverbot.title"),
    NoEscape("\\textbf{"+i18n.t("expierence.alexsupport.name")+"}"),
    i18n.t("expierence.parttime"),
    i18n.t("expierence.alexsupport.reserverbot.describe")
)

itsm_resendbot = Job(
    date(2018, 9, 1),
    date(2019, 3, 1),
    i18n.t("expierence.alexsupport.supportbot.title"),  # + "Python Developer",
    NoEscape("\\textbf{"+i18n.t("expierence.alexsupport.name")+"}"),
    i18n.t("expierence.parttime"),
    i18n.t("expierence.alexsupport.supportbot.describe")
)

itsm_pycards = Job(
    date(2018, 1, 1),
    date(2018, 12, 1),
    i18n.t("expierence.alexsupport.pds.title"),  # + "Developer(Python, C++) ",
    NoEscape("\\textbf{"+i18n.t("expierence.alexsupport.name")+"}"),
    i18n.t("expierence.parttime"),
    i18n.t("expierence.alexsupport.pds.describe"),
)
itsm_sync_tickets = Job(
    date(2014, 1, 1),
    date(2014, 12, 1),
    i18n.t("expierence.alexsupport.planus.title"),  # + "System Developer(Python)",
    NoEscape("\\textbf{"+i18n.t("expierence.alexsupport.name")+"}"),
    i18n.t("expierence.parttime"),
    EnumItem(
        arguments=[
            Item(i18n.t("expierence.tmp") + "Clients prefered use their own ticket system"),
            Item(i18n.t("expierence.tmp") + "We wanted to make possible to work with them all from one point"),
            Item(
                i18n.t(
                    "expierence.tmp") + "Develop django application for syncronization tickets from clients ticket-systems to one we was using"
            ),
            Item(i18n.t("expierence.tmp") + "Later some clients agreed to use the same system."),
        ]
    ),
    hide=True,
)
itsm_pbx = Job(
    date(2011, 3, 1),
    date(2014, 2, 1),
    i18n.t("expierence.alexsupport.pbx.title"),  # "System Developer(Python) ",
    NoEscape("\\textbf{"+i18n.t("expierence.alexsupport.name")+"}"),
    i18n.t("expierence.parttime"),
    i18n.t("expierence.alexsupport.pbx.describe")
)
mallina_sysadmin = Job(
    date(2011, 3, 1),
    date(2013, 6, 1),
    i18n.t("expierence.mallina.title"),
    "\\textbf{"+i18n.t("expierence.mallina.name")+"}",
    "",
    EnumItem(
        arguments=[
            Item(i18n.t("expierence.mallina.d1")),
            Item(i18n.t("expierence.mallina.d2")),
            Item(i18n.t("expierence.mallina.d3")),
        ]
    ),
)
mallina_ittech = Job(
    date(2011, 3, 1),
    date(2013, 6, 1),
    i18n.t("expierence.mallina1.title") + "It Support ",
    "\\textbf{"+i18n.t("expierence.mallina.name")+"}",
    "",
    EnumItem(
        arguments=[
            Item(i18n.t("expierence.tmp") + "Resolving IT-like problems"),
            Item(i18n.t("expierence.tmp") + "Contact with users"),
        ]
    ),
)
bmstu = Job(
    date(2008, 1, 1),
    date(2011, 5, 1),
    i18n.t("expierence.bmstu.title") + "It Technician",
    i18n.t("expierence.tmp") + "\href{https://www.bmstu.ru/}{\\textbf{BMSTU}}",
    "",
    EnumItem(
        arguments=[
            Item(i18n.t("expierence.tmp") + "Administration, maintenance and upgrade of computer class"),
        ]
    ),
)
