students = dict([
    ('java',set(('vasa', 'kolia', 'marina'))),
    ('python',set(('peta', 'igor', 'marina'))),
    ('fs',set(('vasko', 'piter', 'nadia'))),
    ('frontend',set(('vasa', 'piter', 'marina')))
])
poligroup_students = []
groups = list(students.keys())
for id, group in enumerate(groups):
    for id2, group2 in enumerate(groups[id:],id):
        pass

