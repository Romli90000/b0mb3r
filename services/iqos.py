# -*- coding: utf-8 -*-
from service import Service


class Iqos(Service):
    def send_sms(self):
       
        self.session.get('https://ube.pmsm.org.ru/api/validate/phone?number=' + self.formatted_phone) 
