# Online Python - IDE, Editor, Compiler, Interpreter
# https://www.online-python.com

from datetime import *

issues = [
    { "title": "issue1", "labels": [ 'Overdue' ], "closed": date.today() - timedelta(10) },
    { "title": "issue2", "labels": [ ], "closed": date.today() + timedelta(10) },
    { "title": "issue3", "labels": [ ], "closed": date.today() + timedelta(3) },
    { "title": "issue4", "labels": [ ], "closed": date.today() - timedelta(7) }
]

today = date.today()
thirty_last = today - timedelta(30)
thirty_next = today + timedelta(30)

last = []
next = []
late = []

for issue in issues:
    if issue['closed'] > thirty_last and issue['closed'] < today:
        last.append(issue)
    if issue['closed'] > today and issue['closed'] < thirty_next:
        next.append(issue)
    if 'Overdue' in issue['labels']:
        late.append(issue)

print('# %(project)s Status Report for %(date)s' %
    { "project": 'Automated Server Provisioning', "date": today })

print('\n## Tasks closed since %(date)s: %(tasks)d\n' %
    {  "date": thirty_last, "tasks": len(last) })
if len(last) > 0:
    for issue in last:
        print('- %(title)s' % { "title": issue['title'] })
else:
    print('- No closed tasks')

print('\n## Tasks planned before %(date)s: %(tasks)d\n' %
    {  "date": thirty_next, "tasks": len(next) })
if len(next) > 0:
    for issue in next:
        print('- %(title)s' % { "title": issue['title'] })
else:
    print('- No upcoming tasks')

print('\n## Overdue tasks: %(tasks)d\n' %
    { "tasks": len(late), "date": thirty_last })
if len(late) > 0:
    for issue in late:
        print('- %(title)s' % { "title": issue['title'] })
else:
    print('- No overdue tasks')
