# Visualizacion con Plotly

### Instalacion
Este taller requiere tener instalado Python y Jupyter, la forma mas facil de hacer esto para diversas plataforma es instalando [Anaconda](https://www.continuum.io/downloads).

Si ya tiene Python y `pip` instalado, para instalar jupyter solo tienes que correr el comando:

```
pip install jupyter
```

### Codigo
Si usas git puedes clonar este repositorio, de otra manera descarga el `.zip` de la pagina de github con el boton que dice "Clone or download". Asegurate de extrear este archivo.

Una vez descarges o clones el codigo incresa a la carpeta donde esta el codigo desde una terminal.

### Jupyter
Para correr el taller debemos iniciar Jupyter de forma compatible con Plotly, debido a recientes cambios en Jupter debemos ejecutar el comando siguiente comando desde la terminal, si usas Anaconda debes utilizar la terminal de anaconda.

```bash
jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000000 .
```

Asegurate de primero estar ubicado en la carpeta con el codigo. Una vez ejecutes este comando se deberá abrir una ventana en algun browser. Abre el archivo que dice `ìntroduccion-plotly` para iniciar el taller.
