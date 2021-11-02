"""Hello CLI."""
import attr
import click


class Dog:
    def __init__(self, *, breed):
        self.breed = breed

    @classmethod
    def pug_factory(cls):
        return cls(breed='pug')

    def bark(self):
        if self.breed == 'pug':
            print('bark')
            return
        print('BARK')

    def bark_at(self, *, person):
        self.bark()
        print(person)


@attr.s(kw_only=True, slots=True, frozen=True)
class Cat:
    breed: str = attr.ib()

    @classmethod
    def tabby_factory(cls):
        return cls(breed='tabby')

    def meow(self):
        if self.breed == 'tabby':
            print('meow')
            return
        print('MEOW')

    def meow_at(self, *, person):
        self.meow()
        print(person)


@click.command()
@click.argument('breed')
def cli(breed):
    """Print phrase."""
    dog = Dog(breed=breed)
    dog.bark()
    pug = Dog.pug_factory()
    pug.bark()
    pug.bark_at(person='john')
    cat = Cat(breed='siamese')
    cat.meow()
    tabby = Cat.tabby_factory()
    tabby.meow()
    tabby.meow_at(person='john')
