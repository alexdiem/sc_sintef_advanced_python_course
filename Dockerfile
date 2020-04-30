FROM jupyter/scipy-notebook:e255f1aa00b2

USER root
RUN apt update \
  && apt install -yq --no-install-recommends \
  python3-dev \
  libpq-dev \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

USER $NB_UID
RUN pip install --no-cache-dir psycopg2 \
                               plotly \
			       nbgitpuller \
			       nodejs \
			       ipywidgets

RUN export NODE_OPTIONS=--max-old-space-size=4096
RUN jupyter serverextension enable nbgitpuller --sys-prefix
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager
RUN jupyter labextension install jupyterlab-plotly
RUN jupyter labextension install plotlywidget
RUN unset NODE_OPTIONS
