# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 10:35:15 2025

@author: Carlos - SC
"""

import geopandas as gpd
import rasterio
from rasterio.mask import mask
import numpy as np
import matplotlib.pyplot as plt

# --- CAMINHOS ---
mapbiomas_path = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto02\inputs\mapbiomas.tif"
shapefile_uf_path = r"C:\Users\Carlos - SC\Documents\GitHub\ENS5132\Projeto02\inputs\BR_Municipios_2022.shp"

# --- 1. Ler shapefile e extrair geometria de SC ---
geoUF = gpd.read_file(shapefile_uf_path)
geoSC = geoUF[geoUF['SIGLA_UF'] == 'SC']
geom_sc = [geoSC.geometry.union_all()]

# --- 2. Recortar o raster diretamente para SC ---
with rasterio.open(mapbiomas_path) as src:
    out_image, out_transform = mask(src, shapes=geom_sc, crop=True)
    uso = out_image[0]
    perfil = src.profile.copy()

# --- 3. Visualizar resultado ---
plt.figure(figsize=(10, 6))
plt.imshow(uso, cmap='tab20', interpolation='none')
plt.title("Mapa do uso do solo em Santa Catarina (recorte direto)")
plt.colorbar(label="Classe MapBiomas")
plt.axis('off')
plt.show()