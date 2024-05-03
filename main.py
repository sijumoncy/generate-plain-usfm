import asyncio
from usfm_grammar import USFMParser, Filter
import sys
import os

async def usfm_to_json(input_usfm: str):
    "usfm to json with grammar"
    usfm_parser = USFMParser(input_usfm)
    print('1')
    output_content = usfm_parser.to_usj(include_markers=Filter.BCV+Filter.TEXT)
    print('2')
    return output_content


async def usj_to_usfm(usj_obj):
    "usj to usfm"
    print("3")
    converted_usfm = USFMParser(from_usj=usj_obj)
    print("4")
    return converted_usfm.usfm


async def main():
    "main entry"
    try:
        args = sys.argv
        filename = ''

        if len(args) > 1:
            filename = args[1]
        else:
            print("Filename arguments is not provided, please try : python3 main.py <fileName.usfm> ")
            return

        if os.path.isfile(f'source/{filename}'):
            print("file Found. Started Processing. Please wait...")
            usfm_content: str = ''
            # reading usfm
            # with open('source/TIT.usfm') as f:
            #     usfm_content = f.read()
            
            # parsed_usj = await usfm_to_json(usfm_content)
            # usfm_from_usj = await usj_to_usfm(parsed_usj)
            # print("5")
            # usfm_obj = open("out/TIT.usfm", 'w', encoding = "utf-8")
            # usfm_obj.write(usfm_from_usj)
            print(f"Completed Processing.Check the output in out/{filename}")
        else:
            print(f"File : {filename} not exist in source directory.")
    except Exception as e:
        print("Error during processing : ", e)

    

if __name__ == "__main__":
    asyncio.run(main())
