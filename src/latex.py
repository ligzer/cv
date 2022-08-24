import os
import shutil

from pylatex import Command, Document, Section
from pylatex.base_classes import Arguments, CommandBase, Environment
from pylatex.utils import NoEscape

import i18n


class TwentyItem(CommandBase):
    _latex_name = "twentyitem"


class Twenty(Environment):
    _latex_name = "twenty"


if __name__ == "__main__":
    image_filename = os.path.join(os.path.dirname(__file__), "img/linkedin.png")
    i18n.load_path.append("./i18n/")
    i18n.set('locale', 'ru')
    i18n.set('fallback', 'en')

    import exp

    name = i18n.t("person.Michael")
    surname = i18n.t("person.Prokopenko")
    title = i18n.t("person.DevOps")
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
    doc.preamble.append(Command("cvjobtitle", title))
    # doc.preamble.append(Command("cvaddress", i18n.t("person.cvaddress")))
    # https://www.google.com/maps/place/Bar,+Montenegro/@42,19,6z/
    doc.preamble.append(Command("cvnumberphone", i18n.t("person.cvphone")))
    doc.preamble.append(Command("cvmail", "mike.pro@alexsupport.org"))
    doc.preamble.append(Command("cvlinkedin", "linkedin.com/in/ligzer"))
    doc.preamble.append(Command("cvtelergram", "t.me/ligzer"))
    # doc.preamble.append(Command("cvrelocation", i18n.t("person.cvrelocation")))
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

    with doc.create(Section(i18n.t("person.work_experience"))):
        # doc.append("Experienced in deploying and supporting different it-infrastructures."
        #            "Have sound knowledge of networking and basic network services."
        #            "Develop projects on different languages."
        #            "A lot of experience in installation, deployment and maintenance of pupular products."
        #            "f.e. MS Active Directory, MS SQL, Postgres, VMWare ESXi, Proxmox ve, nginx, GitLab CI.")
        with doc.create(Twenty()):
            for job in [x for x in exp.jobs if not x.hide][0:7]:
                job: exp.Job = job
                doc.append(
                    TwentyItem(
                        arguments=Arguments(
                            NoEscape(job.dates()),
                            NoEscape(job.title),
                            NoEscape(job.company),
                            NoEscape(job.format),
                            job.description,
                        )
                    )
                )

    with doc.create(Section(i18n.t("person.education"))):
        with doc.create(Twenty()):
            for edu in exp.educations:
                edu: exp.Job = edu
                doc.append(
                    TwentyItem(
                        arguments=Arguments(
                            NoEscape(edu.dates()),
                            NoEscape(edu.title),
                            NoEscape(edu.company),
                            NoEscape(edu.format),
                            NoEscape(edu.description),
                        )
                    )
                )
    pdfname = f"./latex/{title} {name} {surname}"
    doc.generate_pdf(pdfname, clean_tex=False, compiler="xelatex")
    shutil.copy(f"{pdfname}.pdf", "..")
