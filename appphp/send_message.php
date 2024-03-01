<?php
require_once 'MessageManager.php';

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    $message = $data['message'] ?? ''; 

    $messageManager = new MessageManager();
    $success = $messageManager->sendMessage($message);

    if ($success) {
        echo json_encode(['status' => 'success', 'message' => 'Mensagem enviada com sucesso.']);
    } else {
        http_response_code(500);
        echo json_encode(['status' => 'error', 'message' => 'Falha ao enviar a mensagem.']);
    }
} else {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Método de solicitação não permitido.']);
}

