<?php
require_once 'Database.php';

class Chat {
    private $conn;

    public function __construct() {
        $database = new Database();
        $this->conn = $database->getConnection();
    }

    public function sendMessage($message,$user) {
        $query = "INSERT INTO messages (message,user) VALUES (:message,:user)";
        $stmt = $this->conn->prepare($query);

        $message=htmlspecialchars(strip_tags($message));

        $stmt->bindParam(":message", $message);
        $stmt->bindParam(":user", $user);
        if($stmt->execute()) {
            return true;
        }

        return false;
    }

    public function getMessages($lastId = 0) {
        $query = "SELECT id, message, user FROM messages WHERE id > :lastId ORDER BY id DESC";
        $stmt = $this->conn->prepare($query);

        $stmt->bindParam(":lastId", $lastId, PDO::PARAM_INT);
        $stmt->execute();

        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}
?>
