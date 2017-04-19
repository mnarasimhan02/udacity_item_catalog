from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, fanShop, fanItem, User

engine = create_engine('sqlite:///fanshopwithgears.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

picture = "https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg"

user1 = User(name="Mahesh", email="mahesh@gmail.com", picture = picture)
session.add(user1)
session.commit()

user2 = User(name="Sportuser", email="coder@gmail.com", picture = picture)
session.add(user2)
session.commit()

shop1 = fanShop(name="Fans Edge",description = "Sports and Fitness Fan Shop", user_id = user1.id )
session.add(shop1)
session.commit()

shop2 = fanShop(name="Sports Fan Shop",description = "Specializing in sports novelty items, supplies", user_id = user2.id )
session.add(shop2)
session.commit()
	
fan1 = fanItem(name="Jersey",description = "Authentic primary jersey", user_id = user1.id, price = "11", shop_id = shop1.id)
session.add(fan1)
session.commit()

fan2 = fanItem(name="T-Shirt ",description = "Logo set T-shirt", user_id = user1.id, price = "33", shop_id = shop1.id)
session.add(fan2)
session.commit()

fan3 = fanItem(name="Custom Jersey",description = "Replica primary custom jersey", user_id = user2.id, price = "22", shop_id = shop2.id)
session.add(fan3)
session.commit()

fan4 = fanItem(name="Pants",description = "black anthem pants", user_id = user2.id, price = "33", shop_id = shop2.id)
session.add(fan4)
session.commit()