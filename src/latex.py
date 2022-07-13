import shutil

from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Command, UnsafeCommand
from pylatex.base_classes import CommandBase, Arguments, Environment
from pylatex.utils import NoEscape
import exp
import os
from datetime import datetime


class TwentyItem(CommandBase):
    _latex_name = 'twentyitem'


class Twenty(Environment):
    _latex_name = 'twenty'


if __name__ == '__main__':
    image_filename = os.path.join(os.path.dirname(__file__), 'img/linkedin.png')

    name = 'Michael'
    surname = 'Prokopenko'
    title = 'DevOps'
    doc = Document(
        documentclass='twentysecondcv',
        document_options=["a4paper", ],
        fontenc=None,
    )
    doc.preamble.append(Command('cvname', NoEscape(f'{name}\\\\{surname}')))  # your name
    doc.preamble.append(Command('cvjobtitle', title))  # your actual job position
    doc.preamble.append(Command('cvaddress', 'Montenegro, Bar'))  # address
    doc.preamble.append(Command('cvnumberphone', '+382 6853 9017'))  # telephone number
    doc.preamble.append(Command('cvmail', 'mike.pro@alexsupport.org'))  # e-mail
    doc.preamble.append(Command('cvlinkedin', 'linkedin.com/in/ligzer'))
    doc.preamble.append(Command('cvtelergram', 't.me/ligzer'))
    doc.preamble.append(Command('cvrelocation', 'Relocation possible'))
    doc.preamble.append(NoEscape('\\def\changemargin#1#2{\\list{}{\\rightmargin#2\\leftmargin#1}\\item[]}'
                                 '\\let\endchangemargin=\\endlist'))
    doc.preamble.append(Command(
        'skills',
        # \\textbf{Vagrant}
        arguments=[

            NoEscape(
                '\\textbf{DevOps}, \\textbf{GitLab CI},\\textbf{Ansible},\\textbf{~Proxmox~},'
                '\\textbf{~~~~Esxi~~~~},\\textbf{Sentry},\\textbf{Systemd},\\textbf{Docker},\\textbf{Zabbix}'
            ),
            NoEscape(
                '\\textbf{Dev},'
                '\\textbf{~~~~~Python~~~~~},'
                '\\textbf{~~~C++~~~},'
                '\\textbf{~~~~~Django~~~~~},'
                '\\textbf{~~~~Celery~~~~},'
                '\\tiny\\textbf{javascript},'
                '\\textbf{React},'
                '\\textbf{Redux}'),
            NoEscape(
                ' \\textbf{other},'
                '\\textbf{~~~~~Linux~~~~~},'
                '\\textbf{Win Servers},'
                '\\scriptsize\\textbf{Active}\\\\\scriptsize\\textbf{Directory},'
                '\\textbf{Mikrotik},'
                '\\textbf{Asterisk},'
                '\\textbf{Networking}'),
        ]
    ))

    doc.append(Command('makeprofile'))
    doc.append(NoEscape('{\Huge\headingfont\color{headercolor}\givencvjobtitle}'))
    with doc.create(Section('Work Experience')):
        with doc.create(Twenty()):
            for job in [x for x in exp.jobs if not x.hide][0:6]:
                job: exp.Job = job
                doc.append(TwentyItem(arguments=Arguments(
                    NoEscape(job.dates()),
                    NoEscape(job.title),
                    NoEscape(job.company),
                    NoEscape(job.format),
                    job.description
                )))

    with doc.create(Section('Education')):
        with doc.create(Twenty()):
            for edu in exp.educations:
                edu: exp.Job = edu
                doc.append(TwentyItem(arguments=Arguments(
                    NoEscape(edu.dates()),
                    NoEscape(edu.title),
                    NoEscape(edu.company),
                    NoEscape(edu.format),
                    NoEscape(edu.description)
                )))
    pdfname = f'./latex/{title} {name} {surname}'
    doc.generate_pdf(pdfname, clean_tex=False, compiler="xelatex")
    shutil.copy(f"{pdfname}.pdf", '..')