import json
import requests
from urllib import parse

paths = [
    "",
    "/graphql",
    "/graphql/console",
    "graphql.php",
    "graphiql",
    "explorer",
    "altair",
    "/playground"
]

query = """{
  __schema {
    types {
      name
    }
  }
}
"""

for path in paths:
    hostname = 'http://159.100.248.211'
    endpoint = parse.urljoin(hostname, path)
    try:
        print(f"Attempt: {endpoint}")
        response = requests.post(endpoint, json={'query': query}, timeout=0.1)
    except Exception:
        print("No GraphQL endpoint found")
    else:
        if response.status_code == 200:
            json_data = json.loads(response.text)
            if json_data.get('data'):
                print("It is a GraphQL endpoint",endpoint)
