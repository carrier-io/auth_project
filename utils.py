from flask import session, current_app


def current_user_id() -> str:
    return session['auth_attributes']['sub']


def current_user_email() -> str:
    return session['auth_attributes']['email']
