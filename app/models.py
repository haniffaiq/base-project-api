from marshmallow import Schema, fields, ValidationError


class RegistrationSchema(Schema):
    name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

class LoginSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

class User(Schema):
    name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)