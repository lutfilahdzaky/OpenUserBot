import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.oi(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	sleep(3)
	await typew.edit("`Muka Gw Burik...`")
	sleep(3)
	await typew.edit("`Kayak Kontol`")
	sleep(1)
	await typew.edit("`Muka Gw Burik Kayak Kontol`")
# Create by myself @AkameNFS





