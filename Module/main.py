import asyncio
import aiohttp
import datetime
import json

ResponseData=[]

async def api(url,key):
    # global ReponseData
    session = aiohttp.ClientSession()

    response = await session.get(url)

    text=await response.read()
    text= json.loads(text)
    await session.close()
    ResponseData.append(text[key]+"\n")

async def main(url,key):
    tasks=[]
    for x in range(500):
        tasks.append(asyncio.create_task(api(url,key)))
    for t in tasks:
        await t
    with open("Output.txt","a",encoding="utf-8") as f:
        f.writelines(ResponseData)

def starter(url,key):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(url,key))