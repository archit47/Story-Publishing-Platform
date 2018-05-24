from sqlalchemy import (Column, DateTime, Integer, String, Boolean,
                        func, ForeignKey)
from sqlalchemy.orm import relationship, backref
from sqlalchemy import PrimaryKeyConstraint
from src.models import Author


class Story:

    __tablename__ = 'story'

    __table_args__ = (
        PrimaryKeyConstraint('id'),
        {},
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_on = Column(DateTime, default=func.now())
    updated_on = Column(DateTime, default=func.now())

    is_draft = Column(Boolean, default=True)
    published_on = Column(DateTime, nullable=True)

    title = Column(String, default='Title', nullable=False)
    story_content = Column(String, default='Content for this story', nullable=True)

    # Relationship with author table
    # Author ID of the author who wrote this story/draft
    author_id = Column(Integer, ForeignKey('author.id'), nullable=False)
    author = relationship(Author,
                          backref=backref('stories', uselist=True)
    )

    upvote_count = Column(Integer, default=0)

    # Soft delete a story, hard-delete a draft
    is_deleted = Column(Boolean, default=False)

    def __init__(self):
        pass

