from flask import Flask
from app import db, Pizza, Restaurant, RestaurantPizza


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


# sample
with app.app_context():
    pizza1 = Pizza(name='Margherita', ingredients='Dough, Tomato Sauce, Mozzarella Cheese')
    pizza2 = Pizza(name='Pepperoni Feast', ingredients='Dough, Tomato Sauce, Mozzarella Cheese, Pepperoni')
    
    restaurant1 = Restaurant(name='Pizza Inn', address='298 Buruburu 11201')
    restaurant2 = Restaurant(name='Pomodoro', address='village market 10019')

    restaurant_pizza1 = RestaurantPizza(price=10, pizza=pizza1, restaurant=restaurant1)
    restaurant_pizza2 = RestaurantPizza(price=12, pizza=pizza2, restaurant=restaurant1)
    restaurant_pizza3 = RestaurantPizza(price=8, pizza=pizza1, restaurant=restaurant2)

    db.session.add_all([pizza1, pizza2, restaurant1, restaurant2, restaurant_pizza1, restaurant_pizza2, restaurant_pizza3])
    db.session.commit()

print('Sample data added to the database.')