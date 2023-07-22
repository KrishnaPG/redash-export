#
# Usage:
#   python ./dashboard_export.py --redash-url http://10.7.0.4:33080/  --api-key P4KlA0AM4JwYA1M6aNoydt5GVfMmZHQ5CVVexEZK
#
import click
import requests
import re
import json

def get_dashboards(url, api_key):
    headers = {'Authorization': 'Key {}'.format(api_key)}
    path = "{}/api/dashboards".format(url)
    has_more = True
    page = 1
    while has_more:
        response = requests.get(path, headers=headers, params={'page': page}).json()
        for result in response['results']:
            dashboard = requests.get("{}/{}".format(path, result['slug']), headers=headers).json()
            save_dashboard(dashboard)
        has_more = page * response['page_size'] + 1 <= response['count']
        page += 1

    return


def save_dashboard(dashboard):
    dashboardName = re.sub(r"\W+", '_', dashboard['name'])
    filename = 'dashboard_{}_{}.json'.format(dashboard['id'], dashboardName)
    with open(filename, 'w') as f:
        f.write(json.dumps(dashboard, indent=2))
        print('Generated: {}'.format(filename))

@click.command()
@click.option('--redash-url')
@click.option('--api-key', help="API Key")
def main(redash_url, api_key):
    get_dashboards(redash_url, api_key)


if __name__ == '__main__':
    main()