def write( data ):
    with open( "log.txt", "a+" ) as file:
        file.write( f"{data}\n" )