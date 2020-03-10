FROM jupyter/scipy-notebook:e255f1aa00b2

USER root
RUN apt update \
  && apt install -yq --no-install-recommends \
  python3-dev \
  libpq-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

USER $NB_UID

RUN pip install --no-cache-dir nbgitpuller
RUN jupyter serverextension enable nbgitpuller --sys-prefix

RUN pip install --no-cache-dir psycopg2

RUN pip install --no-cache-dir plotly

RUN git clone https://github.com/akdiem/sc_sintef_advanced_python_course.git