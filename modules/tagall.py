# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

@bot.on(events.NewMessage(pattern=r"\.tagall", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tagall"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.edit(mentions)
