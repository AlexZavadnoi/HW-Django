from django.db import models
from django.contrib.auth.models import User

books = [
    {
        "id": 1,
        "title": "Fluent Python",
        "released_year": 2015,
        "description": "Python’s simplicity lets you become productive quickly, \nbut this often means you aren’t using everything it has to offer. \nWith this hands-on guide, you’ll learn how to write effective, \nidiomatic Python code by leveraging its best—and possibly most neglected—features. \nAuthor Luciano Ramalho takes you through Python’s core language features and libraries, \nand shows you how to make your code shorter, faster, \nand more readable at the same time.",
        "author_id": 1
    },
    {
        "id": 2,
        "title": "Django for beginners",
        "released_year": 2018,
        "description": "Django for Beginners is a project-based introduction to Django, \nthe popular Python-based web framework. Suitable for total beginners \nwho have never built a website before as well as professional programmers \nlooking for a fast-paced guide to modern web development and Django fundamentals.",
        "author_id": 2
    },
    {
        "id": 3,
        "title": "Django 2 by Example Build powerful and reliable Python web applications from scratch",
        "released_year": 2018,
        "description": "If you want to learn the entire process of developing professional web applications with Django 2, \nthen this book is for you. You will walk through the creation of four professional Django 2 projects, \nteaching you how to solve common problems and implement best practices. \nYou will learn how to build a blog application, a social image bookmarking website, \nan online shop and ane - learning platform. The book will teach you how to enhance your applications with AJAX,\n create RESTful APIs and set up a production environment for your Django 2 projects.\nThe book walks you through the creation of real-world applications, solving common problems, \nand implementing best practices. By the end of this book, you will have a deep understanding \nof Django 2 and how to build advanced web applications.",
        "author_id": 3
    },
    {
        "id": 4,
        "title": "Two Scoops of Django 1.11: Best Practices for the Django Web Framework",
        "released_year": 2017,
        "description": "In this book we introduce you to the various tips, tricks, patterns, \ncode snippets, and techniques that wel ve picked up over the years. \nWe have put thousands of hours into the fourth edition of the book, \nwriting and revising its material to include significant improvements and new material \nbased on feedback from previous editions.",
        "author_id": 4
    },
    {
        "id": 5,
        "title": "Django for APIs",
        "released_year": 2018,
        "description": "Take a modern API-first approach to creating 3 different Django back-ends: \na Library API, Todo API, and a Blog API with user authentication, permissions, proper documentation, and more. You'll even learn how to connect them to a React front - end for a truly full-stack web application.",
        "author_id": 2
    },
    {
        "id": 6,
        "title": "Django for Professionals",
        "released_year": 2019,
        "description": "This book covers in-depth how professional Django programmers do their \njob and build real-world web applications. Topics covered include Docker, environment variables, payments, search, permissions, \nfile/image uploads, testing, security, performance, and deployment.",
        "author_id": 2
    },
    {
        "id": 7,
        "title": 'Django Design Patterns and Best Practices: Industry-standard web development techniques \nand solutions using Python',
        "released_year": 2018,
        "description": "Building secure and maintainable web applications requires comprehensive knowledge. \nThe second edition of this book not only sheds light on Django, \nbut also encapsulates years of experience in the form of design \npatterns and best practices. Rather than sticking to GoF design patterns, \nthe book looks at higher-level patterns. Using the latest version of Django \nand Python, you will learn about Channels and asyncio while building \na solid conceptual background.\nThe book compares design choices to help you make everyday decisions faster \nin a rapidly changing environment.",
        "author_id": 5
    },
    {
        "id": 8,
        "title": 'Django Unleashed',
        "released_year": 2015,
        "description": "Django is an amazingly powerful system for creating modern, dynamic websites. \nBut programming Django hasn’t always been easy–until now. \nDjango Unleashed is your step-by-step, beginner-friendly guide to \nleveraging Django’s core capabilities and its powerful contributed library. \nYou’ll learn in the most effective way possible: hands on, by building \na fully functional Django website from scratch. \nYou’ll even deploy the website to the cloud.",
        "author_id": 6
    },
    {
        "id": 9,
        "title": 'Beginning Django E-Commerce',
        "released_year": 2017,
        "description": "Beginning Django E-Commerce guides you through producing an e-commerce site using Django, \nthe most popular Python web development framework. \nTopics covered include how to make a shopping cart, a checkout, \nand a payment processor: how to make the most of Ajax; and search engine optimization best practices. \nThroughout the book, you'll take each topic and apply it to build a single example site, \nand all the while you'll learn the theory behind what you're architecting.",
        "author_id": 7
    },
    {
        "id": 10,
        "title": "Practical Django 2 and Channels 2",
        "released_year": 2018,
        "description": "The book starts with the basics and explains the difference between a Django project and a Django app, \nthe most important settings, how to change them, and the fundamentals of packaging. \nYou'll then be introduced to all the standard tools of Django, along with a sample project. \nThe book then moves on to Channels, a recent addition to the Django ecosystem. \nIt extends the framework with support for real-time operations such \nas Websockets and other asynchronous features.",
        "author_id": 8
    }
]

authors = [
    {
        'id': 1,
        'first_name': 'Luciano',
        'last_name': 'Ramalho',
        'age': 51
    },
    {
        'id': 2,
        'first_name': 'William',
        'last_name': 'S. Vincent',
        'age': 52
    },
    {
        'id': 3,
        'first_name': 'Antonio',
        'last_name': 'Mele',
        'age': 56
    },
    {
        'id': 4,
        'first_name': 'Daniel Roy',
        'last_name': 'Greenfeld',
        'age': 54
    },
    {
        'id': 5,
        'first_name': 'Arun ',
        'last_name': 'Ravindran',
        'age': 49
    },
    {
        'id': 6,
        'first_name': 'Andrew',
        'last_name': 'Pinkham',
        'age': 39
    },
    {
        'id': 7,
        'first_name': 'James',
        'last_name': 'McGaw',
        'age': 45
    },
    {
        'id': 8,
        'first_name': 'Federico',
        'last_name': 'Marani',
        'age': 49
    }
]


class Authors(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()

    @staticmethod
    def create_authors():
        for y in authors:
            author = Authors(first_name=y['first_name'], last_name=y['last_name'], age=y['age'])
            author.save()

    def __str__(self):
        return f'{self.pk}: {self.first_name} {self.last_name}, "Age:" {self.age}'


class Profile(models.Model):
    info = models.CharField(max_length=100)
    author = models.OneToOneField(Authors, on_delete=models.SET_NULL, blank=True, null=True)


class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    released_year = models.IntegerField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0)

    @staticmethod
    def create_books():
        for x in books:
            book = Books(title=x['title'], description=x['description'], released_year=x['released_year'],
                         author_id=x['author_id'])
            book.save()

    def __str__(self):
        return f'{self.pk}: {self.title}, {self.description}, {self.released_year}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class ReviewBook(models.Model):
    rating = models.SmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()

    class Meta:
        unique_together = ('user', 'book')
