from django.db import models
from django.contrib import auth

class Person(models.Model):
    '''' Model for Author '''
    name = models.CharField(max_length=20, help_text="The person first name")
    last_name = models.CharField(max_length=20, help_text="The person last name")
    email = models.EmailField(help_text="The contact email for person")

    def __str__(self):
        return f'{self.last_name}, {self.name}, email:{self.email}'

class Author(Person):
    ''' Model for Author '''

class Contributor(Person):
    ''' Model for contributor to a Book e.g. author, editor, co-author'''

class Publisher(models.Model):
    ''' Model for publisher '''
    name = models.CharField(max_length=50, help_text="The name of Publisher")
    website = models.URLField(help_text="The Publisher's website")
    email = models.EmailField(help_text="The Publishers email address")
    
    def __str__(self):
        return self.name

class Book(models.Model):
    ''' Model for Book '''
    title = models.CharField(max_length=70, help_text="The title of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")    
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")
    no_of_copies = models.IntegerField()

    def __str__(self):
        return f'"{self.title}" - {self.author}'

class BookContributor(models.Model):
    """ Many to many relation table """
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book", choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    '''Model for book review '''
    content = models.TextField(help_text="The review text")
    rating = models.IntegerField(help_text="The rating the reviewers has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was created.")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review was edited.")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)



