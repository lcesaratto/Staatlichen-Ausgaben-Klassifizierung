# Case-Study: Staatlichen Ausgaben Klassifizierung

## Datenbeschreibung

Der Bundesstaat Berlin veröffentlicht jährlich die Details von staatlichen Ausgaben. Die Datensatz und Dateidefinitionen sind zu finden unter:

- https://www.berlin.de/sen/finanzen/service/zuwendungsdatenbank/

Ein Auszug der Dateien:

| Name                                                                     | Geber               | Art              | Jahr | Anschrift                       | Politikbereich | Zweck                                      | Betrag |
| ------------------------------------------------------------------------ | ------------------- | ---------------- | ---- | ------------------------------- | -------------- | ------------------------------------------ | ------ |
| ImPULS e. V.                                                             | Bezirksamt Neukölln | Projektförderung | 2016 | Bat-Yam-Platz 1, 12353 Berlin   | Bildung        | Sprachschulungen für aktive Gropiusstädter | 6607   |
| Verein zur Förderung der Kommunikation unter Gropiusstädter Frauen e. V. | Bezirksamt Neukölln | Projektförderung | 2016 | Löwensteinring 22, 12353 Berlin | Familie        | Kinderbildungscafe                         | 2499   |
| Verein zur Förderung der Kommunikation unter Gropiusstädter Frauen e. V. | Bezirksamt Neukölln | Projektförderung | 2016 | Löwensteinring 22, 12353 Berlin | Jugend         | Service Learning                           | 15363  |

## Aufgabenbeschreibung

### Klassifizierung

Einzelne Ausgaben müssen basierend auf Zweck Felde, in den passenden Politikbereich zugeordnet werden.

### Clustering/Topic Modelling

In der Praxis fehlen die Kategorie-Kennzeichnungen. Um dieses Problem beheben zu können, wird nach Gruppierungen in dem Datensatz gesucht. Deine Aufgabe ist es, diese Gruppierungen anhand einer Kombination der Felder Zweck und Name zu finden.

### Technologies

- Python 3.9+
- Poetry
- Scrapy
- Pandas
- Seaborn
- Pytorch
- Huggingface
- Scikit-learn
- Spacy
- Docker

### Data gathering

1. Execute cells in `0_Scrape_dataset.ipynb` to get the dataset downloaded to `data/raw_data.csv`

### Local Development

1. Clone repository and `cd` into repository directory
2. Check Python version `python -V`. Check recommended Python version in Technologies section
3. [Install Poetry](https://python-poetry.org/docs/#installation) (recommended) or skip this step for an isolated installation of Poetry
4. Create a virtual enviroment `python -m venv venv`
5. Install Poetry inside the virtual enviroment `pip install poetry`. Skip this step if Poetry is already available globally (as explained in step 3)
6. Install dependencies `poetry install`
7. Install CUDA 11 or newer
8. Execute in console `poe force-cuda11` to install Pytorch 1.7.1+cu110 or simply `poetry add torch`, but be careful that the pytorch version is compatible with the CUDA version installed. For more information about poe check the [link](https://github.com/python-poetry/poetry/issues/2613#issuecomment-799693903)
9. Execute `jupyter-lab` to visualize the project notebooks

### Local Deployment for Windows Users

1. [Install Docker](https://docs.docker.com/desktop/windows/install/) with WSL2 backend
2. Check WSL version installed `wsl -l -v`. The listed version must be 2
3. Execute in Windows Console `docker run hello-world` to check if Docker is working correctly
4. Execute in console `docker-compose up -d --build` to create the container
5. Jupyter Lab available at `http://localhost:10000/lab`. Password is "docker"

### Local Deployment for Linux/Mac Users

1. [Install Docker](https://www.docker.com/products/docker-desktop)
2. Execute in console `docker-compose up -d --build` to create the container
3. Jupyter Lab available at `http://localhost:10000/lab`. Password is "docker"
