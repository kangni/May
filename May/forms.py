# -*- coding: utf-8 -*-
from flask_wtf import Form

from wtforms import StringField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, URL


class CommentForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=225)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])


class PostForm(Form):
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Content', [DataRequired()])
