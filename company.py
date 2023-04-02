import persons

# creating custom examples
managers = [
    persons.Manager(f'Manager_{count}', 'Family#', count + 20)
    for count in range(1, 4)
]

agents = [
    persons.Agent(f'Agent_{count}', 'Family#', count + 20)
    for count in range(1, 4)
]

workers = [
    persons.Worker(f'Worker_{count}', 'Family#', count + 20)
    for count in range(1, 4)
]

# set volume sales
for volume, agent in enumerate(agents):
    agent.set_volume(volume * 100)
# set working hours
for hours, worker in enumerate(workers):
    worker.set_working_hours(hours + 100)

# print each info
for employee in list([*managers, *agents, *workers]):
    print(f'\n{employee.get_info()}\nSalary: {employee.get_salary()}')
