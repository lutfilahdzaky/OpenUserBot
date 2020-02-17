import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.santet(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Memulai Menyantet Korban...`")
	sleep(1)
await typew.edit("`Mencari Informasi Korban`")
sleep(1)
await typew.edit("`Informasi Didapatkan`")
sleep(1)
await typew.edit("`Mengirim Santen Diproses`")
sleep(1)
await typew.edit("0%")
number = 1
sleep(1)
await typew.edit(str(number) + "%   ▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   █████████████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ██████████████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████████▊")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ███████████████▉")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████████")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████████▎")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████████▍")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████████▌")
number = number+ 1
sleep(0.03)
await typew.edit(str(number) + "%   ████████████████▌")
sleep(1)
await typew.edit("`Korban Telah Disantet!`")
sleep(1)
await typew.edit("`Tapi Boong. Hiya Hiya Hiya`")
# I did it for two hours :D just ctrl+c - crtl+v






