# -*- coding:utf-8 -*-

import json

from peewee import *
from playhouse.shortcuts import model_to_dict

myDB = MySQLDatabase("StudyEnglish",
                     host='localhost',
                     user='root',
                     passwd='11111111')

myDB.connect()


class MySQLModel(Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = myDB


class Words(MySQLModel):
    word = CharField()
    translation = CharField()

    @staticmethod
    def get_unprocessed_words(limit=10):
        words = list(Words.select().order_by(Words.id.asc()).limit(limit).offset(10).dicts())
        return words

    class Meta:
        db_table = 'englishwords'
