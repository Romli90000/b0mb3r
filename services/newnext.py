# -*- coding: utf-8 -*-
from service import Service


class NewNext(Service):
    def send_sms(self):
        name = ''.join(random.choice(string.ascii_letters) for _ in range(9))
        self.session.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
            'client': {'firstName': name, 'lastName': name + er, 'phone': self.formatted_phone,
                       'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {'
                                                                       '\n  registration(client: $client) {'
                                                                       '\n    token\n    __typename\n  }\n}\n'})
