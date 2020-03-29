import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	sleep(1)
	await typew.edit("`Ucap Salam Goblok...`")
	sleep(1)
	await typew.edit("`Assalamualaikum`")
# Create by myself @AkameNFS

@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	sleep(1)
	await typew.edit("`Ucap Salam Goblok...`")
	sleep(1)
	await typew.edit("`Assalamualaikum`")
# Create by myself @AkameNFS





