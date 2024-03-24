"""
*   Tarpit.
*    
*   vs1m, 2024.
"""
import os, json, datetime
from flask import Flask, request

### Modules ###
from modules import discord, filter, logging

### Global Variables ###
# Get these from settings.json
HOST        = "0.0.0.0"
PORT        = "7777"
LOGGING     = False
PATH_BLOCK  = []
WEBHOOK     = None

app = Flask(__name__)

### Paths ###
@app.route("/")
@app.route("/index.html")
def index():
    return ""


@app.route("/<path:path>")
def paths( path ):
    data = {
        "path"    : "",
        "address" : "",
        "headers" : "",
        "cookies" : "",
    }

    update_pathblock()
    if path in PATH_BLOCK:
        # Don't log Favicon.
        if path == "favicon.ico": 
            return "200"

        log( f"[{datetime.datetime.now()}][{request.remote_addr}] BLOCKED PATH -> { path }" )
        return "200"
    
    try:
        data[ "path" ]    = path
        data[ "cookies" ] = request.cookies
        data[ "address" ] = request.remote_addr
        data[ "headers" ] = dict( request.headers )
            
        log( f"[{datetime.datetime.now()}][{request.remote_addr}] Asked for -> { path }" )

    except Exception as e:
        print( "! exception, details: ", e )

    discord.send( data, WEBHOOK )

    return "200"


### Helper functions ###
def log( msg ):
    if LOGGING:
        logging.write( msg )


def update_pathblock():
    global PATH_BLOCK
    _pathlist = filter.pathlist()
    
    # Error has occured, don't update
    if _pathlist == [ None ]:
        return False
    
    PATH_BLOCK = _pathlist


def load_config():
    global HOST 
    global PORT 
    global LOGGING 
    global WEBHOOK
    global PATH_BLOCK 

    config = dict()

    if not os.path.exists( "settings.json" ):
        print( "! Did not find settings.json .. trying to create it .." )
        with open( "settings.json", "w+" ) as file:
            file.write("""
{
    "host" : "0.0.0.0",
    "port" : "8888",

    "logging" : true,

    "path_block" : [
        "index.html", "favicon.ico"
    ],
    
    "discord_hook" : ""
}        
""" )
        
        print( "!!! CREATED settings.json, REMEMBER TO ADD YOUR WEBHOOK ADDRESS" )
        exit()

    try:
        with open( "settings.json", "r" ) as file:
            config = json.load( file )

        HOST        = config[ "host" ]
        PORT        = config[ "port" ]
        LOGGING     = config[ "logging" ]
        PATH_BLOCK  = config[ "path_block" ]
        WEBHOOK     = config[ "discord_hook" ]

    except KeyError as e:
        print( "! ran into an KeyError: ", e )
        print( "Is the settings.json file intact?" )
        return False
    
    except Exception as e:
        print( "! ran into an exception, details: ", e )
        print( "!!! RUNNING APPLICATION WITH DEFAULT SETTINGS !!!" )
        print( "!!! AND NO PATH FILTER !!!" )
        return False

    return True


if __name__ == "__main__":
    load_config()
    app.run( host= HOST, port= PORT )
