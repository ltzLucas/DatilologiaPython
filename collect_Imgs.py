import os
import cv2

PASTA_DADOS = './data'
if not os.path.exists(PASTA_DADOS):
    os.makedirs(PASTA_DADOS)

numero_de_classes = 1
tamanho_dataset = 300
cap = cv2.VideoCapture(0)

# Loop para cada classe
for j in range(numero_de_classes):
    if not os.path.exists(os.path.join(PASTA_DADOS, str(j))):
        os.makedirs(os.path.join(PASTA_DADOS, str(j)))

    print('Coletando dados para a classe {}'.format(j))

    pronto = False
    while True:
        # Captura do frame da câmera
        ret, frame = cap.read()

        # Adiciona texto na imagem exibida
        cv2.putText(frame, 'Pronto? Pressione "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 3,
                    cv2.LINE_AA)

        # Exibe o frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    contador = 0
    while contador < tamanho_dataset:
        # Captura do frame da câmera
        ret, frame = cap.read()

        # Exibe o frame
        cv2.imshow('frame', frame)
        cv2.waitKey(25)

        # Salva o frame como uma imagem no disco
        cv2.imwrite(os.path.join(PASTA_DADOS, str(j), '{}.jpg'.format(contador)), frame)

        contador += 1

cap.release()
cv2.destroyAllWindows()
