import requests

class Discord_hook:
    def __init__( self, url ):
        self.webhook = url


    ### Implementation ###
    def beautify( self, data ) -> str:
        """
        * @brief
        *   format the raw request data into a human readable form. 
        """
        s_data = str()

        _headers = f"+ Request Headers: "
        for key in sorted( data[ "headers" ] ):
            _headers += f"\n\t> { key }: { data[ 'headers' ][ key ]}"
        _headers += "\n"

        _path    = f"+ Path requested: \n\t> { data[ 'path' ]}\n"
        _path    = f"+ Params: \n\t> { data[ 'params' ]}\n"
        _address = f"+ Remote address: \n\t> { data[ 'address' ] }\n" 
        _cookies = f"+ Cookies: \n\t> { data[ 'cookies' ] }\n"

        s_data = f"```\n{ _path }\n{ _address }\n{ _headers }\n{ _cookies }\n```"

        return s_data


    ### Interface ###
    def send( self, data):
        message = { 
            "content" : self.beautify( data )
        }

        if self.webhook == None:
            print( "[!] [DISCORD] Can't send to webhook: Webhook is 'None'" )
            return False

        response = requests.post(
            "https://discord.com/api/webhooks/" + self.webhook,
            json = message
        )

        if int(response.status_code) == 400:
            print(f"[!] [DISCORD] 400 from webhook: ", response.text)
            return False

        if int(response.status_code) == 404:
            print(f"[!] [DISCORD] 404 from webhook: ", response.text)
            print("[!] [DISCORD] IS THE WEBHOOK ADDRESS CORRECT?")
            return False

        print("[+] [DISCORD] Sent message to hook!")
        return True