#SYSTEM
Linux-Ubuntu:20.04

#Jupyter notebook with Pyspark Docker
sudo docker run -it --rm -p 10012:8888 -v "${PWD}":/home/jovyan/work jupyter/pyspark-notebook:a374cab4fcb6

#Jupyter token-password from logs jupyter/pyspark-notebook:a374cab4fcb6
jupyter-token=<JUPYTER-TOKEN>
jupyter-password=<JUPYTER-PASSWORD>

#Hive Volume external
volume external :
sudo docker volume create --name spark_volume --opt type=none --opt device=<SPARK_ACTIVE_DIRECTORY> --opt o=bind

#Under ./spark run analysis.ipynb


hive referance:
-https://github.com/big-data-europe/docker-hive.git
jupyter/pyspark container referance:
-https://hub.docker.com/r/jupyter/pyspark-notebook
