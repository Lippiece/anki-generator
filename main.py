import genanki
import src.models as models

# Notes
cloze_note1 = genanki.Note(
  model=models.cloze_model,
  fields=['Old applications were {{c1::huge monolithic}} apps with 5+ million lines of code that took hours to build and deploy.', '']
)

cloze_note2 = genanki.Note(
  model=models.cloze_model, 
  fields=['Recently, applications have been broken into smaller {{c1::microservices}}.', '']  
)

fib_note = genanki.Note(
  model=models.fib_model,
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

map(lambda note: deck.add_note(note), notes)

genanki.Package(deck).write_to_file('application_evolution_cloze.apkg')
