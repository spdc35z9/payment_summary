import datetime


class JpEra:
    def __init__(self, shorthand, era_name, begin_date, end_date=datetime.date.max):
        self.shorthand = shorthand
        self.era_name = era_name
        self.begin_date = begin_date
        self.end_date = end_date

    def in_term(self, target_date):
        return self.begin_date <= target_date <= self.end_date

    def jp_year(self, year):
        return year - (self.begin_date.year - 1)


JP_ERA = (
    JpEra("M", "明治", datetime.date(1868,  9,  8), datetime.date(1912,  7, 29)),
    JpEra("T", "大正", datetime.date(1912,  7, 30), datetime.date(1926, 12, 24)),
    JpEra("S", "昭和", datetime.date(1926, 12, 25), datetime.date(1989,  1, 7)),
    JpEra("H", "平成", datetime.date(1989,  1,  8), datetime.date(2019,  4, 30)),
    JpEra("R", "令和", datetime.date(2019,  5,  1)),
)


def parse_jp_datetime(target_str, fmt='%y.%m.%d %H:%M'):
    """
    '元年' とはならない。ショートハンドのみ
    :target_str: 'H30.01.15 09:52'
    :fmt:
    :return: datetime.datetime
    """
    x, xs = target_str[0], target_str[1:]
    for era in JP_ERA:
        if x != era.shorthand:
            continue

        c = datetime.datetime.strptime(xs, fmt)
        y = era.begin_date.year + c.year % 100 - 1
        return datetime.datetime(y, c.month, c.day, c.hour, c.minute, c.second)

    raise ValueError('unknown era `%s`.' % x)


def jp_era(target_date):
    """
    :target_date: datetime.date(2018, 1, 15)
    :return: (shorthand, era_name, jp_year)
    """
    for era in JP_ERA:
        if era.in_term(target_date):
            return era.shorthand, era.era_name, era.jp_year(target_date.year)

    raise ValueError('should not be reached here `%s`.' % target_date)
