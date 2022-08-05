states = {
  'Oregon': 'OR',
  'Florida': 'FL',
  'California': 'CA',
  'Missouri': 'MO',
  'New York': 'NY',
  'Michigan': 'MI'
}

cities = {
    'MO': 'StL',
    'CA': 'Los Angeles',
    'FL': 'Jacksonville',
    'MI': 'Detroit'
}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("Missour has: ", cities['MO'])

print('-' * 10)
print("New York's abbreviation is: ", states['New York'])
print("Missouri's abbreviation is: ", states['Missouri'])

print('-' * 10)
for abbrev, state in list(states.items()):
    print(f"{state} is abbreviated {abbrev}.")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has a city named {city}.")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev};")
    print(f" and has city {cities[abbrev]}.")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, this state isn't real yet.")

city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")
