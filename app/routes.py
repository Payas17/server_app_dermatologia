"""File containing all endpoints in the app."""
import json
from flask import request, jsonify
from flask_restful import Resource
from app import app

class Index(Resource):
    """home endpoint"""
    @classmethod
    def get(cls):
        """get mmethod"""
        return 'Hello index'


class Android(Resource):
    """android endpoint"""
    @classmethod
    def get(cls):
        """get mmethod"""
        return "Hello, android"


class AllUsers(Resource):
    """all users endpoint"""
    @classmethod
    def get(cls):
        """get mmethod"""
        try:
            users = User.query.all()
            return jsonify([e.name for e in users])
        except Exception as exception:  # pylint: disable = broad-except
            return str(exception)
