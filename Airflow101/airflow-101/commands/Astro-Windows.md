- Download the Latest .exe file from https://github.com/astronomer/astro-cli/releases

- Rename the file to `astro.exe`.

- Add the path to system environment.

- Initiate astro environment: `C:\User\Downloads\astro dev init`.

- To start the dev:

    - Start docker engine

    - Inside astro environment `C:\User\Downloads\astro dev start`

- `astro dev run providers list` to see a list of providers.

- `astro dev stop` to stop the container.

- `astro dev start` to start the container.

- `astro dev restart` to restart the container.

- To parse a dag: `astro dev parse`

- To test dags: `astro dev pytest`

- To test DAGs efficiently: `astro dev run <dag-id>`

- 