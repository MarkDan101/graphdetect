
import requests,urllib3
import logging
from colorama import Fore, init
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Detector:
    init()
    GREEN = Fore.GREEN
    RESET = Fore.RESET
    GRAY = Fore.LIGHTBLACK_EX
    logger = logging.getLogger(__name__)

    def __init__(self,url):
        self.graphql_paths = [
            "",
            "/graphql",
            "/graphql/console",
            "/graphql.php",
            "/graphiql",
            "/graphiql.php",
            "/explorer",
            "/altair",
            "/playground"
        ]
        self.url = url

    def run(self):
        graphql = False
        for endpoint in self.graphql_paths:
            try:
                response = requests.get(self.url+endpoint,verify=False)
                if response.status_code in [200, 403]:
                    print('{}[+] GraphQL detected on {}{}'.format(self.GREEN,self.url+endpoint,self.RESET))
                    graphql = True
            except:
                self.logger.error('Endpoint is not reponding')
                continue
        if not graphql:
            print('{}[-] No GraphQL detected {}'.format(self.GRAY,self.RESET))