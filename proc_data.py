import re

# ^\d{4} [A-Z0-9]{2} \d{2}:\d{2}:\d{2}[.]\d{3} \d{2}$
# ^\d{4} [A-Z0-9]{2} [0-2]\d:[0-6]\d:[0-6]\d[.]\d{3} \d{2}$
pattern = re.compile(r'\d{4} [A-Z0-9]{2} [0-2]\d:[0-6]\d:[0-6]\d[.]\d{3} \d{2}\r')


def check_input_data(readline):
    if pattern.fullmatch(readline):
        return True
    return False


class CheckTimeData:
    player_number = "0000"
    channel_id = "00"
    hours = 0
    minutes = 0
    seconds = 0
    float_of_time = 0
    group_number = 0

    def __init__(self):
        self.clear_data()

    def __init__(self, string):
        self.clear_data()
        self.format_input(string)

    def clear_data(self):
        self.player_number = "0000"
        self.channel_id = "00"
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.float_of_time = 0
        self.group_number = 0

    def format_input(self, string):
        if not check_input_data(string):
            return

        self.player_number = string[0:4]
        string = string[5:]

        self.channel_id = string[0:2]
        string = string[3:]

        self.hours = int(string[0:2])
        string = string[3:]
        self.minutes = int(string[0:2])
        string = string[3:]
        self.seconds = int(string[0:2])
        string = string[3:]

        self.float_of_time = int(string[0:3])
        string = string[4:]

        self.group_number = int(string[0:2])

    def get_group_number(self):
        return self.group_number

    def display_info(self):
        print('спортсмен, нагрудный номер ' + self.player_number +
              ' прошёл отсечку ' + self.channel_id + ' в ' +
              str(self.hours).zfill(2) + ':' +
              str(self.minutes).zfill(2) + ':' +
              str(self.seconds).zfill(2) + '.' +
              str(self.float_of_time)[0])

    def print_info_to_file(self, file):
        if not file.closed:
            file.write(self.player_number + ' ' +
                       self.channel_id + ' ' +
                       str(self.hours).zfill(2) + ':' +
                       str(self.minutes).zfill(2) + ':' +
                       str(self.seconds).zfill(2) + '.' +
                       str(self.float_of_time).zfill(3) + ' ' +
                       str(self.group_number).zfill(2) + '\n'
                       )
