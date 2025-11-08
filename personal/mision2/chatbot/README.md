# guia  de implementacion del chatbot, supervisado
pip install scikit-learn
pip install numpy
pip install gym==0.26.2
pip install gym-notices
pip install scikit-learn numpy gym==0.26.2 gym-notices

crear el archivo setup:nltk.py
```
import nltk 

try:
    nltk.download('punkt')
    print(" NLTK punkt descargado correctamente")
except Exception as e:
    print("error durante la descarga:",e)

    ```
    python setup_nltk.py
    