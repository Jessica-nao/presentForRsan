import re

table_data = ''
exist_problems = set()
with open('virtual_contest.html') as f:
    table_data = f.read()
    a_tabs = re.findall(r'<a href="https.+?"',table_data)
    for a_tab in a_tabs:
        exist_problems.add(a_tab[9:-1])

bootcamp_problems = set()
difficulties = ['easy', 'medium', 'hard',]
for diff in difficulties:
    with open(f'bootcamp_{diff}.html') as f:
        table_data = f.read()
        a_tabs = re.findall(r'<a href="https.+?"',table_data)
        for a_tab in a_tabs:
            if 'submissions' not in a_tab:
                bootcamp_problems.add(a_tab[9:-1])

should_add = bootcamp_problems - exist_problems
should_remove = exist_problems - bootcamp_problems

result = f'should add: {should_add} \nshould remove: {should_remove}'
with open('report.txt','w') as f:
    f.write(result)
