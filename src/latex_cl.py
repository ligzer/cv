import os
import shutil
from datetime import datetime

from pylatex import (Alignat, Axis, Command, Document, Figure, Math, Matrix,
                     Plot, Section, Subsection, Tabular, TikZ, UnsafeCommand)
from pylatex.base_classes import Arguments, CommandBase, Environment
from pylatex.utils import NoEscape

import exp


class TwentyItem(CommandBase):
    _latex_name = "twentyitem"


class Twenty(Environment):
    _latex_name = "twenty"


if __name__ == "__main__":

    name = "Michael"
    surname = "Prokopenko"
    title = "DevOps"
    doc = Document(
        documentclass="twentysecondcv",
        document_options=[
            "a4paper",
        ],
        fontenc=None,
    )
    doc.preamble.append(
        Command("cvname", NoEscape(f"{name}\\\\{surname}"))
    )  # your name
    doc.preamble.append(Command("cvjobtitle", title))  # your actual job position
    doc.preamble.append(Command("cvaddress", "Montenegro, Bar"))  # address
    # https://www.google.com/maps/place/Bar,+Montenegro/@42,19,6z/
    doc.preamble.append(Command("cvnumberphone", "+382 6853 9017"))  # telephone number
    doc.preamble.append(Command("cvmail", "mike.pro@alexsupport.org"))  # e-mail
    # doc.preamble.append(Command("cvlinkedin", "linkedin.com/in/ligzer"))
    doc.preamble.append(Command("cvtelergram", "t.me/ligzer"))
    doc.preamble.append(Command("cvrelocation", "Relocation possible"))
    # \setmainfont[Script=Greek]{GFS Artemisia}
    # \setsansfont[Script=Greek]{GFS Neohellenic}
    doc.preamble.append(
        NoEscape(
            "\\def\changemargin#1#2{\\list{}{\\rightmargin#2\\leftmargin#1}\\item[]}"
            "\\let\endchangemargin=\\endlist"
        )
    )
    doc.preamble.append(
        Command(
            "skills",
            # \\textbf{Vagrant}
            arguments=[
                NoEscape(
                    "\\textbf{DevOps},"
                    "\\textbf{~Proxmox~},"
                    "\\textbf{Sentry},"
                    "\\textbf{Zabbix},"
                    "\\textbf{GitLab CI},"
                    "\\textbf{Ansible},"
                    "\\textbf{Terraform},"
                    "\\textbf{Docker},"
                    "\\textbf{~~k8s~~},"
                    "\\textbf{Systemd},"
                    "\\textbf{~~~~Esxi~~~~}"
                ),
                NoEscape(
                    "\\textbf{Dev},"
                    "\\textbf{~~~~~Python~~~~~},"
                    "\\textbf{~~~C++~~~},"
                    "\\textbf{~~~~~Django~~~~~},"
                    "\\textbf{~~~~Celery~~~~},"
                    "\\tiny\\textbf{javascript},"
                    "\\textbf{React},"
                    "\\textbf{Redux}"
                ),
                NoEscape(
                    " \\textbf{other},"
                    "\\textbf{~~~~~Linux~~~~~},"
                    "\\textbf{Win Servers},"
                    "\\scriptsize\\textbf{Active}\\\\\scriptsize\\textbf{Directory},"
                    "\\textbf{Mikrotik},"
                    "\\textbf{Asterisk},"
                    "\\textbf{Networking}"
                ),
            ],
        )
    )

    doc.append(Command("makeprofile"))
    doc.append(NoEscape("{\Huge\headingfont\color{headercolor}\givencvjobtitle}"))

    with doc.create(Section("About me")):
        txt = "Я хочу развиваться в индустрии разработки. Имею много " \
              "I want to progress in development industry." \
              "I have a lot of experience in maintenance and development, but have never worked in big company," \
              "so i want get more experience in collective work."
        # txt = "Привет, почему я хочу работать у вас? Вы находитесь не в РФ."
        #        "Я тоже хочу, сейчас я имею внж на год в черногории и могу работать удалённо."
        #        "Почему я вам полезен? Большая часть моего опыта связана с поддержкой ПО для ресторанного бизнеса."
        #        "Я очень много работал с r-keeper, sh4 и iiko(сравнительно меньше)."
        #        "Решал разные задачи связанные с их отчётами, настройкой оборудования и поддержки в ресторане,"
        #        " интеграциями сторонних продуктов, разработкой собственных продуктов и инструментов."

        txt = "Why i want to work on you? You are not in Russia. " \
            "So i want to be. Now i'm located in Montenegro, have residence permit for one year and can work remotely. " \
            "\\\\   I am looking for my growth in development direction and money gain." \
            "\par " \
            "Why i am usefully for you? Most of my experience related to it supporting restaurant business. " \
            "I have worked a lot with r-keeper, sh4 and iiko(not so much). \\\\" \
            "I solve different tasks about deploying and maintenance restaurant system, \\\\ support data analytics, " \
            "integration outsource products and developing own products and tools."
        doc.append(NoEscape(txt))
    pdfname = f"./latex/cover letter"
    doc.generate_pdf(pdfname, clean_tex=False, compiler="xelatex")
    shutil.copy(f"{pdfname}.pdf", "..")
