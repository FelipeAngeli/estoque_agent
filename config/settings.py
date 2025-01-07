import os
from decouple import config

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

DATABASE_URI = 'sqlite:///estoque.db'