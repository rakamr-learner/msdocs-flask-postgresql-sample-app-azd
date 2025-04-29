from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import validates

from app import db


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    street_address = Column(String(250)) #menambahkan karakter string dari 50 ke 250
    description = Column(String(250))

    def __str__(self):
        return self.name

# class Review(db.Model): --the original code tetap di keep untuk cek perbedaannya
#     __tablename__ = 'review'
#     id = Column(Integer, primary_key=True)
#     restaurant_id = Column(Integer, ForeignKey('restaurant.id', ondelete="CASCADE"))
#     user_name = Column(String(30))
#     rating = Column(Integer)
#     review_text = Column(String(500))
#     review_date = Column(DateTime) 

class Review(db.Model):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id', ondelete="CASCADE"))  # diganti dari restaurant
    user_name = Column(String(30))
    rating = Column(Integer)
    review_text = Column(String(500))
    review_date = Column(DateTime)

    @validates('rating')
    def validate_rating(self, key, value):
        assert value is None or (1 <= value <= 5)
        return value

    @validates('rating')
    def validate_rating(self, key, value):
        assert value is None or (1 <= value <= 5)
        return value

    def __str__(self):
        return f"{self.user_name}: {self.review_date:%x}"
