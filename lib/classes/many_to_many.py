# everything in one file

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            print("Name must be of type str and longer than 0 characters.")
            self._name = None
        else:
            self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({article.magazine.category for article in self._articles}) if self._articles else None


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            print("Name must be string between 2 and 16 characters.")
            self._name = None
        else:
            self._name = name

        if not isinstance(category, str) or len(category) == 0:
            print("Category must be string longer than 0 characters.")
            self._category = None
        else:
            self._category = category

        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            print("Name must be string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            print("Category must be string longer than 0 characters.")

    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        authors = [author for author in self.contributors() if len([a for a in author.articles() if a.magazine == self]) > 2]
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        if not any(mag._articles for mag in cls.all):
            return None
        return max(cls.all, key=lambda mag: len(mag._articles))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author object")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine object")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            print("Title must be string between 5 and 50 characters.")
            self._title = None
        else:
            self._title = title

        self.author = author
        self.magazine = magazine

        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title") and self._title is not None:
            print("Title cannot be changed once set.")
        elif not isinstance(value, str) or not (5 <= len(value) <= 50):
            print("Title must be string between 5 and 50 characters.")
        else:
            self._title = value
