# Makefile pour la documentation Sphinx

# Configuration des variables
SPHINX_PROJECT = "jeu-du-pendu"
SPHINX_DOCS = "_build"
SPHINX_SOURCE = "docs/source"
SPHINX_OUTPUT = "docs"

# Génération de la documentation
sphinx:
	@echo "Génération de la documentation Sphinx..."
	@cd docs && sphinx-build -b html source ${SPHINX_DOCS}

# Nettoyer les fichiers temporaires et les fichiers de build
clean:
	@echo "Nettoyage des fichiers temporaires..."
	@rm -rf ${SPHINX_DOCS}

# Affichage de l'aide
help:
	@echo "Utilisez les cibles suivantes :"
	@echo "  sphinx   : Génère la documentation Sphinx."
	@echo "  clean    : Nettoie les fichiers temporaires et les fichiers de build."
