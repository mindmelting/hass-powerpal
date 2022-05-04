from encodings import utf_8
import sys
import asyncio
import logging

from bleak import BleakClient, BleakScanner, BleakError

logger = logging.getLogger(__name__)

ADDRESS = (
    "30:1B:97:00:00:00"
)
MY_PAIRING_CODE = 123123

pairingCodeChar = '59DA0011-12F4-25A6-7D4F-55961DCE4205'
powerpalUUIDChar ='59DA0009-12F4-25A6-7D4F-55961DCE4205'

def convert_pairing_code(original_pairing_code):
    return original_pairing_code.to_bytes(4, byteorder='little')


async def main(address, my_pairing_code):
    async with BleakClient(address) as client:
        logger.info(f"Connected: {client.is_connected}")


        logger.info(f"Authenticating with pairing_code: {my_pairing_code}, converted: {convert_pairing_code(my_pairing_code)}")
        await client.write_gatt_char(pairingCodeChar, convert_pairing_code(my_pairing_code), response=False)
        logger.info('Writing: Success')

        await asyncio.sleep(0.5)

        logger.info(f"Attempting to retrieve apikey (Powerpal UUID)...")

        apikey = await client.read_gatt_char(powerpalUUIDChar)

        logger.info(f"Retrieved apikey: {apikey}")

        # while True:
        #     await asyncio.sleep(0.1)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main((sys.argv[1] if len(sys.argv) >= 2 else ADDRESS),(sys.argv[2] if len(sys.argv) == 3 else MY_PAIRING_CODE)))
