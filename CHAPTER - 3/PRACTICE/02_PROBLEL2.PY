letter = ''' Dear <|NAME|>,
            You are selected!
            Date: <|DATE|>'''

print(letter.replace('<|NAME|>', 'Sahil').replace('<|DATE|>', '01-01-2023'))
