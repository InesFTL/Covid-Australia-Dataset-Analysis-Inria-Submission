# INRIA-Submission
My submission for the INRIA-APHP-assignement : https://github.com/agramfort/inria-aphp-assignment


## Fichiers
- data.db  : Base de données sqlite contenant deux tables.
- Notebook_Final_1.ipynb : Jupyter Notebook présentant l'exploration et le nettoyage des données fournis
- detect_duplicates.ipynb : Jupyter Notebook présentant la fonction *detect_duplicates* qui rend en sortie le dataframe **df_patient** sans doublons.
                      Le notebook contient aussi la session *pytest* lancé pour tester la fonction *detect_duplicates* à partir du fichier *test.py* 
                      ainsi que d'autre tests optionnels.
- test.py : Fichier contenant notre fonction *detect_duplicates* et son pytest 
- Notebook_Final_2.ipynb : Jupyter Notebook présentant la jointure entre le dataframe sans doublons **df_patient** et le dataframe **df_pcr** et la prévalence
                     des tests PCR

- *df_dedup_clean.csv* : Fichier csv contenant le dataframe **df_patient** nettoyé et corrigé des données incohérentes mais contenant toujours les doublons
- *df_pcr_clean_final.csv* : Fichier csv contenant le dataframe **df_pcr** nettoyé et corrigé des données incohérentes 
- *df_patient_dup.csv* : Fichier csv contenant tout les doublons du dataframe **df_patient** pour les 10 000 premières entrées. Ce fichier permet de tester
                         pour la fonction pytest.
- *df_patient_clear_final_f.csv* : Fichier csv contenant le dataframe **df_patient** issue de la fonction *detect_duplicates* 
- *df_patient_pcr_clean.csv* : Fichier csv contenant la jointure entre le dataframe **df_patient** et **df_pcr** nettoyé et sans doublons par la clé *patient_id*


## Requirements
- python ==3.6.4
- Sqlachemy
- pandas == 1.0.5
- fuzzywuzzy == 0.18.0
- python-Levenshtein==0.12.0
- time
- seaborn ==0.10.1
- matplotlib ==3.2.2
