from faker import Faker
from .models import User
import random
from . import db
from werkzeug.security import generate_password_hash

fake = Faker(['it_IT'])

def add_fake_data():
    for _ in range(10):
        name = fake.name()

        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]

        # Random domains for emails generated with Chat GPT
        random_domains = ['fakeemail.com', 'examplemail.net', 'tempmail.co', 'dummydomain.org']
        new_user = User(
            first_name = first_name,
            last_name=last_name,
            email = f"{first_name}{last_name}@{random.choice(random_domains)}",
            password=generate_password_hash(f"{first_name}{last_name}{random.randrange(0, 1000)}", method='pbkdf2:sha256'),
            confirmed = False
        )

        db.session.add(new_user)
        db.session.commit()

