# TFG
Repositori del meu Treball Final de Grau en Matemàtica Computacional i Analítica de Dades: Implementació i resultats sobre la detecció i classificació de fruites imperfectes. Aquest repositori conté tot el codi rellevant i la documentació necessària.

# train
En el fitxer `train.ipynb` es realitza l'entrenament d'un model YOLO (versió 8) per a la base de dades original de fruites sintètiques. 
Inclou la configuració inicial, el carregament i preprocessament de les dades, l'entrenament i l'avaluació del rendiment del model amb diverses mètriques.
  ## Requisits
  - Assegurat d'utilitzar una GPU per agilitzar els càlculs.
  - Si no utilitzes Google Colab assegurat de tenir instal·lades les llibreries: matplotlib, IPython, pandas 
  Pots instal·lar aquestes dependències executant el següent codi:
  ```python
  pip install matplotlib ipython pandas
  ```
  ## Carregament i preprocessament de les dades:
  S'importen les dades des de la plataforma Roboflow, La clau de l'API no està inclosa en aquest codi per raons de seguretat.
  Un cop realitzada la importació de les dades et demanarà fer un reset. Abans d'executar la següent cel·la, assegura't de tenir totes les rutes correctes en el fitxer **data.yaml**.

Per dur a terme l'Experiment 2 amb la base de dades augmentada, només s'hauria de modificar la cel·la de carregament i preprocessament de dades:
 ```python
#Import the dataset with Data Augmentation from Roboflow
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="api_key")
project = rf.workspace("fruitesd").project("fd-ndbok")
version = project.version(4)
dataset = version.download("yolov8")
```

# classif
En el fitxer "classif2.py" es realitza la detecció i classificació de les fruites amb el model entrenat per una nova base de dades amb imatges reals.

En l'experiment 1 i 3, s'utilitza com a **model_path** la ruta del fitxer de pesos: best1.pt
En l'experiment 2, s'utilitza com a **model_path** la ruta del fitxer de pesos: best2.pt

En l'experiment 1 i 2, s'utilitza com a **path_validation** la ruta de les imatges en aquest repositori: https://bit.ly/base_de_dades_validacio
En l'experiment 3, s'utilitza com a **path_validation** la ruta de les imatges en aquest repositori: https://bit.ly/base_de_dades_validacio_2

Un cop amb el model i les imatges configurades. Per cada imatge s'aplica el model:
```python
result = model(source=img_path, show=False, conf=0.6, save=True)
```
Pots modificar aquesta linia per augmentar o disminuir el llindar de confiança en la detecció i classificació i per mostrar i guardar les imatges, posant True al parametre show i/o save. 
A més, si estableixes el paràmetre source=0, ho pots aplicar a imatges en temps real amb la càmara de l'ordinador.
