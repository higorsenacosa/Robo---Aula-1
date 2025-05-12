from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rapidfuzz import process
import webbrowser

class ActionPedirMusica(Action):
    def name(self) -> str:
        return "action_pedir_musica"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Lista de músicas da Lady Gaga com seus respectivos links do YouTube
        musicas = {
            "Alejandro": "https://www.youtube.com/watch?v=niqrrmev4mA",
            "Bad Romance": "https://www.youtube.com/watch?v=qrO4YZeyl0I",
            "Poker Face": "https://www.youtube.com/watch?v=bESGLojNYSo",
            "Judas": "https://www.youtube.com/watch?v=7Nr33m1zXVE",
            "Shallow": "https://www.youtube.com/watch?v=bo_efYhYU2A",
            "Rain On Me": "https://www.youtube.com/watch?v=AoAm4om0wTs",
            "Born This Way": "https://www.youtube.com/watch?v=wV1FrqwZyKw",
            "Just Dance": "https://www.youtube.com/watch?v=2Abk1jAONjw",
            "Paparazzi": "https://www.youtube.com/watch?v=d2smz_1L2_0",
            "Telephone": "https://www.youtube.com/watch?v=EVBsypHzF3U"
        }

        # Obter a última mensagem do usuário
        user_message = tracker.latest_message.get('text', '').lower()

        # Tentar encontrar a música mencionada na mensagem
        nomes_musicas = list(musicas.keys())
        resultado = process.extractOne(user_message, nomes_musicas, score_cutoff=60)

        if resultado:
            nome_musica = resultado[0]
            link = musicas[nome_musica]
            webbrowser.open_new_tab(link)
            dispatcher.utter_message(text=f"Certo, vou abrir a música {nome_musica} no YouTube: {link}")
        else:
            dispatcher.utter_message(text="Desculpe, não encontrei essa música. Poderia verificar o nome e tentar novamente?")

        return []