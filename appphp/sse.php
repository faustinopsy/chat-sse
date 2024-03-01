<?php
require_once 'Chat.php';

set_time_limit(0);

header('Content-Type: text/event-stream');
header('Cache-Control: no-cache');

session_write_close();

$chat = new Chat();
$lastId = isset($_GET['lastId']) ? (int)$_GET['lastId'] : 0;

while (true) {
    if (connection_aborted()) {
        break;
    }
    $messages = $chat->getMessages($lastId);
    if (count($messages) > 0) {
        $lastMessage = end($messages);
        $lastId = $lastMessage['id'];

        echo "id: {$lastId}\n";
        echo "data: " . json_encode($messages) . "\n\n";
    } else {
        echo ": lol\n\n";
    }

    ob_flush();
    flush();
    sleep(1);
}

