<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $text = $_POST['text'];

  // Pass the text to the video generation script
  header("Location: generate_video.php?text=" . urlencode($text));
  exit;
}
?>
<html>
<head>
  <title>Text to Video Converter</title>
</head>
<body>
  <h1>Text to Video Converter</h1>
  <?php
  // Display any success/error messages
  if (isset($_GET['message'])) {
    $message = $_GET['message'];
    echo "<p>$message</p>";
  }
  ?>
  <?php include 'form.html'; ?>
</body>
</html>
