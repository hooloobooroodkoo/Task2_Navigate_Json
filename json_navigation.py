"""
This module includes function which will help the user\
to find needed information zbout Twitter user in json file.
"""
import json
from colored import fg, attr


def read_json_return_data(path):
    """
    This function reads json file and returns data from it.
    """
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def find_in_json(data, previous_data):
    """
    This function gives an opportunity to the user to find needed information in json file.
    """
    print('%sChoose the type of information you want to see \nor make one step back entering "back":%s' % (
        fg(99), attr(0)))
    print(list(data.keys()))
    key = input()
    if key == 'back':
        return find_in_json(previous_data[-2], previous_data[:-1])
    elif key == '':
        return None
    else:
        if isinstance(data[key], list):
            print(f'%sHere are several blocks of information.\nChoose block from 1 to {len(data[key])}:%s' % (
                fg(99), attr(0)))
            index = int(input()) - 1
            previous_data.append(data[key][index])
            return find_in_json(data[key][index], previous_data)
        if isinstance(data[key], dict):
            previous_data.append(data[key])
            return find_in_json(data[key], previous_data)
    return f'%s{data[key]}%s' % (fg(99), attr(0))


if __name__ == "__main__":
    print('%sPlease enter the path to json file:%s' % (fg(99), attr(0)))
    path_to_json = input()
    data_from_json = read_json_return_data(path_to_json)
    print(find_in_json(data_from_json, [data_from_json]))

