
class bcolors:
    HEADER = '\033[95m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def show(data, query):
    print("\n\n\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print('\n', bcolors.OKBLUE, bcolors.BOLD, bcolors.HEADER, "Here's a list of {} near you".format(query), bcolors.ENDC, '\n')
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    print('\n')
    for item in data:
        print('  - ', bcolors.BOLD, item['name'], bcolors.ENDC, '\n')
        print(bcolors.OKGREEN, '    * ', bcolors.ENDC,
              bcolors.DARKCYAN ,'Address: ' , bcolors.ENDC,
              item['formatted_address'], '\n',
              bcolors.OKGREEN, '   * ', bcolors.ENDC,
              bcolors.DARKCYAN ,'Rating: ' , bcolors.ENDC,
              item['rating'], '\n',
              )
