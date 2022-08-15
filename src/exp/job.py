from pylatex.utils import NoEscape


class Job:
    def __init__(
        self, date_begin, date_end, title, company, format, description, hide=False
    ):
        self.date_begin = date_begin
        self.date_end = date_end
        self.title = title
        self.company = company
        self.format = format
        self.description = description
        self.hide = hide

    def dates(self):
        begin = self.date_begin.strftime("%b %Y")
        if self.date_end:
            end = self.date_end.strftime("%b %Y")
        else:
            end = "..."
        return NoEscape(f"{begin} -\\\\{end}")
