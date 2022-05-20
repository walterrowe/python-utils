# Online Python - IDE, Editor, Compiler, Interpreter
# https://www.online-python.com

from datetime import *

class Issue():
    def __init__(self, title, labels, closed):
        self.title = title
        self.labels = labels
        self.closed = closed

    def __repr__(self):
        return str(self.__class__) + ': ' + str(self.__dict__)

    def __str__(self):
        return f'Title: {self.title}, Closed: {self.closed}, Labels: {self.labels}'

    def __add__(x, y):
        return [ x, y ]

    def print(self):
        if isinstance(self,list):
            for mine in self:
                mine.print
        else:
            print (f'Title: {self.title}, Closed: {self.closed}, Labels: {self.labels}')

issues = []
# issues_list = [
#     { "title": "issue1", "labels": [ 'Overdue' ], "closed": today - timedelta(10) },
#     { "title": "issue2", "labels": [ ], "closed": date.today() + timedelta(10) },
#     { "title": "issue3", "labels": [ ], "closed": date.today() + timedelta(3) },
#     { "title": "issue4", "labels": [ ], "closed": date.today() - timedelta(7) }
# ]

today = date.today()
thirty_last = today - timedelta(30)
thirty_next = today + timedelta(30)

issues = issues + [ Issue(title="issue1", closed=(today-timedelta(10)), labels=[ 'Overdue' ] ) ]
issues = issues + [ Issue(title="issue2", closed=(today+timedelta(10)), labels=[] ) ]
issues = issues + [ Issue(title="issue3", closed=(today+timedelta(3)) , labels=[] ) ]
issues = issues + [ Issue(title="issue4", closed=(today-timedelta(7)) , labels=[] ) ]

last = []
next = []
late = []

report = []

for issue in issues:
    if issue.closed > thirty_last and issue.closed < today:
        last.append(issue)
    if issue.closed > today and issue.closed < thirty_next:
        next.append(issue)
    if 'Overdue' in issue.labels:
        late.append(issue)

report.append('# %(project)s Status Report for %(date)s\n' %
    { "project": 'Automated Server Provisioning', "date": today })

report.append('\n## Tasks closed since %(date)s: %(tasks)d\n' %
    {  "date": thirty_last, "tasks": len(last) })
if len(last) > 0:
    for issue in last:
        report.append('\n- %(title)s' % { "title": issue.title })
else:
    report.append('\n- No closed tasks')

report.append('\n## Tasks planned before %(date)s: %(tasks)d\n' %
    {  "date": thirty_next, "tasks": len(next) })
if len(next) > 0:
    for issue in next:
        report.append('\n- %(title)s' % { "title": issue.title })
else:
    report.append('\n- No upcoming tasks')

report.append('\n## Overdue tasks: %(tasks)d\n' %
    { "tasks": len(late), "date": thirty_last })
if len(late) > 0:
    for issue in late:
        report.append('\n- %(title)s' % { "title": issue.title })
else:
    report.append('\n- No overdue tasks')

report_name = 'status-' + today.strftime('%Y-%m-%d') + '.md'
report_file = open(report_name,'w')
report_file.writelines(report)
report_file.close()
