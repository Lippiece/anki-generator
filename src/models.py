import genanki

# Cloze Model
cloze_model = genanki.Model(
  1607392319,
  'Cloze',
  fields=[
     {'name': 'Text'},
     {'name': 'Extra'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{cloze:Text}}',
      'afmt': '{{cloze:Text}}<hr id="answer">{{Extra}}'
    }
  ]
)

# Fill-in-the-blank Model
fib_model = genanki.Model(
  1607392319,
  'Fill in the Blank',
  fields=[
     {'name': 'Question'},
     {'name': 'Answer'}    
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}'
    }
  ]  
)


