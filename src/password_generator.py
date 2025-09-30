import random
import string
from abc import ABC, abstractmethod
import nltk


class PasswordGenerator(ABC):

  @abstractmethod
  def generate(self):
    pass


class PinGenerator(PasswordGenerator):
  def __init__(self, length=8):
    self.length = length
  def generate(self):
    return "".join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
  def __init__(self, length=8, include_numbers=False, include_symbols=False):
    self.length = length
    self.characters = string.ascii_letters
    if include_numbers:
      self.characters += string.digits
    if include_symbols:
      self.characters += string.punctuation   

  def generate(self):
    return "".join([random.choice(self.characters) for _ in range(self.length)])


class MemorabalePasswordGenerator(PasswordGenerator):
  def __init__(
    self,
    num_of_words=4,
    separator="-",
    capitalize=False,
  ):
    self.num_of_words = num_of_words
    self.separator = separator
    self.capitalize = capitalize

  def generate(self):
    password_words = [random.choice(nltk.corpus.words.words()) for _ in range(self.num_of_words)]
    if self.capitalize:
      password_words = [word.upper() if random.choice((True, False)) else word.lower() for word in password_words]

    return self.separator.join(password_words)  
