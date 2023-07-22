# redash-export
Export Redash Queries and Dashboards as JSON

Redash allows you to create queries and dashboards through UI. But if you need to persist the created queries, visualization settings and the dashboards as code, so that you can recreate them later in another Redash instance, you can use this Export scripts.

## Usage:
```sh
   python ./dashboard_export.py --redash-url <YOUR_REDASH_URL>  --api-key <YOUR_REDASH_API_KEY>
```
