from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import SportCategory, Base, SportItem

engine = create_engine('sqlite:///sportsitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



# Sports items for Soccer
category1 = SportCategory(name="Soccer")

session.add(category1)
session.commit()

sportItem1 = SportItem(name="Soccer ball", description="For you to kick around",
                      sportcategory=category1)

session.add(sportItem1)
session.commit()


sportItem2 = SportItem(name="Soccer shirt", description="A shirt with number",
                      sportcategory=category1)

session.add(sportItem2)
session.commit()


# Sports items for Basketball
category2 = SportCategory(name ="Basketball")

session.add(category2)
session.commit()


sportItem1 = SportItem(name="Basketball ball", description="Marutama, or orange ball with black lines",
                     sportcategory=category2)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name="Jersey", description="Lightweight tank top good for letting the skin breathe",
                     sportcategory=category2)

session.add(sportItem2)
session.commit()


# Sports items for Frisbee
category3 = SportCategory(name = "Frisbee")

session.add(category3)
session.commit()


sportItem1 = SportItem(name="Frisbee plate", description="A flat plate to throw around",
                     sportcategory=category3)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name="Ball", description="An alternative to the frisbee plate",
                     sportcategory=category3)

session.add(sportItem2)
session.commit()


# Sports items for Baseball
category4 = SportCategory(name ="Baseball")

session.add(category4)
session.commit()


sportItem1 = SportItem(name="Baseball ball", description="Ball to hit with a bat",
                     sportcategory=category4)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name="Baseball bat", description="A bat to hit the ball",
                     sportcategory=category4)

session.add(sportItem2)
session.commit()


# Sports items for Snowboarding
category5 = SportCategory(name ="Snowboarding")

session.add(category5)
session.commit()


sportItem1 = SportItem(name="Fashion reflective goggles", description="To protect your eyes from the sun reflecting on the snow",
                     sportcategory=category5)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name="Snow board", description="To glide on the glistening snow",
                     sportcategory=category5)

session.add(sportItem2)
session.commit()


# Sports items for Rockclimbing
category6 = SportCategory(name ="Rockclimbing")

session.add(category6)
session.commit()

sportItem1 = SportItem(name="Rope", description="To hang yourself from a safe and secure place",
                     sportcategory=category6)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name="Gloves", description="Protects your precious hands from the rough surface of a cliff",
                     sportcategory=category6)

session.add(sportItem2)
session.commit()


# Sports items for Foosball
category7 = SportCategory(name ="Foosball")

session.add(category7)
session.commit()

sportItem1 = SportItem(name="Tiny plastic ball", description="To play foosball",
                     sportcategory=category7)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name="Fashion shades", description="To look cool while playing foosball",
                     sportcategory=category7)

session.add(sportItem2)
session.commit()


# Sports items for Hockey
category8 = SportCategory(name ="Hockey")

session.add(category8)
session.commit()


sportItem1 = SportItem(name="Hockey gloves", description="To protect your hands",
                     sportcategory=category8)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name="Hockey plate", description="To be used to play hockey",
                     sportcategory=category8)

session.add(sportItem2)
session.commit()


# Sports items for Skating
category9 = SportCategory(name ="Skating")

session.add(category9)
session.commit()


sportItem1 = SportItem(name="Skating rink", description="Buy the whole rink",
                     sportcategory=category9)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name="Skating shoes", description="To skate",
                     sportcategory=category9)

session.add(sportItem2)
session.commit()


print "added sports items!"
