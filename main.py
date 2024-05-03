import asyncio
from usfm_grammar import USFMParser, Filter
import sys
import os
from colorama import init, Fore, Back
import pathlib

async def usfm_to_json(input_usfm: str):
    "usfm to json with grammar"
    usfm_parser = USFMParser(input_usfm)
    output_content = usfm_parser.to_usj(include_markers=Filter.BCV+Filter.TEXT)
    return output_content


async def usj_to_usfm(usj_obj):
    "usj to usfm"
    converted_usfm = USFMParser(from_usj=usj_obj)
    return converted_usfm.usfm


async def main():
    "main entry"
    try:
        # init coloroma
        init(autoreset=True)

        args = sys.argv
        filenames = []

        if len(args) > 1:
            if args[1] == 'all':
                extension = '.usfm'
                filenames = [f for f in os.listdir("source") if f.endswith(extension)]
            else: 
                filenames = args[1:]
        else:
            print(Fore.RED + Back.LIGHTWHITE_EX + "Filename arguments is not provided, please try : python3 main.py <fileName.usfm> ")
            return

        # create out directory
        pathlib.Path("out").mkdir(parents=True, exist_ok=True)

        for file in filenames:
            if os.path.isfile(os.path.join("source", file)):
                print(Fore.LIGHTGREEN_EX + f"file {file} Found. Started Processing. Please wait...")
                usfm_content: str = ''
                # reading usfm
                with open(os.path.join("source", file)) as f:
                    usfm_content = f.read()
                parsed_usj = await usfm_to_json(usfm_content)
                usfm_from_usj = await usj_to_usfm(parsed_usj)
                usfm_obj = open(os.path.join("out", file), 'w', encoding = "utf-8")
                usfm_obj.write(usfm_from_usj)
                print(Fore.GREEN + f"Completed Processing : {file}")
            else:
                print(Fore.RED + Back.LIGHTWHITE_EX + f"File : {file} not exist in source directory.")
            print(Fore.CYAN + "-----------------------------------------------------------------------------------------------------")
        print("Processing Completed. Check /out for the files")
    except Exception as e:
        print(Fore.RED + Back.LIGHTWHITE_EX + "Error during processing : ", e)

    

if __name__ == "__main__":
    asyncio.run(main())
