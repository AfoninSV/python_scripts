data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "total_in": 444,
        "total_out": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}


def print_pair_values(data_dict):
    for i_item, item in enumerate(data_dict.items()):
        if i_item % 2 == 0:
            print(f'{item[0]} : {item[1]} ')

        elif i_item == 1:
            print(f'{item[0]} :')
            for key in item[1].keys():
                print(f'\t{key} : {item[1][key]}')

        elif i_item == 3:
            print(f'{item[0]} :')
            for i_dict in item[1]:

                for i_key in i_dict:

                    if i_key == 'sec_token_info' or i_key == 'fst_token_info':
                        print(f'\t{i_key} :')
                        for j_dict in i_dict[i_key]:
                            print(f'\t\t{j_dict} : {i_dict[i_key][j_dict]}')
                    else:
                        print(f'\t{i_key} : {i_dict[i_key]}')



data['ETH']['total_diff'] = 100
data['tokens'][0]['fst_token_info']['name'] = 'doge'
data['ETH']['total_out'] = data['tokens'][1].pop('total_out')
data['tokens'][1]['sec_token_info']['total_price'] = \
    data['tokens'][1]['sec_token_info'].pop('price')

print_pair_values(data)