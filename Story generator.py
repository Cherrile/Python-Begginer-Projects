import random
when = ['A few years ago', 'Yesterday',
        'last night', 'A long time ago', 'On 20th Dec']
who = ['a donkey', 'an elephant', 'a hen', 'a turtle', 'a cat']
name = ['Ali', 'Marion', 'Mark',  'Tekashi ', 'Tina']
residence = ['lisbon', 'la paz', 'Nairobi', 'Kinshasa', 'San Diego']
went = ['cinema', 'university', 'school', 'musuem', 'park', ]
happened = ['eats a burger', 'made some new friends',
            'found a secret key', 'solved a mystery ', 'baked a cake']
print(random.choice(when) + ',' + random.choice(who) + ' that lived in ' +
      random.choice(residence) + ', went to the ' +
      random.choice(went) + ' and ' + random.choice(happened))

# random module used to select and print random floats or strings that are pseudo-random hence not really random
