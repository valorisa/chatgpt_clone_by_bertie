import gradio as gr
import os
from openai import OpenAI
from dotenv import load_dotenv
import fitz  # PyMuPDF pour PDF
import base64  # Pour encoder les images en base64

# Chargement de la clé API depuis le fichier .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Fonctions pour chaque fonctionnalité
def chat_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Modèle accessible à tous
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur: {str(e)}"

def generer_image(prompt):
    try:
        response = client.images.generate(
            model="dall-e-2",  # DALL-E 2 est généralement plus accessible
            prompt=prompt,
            size="1024x1024",
            n=1
        )
        return response.data[0].url
    except Exception as e:
        return f"Erreur: {str(e)}"

def transcrire_audio(audio_path):
    try:
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcript.text
    except Exception as e:
        return f"Erreur: {str(e)}"

def analyser_pdf(pdf_path):
    try:
        texte_complet = ""
        doc = fitz.open(pdf_path)
        for page in doc:
            texte_complet += page.get_text() + "\n"
            
        # Limiter la taille du texte pour éviter de dépasser les limites de tokens
        if len(texte_complet) > 15000:
            texte_complet = texte_complet[:15000] + "...[texte tronqué]"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Analyse ce texte:\n{texte_complet}"}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur lors de l'analyse du PDF: {str(e)}"

def analyser_image(image_path):
    try:
        # Pour utiliser Vision, vous avez besoin d'encoder l'image en base64
        with open(image_path, "rb") as img_file:
            base64_image = base64.b64encode(img_file.read()).decode('utf-8')
            
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",  # Ce modèle est nécessaire pour l'analyse d'images
            messages=[
                {
                    "role": "user", 
                    "content": [
                        {"type": "text", "text": "Décris cette image en détail."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                }
            ],
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erreur lors de l'analyse de l'image: {str(e)}\n\nNote: L'analyse d'image nécessite GPT-4 Vision. Utilisez une autre fonctionnalité ou mettez à niveau votre compte OpenAI."

# Interface Gradio inspirée par ChatGPT.com
with gr.Blocks(title="chatgpt_clone_by_bertie", theme=gr.themes.Soft()) as demo:
    
    gr.Markdown("# chatgpt_clone_by_bertie")
    
    # Onglet Chat classique
    with gr.Tab("💬 Chat classique"):
        chatbot_input = gr.Textbox(label="Entrez votre message", placeholder="Tapez votre message ici...")
        chatbot_output = gr.Textbox(label="Réponse de l'IA")
        btn_chat = gr.Button("Envoyer")
        btn_chat.click(fn=chat_gpt, inputs=chatbot_input, outputs=chatbot_output)
    
    # Onglet Génération d'image
    with gr.Tab("🖼️ Génération d'image (DALL-E)"):
        prompt_img = gr.Textbox(label="Description de l'image", placeholder="Décrivez l'image que vous souhaitez générer...")
        output_img = gr.Image(label="Image générée")
        btn_img = gr.Button("Générer l'image")
        btn_img.click(fn=generer_image, inputs=prompt_img, outputs=output_img)

    # Onglet Transcription audio
    with gr.Tab("🎙️ Transcription audio (Whisper)"):
        audio_input = gr.Audio(type="filepath", label="Importer un fichier audio")
        transcription_output = gr.Textbox(label="Texte transcrit")
        btn_audio = gr.Button("Transcrire l'audio")
        btn_audio.click(fn=transcrire_audio, inputs=audio_input, outputs=transcription_output)
    
    # Onglet Analyse de PDF
    with gr.Tab("📄 Analyse de PDF"):
        pdf_input = gr.File(label="Importer un PDF", file_types=[".pdf"])
        pdf_output = gr.Textbox(label="Analyse du PDF")
        btn_pdf = gr.Button("Analyser le PDF")
        btn_pdf.click(fn=analyser_pdf, inputs=pdf_input, outputs=pdf_output)

    # Onglet Analyse d'image
    with gr.Tab("🔍 Analyse d'image"):
        img_input_analysis = gr.Image(type="filepath", label="Importer une image")
        img_analysis_output = gr.Textbox(label="Analyse de l'image")
        btn_analyse_img = gr.Button("Analyser l'image")
        btn_analyse_img.click(fn=analyser_image, inputs=img_input_analysis, outputs=img_analysis_output)

    # Note sur les limitations
    gr.Markdown("""
    ## Remarques importantes
    - L'accès à certains modèles (GPT-4, DALL-E 3, Vision) peut nécessiter un abonnement OpenAI payant
    - Si vous rencontrez des erreurs, vérifiez votre clé API dans le fichier .env
    - Les fichiers PDF volumineux peuvent être tronqués pour respecter les limites de tokens
    """)

# Lancer l'application
demo.launch()

