import json


### Interface ###
def pathlist() -> list:   
    return load_from_config()


### Implementation ###
def load_from_config() -> list:
    config = dict()
    path_block = list()

    try:
        with open( "settings.json", "r" ) as file:
            config = json.load( file )

        path_block = config[ "path_block" ]

    except KeyError as e:
        print( "! ran into an KeyError reading settings.json['path_block']: ", e )
        print( "Is the settings.json file intact?" )
        return [ None ]

    except Exception as e:
        print( "! ran into an exception reading settings.json['path_block']: ", e )
        return [ None ]

    return path_block
