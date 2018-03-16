import json

# schema = {}  
# schema['people'] = []  
# schema['people'].append({  
#     'name': 'Scott',
#    'website': 'stackabuse.com',
#     'from': 'Nebraska'
})
schema['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
schema['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

print schema


# write data to dict object



with open('dbschema.json', 'w') as f:
    json.dump(schema, f, indent = 4)



