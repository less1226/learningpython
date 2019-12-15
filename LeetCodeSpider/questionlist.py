#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import requests
import json

_all_question_url = 'https://leetcode-cn.com/api/problems/all/'
_question_url = 'https://leetcode-cn.com/problems/'
_graphql_url = 'https://leetcode-cn.com/graphql/'
_questions_content_path = os.getcwd() + '/questioncontent'

_graphql_params = {
    "operationName":
    "questionData",
    "variables": {
        "titleSlug": ""
    },
    "query":
    "query questionData($titleSlug: String!) {  question(titleSlug: $titleSlug) {    questionId    questionFrontendId    boundTopicId    title    titleSlug    content    translatedTitle    translatedContent    isPaidOnly    difficulty    likes    dislikes    isLiked    similarQuestions    contributors {      username      profileUrl      avatarUrl      __typename    }    langToValidPlayground    topicTags {      name      slug      translatedName      __typename    }    companyTagStats    codeSnippets {      lang      langSlug      code      __typename    }    stats    hints    solution {      id      canSeeDetail      __typename    }    status    sampleTestCase    metaData    judgerAvailable    judgeType    mysqlSchemas    enableRunCode    envInfo    book {      id      bookName      pressName      description      bookImgUrl      pressImgUrl      productUrl      __typename    }    isSubscribed    __typename  }}"
}


class QuestionList():
    def __init__(self):
        self._question_list = list()
        self.initianlize()

    def initianlize(self):
        if len(self._question_list) != 0:
            return
        try:
            with open('allproblemlist.json', 'r') as fp:
                self._question_list = json.load(fp)
        except FileNotFoundError:
            self.create_list()

    def create_list(self):
        r = requests.get(_all_question_url)
        self._question_list = [
            i for i in r.json()['stat_status_pairs']
            if i['paid_only'] == False
        ]
        with open('allproblemlist.json', 'w') as fp:
            json.dump(self._question_list, fp)

    def get_question(self, **kw):
        if 'frontend_question_id' in kw:
            question__title_slug = [
                i['stat']['question__title_slug'] for i in self._question_list
                if i['frontend_question_id'] == kw['frontend_question_id']
            ]
        elif 'question__title' in kw:
            question__title_slug = [
                i['stat']['question__title_slug'] for i in self._question_list
                if i['question__title'] == kw['question__title']
            ]

        _graphql_params['variables']['titleSlug'] = question__title_slug[0]
        l = requests.post(_graphql_url, json=_graphql_params)
        question = l.json()['data']['question']

        return question

    def create_qusetion_files(self):
        if not os.path.exists(_questions_content_path):
            os.mkdir(_questions_content_path)
            
        for i in self._question_list:
            title_slug = i['stat']['question__title_slug']
            question_frontend_id = i['stat']['frontend_question_id']
            
