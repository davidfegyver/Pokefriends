import asyncio
import time

from PIL import Image
import yaml


from pyocr import pyocr
from pyocr import builders
from ADBlib import ADBlib
import sys
import re
friends = int(input("Barátok:"))
class Main:
    def __init__(self):
        with open("config.yaml", "r") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
        tools = pyocr.get_available_tools()
        self.tool = tools[0]
        self.friends = friends


    async def cap_and_crop(self, box_location):
        screencap = await self.p.screencap()
        crop = screencap.crop(self.config['locations'][box_location])
        text = self.tool.image_to_string(crop).replace("\n", " ").replace(" ","").replace("|","l")
        return text

    async def tap(self, location):
        coordinates = self.config['locations'][location]
        await self.p.tap(*coordinates)


    async def start(self):
        friendfile = open('friends.txt', 'a')
        self.p = ADBlib()
        for i in range(self.friends):
            try:
                name = await self.cap_and_crop("friendname")
                await self.tap('tap')
                friendfile.write(name+'\n')
            except:
                print("Error")


        friendfile.close()
if __name__ == '__main__':

    start_time = time.time()
    asyncio.run(Main().start())
    runtime = time.time() - start_time
    print("--- %s Barát lementve. Lefutási idő: %s másodperc. SPF(Second Per Friend): %s ---" % (friends,runtime, runtime/friends))




