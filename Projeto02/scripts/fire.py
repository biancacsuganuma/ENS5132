# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 19:02:15 2025

@author: Carlos - SC
"""

import pandas as pd
import numpy as np
import xarray as xr
import netCDF4 as CDF4
import os
import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt
#import folium
import contextily as cx
import rasterio as rio
from rasterio.enums import Resampling

# Caminho do arquivo
ufPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto02\inputs\BR_Municipios_2022.shp"
geoUF = gpd.read_file(ufPath)

# --- 2. Filtrar só os estados da Região Sul ---
geoSul = geoUF[geoUF['SIGLA_UF'].isin(['PR', 'SC', 'RS'])]

# --- 3. Unir em uma única geometria ---
geom_sul = [geoSul.unary_union]


# --- 4. Recortar o raster MapBiomas ---
# Caminho do arquivo
mapbiomasPath = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto02\inputs\mapbiomas.tif"

# Abrir raster original
from rasterio.mask import mask

with rio.open(mapbiomasPath) as src:
    # AQUI é onde o recorte acontece:
    out_image, out_transform = mask(src, shapes=geom_sul, crop=True)

    uso = out_image[0]           # Matriz recortada (com valores do raster original)
    perfil = src.profile.copy()  # Copia os metadados para poder salvar depois


# --- 1. Selecionar municípios do Sul ---
geoSul = geoMun[geoMun['SIGLA_UF'].isin(['PR', 'SC', 'RS'])]

# --- 2. Unir todos os municípios em uma única geometria ---
geom_sul = [geoSul.unary_union]

# --- 3. Recortar o raster usando a geometria da Região Sul ---
mapbiomas_path = r"C:\Users\Leonardo.Hoinaski\Documents\ENS5132\projeto02\inputs\mapbiomas_10m_collection2_integration_v1-classification_2023 (2).tif"

with rasterio.open(mapbiomas_path) as src:
    out_image, out_transform = rasterio.mask.mask(src, geom_sul, crop=True)
    uso = out_image[0]
    perfil = src.profile.copy()