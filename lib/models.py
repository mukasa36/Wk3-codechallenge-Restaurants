from sqlalchemy import Column,Integer,Text,ForeignKey,Table
from sqlalchemy.orm import relationship,backref
from sqlalchemy.ext.declarative import declarative_base

from database import session

Base = declarative_base()

restaurant_customer = Table(
    'restaurant_customer',
Base.metadata,
Column('customer_id',Integer,ForeignKey('restaurants.id')),
Column('customer_id',Integer,ForeignKey('customer.id'))
)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer,primary_key=True)
    name = Column(Text)
    price = Column(Integer)
    reviews = relationship("Reviews", back_popultes="restaurant")
    customers = relationship(
        "Customer", secondary=restaurant_customer, back_popultes="restaurants")
    

    def __repr__(cls):
        pass
        return f'Restaurant: {cls.name}, price: {cls.price}'

    def restaurant_reviews(self):
        reviews = self.reviews
        formatted_reviews = [
            f'Review by {review.customer.full_name()}: {review.star_rating} stars'
            for review in reviews
        ]
        return formatted_reviews

    def restaurant_customer(self):
        return self.customer

    @classmethod
    def fanciest(cls):
        print(session.query(cls).order_by(cls.price.desc()).first())

    def total_reviews(self):
        return [f'Review for{self.name} by {self.customer.full_name()} : {review.star_rating} stars.' for review in self.reviews]