import requests
import asyncio  
async def compile_code(code):
    print("compiling...")
    url = "https://online-code-compiler.p.rapidapi.com/v1/"
    payload = {
        "language": "java",
        "version": "latest",
        "code": f"{code}",
        "input": None
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "4a1a56f92dmshb5aedf64a947abfp1f1a18jsnf46627b6bf76",
        "X-RapidAPI-Host": "online-code-compiler.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return (response.json())
# async def main():   
#     response=await compiler(code)  
#     print (response['output'])   
# asyncio.run(main())  

