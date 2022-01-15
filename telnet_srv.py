import asyncio
import logging
import telnetlib3
from proc_data import CheckTimeData


async def shell(reader, writer):
    try:
        inp = await reader.readline()
    finally:
        if CheckTimeData.check_input_data(inp):
            obj = CheckTimeData(inp)

            await obj.print_info_to_file()

            if obj.get_group_number() == 0:
                await obj.display_info()

    if inp:
        await shell(reader=reader, writer=writer)

# создание Telnet-сервера
loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(host='localhost', port=23, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())
