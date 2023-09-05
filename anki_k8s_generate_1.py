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

# Notes
cloze_note1 = genanki.Note(
  model=cloze_model,
  fields=['Old applications were {{c1::huge monolithic}} apps with 5+ million lines of code that took hours to build and deploy.', '']
)

cloze_note2 = genanki.Note(
  model=cloze_model, 
  fields=['Recently, applications have been broken into smaller {{c1::microservices}}.', '']  
)

fib_note = genanki.Note(
  model=fib_model,
  fields=['The main benefit of microservices is speeding up _________ by avoiding bottlenecks.', 'development']
)

# Deck
deck = genanki.Deck(
  2059400110,
  'Application Evolution')
  
notes = [
  cloze_note1,
  cloze_note2,
  fib_note
]

map(lambda n: deck.add_note(n), notes)

genanki.Package(deck).write_to_file('application_evolution_cloze.apkg')
