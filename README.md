# chatgpt_clone_by_bertie

## Description
`chatgpt_clone_by_bertie` est un clone personnalisé de ChatGPT qui intègre plusieurs fonctionnalités avancées de l'API OpenAI dans une interface conviviale inspirée du design original de ChatGPT.com. Cette application vous permet d'accéder à diverses technologies d'IA à travers une interface unique en utilisant votre propre clé API OpenAI.

## Fonctionnalités
- **💬 Chat classique** - Interaction avec le modèle GPT-3.5 Turbo
- **🖼️ Génération d'image (DALL-E)** - Création d'images à partir de descriptions textuelles
- **🎙️ Transcription audio (Whisper)** - Conversion de fichiers audio en texte
- **📄 Analyse de PDF** - Extraction et analyse du contenu des fichiers PDF
- **🔍 Analyse d'image (Vision)** - Description et analyse d'images téléchargées

## Prérequis
- Python 3.8 ou version ultérieure
- Compte OpenAI avec une clé API valide
- Connexion Internet

## Installation

### 1. Cloner le dépôt
```shell
git clone https://github.com/valorisa/chatgpt_clone_by_bertie.git
cd chatgpt_clone_by_bertie
```

### 2. Créer un environnement virtuel (recommandé)
```shell
python -m venv venv
source venv/bin/activate
# Sur Windows: venv\Scripts\activate
```

### 3. Installer les dépendances
```shell
pip install -r requirements.txt
```

## Configuration

### 1. Créer un fichier .env
Créez un fichier `.env` à la racine du projet et ajoutez votre clé API OpenAI :
```OPENAI_API_KEY=votre_clé_api_openai_ici```


Pour obtenir une clé API OpenAI :
1. Rendez-vous sur [platform.openai.com](https://platform.openai.com)
2. Créez un compte ou connectez-vous
3. Accédez à la section "API Keys"
4. Créez une nouvelle clé API

## Utilisation

### Démarrer l'application
```shell
python app.py
```

L'application sera accessible à l'adresse ```http://127.0.0.1:7860``` dans votre navigateur.

### Navigation dans l'interface
- Utilisez les onglets en haut de l'interface pour basculer entre les différentes fonctionnalités
- Chaque fonctionnalité possède son propre formulaire adapté

### Limites
- L'accès à certains modèles (GPT-4, DALL-E 3, Vision) peut nécessiter un abonnement OpenAI payant
- Les fichiers PDF volumineux sont automatiquement tronqués pour respecter les limites de tokens
- La qualité des images générées dépend du modèle DALL-E disponible avec votre compte

## Dépannage

### Erreur 429 - Quota dépassé
Si vous recevez l'erreur "You exceeded your current quota", cela signifie que vous avez dépassé votre quota gratuit OpenAI. Solutions possibles :
- Passez à un abonnement payant sur OpenAI
- Créez un nouveau compte avec des crédits gratuits
- Modifiez le code pour utiliser des modèles moins coûteux

### Problèmes de connexion à l'API
- Vérifiez que votre clé API est correctement configurée dans le fichier `.env`
- Assurez-vous que votre connexion Internet fonctionne
- Vérifiez que la clé API n'a pas expiré

## Structure du projet
```bash
chatgpt_clone_by_bertie/
├── app.py                 # Script principal contenant l'application Gradio
├── .env                   # Fichier de configuration pour la clé API OpenAI (à créer manuellement)
├── requirements.txt       # Liste des dépendances Python nécessaires au projet
├── LICENSE                # Fichier de licence (MIT) décrivant les droits d'utilisation du projet
├── README.md              # Documentation principale du projet
└── assets/                # Dossier contenant les fichiers temporaires et téléchargés
    ├── audio/             # Dossier pour les fichiers audio importés par l'utilisateur
    ├── images/            # Dossier pour les images générées ou téléchargées
    └── pdfs/              # Dossier pour les fichiers PDF analysés

```

## Technologies utilisées
- **Gradio** - Framework pour l'interface utilisateur
- **OpenAI API** - Accès aux modèles d'IA
- **PyMuPDF** - Traitement des fichiers PDF
- **Python-dotenv** - Gestion des variables d'environnement

## Licence
Ce projet est disponible sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## Crédits
- Interface inspirée de ChatGPT.com
- Développé par Bertie
- API fournie par OpenAI

**Note importante**: Cette application nécessite une clé API OpenAI valide. L'utilisation des API OpenAI peut engendrer des coûts selon votre plan d'abonnement.
