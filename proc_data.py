import re
import asyncio

# ^\d{4} [A-Z0-9]{2} \d{2}:\d{2}:\d{2}[.]\d{3} \d{2}$
# ^\d{4} [A-Z0-9]{2} [0-2]\d:[0-6]\d:[0-6]\d[.]\d{3} \d{2}$
# (?P<player_number>\d{4}) (?P<channel_id>[A-Z0-9]{2}) (?<timestamp>[0-2]\d:[0-5]\d:[0-6]\d[.]\d{3}) (?P<group_number>\d{2})\r

pattern = re.compile(r'\d{4} [A-Z0-9]{2} [0-2]\d:[0-5]\d:[0-6]\d[.]\d{3} \d{2}\r')


class CheckTimeData:
    check_data = {'player_number': '0000',
                  'channel_id': '00',
                  'timestamp': '00:00:00.000',
                  'group_number': 0}

    def __init__(self, string):
        self.format_input(string)

    @staticmethod
    def check_input_data(input_string):
        if pattern.fullmatch(input_string):
            return True
        return False

    def format_input(self, string):
        if not CheckTimeData.check_input_data(string):
            return

        string = string.rstrip('\r')
        result = re.split(' ', string)

        self.check_data['player_number'] = result[0]
        self.check_data['channel_id'] = result[1]
        self.check_data['timestamp'] = result[2]
        self.check_data['group_number'] = int(result[3])

    def get_group_number(self):
        return self.check_data.get('group_number')

    async def display_info(self):
        print('спортсмен, нагрудный номер ' + self.check_data.get('player_number') +
              ' прошёл отсечку ' + self.check_data.get('channel_id') +
              ' в ' + self.check_data.get('timestamp')[:-2])

    async def print_info_to_file(self, filename='log.txt'):
        with open(filename, 'a') as file:
            file.write(self.check_data['player_number'] + ' ' +
                       self.check_data['channel_id'] + ' ' +
                       self.check_data['timestamp'] + ' ' +
                       str(self.check_data['group_number']).zfill(2) + '\n'
                       )
