import asyncio
import telnetlib3

from proc_data import check_input_data
from proc_data import CheckTimeData

# @asyncio.coroutine
def shell(reader, writer):
    while 1:
        try:
            inp = yield from reader.readline()
        except:
            pass #
        finally:
            if not check_input_data(inp):
                continue

            obj = CheckTimeData(inp)

            file = open('log.txt', 'a')
            try:
                obj.print_info_to_file(file)
            finally:
                file.close()

            if obj.get_group_number() == 0:
                obj.display_info()

# создание Telnet-сервера
loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=23, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())
