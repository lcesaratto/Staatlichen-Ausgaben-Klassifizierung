# Staatlichen Ausgaben Klassifizierung

## Case-Study

### Technologies

- Python 3.9+
- Poetry
- Scrapy
- Pandas
- Seaborn
- Pytorch
- Huggingface
- Scikit-learn

### Data gathering

1. Execute `scrapy_web_crawler.py` to get the dataset downloaded to `data/raw_data.csv`

### Local Development

1. Clone repository and `cd` into repository directory
2. Check Python version `python -V`. Check recommended Python version in Technologies section
3. [Install Poetry](https://python-poetry.org/docs/#installation) (recommended) or skip this step for an isolated installation of Poetry
4. Create a virtual enviroment `python -m venv venv`
5. Install Poetry inside the virtual enviroment `pip install poetry`. Skip this step if Poetry is already available globally (as explained in step 3)
6. Install dependencies `poetry install`
7. Execute `jupyter-lab` to visualize the project notebooks

### Local Deployment for Windows Users

1. [Install Docker](https://docs.docker.com/desktop/windows/install/) with WSL2 backend
2. Check WSL version installed `wsl -l -v`. The listed version must be 2
3. Execute in Windows Console `docker run hello-world` to check if Docker is working correctly
4. [Install GIT Bash](https://gitforwindows.org/) and execute `bash create_container.sh`, OR...
5. Execute in Windows Console manually the commands inside `create_container.sh`

### Local Deployment for Linux/Mac Users

1. [Install Docker](https://www.docker.com/products/docker-desktop)
2. Execute in Terminal `make build` followed by `make run`

### For later reference

https://github.com/python-poetry/poetry/issues/2613#issuecomment-799693903
poetry install
poe force-cuda11
