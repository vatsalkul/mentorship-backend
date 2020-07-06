from typing import Optional
from datetime import datetime

from app.database.models.user import UserModel
import time
from app.database.sqlalchemy_extension import db

class ForumPostsModel(db.Model):
    """Defines attributes for the posts available in forums.

    Attributes:
        id: integer primary key that defines the post.
        user_id: integer indicates the id of the user.
        title: A string indicating the title of the post.
        post_date: float that defines the date of creation of the post.
        modification_date: float that defines the date of modification of the post.
        report_count: Integer indicates the number of reports on the post.
    """

    # Specifying database table used for ForumPosts
    __tablename__ = "posts"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(400))
    post_date = db.Column(db.Float)
    modification_date = db.Column(db.Float)
    report_count = db.Column(db.Integer)


    def __init__(self, title, report_count, modification_date, post_date):
        """Initialises forumPostsModel class with user_id, title, and report_count. """

        self.title = title
        self.post_date = post_date
        self.modification_date = modification_date
        self.report_count = report_count

    def json(self):
        """Returns ForumPostsModel object in json format."""
        return {
            "id": self.id,
            #"user_id": self.user_id,
            "title": self.title,
            "post_date": self.post_date,
            "modification_date": self.modification_date,
            "report_count": self.report_count
        }

    def __repr__(self):
        """Returns the post's id and title. """
        return "Post name %s. ID is %s ." % (self.title, self.id)

    @classmethod
    def is_empty(cls) -> bool:
        """Returns a boolean if the ForumPostsModel is empty or not. """
        return cls.query.first() is None

    def save_to_db(self) -> None:
        """Adds a post to the database. """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        """Deletes a post from the database. """
        db.session.delete(self)
        db.session.commit()
