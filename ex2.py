ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# Write a python expression that gets the email address of Ramit
print("Ramit's email: {}".format(ramit['email']))

# Write a python expression that gets the first of Ramit's interests
print("Ramit's first interest: {}".format(ramit['interests'][0]))

# Write a python expression that gets the email address of Jasmine
for f in ramit['friends']:
  if f['name'] == 'Jasmine':
    print("Jasmine's email: {}".format(f['email']))

# Write a python expression that gets the second of Jan's two interests
for f in ramit['friends']:
  if f['name'] == 'Jan':
    print("Jan's second interest: {}".format(f['interests'][1]))
