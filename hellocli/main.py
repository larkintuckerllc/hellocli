"""Hello CLI."""
import click

class Dog:
    def __init__(self, breed):
        self.breed = breed
    
    @classmethod
    def pug_factory(cls):
        return cls('pug')

    def bark(self):
        if self.breed == 'pug':
            print('bark')
            return
        print('BARK')

    def bark_at(self, *, person):
        self.bark()
        print(person)

@click.command()
@click.argument('breed')
def cli(breed):
    """Print phrase."""
    dog = Dog(breed)
    dog.bark()
    pug = Dog.pug_factory()
    pug.bark()
    pug.bark_at(person='john')
