from datetime import date

import i18n

from .job import Job, company_url

praktikum_devops = Job(
    date(2021, 12, 1),
    date(2022, 10, 1),
    "",
    company_url( i18n.t("education.ya.url"), i18n.t("education.ya.name")) ,
    "",
    i18n.t("education.ya.describe"),
)
bmstu = Job(
    date(2017, 9, 1),
    date(2020, 6, 1),
    "",
    company_url(i18n.t("education.bmstu.url"), i18n.t("education.bmstu.name")),
    "",
    i18n.t("education.bmstu.describe"),
)
