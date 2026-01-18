#!/usr/bin/env python3

from app import app
from models import db, Bakery, BakedGood

with app.app_context():

    # Delete existing data
    BakedGood.query.delete()
    Bakery.query.delete()

    # Create bakeries
    bakery1 = Bakery(name="Delightful donuts")
    bakery2 = Bakery(name="Incredible crullers")

    db.session.add_all([bakery1, bakery2])
    db.session.commit()

    # Create baked goods
    baked_good1 = BakedGood(name="Chocolate dipped donut", price=2.75, bakery_id=bakery1.id)
    baked_good2 = BakedGood(name="Apple-spice filled donut", price=3.50, bakery_id=bakery1.id)
    baked_good3 = BakedGood(name="Glazed honey cruller", price=3.25, bakery_id=bakery2.id)
    baked_good4 = BakedGood(name="Chocolate cruller", price=3.40, bakery_id=bakery2.id)

    db.session.add_all([baked_good1, baked_good2, baked_good3, baked_good4])
    db.session.commit()

    print("Database seeded successfully!")