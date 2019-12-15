#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3

_db_path = 'question.db'


class QuestionDb():
    def __init__(self):
        db_file = os.path.join(os.path.dirname(__file__), _db_path)
        if not os.path.isfile(db_file):
            self.create_db()

    def create_db(self):
        conn = sqlite3.connect(_db_path)
        cursor = conn.cursor()
        try:
            #创建question table
            cursor.execute('''CREATE TABLE question
            (id    INT PRIMARY KEY      NOT NULL,
            frontend_id     INT         NOT NULL,
            title           CHAR(50)    NOT NULL,
            title_slug      CHAR(50)    NOT NULL,
            difficulty      CHAR(10)    NOT NULL,
            content         TEXT        NOT NULL,
            tag             CHAR(30)    NOT NULL,
            status          CHAR(10));
            ''')

            #创建 last_ac_submission table
            cursor.execute('''CREATE TABLE last_ac_submission
            (id    INT PRIMARY KEY      NOT NULL,
            question_slug   CHAR(50)    NOT NULL,
            timestamp       INT         NOT NULL,
            language        CHAR(10)    NOT NULL,
            code            TEXT        NOT NULL,
            runtime         CHAR(10));
            ''')
        finally:
            cursor.close()
            conn.close()
