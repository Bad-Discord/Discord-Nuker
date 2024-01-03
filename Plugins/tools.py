import requests as req, os, random


from Plugins.logger import Logger



class Tools:
    @staticmethod
    def check_token(token: str):
        if req.get("https://discord.com/api/v10/users/@me", headers={"Authorization": "Bot %s" % token}).status_code == 200:
            return True
        else:
            Logger.Error.error("Invalid token %s" % token)
            return False
    
    @staticmethod
    def get_guilds(token: str):
        headers = {"Authorization": "Bot %s" % token , "Content-Type": 'application/json'}
        url = Tools.api("users/@me/guilds")

        request = req.get(url, headers=headers)

        if request.status_code != 200 or len(request.json()) == 0:
            return False
        
        return [[i["id"], i["name"]] for i in request.json()]
    


    @staticmethod
    def proxy():
        if os.path.exists("./proxies.txt"):
            with open("./proxies.txt", "r") as file:
                lines = file.readlines()

                if len(lines) != 0:
                    p = random.choice(
                        [i.strip() for i in lines]
                    )
                    return {"http": p, "https": p}
        else:
            return None
    
    @staticmethod
    def api(endpoint: str):
        base_api = "https://discord.com/api/v10/"
        if endpoint.startswith("/"):
            endpoint = endpoint[1:]

        return base_api+endpoint 
    
    @staticmethod
    async def break_limit(base_api: str, token: str):
        chunk_size = 1000

        users = []

        while True:
            headers = {"Authorization": "Bot %s" % token}
            parm = "?limit=%s" % chunk_size
            if len(users) != 0:
                parm+="&?after=%s" % users[::-1][0]
            
            r = req.get(base_api+parm, headers=headers)
            if r.status_code == 200:
                try:
                    ids = [i["user"]["id"] for i in r.json()]
                except KeyError:
                    ids = [i["id"] for i in r.json()]


                users+=ids

                if len(ids) < chunk_size: break
            else:
                break
        
        return users

    @staticmethod
    def chunker(text, chunk_size: int) -> list:
        length = len(text)
        num = 0
        chunks = []

        while num < len(text):
            chunks.append(text[num:length-(length-(chunk_size))+num:])
            num+=chunk_size

        return chunks
    
    @staticmethod
    def information(guild_id: str, token: str):
        url = Tools.api("users/@me")
        headers = {"Authorization": "Bot %s" % token}

        user = req.get(url, headers=headers)

        url = Tools.api(f"/guilds/{guild_id}")
        guild = req.get(url, headers=headers)


        info_dict = {
            "user": user.json(),
            "guild": guild.json()
        }
        return info_dict