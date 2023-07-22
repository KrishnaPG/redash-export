#
# Usage:
#   python ./query_export.py --redash-url http://10.7.0.4:33080/  --api-key P4KlA0AM4JwYA1M6aNoydt5GVfMmZHQ5CVVexEZK
#
import click
import requests
import re
import json

def get_queries(url, api_key):
    headers = {'Authorization': 'Key {}'.format(api_key)}
    path = "{}/api/queries".format(url)
    has_more = True
    page = 1
    while has_more:
        response = requests.get(path, headers=headers, params={'page': page}).json()
        for result in response['results']:
            query = requests.get("{}/{}".format(path, result['id']), headers=headers).json()
            save_query(query)
        has_more = page * response['page_size'] + 1 <= response['count']
        page += 1

    return


def save_query(query):
    queryName = re.sub(r"\W+", '_', query['name'])
    filename = 'query_{}_{}.json'.format(query['id'], queryName)
    with open(filename, 'w') as f:
        f.write(json.dumps(query, indent=2))
        print('Generated: {}'.format(filename))

@click.command()
@click.option('--redash-url')
@click.option('--api-key', help="API Key")
def main(redash_url, api_key):
    get_queries(redash_url, api_key)


if __name__ == '__main__':
    main()