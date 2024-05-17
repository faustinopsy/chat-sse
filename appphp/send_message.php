<?php

require 'vendor/autoload.php';
use Chat\App\Chat;

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    $message = $data['message'] ?? ''; 
    $user = $data['usuario'] ?? ''; 
    $chat = new Chat();
    $success = $chat->sendMessage($message,$user);

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

