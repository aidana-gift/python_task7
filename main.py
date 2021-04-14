from datetime import date

band = {
    'members': {
        'Alex': {
            'role': 'guitar',
            'birthdate': date(1975, 3, 10)
        },
        'Roman': {
            'role': 'singer',
            'birthdate': date(1970, 8, 9)
        },
        'Tomiris': {
            'role': 'singer',
            'birthdate': date(1980, 9, 25)
        }
    },
    'concerts': {
        'Oslo': {
            'income': 2522,
            'date': date(2020, 4, 15),
            'expenses': [345, 431, 999]
        },
        'Tokyo': {
            'income': 5000,
            'date': date(2020, 2, 22),
            'expenses': [345, 650, 200]
        },
        'Berlin': {
            'income': 4000,
            'date': date(2019, 1, 30),
            'expenses': [785, 120, 110, 80]
        },
        'Moscow': {
            'income': 3000,
            'date': date(2020, 6, 17),
            'expenses': [50, 431, 250, 60]
        },
        'Nairobi': {
            'income': 1500,
            'date': date(2019, 8, 27),
            'expenses': [120, 45, 321]
        },
    }
}

def add_member(name, role, birth):
    band['members'][name] = {
        'role': role,
        'birthdate': birth
    }

def delete_member(name):
    band['members'].pop(name)

def add_concert(city, income, date, expenses):
    band['concerts'][city] = {
        'income': income,
        'date': date,
        'expenses': expenses
    }

def profit():
    profit = 0
    for key, value in band['concerts'].items():
        profit += band['concerts'][key]['income'] - sum(band['concerts'][key]['expenses'])
    return profit


# add_member('Person ', 'drumer', date(1981, 2, 13) )
# print(band)
#
# delete_member('Alex')
# print(band)
#
# add_concert('Bishkek', 2000, date(2020, 7, 15), [190, 500])
# print(band)

print(profit())
