from service import Service
import random
import string


class Grab(Service):
    def send_sms(self):
        name = ''.join(random.choice(string.ascii_letters) for _ in range(9))
        mail = ''.join(random.choice(string.ascii_letters) for _ in range(9)) + '@gmail.com'
        self.session.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': self.formatted_phone, 'countryCode': self.country_code, 'name': name,
                                'email': mail})
