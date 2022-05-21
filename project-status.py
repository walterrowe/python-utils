# Online Python - IDE, Editor, Compiler, Interpreter
# https://www.online-python.com

from datetime import *
import issue

# # Issue class used for testing
# class Issue():
#     def __init__(self, title, labels, closed):
#         self.title = title
#         self.labels = labels
#         self.closed = closed
#
#     def __repr__(self):
#         return str(self.__class__) + ': ' + str(self.__dict__)
#
#     def __str__(self):
#         return f'Title: {self.title}, Closed: {self.closed}, Labels: {self.labels}'
#
#     def __add__(x, y):
#         return [ x, y ]
#
#     def print(self):
#         if isinstance(self,list):
#             for mine in self:
#                 mine.print
#         else:
#             print (f'Title: {self.title}, Closed: {self.closed}, Labels: {self.labels}')


# relative dates for report
today = date.today()
thirty_last = today - timedelta(30)
thirty_next = today + timedelta(30)

# sample issues to test against
issues = []
issues = issues + [ issue.Issue(title="issue1", closed=(today-timedelta(10)), labels=[ 'Overdue' ] ) ]
issues = issues + [ issue.Issue(title="issue2", closed=(today+timedelta(10)), labels=[] ) ]
issues = issues + [ issue.Issue(title="issue3", closed=(today+timedelta(3)) , labels=[] ) ]
issues = issues + [ issue.Issue(title="issue4", closed=(today-timedelta(7)) , labels=[] ) ]

# build report collections
last = []       # closed last 30 days
next = []       # due in next 30 days
late = []       # issues that are overdue
for issue in issues:
    if issue.closed > thirty_last and issue.closed < today:
        last.append(issue)
    if issue.closed > today and issue.closed < thirty_next:
        next.append(issue)
    if 'Overdue' in issue.labels:
        late.append(issue)

# create report lines
report = []     # report output lines
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


# write report file
report_name = 'status-' + today.strftime('%Y-%m-%d') + '.md'
report_file = open(report_name,'w')
report_file.writelines(report)
report_file.close()
