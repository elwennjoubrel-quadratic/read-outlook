# read-outlook

Ajouter un fichier `data.pst` à la racine.

Dans un terminal
```bash
pip install -r requirements.txt
ratom entities -p -m data.pst
```

On crée comme ça un fichier sqlite qui contient toutes les données, voir la [doc](https://github.com/libratom/libratom)

Ensuite dans le fichier `main.py`, on a deux commandes qui vont permettre de remplir le fichier `files.json` avec le sha256 et les id des mails concernés par des pièces jointes PDF.
Une fois ce fichier rempli, dans un terminal :

```bash
ratom emldump files.json
```
Crée un dossier qui contient les fichier eml des mails considérés, mais surtout des dossiers pour tous les attachements.
