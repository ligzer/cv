from datetime import date, timedelta
from itertools import cycle

import matplotlib.pyplot as plt

cycol = cycle("bgrcmk")
cyrange = cycle(
    range(
        1,
        100,
    )
)


def add_job(job):
    x = [
        job.begin,
        job.end,
    ]
    # corresponding y axis values
    i = next(cyrange)
    y = [i, i]

    # plotting the points
    plt.plot(
        x,
        y,
        color=next(cycol),
        linewidth=2,
        markerfacecolor="blue",
        marker=".",
        markersize=6,
    )
    plt.text(job.begin, i, job.title)

    print(
        "\\twentyitem\n"
        f"{{{job.begin.strftime('%b %Y')} - \\\\ {job.end.strftime('%b %Y')}}}\n"
        f"{{ {job.title} }}\n"
    )
    # print(f"{job.begin.strftime('%b %Y')} - {job.end.strftime('%b %Y')}  {job.title}")


class Job:
    def __init__(
        self,
        begin,
        title="",
        end=date.today(),
        len=None,
    ):
        self.begin = begin
        if len:
            self.end = self.begin + timedelta(days=30 * len)
        else:
            self.end = end
        self.title = title

    def __gt__(self, other):
        return self.end > other.end

    def __lt__(self, other):
        return self.end > other.end

    def __eq__(self, other):
        return self.end == other.end


jobs = [
    Job(
        date(2008, 1, 1),
        "BMSTU",
        date(2011, 5, 1),
    ),
    Job(date(2011, 3, 1), "Mallina LTD - IT Support", date(2013, 6, 1)),
    Job(
        date(2011, 6, 1),
        "Mallina LTD - System and Database administrator",
        date(2013, 6, 1),
    ),
    Job(date(2013, 6, 1), "Individual Entrepreneur Dmitriev - IT Support"),
    Job(date(2011, 3, 1), "planus - pbx System Developer(Python)", len=36),
    Job(date(2018, 1, 1), "pycards - Developer(Python, C++)", len=12),
    Job(date(2018, 9, 1), "planus - telegram resend Developer(Python)", len=12),
    Job(date(2014, 1, 1), "planus - sync tickets System Developer(Python)", len=24),
    Job(date(2019, 12, 1), "telegram reserve bot Developer(Python)", len=12),
    Job(date(2017, 11, 2), "anzu sklad - Fullstack developer(JS, Python)", len=24),
    Job(date(2021, 1, 1), "DMDK anzu sklad - Fullstack developer(JS, Python)"),
    Job(date(2022, 3, 1), "YourCodeReview (github administrator)"),
]


def print_years():
    begin = date(2007, 1, 1)
    end = date.today()
    plt.ylim(0, len(jobs) + 1)
    plt.xlim(begin, end)

    list(map(add_job, sorted(jobs)))
    plt.show()


if __name__ == "__main__":
    print_years()
