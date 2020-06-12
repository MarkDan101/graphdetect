
import argparse, requests, urllib.request

parser = argparse.ArgumentParser(description="GraphQL endpoint dectector")
parser.add_argument("url", type=str, help="To accept ")
parser.add_argument("--output",action='store',default=False, help='verify')
#parser.add_argument("input_queue",action='store',default=False,help='input rec')
args = parser.parse_args()
url=args.url
#output=args.output
#input_queue = args.input_queue
consoleDict = [
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
for endpoint in consoleDict:
        ep = url+endpoint
        response = requests.get(ep)
        if response.status_code in [200, 403]:
            print('Its a graphql Page', endpoint)
        

output = args.output
