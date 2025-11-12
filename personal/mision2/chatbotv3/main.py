from chatbot.data import training_data
from chatbot.model import buid_and_train_model, predict_answer, load_model

def chat(model, vectorizer, unique_answers):
    """Inicia el modelo de conversación"""
    print("\n 💬 chat iniciado. DEscriba salir para terminar \n")
    while True:
        user = input("tu: ").strip()
        if user.lower() in {"salir","exit","quit"}:
            print("bot: !hasta pronto¡")
            break
        response = predict_answer(model, vectorizer, unique_answers, user)
        print("bot:", response)
        
        
        
def main():
    # Intentar cargar el modelo
    model, vectorizer, unique_answers = load_model()
    #Mdenu principal
    while True:
        print("\n=== 🤖 MENU PRINCIPAL DEL CHATBOT ===")
        print("1️⃣ Chatea con el modelo")
        print("2️⃣ Reentrenar el modelo")
        print("3️⃣ Salir")
        opcion= input("\n Elige una opcion (1-3): ").strip()
        if opcion == "1":
            if model is None:
                print("\n no hay modelo entrenado. entrenalo primero.")
            else:
                chat(model, vectorizer, unique_answers)
                
        elif opcion == "2":
            print("\n 🤸 Reentrenando el modelo con los nuevos datos...")
            model, vectorizer, unique_answers=buid_and_train_model(training_data)
            print(" modelo actualizado correctamente")
        elif opcion == "3":
            print("\👍 hasta luego!")
            break
        else:
            print("\n ❌opcion no vbalida. intenta nuevamente")
            
         
        
  
if __name__ == "__main__":
    main()
    