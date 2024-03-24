"""
*   This is slightly messy with only Discord as the interface.
*
*   It's implemented this way to make implementing new alert
*   systems easier. If you want to add for example Telegram,
*   you'd just have to import it, add to initialization,
*   and then switch the send() function so that it sends the
*   data to Telegram.send() instead of Discord.send(). 
*
*   I have left comments as TODO:'s for this exact purpose!
*
"""

from .messaging import discord

### Global Variables ###
Discord = None


def initialization( webhook_url ): 
    global Discord
    Discord = discord.Discord_hook( webhook_url )

    #TODO: Add:
    # Telegarm = telegram.Telegram_hook( url )


def send( data ):
    Discord.send( data )

    #TODO: Add:
    # Telegarm.send( data )