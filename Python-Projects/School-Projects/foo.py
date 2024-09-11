import yaml

data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'johm.doe@example.com',
    'skills': [
        'Python',
        'JavaScript',
        'Node.js'
    ],
    'experience' : {
        'years': 5,
        'companies' : [
            'Company A',
            'Company B'
        ]
    }
}

yaml_output = yaml.dump(data, default_flow_style=False)
print('YAML file generated successfully!')
print(yaml_output)