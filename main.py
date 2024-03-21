from os import listdir
from json import load


def get_addresses():
    with open('addresses.txt') as f:
        return f.read().splitlines()


def get_all_elibigle_addresses():
    all_addresses_lst = []
    for index, json_file in enumerate(listdir('jsons')):
        with open(f'jsons/{json_file}', encoding="utf-8") as f:
            addresses = load(f)
            # print(f'Parsing file: [{index+1}/{len(listdir("jsons"))}]')
            all_addresses_lst.append(addresses)

    all_addresses = dict(dict_item for dict_part in all_addresses_lst for dict_item in dict_part.items())
    print(f'Loaded all eligible addresses count: {len(all_addresses)}\n')
    return all_addresses


def get_my_eligible(addresses: dict, all_eligible: dict):
    total_points = 0
    total_wallets = 0
    for index, address in enumerate(addresses):
        points = all_eligible.get(address.lower()) or 0
        print(f'[{index+1}/{len(addresses)}] {address}: {points}')
        if points > 0:
            total_points += points
            total_wallets += 1

    print(f'\nTotal points: {total_points}\nWallets statistics: {total_wallets}/{len(addresses)} eligible')


if __name__ == '__main__':
    addresses = get_addresses()
    all_eligible = get_all_elibigle_addresses()

    get_my_eligible(addresses=addresses, all_eligible=all_eligible)

    input(f'\n\n> Exit')
