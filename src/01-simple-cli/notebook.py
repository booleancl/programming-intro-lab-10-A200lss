from note import Note
class Notebook:
     def __init__(self):
        self.notes = []
    
     def add_note(self, content, *tags):
         new_note = Note(content, *tags)
         self.notes.append(new_note)

     def edit_content(self, id, new_content):
         for note in self.notes:
             if note.id == id:
                 note.content = new_content

     def edit_tags(self, id, *new_tags):
         for note in self.notes:
             if note.id == id:
                 note.tags = [*new_tags]


     def search(self, target):
          result = []
          for note in self.notes:
              if note.match(target):
                  result.append(note)
          return result

    