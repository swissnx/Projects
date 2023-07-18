
import requests
from datetime import datetime as dt


class SteamIDFinder:
    def __init__(self):
        self.__steamid64ident = 76561197960265728
        self.__apikey = "YOUR_API_KEY_HERE"
        self.__steam_id = None
        self.__name = None
        self.__profile_url = None
        self.__profile_permalink = None
        self.__BASE_URL = "http://api.steampowered.com/"
        self.__USER_URL = self.__BASE_URL + "ISteamUser/GetPlayerSummaries/v0002/"
        self.__GAME_URL = self.__BASE_URL + "IPlayerService/GetOwnedGames/v0001/"
        self.__BAN_URL = self.__BASE_URL + "ISteamUser/GetPlayerBans/v1/"

    def __steam64_to_steamid(self, steam64):
        steamidacct = int(steam64) - self.__steamid64ident
        y = '0:' if steamidacct % 2 == 0 else '1:'
        steamid = ['STEAM_0:', y, str(steamidacct // 2)]
        return ''.join(steamid)

    def __steamid_to_steam64(self, steamid):
        sid_split = steamid.split(':')
        steam64 = int(sid_split[2]) * 2
        if sid_split[1] == '1':
            steam64 += 1
        steam64 += self.__steamid64ident
        return steam64

    @staticmethod
    def __steamid_to_usteamid(steamid):
        steamid_split = steamid.split(':')
        y = int(steamid_split[1])
        z = int(steamid_split[2])
        steamacct = z * 2 + y
        usteamid = ['U:1:', str(steamacct)]
        return ''.join(usteamid)

    def __steam64_to_usteamid(self, steam64):
        steamidacct = int(steam64) - self.__steamid64ident
        usteamid = ['U:1:', str(steamidacct)]
        return ''.join(usteamid)

    @staticmethod
    def __usteamid_to_steamid(usteamid):
        for ch in ['[', ']']:
            if ch in usteamid:
                usteamid = usteamid.replace(ch, '')
        usteamid_split = usteamid.split(':')
        z = int(usteamid_split[2])
        y = '0:' if z % 2 == 0 else '1:'
        steamacct = z // 2
        steamid = ['STEAM_0:', y, str(steamacct)]
        return ''.join(steamid)

    def __usteamid_to_steam64(self, usteamid):
        for ch in ['[', ']']:
            if ch in usteamid:
                usteamid = usteamid.replace(ch, '')
        usteamid_split = usteamid.split(':')
        steam64 = int(usteamid_split[2]) + self.__steamid64ident
        return steam64

    def __fetch_name(self):
        response = requests.get(f"{self.__USER_URL}/?key={self.__apikey}&steamids={self.__steam_id}")
        data = response.json()
        self.__name = data["response"]["players"][0]["personaname"]

    def __generate_profile_url(self):
        response = requests.get(f"{self.__USER_URL}/?key={self.__apikey}&steamids={self.__steam_id}")
        data = response.json()
        self.__profile_url = data["response"]["players"][0]["profileurl"]

    def __generate_profile_permalink(self):
        self.__profile_permalink = f"https://steamcommunity.com/profiles/{self.__steam_id}"

    def __get_profile_state(self, pState):
        profile_states = {0: "Offline",
                          1: "Online",
                          2: "Busy",
                          3: "Away",
                          4: "Snooze",
                          5: "Looking to trade",
                          6: "Looking to play"
                          }
        return profile_states.get(pState, "Unknown")

    def __get_visibility_state(self, viState):
        visibility_states = {1: "Private",
                             3: "Public"
                             }
        return visibility_states.get(viState, "Unknown")

    def __retrieve_profile_photos(self):
        request = requests.get(self.__USER_URL + "?key=" + self.__apikey + "&steamids=" + str(self.__steam_id))
        response = request.json()
        data = response["response"]["players"][0]
        avatars = {"normal": data["avatar"],
                   "medium": data["avatarmedium"],
                   "full": data["avatarfull"]
                   }
        return avatars

    def __get_games(self, includeFree=False):
        includeFree = includeFree and "1" or "0"
        steam_id = str(self.__steam_id)
        request = requests.get(
            self.__GAME_URL + "?key=" + self.__apikey + "&steamid=" + steam_id + "&include_played_free_games=" + includeFree + "&include_appinfo=1"
        )
        response = request.json()
        data = response["response"]

        if not data:
            return None, None
        games = []
        for game in data["games"]:
            game_object = {"id": game["appid"],
                           "name": game["name"],
                           "playtime": game["playtime_forever"] // 60 #converting to hrs
                           }
            games.append(game_object)
        return data["game_count"], games

    def __get_bans(self):
        request = requests.get(self.__BAN_URL + "?key=" + self.__apikey + "&steamids=" + str(self.__steam_id))
        response = request.json()
        data = response["players"][0]
        return data["VACBanned"], data["NumberOfVACBans"]

    def __get_account_creation_date(self):
        response = requests.get(f"{self.__USER_URL}/?key={self.__apikey}&steamids={self.__steam_id}")
        data = response.json()
        time_created = data["response"]["players"][0]["timecreated"]
        creation_date = dt.fromtimestamp(time_created)
        return creation_date

    def __run(self):
        while True:
            steam_id = input("\nEnter Steam ID: ")
            if steam_id.startswith("STEAM_0"):
                self.__steam_id = self.__steamid_to_steam64(steam_id)
            elif steam_id.startswith("U:1"):
                self.__steam_id = self.__usteamid_to_steam64(steam_id)
            elif steam_id.isdigit() and len(steam_id) < 16:
                self.__steam_id = int(steam_id) + self.__steamid64ident
            else:
                self.__steam_id = steam_id
            self.__fetch_name()
            self.__generate_profile_url()
            self.__generate_profile_permalink()
            game_count, games = self.__get_games(includeFree=True)
            vac_banned, vac_ban_count = self.__get_bans()
    
            print(f"\nSteam ID: {self.__steam64_to_steamid(self.__steam_id)}")
            print(f"Steam ID3: {self.__steam64_to_usteamid(self.__steam_id)}")
            print(f"Steam32 ID: {int(self.__steam_id) - self.__steamid64ident}")
            print(f"Steam64 ID: {self.__steam_id}")
            print(f"\nName: {self.__name}")
            print(f"Profile URL: {self.__profile_url}")
            print(f"Permalink: {self.__profile_permalink}")
    
            response = requests.get(f"{self.__USER_URL}/?key={self.__apikey}&steamids={self.__steam_id}")
            data = response.json()
            self.__name = data["response"]["players"][0]["personaname"]
            self.__profile_url = data["response"]["players"][0]["profileurl"]
            self.__profile_permalink = f"https://steamcommunity.com/profiles/{self.__steam_id}"
            profile_state = self.__get_profile_state(data["response"]["players"][0]["personastate"])
            visibility_state = self.__get_visibility_state(data["response"]["players"][0]["communityvisibilitystate"])
            avatars = self.__retrieve_profile_photos()
            game_count, user_games = self.__get_games(includeFree=True)
            vac_banned, vac_ban_count = self.__get_bans()
    
            print(f"\nVisibility Status: {visibility_state}")
            print(f"Online State: {profile_state}")
            print("Avatars:")
            for k, v in avatars.items():
                print(f"  avatar_{k}: {v}")
              
            print(f"\nAccount Created: {self.__get_account_creation_date()}")
            print(f"VAC Banned: {vac_banned}")
            print(f"Game Bans Count: {vac_ban_count}")

            while True:
                show_games = input("\nWould you like the game list to be printed? (y/n): ")
                if show_games.lower() == "y":
                    print(f"\nTotal Games: {game_count}\n")
                    if user_games is not None:
                        for game in user_games:
                            game_id = game['id']
                            game_name = game['name']
                            game_playtime = game['playtime']
                            print(f"ID: {game_id} | Game: {game_name} | Playtime: {game_playtime}")
                    break
                elif show_games.lower() == "n" or not show_games:
                    break

            try_again = input("\nTry a new Steam ID? (y/n): ")
            if try_again.lower() != "y":
                break

    def run(self):
        try:
            self.__run()
        except Exception as e:
            print(f"\n\u001b[3m✶!✶ Error: \u001b[38;5;200m{e}\u001b[0m")


if __name__ == "__main__":
    steam_id_finder = SteamIDFinder()
    steam_id_finder.run()
