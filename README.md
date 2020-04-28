# project_templates
Default starting points for projects.
Takes into account the notebook script development, documentation, references, as well as object oriented code development.


## data
Types of data stored for the project
* external --> Data from third party sources
* interim --> Intermediate data that has been transformed
* processed --> The final, canonical data sets for modeling
* raw --> The original, immutable data dump


## docs
A default Sphinx project; see sphinx-doc.org for details


## models
Trained and serialized models; model predictions, or model summaries


## notebooks
Jupyter notebooks. Namoing convention is a number (for ordering), the creator's initials, and a short '-' delimited descriptions, e.g. '1.0-gks-initial-data-exploration'


## references
Data dictionaries, manuals, and all other explanatory materials.


## reports
Generated analysis as HTML, PDF, LaTex, etc
### figures
Generated graphics and figures to be used in reporting


## requirements.txt
The requirement file for reproducing the analysis environment e.g. generated with 'pip freeze > requirements.txt'


## setup.py
Make this project pip installable with 'pip install -e'


## src
Source code for use in this project

### \__init\__.py
Makes scr a Python module

### data
Scripts to download or generate data
#### make_dataset.py

### features
Scripts to turn raw data into features for modeling
#### build_features.py

### models
Scripts to train models and then use trained models to make predictions
#### predict_model.py
#### train_model.py

### visualization
Scripts to create exploratory and results oriented visualizations
#### visualize.py

### tox.ini
tox file with settings for running tox; see tox.testrun.org


# Note
GitHub doesn't support pushing over the Git protocol, which is indicated by your use of the URL beginning git://. As the error message says, if you want to push, you should use either the SSH URL git@github.com:my_user_name/my_repo.git or the "smart HTTP" protocol by using the https:// URL that GitHub shows you for your repository.

If you want to change the URL of origin, you can just do:

git remote set-url origin git@github.com:my_user_name/my_repo.git

or

git remote set-url origin https://github.com/my_user_name/my_repo.git



git remote set-url origin https://gotitsingh13@github.com/project_templates.git


git@github.com:gotitsingh13/project_templates.git