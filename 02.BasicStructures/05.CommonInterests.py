# -*- coding: utf-8 -*-

ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

ivan_interests = set(ivan)
maria_interrests = set(maria)

print(", ".join(ivan_interests.intersection(maria_interrests)))