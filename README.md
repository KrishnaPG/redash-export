# redash-export
Export Redash Queries and Dashboards as JSON

Redash allows you to create queries and dashboards through UI. But if you need to persist the created queries, visualization settings and the dashboards as code, so that you can recreate them later in another Redash instance, you can use this Export scripts.

## Usage:
 - To export the Queries from the Redash, run the below command:
   ```sh
      python ./query_export.py --redash-url <YOUR_REDASH_URL>  --api-key <YOUR_REDASH_API_KEY>
   ```
 - To export the Dashboards from the Redash, run the below command:
   ```sh
      python ./dashboard_export.py --redash-url <YOUR_REDASH_URL>  --api-key <YOUR_REDASH_API_KEY>
   ```

#### Credit
Originally based on the GIST: https://gist.github.com/y-yoi/059006cbab4437ad6eca94c1cf497ccf later heavily modified to streamline the download and output to JSON.
