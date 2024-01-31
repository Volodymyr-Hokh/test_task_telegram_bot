from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from database.models import Report


engine = create_engine(config.SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def add_report(
    telegram_id,
    location,
    food_quality,
    food_quality_rate,
    service,
    service_rate,
    ambiance,
    ambiance_rate,
    menu,
    menu_rate,
    cleanliness,
    cleanliness_rate,
    image,
    report,
):
    new_report = Report(
        telegram_id=telegram_id,
        location=location,
        food_quality=food_quality,
        food_quality_rate=food_quality_rate,
        service=service,
        service_rate=service_rate,
        ambiance=ambiance,
        ambiance_rate=ambiance_rate,
        menu=menu,
        menu_rate=menu_rate,
        cleanliness=cleanliness,
        cleanliness_rate=cleanliness_rate,
        image=image,
        report=report,
    )
    session.add(new_report)
    session.commit()
