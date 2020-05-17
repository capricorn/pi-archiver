import asyncio

from predictit import piws
from predictit import pi

async def callback(msg):
    print(msg)

async def main():
    ws = piws.PredictItWebSocket()
    ws.set_queue_callback(callback)
    await ws.start()

#asyncio.run(main())
p = pi.PredictItAPI(0)
print(p.get_markets())
