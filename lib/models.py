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
    status = CharField()

    @staticmethod
    def get_unprocessed_words(limit=10):
        words = Words.select().where(Words.status == None).order_by(Words.id.asc()).limit(limit)
        return words

    def get_select_words(limit=10):
        select_words = list(
            Words.select().where(Words.status == 1).order_by(Words.id.desc()).limit(limit).dicts())
        return select_words

    def updates_status(self):
        self.status = 1
        self.save()


    class Meta:
        db_table = 'tofel'
