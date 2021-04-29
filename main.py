"""required libs"""
import pandas as pd
import json

"""The Main Dictionary"""
main_dict = {"intents": []}

"""Take The tag,pattern & response and adds them to the dictionary"""
def add_to_dict(tag, pattern, response):
    pattern_set = list()
    response_set = list()
    if len(main_dict["intents"]) > 0:
        for i in range(len(main_dict["intents"])):
            if main_dict["intents"][i]["tag"] == tag:
                main_dict["intents"][i]["patterns"].append(pattern)
                main_dict["intents"][i]["responses"].append(response)
                break
        else:
            pattern_set.append(pattern)
            response_set.append(response)
            main_dict["intents"].append({"tag": tag, "patterns": pattern_set, "responses": response_set})
    else:
        pattern_set.append(pattern)
        response_set.append(response)
        main_dict["intents"].append({"tag": tag, "patterns": pattern_set, "responses": response_set})


"""The Main adding fuction"""
def add_to_dict_main(t, pattern, response='NO RESPONSE'):
    tags = t.split("#")
    for tag in tags:
        add_to_dict(tag, pattern, response)


"""This fuction reads the CSV file"""
def read_csv(filename):
    return pd.read_csv(filename)


"""This function converts the CSV file to the main dictionary"""
def csv_to_dict(dataframe):
    for row in dataframe.iterrows():
        add_to_dict_main(row[1][0], row[1][1])


"""This function converts the main dictionary to json format"""
def dict_to_json():
    fname = input("Enter CSV File Name : ")
    try:
        df = read_csv("{}.csv".format(fname))
        csv_to_dict(df)
        with open("{}.json".format(fname), 'a', encoding='utf8') as jsonfile:
            json_data = json.dumps(main_dict)
            jsonfile.write(json_data)
    except FileNotFoundError as e:
        print(str(e))

"""Main"""
if __name__ == "__main__" :
    """Number of files you want to convert ( must be integer )"""
    try:
        no = int(input("How many CSV files you want to convert ?? "))
        for file in range(no):
            dict_to_json()
    except TypeError as e:
        print(str(e))