from sqlalchemy import Column, DateTime, Integer, String, Boolean, func
from sqlalchemy import PrimaryKeyConstraint


class Author:

    __tablename__ = 'author'

    __table_args__ = (
        PrimaryKeyConstraint('id', 'email'),
        {},
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, default=func.now())

    name = Column(String, nullable=False)
    email = Column(String, nullable=False, primary_key=True, autoincrement=False)

    is_email_verified = Column(Boolean, default=False)
    is_account_suspended = Column(Boolean, default=False)

    # Count of stories published by this author
    story_count = Column(Integer, default=0, )

    def __init__(self):
        pass

