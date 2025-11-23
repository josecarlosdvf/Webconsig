# -*- encoding: utf-8 -*-
"""
Webconsig CRM - Database Models

This file contains the database models for the Webconsig CRM system.
Add your CRM-specific models here (e.g., Customer, Lead, Opportunity, etc.)
"""

from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

# Example base model class for common functionality
class BaseModel:
    """Base model class with common CRUD operations"""
    
    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()
    
    @classmethod
    def get_list(cls):
        return cls.query.all()
    
    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__.get('orig', str(e)))
            raise InvalidUsage(error, 422)
    
    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__.get('orig', str(e)))
            raise InvalidUsage(error, 422)

# Add your CRM models here
# Example:
# class Customer(db.Model, BaseModel):
#     __tablename__ = 'customers'
#     
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), nullable=False)
#     email = db.Column(db.String(128), unique=True, nullable=False)
#     phone = db.Column(db.String(32))
#     company = db.Column(db.String(128))
#     date_created = db.Column(db.DateTime, default=dt.datetime.utcnow)
#     date_modified = db.Column(db.DateTime, default=dt.datetime.utcnow, onupdate=dt.datetime.utcnow)
