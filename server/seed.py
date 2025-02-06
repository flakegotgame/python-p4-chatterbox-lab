from app import db, Message

# Seed initial data
messages = [
    Message(body="Hello, World!", username="Ian"),
    Message(body="Flask is great!", username="Jane"),
    Message(body="React and Flask work together well.", username="John")
]

db.session.add_all(messages)
db.session.commit()

print("Database seeded successfully.")

